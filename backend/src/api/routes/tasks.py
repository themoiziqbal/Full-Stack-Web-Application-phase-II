from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from ..db import get_session
from ..models.models import Todo
from ..api.middleware import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Todo])
def read_tasks(
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    tasks = session.exec(select(Todo).where(Todo.user_id == user_id)).all()
    return tasks

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_task(
    todo: Todo,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    todo.user_id = user_id
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.put("/{task_id}", response_model=Todo)
def update_task(
    task_id: int,
    todo_update: Todo,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    db_todo = session.get(Todo, task_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_todo.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db_todo.title = todo_update.title
    db_todo.description = todo_update.description
    db_todo.completed = todo_update.completed

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    db_todo = session.get(Todo, task_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_todo.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    session.delete(db_todo)
    session.commit()
    return

@router.patch("/{task_id}/toggle", response_model=Todo)
def toggle_task(
    task_id: int,
    session: Session = Depends(get_session),
    user_id: str = Depends(get_current_user)
):
    db_todo = session.get(Todo, task_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_todo.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db_todo.completed = not db_todo.completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo
