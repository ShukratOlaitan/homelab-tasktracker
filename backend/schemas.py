from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    status: str = "todo"


class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True
