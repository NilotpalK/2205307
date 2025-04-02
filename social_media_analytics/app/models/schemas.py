from typing import List, Dict, Optional, Union
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str


class Post(BaseModel):
    id: int
    userid: str
    content: str
    comment_count: Optional[int] = 0


class Comment(BaseModel):
    id: int
    postid: int
    content: str


class UserResponse(BaseModel):
    users: Dict[str, str]


class PostResponse(BaseModel):
    posts: List[Dict]


class CommentResponse(BaseModel):
    comments: List[Dict]


class TopUserResponse(BaseModel):
    top_users: List[Dict[str, Union[str, int]]]


class TopPostResponse(BaseModel):
    posts: List[Post] 