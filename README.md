# Bengal RAWR
### Academic Conflict & Workload Intelligence System

> Automated academic workload analysis pipeline that extracts assessment schedules from course syllabi, detects calendar/workload bottlenecks across concurrent courses, and surfaces timeline insights via an interactive dashboard.

---

## 🏗️ System Architecture

```
[ Client: Vite / React Dashboard (bengal-rawr-dashboard) ]
                        │  (REST / JSON)
                        ▼
[ API Gateway & Application: Django REST Framework (DRF) ]
   ├── Document Ingestion Engine (pdfplumber, python-docx, pytesseract fallback)
   ├── Information Extraction Pipeline
   │    ├── Heuristic Parser (Regex date extractor + keyword taxonomy)
   │    └── ML Classifier Fallback (scikit-learn Logistic Regression, confidence-gated)
   ├── Vector Embedding & Retrieval Layer (sentence-transformers / all-MiniLM-L6-v2)
   └── Conflict & Workload Engine (Rolling weekly/daily load accumulator, collision detector)
                        │
                        ▼
[ Persistence Layer: PostgreSQL (pgvector) / SQLite ]
   ├── Relational: Courses, SyllabusFiles, Events, ConflictWeeks
   └── Vector Store: Document chunk embeddings (384-dim, cosine distance)
```

---

## 🎯 Project Scopes

### In-Scope
- **Document Processing:** Ingestion and OCR parsing of `.pdf`, `.docx`, and `.txt` files up to 10 MB.
- **Extraction & Classification:** Hybrid rule-based + ML classification for academic events and deadlines.
- **Vector Search (RAG):** Semantic document chunk retrieval via cosine similarity (`pgvector` / dense embeddings).
- **Conflict Analysis:** Per-course and cross-course collision tracking with severity classification.
- **API & UI:** DRF CRUD endpoints, conflict calculation APIs, and a Vite/React analytics dashboard.

### Out-of-Scope (Roadmap / Future Work)
- Direct LMS sync (Canvas / Blackboard / Moodle API integrations).
- Calendar export integrations (two-way Google Calendar / iCal sync).
- Multi-tenant enterprise role-based access control (RBAC).
- Distributed async task queue execution (Celery / Redis workers for background batch PDF parsing).

---

## 🚀 Quick Start

### 1. Backend Setup (Django)

```bash
cd bengal_rawr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

cd backend
python manage.py migrate
python manage.py runserver 8000
```

### 2. Frontend Setup (React / Vite)

```bash
cd bengal-rawr-dashboard
npm install
npm run dev
```

Open:
- **Dashboard UI**: http://localhost:3000
- **Django Admin**: http://localhost:8000/admin
- **API Root**: http://localhost:8000/api/v1/

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/upload-syllabus/` | Upload and process a syllabus file |
| `GET` | `/api/v1/courses/` | List all courses |
| `POST` | `/api/v1/courses/` | Create a course |
| `GET` | `/api/v1/events/` | List all events (supports filters) |
| `GET` | `/api/v1/events/?course_id=1` | Filter events by course |
| `GET` | `/api/v1/events/?event_type=midterm` | Filter by event type |
| `POST` | `/api/v1/events/<id>/verify/` | Mark event as human-verified |
| `GET` | `/api/v1/conflicts/` | List conflict weeks |
| `POST` | `/api/v1/conflicts/analyze/` | Re-run full conflict analysis |
| `GET` | `/api/v1/dashboard/` | Dashboard summary data |
| `GET` | `/api/v1/dashboard/heatmap/` | Full heatmap dataset |
| `GET` | `/api/v1/dashboard/weekly-workload/` | Weekly bar chart data |

### Upload Example (curl)
```bash
curl -X POST http://localhost:8000/api/v1/upload-syllabus/ \
  -F "file=@CS101_Syllabus.pdf" \
  -F "course_name=Introduction to Computer Science" \
  -F "course_code=CS101" \
  -F "professor=Dr. Zhang" \
  -F "semester=Spring 2026"
```

### Response
```json
{
  "status": "processed",
  "syllabus_id": 1,
  "course_id": 1,
  "course_name": "Introduction to Computer Science",
  "events_extracted": 12,
  "conflicts_detected": 2
}
```

---

## Workload Weight System

| Event Type | Weight |
|------------|--------|
| Homework / Reading | 1 |
| Assignment / Lab / Quiz | 2 |
| Presentation / Project | 3 |
| Midterm / Exam | 5 |
| Final Exam | 8 |

**Conflict threshold**: ≥ 7 points/week → Warning  
**Critical threshold**: ≥ 12 points/week → Critical 🔥

---

## Module Details

### Module 1 — Document Parser (`core/date_parser/document_parser.py`)
- Handles PDF (pdfplumber), TXT, DOCX
- OCR fallback via pytesseract for scanned PDFs
- Text cleaning: removes page numbers, headers, whitespace normalization

### Module 2 — NLP Engine (`core/nlp_engine/engine.py`)
- spaCy NER for DATE entity extraction (high recall)
- Regex date patterns (ISO, slashes, month names, ordinals)
- Keyword taxonomy for 10 event types
- Context window scanning (±2 lines) for orphaned dates

### Module 3 — Event Structuring
- Converts raw NLP output → structured JSON with course, type, date, weight
- Deduplication on (course, type, date) triple

### Module 4 — Conflict Detection (`core/nlp_engine/conflict_detector.py`)
- Weekly aggregation via ISO calendar weeks
- Daily aggregation for single-day overload detection
- Cross-course exam collision detection
- Consecutive heavy-week streak detection

### Module 5 — ML Classifier (`core/event_classifier/classifier.py`)
- Scikit-learn Logistic Regression on hand-crafted features
- Bootstrap training data built-in (27 labeled examples)
- Retrains from human-verified DB events via `retrain_from_db()`
- Persists model to disk (pickle)

### Module 6 — Django Backend
- DRF REST API with full CRUD
- Bulk event creation via `bulk_create`
- Atomic transactions for data integrity
- File validation: extension + 10MB size limit

### Module 7 — React Dashboard
- Heatmap (GitHub-contribution style, 26 weeks)
- Weekly bar chart with conflict indicators
- Stat cards: courses, events, conflicts, critical weeks
- Upcoming events panel (next 30 days)
- Drag-and-drop upload with progress feedback

---

## Project Structure

```
bengal_rawr/
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── apps/
│   │   └── syllabus/          # Main app (models, views, serializers, admin)
│   │       ├── models.py      # Course, SyllabusFile, Event, ConflictWeek
│   │       ├── views.py       # All API views
│   │       ├── serializers.py # DRF serializers
│   │       ├── urls.py        # URL routing
│   │       └── admin.py       # Rich admin interface
│   └── core/
│       ├── nlp_engine/
│       │   ├── engine.py          # SyllabusNLPEngine
│       │   └── conflict_detector.py  # ConflictDetectionEngine
│       ├── date_parser/
│       │   └── document_parser.py    # DocumentParser (PDF/TXT/DOCX)
│       └── event_classifier/
│           └── classifier.py         # ML EventClassifier
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Full dashboard UI
│   │   └── index.js
│   └── public/index.html
├── requirements.txt
└── scripts/setup.sh
```

---

## Phase 2 Roadmap

- [ ] BERT fine-tuned event classifier
- [ ] Email/calendar export (ICS format)
- [ ] Multi-user authentication
- [ ] Celery async processing for large uploads
- [ ] PostgreSQL migration scripts
- [ ] Docker Compose for one-command deployment
- [ ] Study schedule suggestions based on conflict data
