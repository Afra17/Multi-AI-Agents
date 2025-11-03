from crewai.tools import tool
from typing import List
from pydantic import BaseModel, Field
import os
import json
from crewai import Agent, Task


class ProductSpec(BaseModel):
    specification_name: str
    specification_value: str


class SingleExtractedProduct(BaseModel):
    page_url: str = Field(..., title="The original url of the product page")
    product_title: str = Field(..., title="The title of the product")
    product_image_url: str = Field(..., title="The url of the product image")
    product_url: str = Field(..., title="The url of the product")
    product_current_price: float = Field(..., title="The current price of the product")
    product_original_price: float = Field(title="The original price of the product before discount. Set to None if no discount", default=None)
    product_discount_percentage: float = Field(title="The discount percentage of the product. Set to None if no discount", default=None)
    product_specs: List[ProductSpec] = Field(..., title="The specifications of the product. Focus on the most important specs to compare.", min_items=1, max_items=5)
    agent_recommendation_rank: int = Field(..., title="The rank of the product to be considered in the final procurement report. (out of 5, Higher is Better) in the recommendation list ordering from the best to the worst")
    agent_recommendation_notes: List[str]  = Field(..., title="A set of notes why would you recommend or not recommend this product to the company, compared to other products.")

class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]


class ScrapingAgent:
    def __init__(self, llm, output_dir="./output", scrape_client=None):
        self.llm = llm
        self.output_dir = output_dir
        self.scrape_client = scrape_client
    
        # Define models
        self.ProductSpec = ProductSpec
        self.SingleExtractedProduct = SingleExtractedProduct
        self.AllExtractedProducts = AllExtractedProducts
        
        # Create tool, agent and task
        self.scraping_tool = self._create_scraping_tool()
        self.agent = self._create_agent()
        self.task = self._create_task()
    

    def _create_scraping_tool(self):
        """Create the web scraping tool"""
        @tool
        def web_scraping_tool(page_url: str):
            """
            An AI Tool to help an agent to scrape a web page

            Example:
            web_scraping_tool(
                page_url="https://www.noon.com/saudi-ar/4-in-1-automatic-espresso-machine-1800w-2-6l-cappuccino-latte-espresso-grind-coffee-machine-with-automatic-milk-frother-20-bar-pump-pressure-touchscreen-coffee-maker-for-home-and-office-sk-04032/ZE622C99C49629E605245Z/p/?o=ze622c99c49629e605245z-1&shareId=a8f2656d-996c-42b1-a4f1-0ec14d7ae19c"
            )
            """
            if not self.scrape_client:
                return {"error": "Scrape client not configured"}
            
            schema_json = json.dumps(self.SingleExtractedProduct.model_json_schema(), indent=2)
            
            details = self.scrape_client.smartscraper(
                website_url=page_url,
                user_prompt=f"Extract the following product information in JSON format:\n```json\n{schema_json}\n```\nFrom the web page. Focus on extracting accurate product details, prices, and specifications."
            )
            
            return {
                "product": [details]
            }
        
        return web_scraping_tool
    
    def _create_agent(self):
        """Create the scraping agent"""
        return Agent(
            role="Web scraping agent",
            goal="To extract detailed product information from e-commerce website URLs",
            backstory="\n".join([
                "You are an expert web scraping agent specialized in extracting product information from e-commerce websites.",
                "Your role is to analyze product pages and extract key details like title, price, specifications, and images.",
                "You can identify genuine product information and filter out irrelevant or incorrect data."
            ]),
            llm=self.llm,
            tools=[self.scraping_tool],
            verbose=True,
        )
    
    def _create_task(self):
        """Create the scraping task"""
        return Task(
            description="\n".join([
                "Extract detailed product information from e-commerce store page URLs obtained from search results.",
                "For each product URL, extract the following information:",
                "  - Product title, image URL, and product URL",
                "  - Current price and original price (if on discount)",
                "  - Key product specifications (focus on 3-5 most important specs for comparison)",
                "  - Provide a recommendation rank (1-5) and notes explaining the ranking",
                "Prioritize products with complete information and good value for money.",
                "Ensure all extracted data is accurate and relevant for procurement decision making."
            ]),
            expected_output="A JSON object containing detailed information for all extracted products",
            output_json=self.AllExtractedProducts,
            output_file=os.path.join(self.output_dir, "step_3_search_results.json"),
            agent=self.agent,
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