# 🏛️ The Inner Citadel

> “Nowhere you can go is more peaceful—more free of interruptions—than your own soul.  
> Retreat into your inner citadel.”  
> — *Marcus Aurelius*

A minimalist chatbot built using **LangChain**, **Flask**, **Pinecone**, and **OpenRouter** — designed to be peaceful, clean, and fast.  
Deployed on **Render.com** ☁️

---

## ⚙️ Features
- 🧠 Context-aware chat powered by LangChain  
- 🌲 Semantic search with Pinecone  
- 🤖 Free LLMs via OpenRouter (e.g., Mistral, Claude, Phi)  
- 💬 Clean minimal UI with HTML + CSS  
- 🚀 Easy one-click Render deployment  

---

## 🧠 Tech Stack
| Layer | Technology |
|-------|-------------|
| Backend | Flask |
| LLM | OpenRouter |
| Framework | LangChain |
| Vector DB | Pinecone |
| Deployment | Render.com |
| Frontend | HTML + CSS |

---

## 🚀 Run Locally

### 1️⃣ Clone the Repository<br>
git clone https://github.com/kbinwal7/The-Inner-Citadel.git <br>
cd The-Inner-Citadel<br>
### 2️⃣ Create a Virtual Environment<br>
conda create -n stoic-bot python=3.10 -y <br>
conda activate stoic-bot<br>
### 3️⃣ Install Requirements<br>
pip install -r requirements.txt <br>
### 4️⃣ Add Environment Variables<br>
Create a .env file in the project root: <br>
PINECONE_API_KEY=your_pinecone_api_key <br>
OPENROUTER_API_KEY=your_openrouter_api_key <br>
### 5️⃣ Store Embeddings <br>
python store_index.py <br>
### 6️⃣ Run the Chatbot <br>
python app.py <br>
### 🌐 Deploy 
## 🧘 Philosophy
“You have power over your mind — not outside events.
Realize this, and you will find strength.”
— Marcus Aurelius
Calm, minimal, and thoughtful — your Inner Citadel awaits.







