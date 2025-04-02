from typing import List, Optional
from pydantic import BaseModel


class NumberResponse(BaseModel):
    windowPrevState: List[int]
    windowCurrState: List[int]
    numbers: List[int]
    avg: float


class ExternalApiResponse(BaseModel):
    numbers: List[int] 