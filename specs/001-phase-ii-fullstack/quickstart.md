# Quickstart: Phase II – Full-Stack Web Application

## Development Setup

### Backend (FastAPI)
1. Navigate to `/backend`
2. Create and activate a virtual environment
3. Install dependencies: `pip install fastapi uvicorn sqlmodel psycopg2-binary`
4. Set environment variables (see `.env.example`)
5. Run: `uvicorn src.main:app --reload`

### Frontend (Next.js)
1. Navigate to `/frontend`
2. Install dependencies: `npm install`
3. Set environment variables (see `.env.example`)
4. Run: `npm run dev`

## Database Migrations
- Use Alembic to manage schema changes in the `/backend` directory.
- `alembic revision --autogenerate -m "initial Phase II schema"`
- `alembic upgrade head`
