from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict

from app.services.api_service import APIService
from app.models.schemas import TopUserResponse, TopPostResponse, Post

# Create the API service
api_service = APIService()

# Initialize FastAPI app
app = FastAPI(
    title="Social Media Analytics",
    description="Social Media Analytics API that delivers real-time analytical insights",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint returning service information."""
    return {
        "message": "Welcome to the Social Media Analytics API",
        "endpoints": [
            "/users - Get top users with the most posts",
            "/posts - Get top/latest posts"
        ]
    }


@app.get("/users", response_model=TopUserResponse)
async def get_top_users():
    """Get the top 5 users with the highest number of posts."""
    top_users = api_service.get_top_users(limit=5)
    return {"top_users": top_users}


@app.get("/posts", response_model=TopPostResponse)
async def get_posts(type: str = Query(..., description="Type of posts to retrieve", enum=["latest", "popular"])):
    """
    Get posts based on the query parameter.
    - popular: Posts with the maximum number of comments
    - latest: Latest 5 posts
    """
    if type.lower() == "popular":
        posts = api_service.get_popular_posts()
    elif type.lower() == "latest":
        posts = api_service.get_latest_posts(limit=5)
    else:
        raise HTTPException(status_code=400, detail="Invalid type parameter. Must be 'latest' or 'popular'")
    
    return {"posts": posts}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 