import httpx
import asyncio
from typing import List, Dict, Optional
from .models import ExternalApiResponse

API_ENDPOINTS = {
    "p": "http://20.244.56.144/evaluation-service/primes",
    "f": "http://20.244.56.144/evaluation-service/fibo",
    "e": "http://20.244.56.144/evaluation-service/even",
    "r": "http://20.244.56.144/evaluation-service/rand"
}

# Authentication token
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzNjAzNDI1LCJpYXQiOjE3NDM2MDMxMjUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjAwMGIyZmI2LTVhZTUtNGUzYy05Y2UzLTUxMjBkNmFkMDQ1YyIsInN1YiI6IjIyMDUzMDdAa2lpdC5hYy5pbiJ9LCJlbWFpbCI6IjIyMDUzMDdAa2lpdC5hYy5pbiIsIm5hbWUiOiJuaWxvdHBhbCBrYXNoeWFwIiwicm9sbE5vIjoiMjIwNTMwNyIsImFjY2Vzc0NvZGUiOiJud3B3cloiLCJjbGllbnRJRCI6IjAwMGIyZmI2LTVhZTUtNGUzYy05Y2UzLTUxMjBkNmFkMDQ1YyIsImNsaWVudFNlY3JldCI6IktQQWR2V1JiSnN3ZnpEZFMifQ.E5AJNGztHsC9azKsq8Bo3y48vygDw4NygUre_H3K3YQ"

REQUEST_TIMEOUT = 0.5  # 500ms


async def fetch_numbers(number_type: str) -> Optional[List[int]]:
    """
    Fetch numbers from external API based on number type.
    
    Args:
        number_type: Type of numbers to fetch ('p', 'f', 'e', 'r')
        
    Returns:
        List of numbers or None if request failed
    """
    if number_type not in API_ENDPOINTS:
        return None
        
    url = API_ENDPOINTS[number_type]
    
    # Set up headers with authentication token
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("numbers", [])
            return None
    except (httpx.RequestError, httpx.TimeoutException, asyncio.TimeoutError):
        return None 