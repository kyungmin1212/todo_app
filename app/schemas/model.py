from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {"examples": [{"id": 1, "item": "Example Schema!"}]}
    }


class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [{"item": "Read the next chapter of the book"}]
        }
    }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {"item": "Example Schema 1!"},
                        {"item": "Example Schema 2!"},
                    ]
                }
            ]
        }
    }
