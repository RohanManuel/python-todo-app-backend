from sqlalchemy.orm import Session
from . import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
    return db_todo

def delete_todo(db: Session, id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
