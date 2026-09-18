\# AI Service Desk Copilot



A knowledge-grounded Generative AI assistant for IT Service Desk incident analysis and approved troubleshooting guidance.



\## 🎯 Portfolio Project



This project demonstrates how \*\*Generative AI and Retrieval-Augmented Generation (RAG)\*\* can assist IT Service Desk analysts while keeping troubleshooting guidance grounded in approved Knowledge Base content.



\### Key Capabilities



\* 🔹 \*\*Knowledge-Grounded Incident Analysis\*\*

\* 🔹 \*\*Semantic Knowledge Base Retrieval\*\*

\* 🔹 \*\*Similarity Threshold Decisioning\*\*

\* 🔹 \*\*Controlled AI Abstention\*\*

\* 🔹 \*\*AI Guardrails \& Knowledge Restrictions\*\*

\* 🔹 \*\*Prompt Injection Handling\*\*

\* 🔹 \*\*Human-in-the-Loop Service Desk Workflow\*\*



\## Project Overview



\*\*AI Service Desk Copilot\*\* is a knowledge-grounded Generative AI application designed to assist IT Service Desk analysts with incident analysis, knowledge retrieval, and approved troubleshooting guidance.



The application uses \*\*Retrieval-Augmented Generation (RAG)\*\* to retrieve relevant Knowledge Base (KB) content before generating a response.



A retrieval threshold and deterministic decision logic help prevent the system from generating troubleshooting guidance when sufficient approved knowledge is not available.



The project demonstrates how Generative AI can support Service Desk operations while maintaining \*\*knowledge grounding, AI guardrails, controlled responses, and human oversight\*\*.



\---



\## Problem Statement



IT Service Desk analysts often spend significant time:



\* Understanding incident descriptions

\* Identifying the user's intent

\* Searching Knowledge Base articles

\* Validating approved troubleshooting procedures

\* Determining whether an incident can be resolved or should be escalated



A key challenge with Generative AI is preventing unsupported or invented troubleshooting guidance.



This project explores how \*\*RAG, semantic retrieval, similarity scoring, and deterministic decision controls\*\* can be combined to create a more controlled AI-assisted Service Desk workflow.



\---



\## Solution



The AI Service Desk Copilot follows a knowledge-first approach:



1\. The analyst enters an IT incident.

2\. The system analyzes the incident and identifies the relevant intent.

3\. The RAG component searches the approved Knowledge Base.

4\. Retrieved KB content receives a similarity score.

5\. The score is evaluated against a configured retrieval threshold.

6\. If the KB match is sufficient, the relevant approved content is provided to Gemini.

7\. Gemini generates a response grounded in the retrieved KB.

8\. If sufficient knowledge is unavailable, the system abstains from generating unsupported troubleshooting guidance.



This approach helps keep AI responses aligned with the available approved knowledge.



\---



\## Project Architecture



```text

User Ticket

&#x20;    ↓

Streamlit Interface

&#x20;    ↓

Ticket Analysis

&#x20;    ↓

Knowledge Base Retrieval

&#x20;    ↓

Similarity Score

&#x20;    ↓

Threshold Check (0.74)

&#x20;    ↓

Relevant Approved KB

&#x20;    ↓

Gemini LLM

&#x20;    ↓

Grounded Response

&#x20;    ↓

Service Desk Analyst

```



\### Architecture Flow



\*\*1. Incident Input\*\*

The Service Desk analyst enters an incident into the Streamlit application.



\*\*2. Intent Analysis\*\*

The system analyzes the incident to determine what the user is trying to accomplish or what issue is being reported.



\*\*3. Knowledge Retrieval\*\*

The RAG component searches the approved Knowledge Base using semantic similarity.



\*\*4. Similarity Evaluation\*\*

The retrieved knowledge is evaluated using a similarity score.



\*\*5. Threshold Decision\*\*

A configured retrieval threshold of \*\*0.74\*\* determines whether the retrieved knowledge is sufficiently relevant.



\*\*6. Knowledge Grounding\*\*

When the threshold is met, the relevant KB content is supplied to Gemini as the basis for the response.



\*\*7. Response Generation\*\*

Gemini generates a response grounded in the retrieved knowledge.



\*\*8. Abstention / Insufficient Knowledge\*\*

When the available knowledge does not meet the required threshold, the system can return an insufficient-information response rather than inventing troubleshooting procedures.



\---



\## Key Features



\### 🔹 Knowledge-Grounded Troubleshooting



Responses are based on approved Knowledge Base content rather than unrestricted troubleshooting generation.



\### 🔹 RAG-Based Retrieval



Semantic retrieval identifies KB content relevant to the incident before the LLM generates a response.



\### 🔹 Similarity Threshold



A configurable \*\*0.74 retrieval threshold\*\* controls whether retrieved knowledge is considered sufficient for response generation.



\### 🔹 Controlled Abstention



When the Knowledge Base does not contain sufficient information, the system can abstain instead of generating unsupported troubleshooting steps.



\### 🔹 AI Guardrails



The project includes controls designed to reduce unsupported recommendations and prevent the AI from bypassing Knowledge Base restrictions.



\### 🔹 Prompt Injection Handling



The system was tested against attempts to override the Knowledge Base constraints or request unsupported actions.



\### 🔹 Human-in-the-Loop



The AI is designed to assist Service Desk analysts rather than replace analyst validation and escalation decisions.



\---



\## Knowledge Base



The project currently uses approved Markdown-based Knowledge Base articles covering Service Desk scenarios such as:



\* VPN connectivity issues

\* VPN issues following password changes

\* Corporate Wi-Fi connectivity

\* Outlook email issues

