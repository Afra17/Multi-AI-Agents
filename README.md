# **AI-Powered Multi-Agent Research System**
**Build Multi AI Agents and Automate Tasks with CrewAI and AgentOps !**

## Overview
<div dir="rtl">

An intelligent multi-agent system built with CrewAI and AgentOps that automates product research, price comparison, and procurement reporting using advanced AI agents working in coordinated workflows.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Key Features

**🔍 Smart Search Optimization :**

+ Intelligent Query Generation: AI-powered search query recommendations

+ Multi-Platform Search: Simultaneous search across multiple e-commerce platforms

+ Quality Filtering: Automatic filtering based on confidence scores and ratings

**📊 Advanced Data Extraction:**

+ Structured Product Data: Automated extraction of prices, specifications, and images

+ Price Tracking: Current price, original price, and discount percentages

+ Product Comparison: Side-by-side specification analysis

**📊 Professional Reporting:**

+ Automated Procurement Reports: Comprehensive market analysis

+ Quality Assurance: Multi-stage review and critique process

+ Executive Summaries: Actionable insights for decision makers

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## Core Technologies
<div align="center">

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
    <th>Benefits</th>
  </tr>
  <tr>
    <td><b>🤖 CrewAI</b></td>
    <td>Multi-agent orchestration framework</td>
    <td>Sequential workflow, agent collaboration, task management</td>
  </tr>
  <tr>
    <td><b>📊 AgentOps</b></td>
    <td>Agent monitoring and analytics</td>
    <td>Performance tracking, session replay, debugging tools</td>
  </tr>
  <tr>
    <td><b>🚀 Groq</b></td>
    <td>High-speed LLM inference</td>
    <td>Ultra-fast response times, efficient processing</td>
  </tr>
  <tr>
    <td><b>📝 Pydantic</b></td>
    <td>Data validation and serialization</td>
    <td>Type safety, structured outputs, JSON schema generation</td>
  </tr>
</table>

</div>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## System Architecture

```mermaid
graph TD
    A[User Input] --> B[Search Query Agent]
    B --> C[Search Engine Agent]
    C --> D[Web Scraping Agent]
    D --> E[Report Author Agent]
    E --> F[Report Critic Agent]
    F --> G[Final Report]
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Agent Responsibilities

<div align="center">

<table>
  <tr>
    <th>Agent</th>
    <th>Role</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>🔍 <b>Search Query Agent</b></td>
    <td>Generates optimized search queries</td>
    <td>JSON search queries</td>
  </tr>
  <tr>
    <td>🌐 <b>Search Engine Agent</b></td>
    <td>Searches across multiple platforms</td>
    <td>Filtered search results</td>
  </tr>
  <tr>
    <td>🕸️ <b>Web Scraping Agent</b></td>
    <td>Extracts product details</td>
    <td>Structured product data</td>
  </tr>
  <tr>
    <td>✍️ <b>Report Author Agent</b></td>
    <td>Creates draft procurement report</td>
    <td>Initial report draft</td>
  </tr>
  <tr>
    <td>🧠 <b>Report Critic Agent</b></td>
    <td>Quality assurance and feedback</td>
    <td>Detailed critique</td>
  </tr>
</table>

</div>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📊 AgentOps Monitoring Dashboard
Real-time Monitoring Features

+ 🖥️ Session Replay: Watch exact agent execution sequences

+ 📈 Performance Metrics: Track agent response times and success rates

+ 🔍 Error Analysis: Detailed error tracking and debugging

+ 📋 Agent Analytics: Individual and team performance insights

<img width="1444" height="798" alt="image" src="https://github.com/user-attachments/assets/218499c6-370c-4a2c-88c9-e7c9b5e07538" />



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation & Setup

Clone the repository:
```bash
git clone https://github.com/username/multi-ai-agent.git
cd multi-ai-agent

+ Create a virtual environment and install dependencies:
pip install -r requirements.txt

+ Add your API keys in .env:
AGENTOPS_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
-tools key : 
TAVILY_API_KEY=your_key_here
SGAI_API_KEY=your_key_here

+ Run the system:
python main.py


+ Project Structure

```markdown
manage-AI-agents/
├── Multi_Agent/
│ ├── search_query_agent.py
│ ├── search_engine_agent.py
│ ├── web_scraping_agent.py
│ ├── report_author_agent.py
│ └── report_critic_agent.py
├── agents/
│ └── Manage_agents.ipynb
├── main.py
├── requirements.txt
└── README.md

نسخ الكو

