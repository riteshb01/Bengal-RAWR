# Bengal-RAWR

🐯 Bengal-Rawr: SyllabusGPT
An AI-Powered Academic Logistics Engine for Buffalo State Students.

Bengal-Rawr is a Retrieval-Augmented Generation (RAG) application built to eliminate "Syllabus Shock." By leveraging the massive context window of the Gemini 2.0 API, this tool ingests multiple course syllabi, extracts critical deadlines, and visualizes student academic pressure through an intelligent heatmap.

🚀 The Problem: Syllabus Shock
At the start of every semester, students are bombarded with 15+ page documents for each class. Manually tracking overlapping deadlines across 5-6 courses is error-prone and overwhelming. Bengal-Rawr automates this logistics process, allowing students to focus on learning rather than scheduling.

✨ Key Features
Multi-Modal Extraction: Uses Gemini’s vision capabilities to accurately parse tables and complex layouts in PDF/DocX syllabi.

Academic Pressure Heatmap: A custom algorithm that weights assignments (Quizzes vs. Finals) to visualize "high-stress" weeks.

Relational Metadata Storage: Uses Oracle SQL to securely manage student profiles, course associations, and session logs.

Intelligent Reasoning: Identifies "hidden" conflicts, such as having a major project due in one class the same day as a mid-term in another.

🛠️ The Tech Stack
Brain: Gemini 2.0 Flash API (1M+ Token Context Window)

Backend: Python 3.10 + Flask/FastAPI

Database: Oracle SQL (Metadata/Profiles) + ChromaDB (Vector Embeddings)

Environment: Conda (Isolation & Dependency Management)

Security: python-dotenv for API key masking and .gitignore protocols.

📂 Project Structure
Plaintext
Bengal-Rawr/
├── app.py              # Main application logic
├── extract.py          # Gemini API extraction service
├── database/           # Oracle SQL scripts and connection logic
├── syllabi/            # Temporary storage for processed documents
├── .env                # API Keys (Excluded via .gitignore)
└── environment.yml     # Conda environment configuration
⚙️ Getting Started
1. Prerequisites
Miniconda or Anaconda installed.

A valid Gemini API Key.

2. Environment Setup
Bash
# Clone the repository
git clone https://github.com/your-username/bengal-rawr.git
cd bengal-rawr

# Create the Conda environment
conda env create -f environment.yml
conda activate bengalrawr

# Install dependencies
pip install google-genai python-dotenv
3. Configuration
Create a .env file in the root directory:

Plaintext
GEMINI_API_KEY=your_key_here
ORACLE_DB_URL=your_db_connection_string
🗺️ Roadmap
[x] Initial PDF/DocX Parsing logic.

[x] JSON Schema validation for extracted dates.

[ ] Phase 4: Oracle SQL integration for persistent student profiles.

[ ] Phase 5: Full Web UI with interactive Heatmap.

[ ] Phase 6: Google Calendar API integration for automated sync.

🎓 Academic Context
This project is being developed as a capstone for CIS 494 at Buffalo State University (SUNY). It is intended for presentation at the Student Research and Creativity Conference (SRCC).
