from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone as PineconeLangChain
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from pinecone import Pinecone
from src.prompt import *

app = Flask(__name__)
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

if not PINECONE_API_KEY or not OPENROUTER_API_KEY:
    raise ValueError("Missing one or more required environment variables: PINECONE_API_KEY, OPENROUTER_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)


embeddings = download_hugging_face_embeddings()
if embeddings is None:
    raise ValueError("Failed to initialize HuggingFace embeddings.")

# Connect to existing Pinecone index
index_name = "stoic-chatbot"
index = pc.Index(index_name)

# Create vector store
docsearch = PineconeLangChain(index, embeddings.embed_query, "text")
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})


chatModel = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    model="microsoft/phi-3-mini-128k-instruct",
    temperature=0.7
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])


question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    try:
        msg = request.form.get("msg", "").strip()
        if not msg:
            return "Please provide a message."
        
        response = rag_chain.invoke({"input": msg})
        answer = response.get("answer", "I'm sorry, I couldn't generate a response.")
        return str(answer)
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return "An error occurred while processing your request."

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)