## 📂 Project Structure

```text
.
├── main/                  # Project configuration (settings, asgi, wsgi)
├── station/               # Core application logic
│   ├── models.py          # Database schema (DataSource, Records, AI Results)
│   ├── tasks.py           # Celery background tasks (File processing)
│   ├── services.py        # AI Service layer (Ollama API integration)
│   ├── views.py           # REST API endpoints (Upload & Chat)
│   └── serializers.py     # Data serialization for DRF
├── docker-compose.yml     # Multi-container orchestration
├── Dockerfile             # Container definition (Python 3.13)
├── requirements.txt       # Project dependencies
└── uploads/               # Persistent storage for uploaded documents

______________________________________________________

---

## 👨‍💻 Author

**Ahmed H.Mahmoud** *python Developer*

A tech enthusiast dedicated to building scalable, AI-driven solutions and optimizing system architectures. With a strong background in Linux environments (Parrot Security OS) and backend engineering, I focus on bridging the gap between sophisticated AI models and practical industrial applications like logistics and shipping.

### 🛠 Tech Toolbox:
- **Languages:** Python (Django, FastAPI), JavaScript (React), Bash Scripting.
- **DevOps & Infrastructure:** Docker & Docker Compose, Linux System Administration, Redis, PostgreSQL.
- **AI/ML:** Local LLM Deployment (Ollama, Llama 3), Data Analysis with Pandas.
- **Interests:** Game Theory, Strategic Analysis, Robotics (ROS 2), and OSINT.

### 🔗 Connect with me:
- **GitHub:** [github.com/ah3139184-prog]

- **Email:** [ah3139184@gmail.com]

______________________________________________________

# BigB: AI-Powered Logistics Data Analyzer 🚢🤖

**BigB** is a high-performance full-stack application designed to analyze logistics and shipping data using local Large Language Models (LLMs). Built with **Django**, **Celery**, and **Ollama**, it allows users to upload shipping data (CSV/Text) and interact with it through an AI-driven chat interface.

## 🚀 Key Features
- **Asynchronous Data Processing:** Large files are handled in the background using Celery and Redis.
- **Local AI Integration:** Powered by **Ollama (Llama 3 / TinyLlama)** for private and secure data analysis.
- **Automated Insights:** Extracts shipping routes, commodity pricing, and logistics trends automatically.
- **Context-Aware Chat:** A specialized endpoint to discuss uploaded data with the AI agent.
- **JWT Security:** Fully secured REST API endpoints.
- **Dockerized Environment:** One-command setup for the entire stack.

## 🏗 System Architecture
The project follows a microservices-based approach:
1. **Django REST Framework:** Handles API requests and user authentication.
2. **Celery Worker:** Manages heavy lifting (File parsing & AI Inference).
3. **Redis:** Acts as the message broker between Django and Celery.
4. **PostgreSQL:** Stores metadata, raw data records, and AI analysis results.
5. **Ollama (Host):** Serves the LLM locally for maximum privacy and performance.



## 🛠 Tech Stack
- **Backend:** Python 3.13, Django, DRF
- **Task Queue:** Celery, Redis
- **Database:** PostgreSQL
- **AI/ML:** Ollama, Pandas
- **DevOps:** Docker, Docker Compose, Parrot OS (Development Env)

## 🚦 Getting Started

### Prerequisites
- Docker & Docker Compose
- [Ollama](https://ollama.com/) installed on the host machine.

### Installation & Setup
**Pull the AI Model:**
   ```bash
   ollama pull tinyllama(model is optinal)

Start the containers:
Bash

sudo docker compose up --build -d

Access the API:
The server will be running at http://localhost:8000.

Endpoint,Method,Description
/api/v1/token/,POST,Obtain JWT Access/Refresh tokens.
/api/v1/upload/,POST,Upload CSV/Text files for AI analysis.
/api/v1/chat/<id>/,POST,Chat with the AI about a specific data source.   

Performance Tuning for Limited Resources

As an IT-focused project, BigB is optimized for environments with limited hardware (tested on Parrot OS):

    Swap Management: Designed to handle memory spikes during LLM inference by utilizing system swap space effectively.

    Efficient Processing: Uses pandas with specific chunking potential and offloads heavy tasks to Celery to keep the API responsive.

    Local Inference: Reduces latency and data costs by using TinyLlama or Phi-3 via Ollama on the host machine


