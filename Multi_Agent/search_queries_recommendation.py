from crewai import Agent, Task
from pydantic import BaseModel, Field
from typing import List
from crewai.tools import tool
from typing import List
from pydantic import BaseModel, Field
import os





no_keywords=10
class SuggestedSearchQueries(BaseModel):

     queries: List[str] = Field(...,title="Suggested search queries to be passed to the search engine",
                               min_length=1, max_length=no_keywords)




# search_recommender.py
class SearchQueryRecommender:
    def __init__(self, llm, output_dir="./output"):
        self.llm = llm
        self.output_dir = output_dir
        self.agent = self._create_agent()
        self.task = self._create_task()
    
    def _create_agent(self):
        return Agent(
            role="search_queries_recommendation_agent",
            goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "Generating multiple variations of search queries — including keyword-based looking for specific items"
            ]),
            backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
            llm=self.llm,
            verbose=True
        )
    
    def _create_task(self):
        return Task(
            description="\n".join([
                "Ohay is looking to buy {product_name} at the best prices (value for a price strategy)",
                "The company target any of these websites to buy from: {websites_list}",
                "The stores must sell the product in {country_name}",
                "Generate at maximum {no_keywords} queries.",
                "Search keywords must contains specific brands, types or technologies. Avoid general keywords.",
                "The search query must reach an ecommerce webpage for product, and not a blog or listing page."
            ]),
            expected_output="A JSON object containing a list of suggested search queries.",
            output_json=SuggestedSearchQueries,
            output_file=os.path.join(self.output_dir, "step_1_suggested_search_queries.json"),
            agent=self.agent
        )

    @property
    def get_agent(self):
        return self.agent
    
    @property
    def get_task(self):
        return self.task