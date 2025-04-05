from pydantic import BaseModel

class Expense(BaseModel):
    name: str
    description: str
    amount: float
    category: str