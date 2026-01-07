# Evolution of Todo Project

**One-line Description:** Full-Stack Todo App: Phase I console app & Phase II web application with Next.js frontend, FastAPI backend, Neon PostgreSQL, and Better Auth authentication.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Phases](#phases)  
   - [Phase I: In-Memory Console App](#phase-i-in-memory-console-app)  
   - [Phase II: Full-Stack Web App](#phase-ii-full-stack-web-app)  
3. [Technology Stack](#technology-stack)  
4. [Architecture](#architecture)  
5. [Setup Instructions](#setup-instructions)  
   - [Phase I Setup](#phase-i-setup)  
   - [Phase II Setup](#phase-ii-setup)  
6. [Usage](#usage)  
7. [Development Workflow](#development-workflow)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## Project Overview
The "Evolution of Todo" project is a spec-driven development initiative demonstrating how a simple in-memory console todo app (Phase I) evolves into a modern full-stack web application (Phase II) with persistent storage and authentication. All development follows **Agentic Dev Stack Workflow** using **Claude Code + Spec-Kit Plus**.

---

## Phases

### Phase I: In-Memory Console App
**Objective:** Build a command-line todo application storing tasks in memory.  

**Features:**
- Add tasks with title and description  
- View all tasks with status indicators  
- Update task details  
- Delete tasks by ID  
- Mark tasks as complete/incomplete  

**Constraints:**
- No databases, files, or web interfaces  
- Single-user only  
- CLI menu-driven interface  

**Deliverables:**
- `/src` Python source code  
- Specs in `/specs/history`  
- Constitution, README.md, and CLAUDE.md  

---

### Phase II: Full-Stack Web App
**Objective:** Transform Phase I into a multi-user full-stack web app with persistent storage and authentication.  

**Features:**
- RESTful API endpoints (CRUD for todos)  
- User signup/signin using Better Auth  
- Associate todos with authenticated users  
- Responsive Next.js frontend  
- Data persistence in Neon Serverless PostgreSQL  

**API Endpoints:**

| Method | Endpoint                         | Description               |
|--------|---------------------------------|---------------------------|
| GET    | /api/{user_id}/tasks             | List all tasks           |
| POST   | /api/{user_id}/tasks             | Create a new task        |
| GET    | /api/{user_id}/tasks/{id}        | Get task details         |
| PUT    | /api/{user_id}/tasks/{id}        | Update a task            |
| DELETE | /api/{user_id}/tasks/{id}        | Delete a task            |
| PATCH  | /api/{user_id}/tasks/{id}/complete | Toggle completion      |

**Security:**
- JWT-based authentication for API requests  
- Each user sees only their own todos  
- Requests without token return 401 Unauthorized  

---

## Technology Stack

| Layer       | Technology                        |
|------------|----------------------------------|
| Frontend    | Next.js 16+ (App Router), TypeScript, Tailwind CSS |
| Backend     | Python FastAPI                   |
| ORM         | SQLModel                         |
| Database    | Neon Serverless PostgreSQL       |
| Authentication | Better Auth (JWT)             |
| Dev Stack   | Claude Code + Spec-Kit Plus      |

---

## Architecture
- **Phase I:** Single Python program with in-memory storage and CLI  
- **Phase II:** Full-stack web app (Next.js frontend + FastAPI backend)  
- **Database:** User and Todo tables, tasks scoped by user  
- **Authentication:** Better Auth issuing JWT tokens, verified by FastAPI backend  

---

## Setup Instructions

### Phase I Setup
```bash
cd phase1
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python src/main.py
Phase II Setup
bash
Copy code
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev

# Or run both with Docker
docker-compose up
Usage
Phase I (Console)
Menu-driven interface to Add, View, Update, Delete, and Mark tasks

Phase II (Web)
Sign up / Sign in

View todos

Add, Edit, Delete todos

Toggle completion status

Responsive UI for desktop and mobile

Development Workflow
Read the relevant spec: @specs/features/<feature>.md

Follow the global constitution: speckit.constitution

Implement according to plan: speckit.plan

Complete atomic tasks: speckit.tasks

Implement using Claude Code: speckit.implement

Test and iterate

Contributing
Follow Spec-Driven Development principles

Update specs before implementing changes

No direct code changes without approved tasks

Maintain clean architecture and separation of concerns

License
MIT License
