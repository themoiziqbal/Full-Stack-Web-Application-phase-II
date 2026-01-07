# Research: Phase II – Full-Stack Web Application

## Phase 0: Outline & Research

### Decision: JWT Verification on FastAPI
**Rationale**: To ensure secure communication between the Next.js frontend and FastAPI backend, we will use JWT verification.
**Alternatives Considered**: Session-based auth in FastAPI (rejected as it complicates cross-domain/serverless scaling).

### Decision: Better Auth Integration
**Rationale**: Better Auth provides a high-level API for Next.js and issues industry-standard JWTs that are easily verifiable on the backend.
**Alternatives Considered**: Clerk, Auth0 (rejected to avoid external dependency costs and maintain custom database control).

### Decision: SQLModel with Neon
**Rationale**: SQLModel combines SQLAlchemy and Pydantic, providing a unified model for DB schema and API validation, which perfectly fits our FastAPI + PostgreSQL stack.
**Alternatives Considered**: Prisma (Python support is limited), Tortoise ORM (SQLAlchemy ecosystem is more mature for migrations).
