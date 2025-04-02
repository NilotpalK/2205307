# app/models/schemas.py
from typing import List, Optional
from pydantic import BaseModel, Field

class AverageResponse(BaseModel):
    """
    Defines the structure of the successful response returned by the API.
    """
    windowPrevState: List[int] = Field(
        ..., # Ellipsis means this field is required
        description="State of the number window before the current request was processed.",
        examples=[[1, 2, 3]]
    )
    windowCurrState: List[int] = Field(
        ...,
        description="State of the number window after the current request was processed.",
        examples=[[2, 3, 5]]
    )
    numbers: List[int] = Field(
        ...,
        description="Numbers received from the third-party server in the current request. Empty if fetch failed or timed out.",
        examples=[[5, 8]]
    )
    avg: Optional[float] = Field(
        None,
        description="Average of the numbers in the 'windowCurrState'. Rounded to 2 decimal places. Returns 0.0 if the window is empty.",
        examples=[3.33]
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "windowPrevState": [1, 3, 5, 7],
                    "windowCurrState": [3, 5, 7, 11, 13],
                    "numbers": [11, 13],
                    "avg": 7.80
                },
                 { 
                    "windowPrevState": [2, 4, 6],
                    "windowCurrState": [2, 4, 6],
                    "numbers": [],
                    "avg": 4.00
                }
            ]
        }
    }


class ErrorDetail(BaseModel):

    detail: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"detail": "Invalid number ID: 'x'. Use 'p', 'f', 'e', or 'r'."}
            ]
        }
    }