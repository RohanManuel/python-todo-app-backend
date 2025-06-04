from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str = ""

class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool

class TodoOut(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
