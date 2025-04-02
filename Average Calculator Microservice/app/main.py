from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional
import statistics
from collections import deque

from .models import NumberResponse
from .services import fetch_numbers

app = FastAPI(title="Average Calculator Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Window size for storing numbers
WINDOW_SIZE = 10

# Store for different number types
number_store: Dict[str, deque] = {
    "p": deque(maxlen=WINDOW_SIZE),  # Prime numbers
    "f": deque(maxlen=WINDOW_SIZE),  # Fibonacci numbers
    "e": deque(maxlen=WINDOW_SIZE),  # Even numbers
    "r": deque(maxlen=WINDOW_SIZE),  # Random numbers
}

# Allowed number types
ALLOWED_NUMBER_TYPES = {"p", "f", "e", "r"}


@app.get("/numbers/{number_id}", response_model=NumberResponse)
async def get_numbers(number_id: str):
    """
    Get numbers for a specific number type and calculate average.
    
    Args:
        number_id: Type of numbers to fetch ('p', 'f', 'e', 'r')
    
    Returns:
        Response containing window states, numbers, and average
    """
    if number_id not in ALLOWED_NUMBER_TYPES:
        raise HTTPException(status_code=400, detail="Invalid number type. Must be one of 'p', 'f', 'e', 'r'")
    
    window_prev_state = list(number_store[number_id])
    
    new_numbers = await fetch_numbers(number_id)
    
    if new_numbers:
        for num in new_numbers:
            if num not in number_store[number_id]:
                number_store[number_id].append(num)
    
    window_curr_state = list(number_store[number_id])
    
    if window_curr_state:
        avg = round(statistics.mean(window_curr_state), 2)
    else:
        avg = 0.0
    
    response = NumberResponse(
        windowPrevState=window_prev_state,
        windowCurrState=window_curr_state,
        numbers=new_numbers if new_numbers else [],
        avg=avg
    )
    
    return response 