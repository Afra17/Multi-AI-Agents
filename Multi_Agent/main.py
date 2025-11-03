# Initialize all your components
from crewai import Crew, Process, LLM
import agentops
from tavily import TavilyClient
from scrapegraph_py import Client
from dotenv import load_dotenv
import os
# Import your other agents from their respective files
from search_queries_recommendation import SearchQueryRecommender
from search_engine import SearchEngine
from web_scraping import ScrapingAgent
from procurement_report_author import procurement_report_agent
from procurement_report_critic import procurement_report_critic_agent


#Key Needed
load_dotenv()
agentops_key = os.getenv("AGENTOPS_API_KEY")
agentops.init(
    api_key=agentops_key,
    skip_auto_end_session=True,
    default_tags=['crewai']
)
search_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
scrape_client = Client(api_key=os.getenv("SGAI_API_KEY"))


#LLM
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.1
)
groq_llm2 = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.1
)

#main.py
def main():
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

    # Initialize the search recommender
    output_dir=r"./output"
    search_recommender = SearchQueryRecommender(llm=groq_llm, output_dir=output_dir)
    search_engine = SearchEngine(llm=groq_llm2, output_dir=output_dir, search_client=search_client)
    web_scraping = ScrapingAgent(llm=groq_llm2, output_dir=output_dir, scrape_client=scrape_client)
    procurement_report_author = procurement_report_agent(llm=groq_llm2, output_dir=output_dir)
    procurement_report_critic = procurement_report_critic_agent(llm=groq_llm2, output_dir=output_dir)

    #context_dependency
    search_engine.set_context_dependency(search_recommender.get_task)
    web_scraping.set_context_dependency(search_engine.get_task)
    procurement_report_author.set_context_dependency(web_scraping.get_task)
    procurement_report_critic.set_critique_context(procurement_report_author.get_task)
    procurement_report_critic.set_revision_context(procurement_report_author.get_task,procurement_report_critic.get_critique_task,procurement_report_author.get_agent)
    

    #knowledge_sources
    about_company = "ohay is a company that provides AI solutions to help websites refine their search and recommendation systems."
    company_context = StringKnowledgeSource(
        content=about_company
    )

    # Create the crew
    Ohay_crew = Crew(
        agents=[
            search_recommender.get_agent,
            search_engine.get_agent,
            web_scraping.get_agent,
            procurement_report_author.get_agent,
            procurement_report_critic.get_agent
        ],
        tasks=[
            search_recommender.get_task,
            search_engine.get_task,
            web_scraping.get_task,
            procurement_report_author.get_task,
            procurement_report_critic.get_critique_task,
            procurement_report_critic.get_revision_task
        ],
        process=Process.sequential,
        knowledge_sources=[company_context],  # Make sure company_context is defined
        memory=True
    )
    
    # Execute the crew
    result = Ohay_crew.kickoff(
        inputs={
            "product_name": "Coffee Machine for the Office",
            "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/saudi-en"],
            "country_name": "Saudi",
            "no_keywords": 10,
            "score_th": 0.10,
            "score_ra": 3.5
        }
    )
    
    print("=== RESULTS ===")
    print(result)
    return result

if __name__ == "__main__":
    main()