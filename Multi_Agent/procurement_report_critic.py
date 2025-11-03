import os
from crewai import Agent, Task

class procurement_report_critic_agent:
    def __init__(self, llm, output_dir="./output"):
        self.llm = llm
        self.output_dir = output_dir
        
        print(" Initializing procurement_report_critic_agent...")
        
        # Initialize context attributes FIRST
        self._critique_context = None
        self._revision_context = None
        
        # Create agent and tasks
        self.agent = self._create_critic_agent()
        print("Critic agent created")
        
        self.critique_task = self._create_critique_task()
        print("Critique task created")
        
        self.revision_task = None
        print("procurement_report_critic_agent initialized successfully")
    
    def _create_critic_agent(self):
        """Create the procurement quality assurance expert agent"""
        return Agent(
            role="Procurement Quality Assurance Expert",
            goal="Critically review procurement reports for accuracy, completeness, and quality",
            backstory="""You are a meticulous procurement analyst with 15 years of experience. 
            Your expertise includes:
            - Identifying gaps in market analysis
            - Spotting missing cost factors
            - Checking supplier evaluation completeness
            - Ensuring risk assessment thoroughness
            - Validating data consistency and accuracy
            
            You are known for being thorough, critical, and constructive. You never accept 
            reports at face value and always look for ways to improve them.""",
            llm=self.llm,
            verbose=True,
            reasoning=True,
            max_reasoning_attempts=3
        )
    
    def _create_critique_task(self):
        """Create the critique task"""
        print(f"Creating critique task with context: {self._critique_context}")
        return Task(
            description="""Thoroughly review and critique the draft procurement report.
                
            Provide specific, constructive feedback on:

            **Accuracy & Completeness:**
            - Are all cost factors included?
            - Is the market analysis comprehensive?
            - Are there any factual inaccuracies?
            - Is the data interpretation correct?

            **Structure & Clarity:**
            - Is the report well-organized?
            - Are recommendations clear and actionable?
            - Is the executive summary effective?

            **Gaps & Improvements:**
            - What important information is missing?
            - What sections need more depth?
            - Are there better alternatives not considered?

            Provide detailed, specific feedback that the author can use to improve the report.""",
            agent=self.agent,
            context=self._critique_context,
            expected_output="Detailed critique with specific improvement suggestions"
        )
    
    def _create_revision_task(self, author_agent):
        """Create the revision task"""
        print(f"Creating revision task with context: {self._revision_context}")
        print(f"Author agent type: {type(author_agent)}")
        
        return Task(
            description="""Revise and improve the procurement report based on the detailed critique provided.

            Address all points raised in the critique:
            - Fix any factual inaccuracies
            - Fill identified information gaps
            - Improve structure and clarity
            - Strengthen recommendations
            - Enhance executive summary

            Ensure the final report is polished, comprehensive, and meets the highest quality standards.
            Incorporate the feedback while maintaining your professional writing style.""",
            agent=author_agent,
            context=self._revision_context,
            expected_output="Final, polished procurement report",
            output_file=os.path.join(self.output_dir, "step_4_updated_procurement_report.html")
        )
    
    def set_critique_context(self, author_task):
        """Set context dependency for critique task"""
        print(f"Setting critique context with: {type(author_task)}")
        self._critique_context = [author_task]
        # Recreate the task with the updated context
        self.critique_task = self._create_critique_task()
        print("Critique context set successfully")
        return self
    
    def set_revision_context(self, author_task, critique_task, author_agent):
        """Set context dependency and create revision task"""
        print(f"Setting revision context with:")
        print(f"- Author task: {type(author_task)}")
        print(f"- Critique task: {type(critique_task)}")
        print(f"- Author agent: {type(author_agent)}")
        
        self._revision_context = [author_task, critique_task]
        self.revision_task = self._create_revision_task(author_agent)
        print("Revision context set successfully")
        return self
    
    @property
    def get_agent(self):
        return self.agent
    
    @property
    def get_critique_task(self):
        return self.critique_task
    
    @property
    def get_revision_task(self):
        return self.revision_task
 


 