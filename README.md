\# AI Service Desk Copilot



A knowledge-grounded AI assistant for IT Service Desk incident analysis and troubleshooting.



\## Project Overview



AI Service Desk Copilot is a knowledge-grounded Generative AI application

designed to assist IT Service Desk analysts with incident analysis and

approved troubleshooting guidance.



The application uses Retrieval-Augmented Generation (RAG) to retrieve

relevant knowledge-base content before generating an AI response.



A retrieval threshold and deterministic decision engine help prevent the

system from generating troubleshooting guidance when sufficient approved

knowledge is not available.



\## Problem Statement



IT Service Desk analysts often spend significant time identifying incidents,

searching knowledge-base articles, validating troubleshooting procedures,

and deciding whether an issue can be resolved or should be escalated.



A major challenge is ensuring that AI-generated troubleshooting remains

grounded in approved enterprise knowledge and does not invent unsupported

solutions.



This project explores how Generative AI and Retrieval-Augmented Generation

(RAG) can assist Service Desk analysts while maintaining knowledge grounding,

decision controls, and human oversight.



\## Solution



AI Service Desk Copilot is a knowledge-grounded Generative AI application

designed to assist IT Service Desk analysts with incident analysis and

approved troubleshooting guidance.



The application uses Retrieval-Augmented Generation (RAG) to retrieve

relevant knowledge-base content before generating an AI response.



A retrieval threshold and deterministic decision engine help prevent the

system from generating troubleshooting guidance when sufficient approved

knowledge is not available.



The system can also abstain from generating an AI response when the

retrieved knowledge does not meet the approved similarity threshold.



\## Project Architecture



The AI Service Desk Copilot follows a RAG-based architecture:



User Ticket

&#x20;   ↓

Streamlit Interface

&#x20;   ↓

Ticket Analysis

&#x20;   ↓

Knowledge Base Retrieval

&#x20;   ↓

Similarity Score

&#x20;   ↓

Threshold Check (0.74)

&#x20;   ↓

Relevant Approved KB

&#x20;   ↓

Gemini LLM

&#x20;   ↓

Grounded Response

&#x20;   ↓

Service Desk Analyst



\### Architecture Flow



1\. The Service Desk analyst enters an IT incident into the application.

2\. The system analyzes the incident and identifies the user's intent.

3\. The RAG component searches the approved Knowledge Base.

4\. Retrieved KB content is evaluated using a similarity score.

5\. A retrieval threshold of 0.74 determines whether the KB match is sufficient.

6\. If sufficient information is available, the relevant KB content is provided to Gemini.

7\. Gemini generates a response grounded in the approved KB.

8\. If sufficient KB information is not available, the system returns an insufficient-information response instead of inventing troubleshooting steps.



\## Technologies Used



\- \*\*Python\*\* — Application development and RAG implementation

\- \*\*Streamlit\*\* — Web-based user interface

\- \*\*Google Gemini\*\* — Large Language Model for ticket analysis and response generation

\- \*\*RAG (Retrieval-Augmented Generation)\*\* — Knowledge-grounded response generation

\- \*\*Gemini Embeddings\*\* — Semantic similarity and Knowledge Base retrieval

\- \*\*Markdown (.md)\*\* — Knowledge Base articles

\- \*\*python-dotenv\*\* — Environment variable management

\- \*\*Git \& GitHub\*\* — Version control and project portfolio



\## AI Concepts Demonstrated



\- Generative AI

\- Large Language Models (LLMs)

\- Prompt Engineering

\- Retrieval-Augmented Generation (RAG)

\- Semantic Search

\- Embeddings

\- Similarity Scoring

\- Confidence / Threshold-based Decision Making

\- AI Guardrails

\- Prompt Injection Handling

\- Knowledge Grounding

\- AI Evaluation \& Testing



\## Application Screenshots



\### Main Interface



!\[AI Service Desk Copilot - Main Interface](screenshots/01-main-interface.png)



\### KB-Grounded Response



!\[AI Service Desk Copilot - KB Grounded Response](screenshots/02-kb-grounded-response.png)



\### Insufficient Knowledge Handling



!\[AI Service Desk Copilot - Insufficient Knowledge Response](screenshots/03-insufficient-kb-response.png)

