import requests
import os
from typing import Dict, List, Tuple
import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Base API URL
API_BASE_URL = "http://20.244.56.144/evaluation-service"

AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzNjA0ODg3LCJpYXQiOjE3NDM2MDQ1ODcsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjAwMGIyZmI2LTVhZTUtNGUzYy05Y2UzLTUxMjBkNmFkMDQ1YyIsInN1YiI6IjIyMDUzMDdAa2lpdC5hYy5pbiJ9LCJlbWFpbCI6IjIyMDUzMDdAa2lpdC5hYy5pbiIsIm5hbWUiOiJuaWxvdHBhbCBrYXNoeWFwIiwicm9sbE5vIjoiMjIwNTMwNyIsImFjY2Vzc0NvZGUiOiJud3B3cloiLCJjbGllbnRJRCI6IjAwMGIyZmI2LTVhZTUtNGUzYy05Y2UzLTUxMjBkNmFkMDQ1YyIsImNsaWVudFNlY3JldCI6IktQQWR2V1JiSnN3ZnpEZFMifQ.htWeJEIfiBa02yofhkDL_OMx7UYnk4SP7ef4FI2LOLg"


class APIService:
    """Service to handle API requests to the social media platform test server."""

    def __init__(self):
        """Initialize the API service with auth headers."""
        self.headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }

    @lru_cache(maxsize=1)
    def get_all_users(self) -> Dict:
        """
        Get all users from the API.
        """
        try:
            response = requests.get(f"{API_BASE_URL}/users", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching users: {e}")
            return {"users": {}}

    def get_user_posts(self, user_id: str) -> List:
        """Get posts for a specific user."""
        try:
            response = requests.get(f"{API_BASE_URL}/users/{user_id}/posts", headers=self.headers)
            response.raise_for_status()
            return response.json().get("posts", [])
        except requests.RequestException as e:
            logger.error(f"Error fetching posts for user {user_id}: {e}")
            return []

    def get_post_comments(self, post_id: int) -> List:
        """Get comments for a specific post."""
        try:
            response = requests.get(f"{API_BASE_URL}/posts/{post_id}/comments", headers=self.headers)
            response.raise_for_status()
            return response.json().get("comments", [])
        except requests.RequestException as e:
            logger.error(f"Error fetching comments for post {post_id}: {e}")
            return []

    @lru_cache(maxsize=1)
    def get_top_users(self, limit: int = 5) -> List[Dict]:
        """
        Get top users with the most posts.
        """
        users_data = self.get_all_users()
        users = users_data.get("users", {})
        
        user_post_counts = []
        
        for user_id, user_name in users.items():
            posts = self.get_user_posts(user_id)
            user_post_counts.append({
                "id": user_id,
                "name": user_name,
                "post_count": len(posts)
            })
        
        # Sort by post count in descending order
        user_post_counts.sort(key=lambda x: x["post_count"], reverse=True)
        
        # Return top N users
        return user_post_counts[:limit]

    def get_posts_with_comment_counts(self) -> List[Dict]:
        """Get all posts with their comment counts."""
        users_data = self.get_all_users()
        users = users_data.get("users", {})
        
        all_posts = []
        
        # Get all posts from all users
        for user_id in users:
            user_posts = self.get_user_posts(user_id)
            all_posts.extend(user_posts)
        
        # Get comment counts for each post
        for post in all_posts:
            post_id = post.get("id")
            comments = self.get_post_comments(post_id)
            post["comment_count"] = len(comments)
        
        return all_posts

    def get_popular_posts(self) -> List[Dict]:
        """Get posts with the maximum number of comments."""
        posts = self.get_posts_with_comment_counts()
        
        if not posts:
            return []
        
        # Sort posts by comment count in descending order
        posts.sort(key=lambda x: x.get("comment_count", 0), reverse=True)
        
        # Find the maximum comment count
        max_comment_count = posts[0].get("comment_count", 0) if posts else 0
        
        # Filter posts with the maximum comment count
        most_popular_posts = [post for post in posts if post.get("comment_count", 0) == max_comment_count]
        
        return most_popular_posts

    def get_latest_posts(self, limit: int = 5) -> List[Dict]:
        """Get the latest posts."""
        users_data = self.get_all_users()
        users = users_data.get("users", {})
        
        all_posts = []
        
        # Get all posts from all users
        for user_id in users:
            user_posts = self.get_user_posts(user_id)
            all_posts.extend(user_posts)
        
        # Assume higher IDs are newer posts (based on typical database behavior)
        all_posts.sort(key=lambda x: x.get("id", 0), reverse=True)
        
        return all_posts[:limit] 