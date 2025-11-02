# app/routes.py
from app import APIRouter, HTTPException
from .models import User
from .db import get_table

router = APIRouter()
table = get_table()

@router.post("/users")
def create_user(user: User):
    table.put_item(Item=user.dict())
    return {"message": "User added", "user": user}

@router.get("/users/{user_id}")
def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    item = response.get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="User not found")
    return item

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    table.delete_item(Key={"user_id": user_id})
    return {"message": f"User {user_id} deleted"}
