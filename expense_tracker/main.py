from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from datetime import datetime

expense_list = []
app = FastAPI()

class Expense(BaseModel):
    name: str
    description: str
    amount: float
    category: str
    sub_category: str
    timestamp: datetime
@app.post("/expenses", response_model=Expense)
def add_expense(expense: Expense):
    expense_list.append(expense)
    return expense

@app.get("/expenses", response_model=List[Expense])
def get_expenses():
    return expense_list

@app.get("/expenses/total")
def get_total():
    total = sum(exp.amount for exp in expense_list)
    return {"total": total}