\* Corporate password-related issues



The Knowledge Base acts as the controlled source of troubleshooting information.



\---



\## AI Concepts Demonstrated



\* Generative AI

\* Large Language Models (LLMs)

\* Prompt Engineering

\* Retrieval-Augmented Generation (RAG)

\* Semantic Search

\* Embeddings

\* Similarity Scoring

\* Threshold-Based Decision Making

\* Knowledge Grounding

\* AI Guardrails

\* Prompt Injection Handling

\* AI Evaluation and Testing

\* Human-in-the-Loop AI



\## Technical Skills Demonstrated



\### Generative AI



\* Large Language Models (LLMs)

\* Google Gemini

\* Prompt Engineering

\* Grounded Response Generation



\### RAG \& Knowledge Retrieval



\* Retrieval-Augmented Generation (RAG)

\* Semantic Search

\* Embeddings

\* Similarity Scoring

\* Knowledge Base Retrieval

\* Threshold-Based Retrieval Decisions



\### AI Safety \& Controls



\* Knowledge Grounding

\* AI Guardrails

\* Controlled Abstention

\* Prompt Injection Handling

\* Human-in-the-Loop AI



\### Application \& Tools



\* Python

\* Streamlit

\* Markdown Knowledge Bases

\* python-dotenv

\* Git

\* GitHub



\---



\## Evaluation \& Testing



The application was tested using multiple scenarios to evaluate retrieval quality and response behavior.



Testing included:



\* Relevant KB retrieval

\* Below-threshold KB matches

\* Sufficient vs. insufficient knowledge

\* Unrelated incidents

\* Mixed or multi-issue tickets

\* Unsupported troubleshooting requests

\* Prompt-injection-style requests

\* KB grounding and abstention behavior



The evaluation approach focuses on whether the system:



1\. Retrieves relevant approved knowledge.

2\. Applies the configured retrieval threshold.

3\. Avoids unsupported troubleshooting guidance.

4\. Provides an insufficient-information response when appropriate.

5\. Respects Knowledge Base restrictions.



\---



\## Technologies Used



| Technology            | Purpose                                        |

| --------------------- | ---------------------------------------------- |

| \*\*Python\*\*            | Application development and RAG implementation |

| \*\*Streamlit\*\*         | Web-based user interface                       |

| \*\*Google Gemini\*\*     | LLM for analysis and response generation       |

| \*\*Gemini Embeddings\*\* | Semantic similarity and KB retrieval           |

| \*\*RAG\*\*               | Knowledge-grounded response generation         |

| \*\*Markdown\*\*          | Knowledge Base articles                        |

| \*\*python-dotenv\*\*     | Environment variable management                |

| \*\*Git \& GitHub\*\*      | Version control and portfolio management       |



\---



\## Project Structure



```text

AI-Service-Desk-Copilot/

│

├── app.py

├── rag.py

├── requirements.txt

├── .gitignore

│

├── KnowledgeBase/

│   ├── KB001-...

│   ├── KB002-...

│   ├── KB003-...

│   ├── KB004-...

│   ├── KB005-...

│   └── ...

│

└── screenshots/

&#x20;   ├── 01-main-interface.png

&#x20;   ├── 02-kb-grounded-response.png

&#x20;   └── 03-insufficient-kb-response.png

```



> Environment files and the local Python virtual environment are intentionally excluded from the repository.



\---



\## Application Screenshots



\### Main Interface



!\[AI Service Desk Copilot - Main Interface](screenshots/01-main-interface.png)



\### KB-Grounded Response



!\[AI Service Desk Copilot - KB Grounded Response](screenshots/02-kb-grounded-response.png)



\### Insufficient Knowledge Handling



!\[AI Service Desk Copilot - Insufficient Knowledge Response](screenshots/03-insufficient-kb-response.png)



\---



\## How to Run Locally



\### 1. Clone the repository



```bash

git clone https://github.com/jyotikanwarjo/AI-Service-Desk-Copilot.git

cd AI-Service-Desk-Copilot

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the environment



Windows:



```bash

.venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Configure the Gemini API key



Create a local `.env` file:



```text

GEMINI\_API\_KEY=your\_api\_key\_here

```



> Never commit the `.env` file or expose API keys publicly.



\### 6. Run the application



```bash

streamlit run app.py

```



The application will open locally in your browser.



\---



\## Safety \& Guardrails



This project intentionally follows a \*\*knowledge-first\*\* approach.



The application is designed to:



\* Use approved Knowledge Base content as the troubleshooting source.

\* Avoid inventing procedures when sufficient knowledge is unavailable.

\* Apply a retrieval threshold before using retrieved knowledge.

\* Respect restrictions contained within the Knowledge Base.

\* Support analyst review rather than replacing human judgment.



The project is a portfolio demonstration and is \*\*not intended to provide production enterprise IT support without appropriate validation, governance, security controls, and organizational approval.\*\*



\---



\## Future Enhancements



Potential future enhancements include:



\* Integration with enterprise ticketing platforms such as ServiceNow

\* Automated ticket classification

\* Incident priority and impact analysis

\* Improved evaluation dashboards

\* Knowledge Base administration workflows

\* Retrieval and response quality monitoring

\* Human approval workflows

\* Enterprise authentication and authorization

\* Production deployment and observability



\---



\## Portfolio Value



This project demonstrates practical experience applying Generative AI to an enterprise IT Service Desk use case, with emphasis on:



\*\*Business Problem → RAG → Knowledge Grounding → AI Guardrails → Decision Controls → Evaluation → Human Oversight\*\*



It combines Service Desk domain knowledge with practical Generative AI implementation and responsible AI principles.



