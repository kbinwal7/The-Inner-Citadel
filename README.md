# The Inner Citadel

The Inner Citadel is a lightweight conversational AI application designed to provide calm, focused interactions inspired by Stoic philosophy. The system combines modern language models with semantic search to deliver context-aware responses within a minimal and distraction-free interface.

The application is built using **LangChain**, **Flask**, **Pinecone**, and **OpenRouter-compatible language models**, and is optimized for deployment on platforms such as **Hugging Face Spaces**.

---

## Architecture Overview

The project integrates a simple web interface with a **Retrieval-Augmented Generation (RAG)** pipeline.

**Core Workflow:**
1. A user query is submitted through the web interface.
2. The query is converted into embeddings using a compatible embedding model.
3. **Pinecone** retrieves relevant contextual documents from the vector database.
4. The **LLM** (via OpenRouter) generates a response using the retrieved context.
5. The response is returned to the interface in real-time.

---

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Flask |
| **LLM Interface** | OpenRouter |
| **Framework** | LangChain |
| **Vector Database** | Pinecone |
| **Deployment** | Hugging Face Spaces / Render |
| **Frontend** | HTML, CSS |

---

## Features

* **Context-Aware Responses:** Leverages RAG to provide historically grounded Stoic advice.
* **Vector Search:** Efficient document retrieval using Pinecone.
* **Open Access:** Integration with free/open LLMs through OpenRouter.
* **Distraction-Free UI:** A minimal interface designed for reflection.
* **Simple Deployment:** Streamlined workflow for cloud hosting.

---

## Repository Structure

```text
The-Inner-Citadel/
├── app.py              # Main Flask application
├── store_index.py      # Script to process and upload embeddings
├── templates/          # HTML files for the frontend
├── static/             # CSS and JS assets (style.css, script.js)
├── data/               # Source documents (.pdf or .txt)
├── requirements.txt    # Project dependencies
└── .env                # API Keys (ignored by git)
```
I've refined the entire document into a clean, professional, and properly formatted .md file. I used clear heading hierarchies, consistent code blocks, and horizontal rules to ensure it's easy to read and navigate.

Here is the full content for your README.md:

Markdown
# The Inner Citadel

The Inner Citadel is a lightweight conversational AI application designed to provide calm, focused interactions inspired by Stoic philosophy. The system combines modern language models with semantic search to deliver context-aware responses within a minimal and distraction-free interface.

The application is built using **LangChain**, **Flask**, **Pinecone**, and **OpenRouter-compatible language models**, and is optimized for deployment on platforms such as **Hugging Face Spaces**.

---

## Architecture Overview

The project integrates a simple web interface with a **Retrieval-Augmented Generation (RAG)** pipeline.

**Core Workflow:**
1. A user query is submitted through the web interface.
2. The query is converted into embeddings using a compatible embedding model.
3. **Pinecone** retrieves relevant contextual documents from the vector database.
4. The **LLM** (via OpenRouter) generates a response using the retrieved context.
5. The response is returned to the interface in real-time.

---

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Flask |
| **LLM Interface** | OpenRouter |
| **Framework** | LangChain |
| **Vector Database** | Pinecone |
| **Deployment** | Hugging Face Spaces / Render |
| **Frontend** | HTML, CSS |

---

## Features

* **Context-Aware Responses:** Leverages RAG to provide historically grounded Stoic advice.
* **Vector Search:** Efficient document retrieval using Pinecone.
* **Open Access:** Integration with free/open LLMs through OpenRouter.
* **Distraction-Free UI:** A minimal interface designed for reflection.
* **Simple Deployment:** Streamlined workflow for cloud hosting.

---

## Repository Structure

```text
The-Inner-Citadel/
├── app.py              # Main Flask application
├── store_index.py      # Script to process and upload embeddings
├── templates/          # HTML files for the frontend
├── static/             # CSS and JS assets
├── data/               # Source documents (.pdf or .txt)
├── requirements.txt    # Project dependencies
└── .env                # API Keys
```
# Local Setup
1. Clone the Repository
```
git clone [https://github.com/kbinwal7/The-Inner-Citadel.git](https://github.com/kbinwal7/The-Inner-Citadel.git)
cd The-Inner-Citadel
```
3. Create a Virtual Environment
```
conda create -n stoic-bot python=3.10 -y
conda activate stoic-bot
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Environment Configuration
Create a .env file in the project root:
```
touch .env
```
Paste your API keys into the .env file.
5. Indexing Documents
Place your Stoic texts in the data/ folder, then generate and upload embeddings to Pinecone:
```
python store_index.py
```
6. Running the Application
```
python app.py
```
The Flask server will start locally. Open http://127.0.0.1:5000 in your browser to start your session.

Deployment
Ensure the required environment variables are configured in your deployment platform's dashboard.

Hugging Face Spaces: Use the "Secrets" tab to add your API keys.
