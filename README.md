# Multi-AI-Agents

## Build Multi AI Agents and Automate Tasks with CrewAI and AgentOps !

## Overview
<div dir="rtl">

An intelligent multi-agent system built with CrewAI and AgentOps that automates product research, price comparison, and procurement reporting using advanced AI agents working in coordinated workflows.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Key Features

**Smart Search Optimization :**

+ Intelligent Query Generation: AI-powered search query recommendations

+ Multi-Platform Search: Simultaneous search across multiple e-commerce platforms

+ Quality Filtering: Automatic filtering based on confidence scores and ratings

**Advanced Data Extraction:**

+ Structured Product Data: Automated extraction of prices, specifications, and images

+ Price Tracking: Current price, original price, and discount percentages

+ Product Comparison: Side-by-side specification analysis

**Professional Reporting:**

+ Automated Procurement Reports: Comprehensive market analysis

+ Quality Assurance: Multi-stage review and critique process

+ Executive Summaries: Actionable insights for decision makers




## Core Technologies
<p align="center">

| Technology | Purpose | Benefits |
|-------------|----------|-----------|
| **CrewAI** | Multi-agent orchestration framework | Sequential workflow, agent collaboration, task management |
| **AgentOps** | Agent monitoring and analytics | Performance tracking, session replay, debugging tools |
| **Groq** | High-speed LLM inference | Ultra-fast response times, efficient processing |
| **Pydantic** | Data validation and serialization | Type safety, structured outputs, JSON schema generation |
</p>


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



## 📊 AgentOps Monitoring Dashboard

<img width="1444" height="798" alt="image" src="https://github.com/user-attachments/assets/218499c6-370c-4a2c-88c9-e7c9b5e07538" />
