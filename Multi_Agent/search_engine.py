from crewai import Agent, Task
from pydantic import BaseModel, Field
from typing import List
from crewai.tools import tool
import os 





class SignleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="the page url")
    content: str
    score: float
    rating : float
    search_query: str
    
class AllSearchResult(BaseModel):
    results: List[SignleSearchResult]


class SearchEngine:
    def __init__(self, llm, output_dir="./output",search_client=None):
        self.llm = llm
        self.output_dir = output_dir
        self.search_client = search_client
        
        # Define models
        self.SingleSearchResult = SignleSearchResult
        self.AllSearchResults = AllSearchResult
        
        # Create tool, agent and task
        self.search_tool = self._create_search_tool()
        self.agent = self._create_agent()
        self.task = self._create_task()
                 
                 

    def _create_search_tool(self):
        """Create the search engine tool"""
        @tool
        def search_engine_tool(query: str):
            """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
            if self.search_client:
                return self.search_client.search(query)
            else:
                # Fallback or mock implementation
                return f"Search results for: {query}"
        
        return search_engine_tool

    def _create_agent(self):
        """Create the search engine agent"""
        return Agent(
            role="Search Engine Agent",
            goal="To search for products based on the suggested search query",
            backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
            llm=self.llm,
            verbose=True,
            tools=[self.search_tool]
        )
    
    def _create_task(self):
        """Create the search engine task"""
        return Task(
            description="\n".join([
                "The task is to search for products based on the suggested search queries.",
                "You have to collect results from multiple search queries.",
                "Ignore any suspicious links or not an ecommerce single product website link.",
                "Ignore any search results with confidence score less than ({score_th}) and a customer rating (score) lower than ({score_ra})",
                "The search results will be used to compare prices of products from different websites.",
            ]),
            expected_output="A JSON object containing the search results.",
            output_json=self.AllSearchResults,
            output_file=os.path.join(self.output_dir, "step_2_search_engine.json"),
            agent=self.agent
        )
    
    def set_context_dependency(self, dependency_task):
        """Set context dependency for the task"""
        self.task.context = [dependency_task]
        return self
    
    
    
    @property
    def get_agent(self):
        return self.agent
    
    @property
    def get_task(self):
        return self.task
