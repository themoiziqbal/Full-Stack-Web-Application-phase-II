# Tasks: Phase II – Full-Stack Web Application

**Input**: Design documents from `/specs/001-phase-ii-fullstack/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `backend/` and `frontend/` project structures per implementation plan
- [ ] T002 Initialize Python FastAPI project in `backend/` with SQLModel and dependencies
- [ ] T003 Initialize Next.js project in `frontend/` with TypeScript, Tailwind CSS, and Better Auth
- [ ] T004 [P] Configure environment variables and `.env.example` for both projects

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create SQLModel User and Todo entities in `backend/src/models/`
- [ ] T006 Setup Neon PostgreSQL database connection and Alembic migrations in `backend/`
- [ ] T007 [P] Implement JWT verification middleware in `backend/src/api/middleware.py`
- [ ] T008 [P] Setup centralized routing in `backend/src/api/router.py`
- [ ] T009 [P] Initialize Better Auth instance in `frontend/src/lib/auth.ts`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure User Onboarding (Priority: P1) 🎯 MVP

**Goal**: Users can sign up and sign in securely

**Independent Test**: Successfully register a user, log in, and receive a valid JWT token

- [ ] T010 [US1] Build Signup and Signin pages in `frontend/src/app/(auth)/`
- [ ] T011 [US1] Implement auth hooks for frontend state management in `frontend/src/hooks/useAuth.ts`
- [ ] T012 [US1] Create Auth API endpoints in `backend/src/api/routes/auth.py`
- [ ] T013 [US1] Integrate Better Auth frontend client with backend verification

**Checkpoint**: User onboarding is functional and secure

---

## Phase 4: User Story 2 - Basic Task CRUD (Priority: P1) 🎯 MVP

**Goal**: Authenticated users can manage their private tasks

**Independent Test**: Perform full CRUD operations on tasks and verify they persist in Neon DB

- [ ] T014 [US2] Create Task API endpoints in `backend/src/api/routes/tasks.py` (with auth protection)
- [ ] T015 [US2] Build Todo Dashboard page in `frontend/src/app/dashboard/page.tsx`
- [ ] T016 [US2] Implement "Add Task" and "Delete Task" components in `frontend/src/components/todo/`
- [ ] T017 [US2] Implement "Edit Task" modal in `frontend/src/components/todo/TaskEdit.tsx`
- [ ] T018 [US2] Ensure all task operations are filtered by the authenticated `user_id`

**Checkpoint**: Core Todo CRUD is functional for authenticated users

---

## Phase 5: User Story 3 - Task Completion Management (Priority: P2)

**Goal**: Users can toggle task status

- [ ] T019 [US3] Implement `PATCH /api/tasks/{id}/toggle` endpoint in `backend/src/api/routes/tasks.py`
- [ ] T020 [US3] Add status indicators and toggle UI to `frontend/src/components/todo/TaskItem.tsx`

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T021 [P] Finalize responsive Tailwind CSS layouts for mobile/desktop
- [ ] T022 Handle frontend error messages and "No items" empty states
- [ ] T023 [P] Final validation of `quickstart.md` setup steps

---

## Dependencies & Execution Order

1. **Setup (Phase 1)** -> Foundational (Phase 2)
2. **Foundational (Phase 2)** (CRITICAL) -> All User Stories
3. **User Story 1 & 2** are P1 (MVP priority)
4. **Polish** starts after all P1 stories are functional
