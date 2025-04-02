# Social Media Analytics Microservice

A FastAPI microservice that provides real-time analytics on social media data.

## Features

- Get top 5 users with the highest number of posts
- Get popular posts (posts with maximum comments)
- Get latest 5 posts in real-time

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python run.py
```

2. Access the API at http://localhost:8000

## API Endpoints

### GET /users
Returns the top 5 users with the highest number of posts.

### GET /posts?type=popular
Returns posts with the maximum number of comments.

### GET /posts?type=latest
Returns the latest 5 posts.

## Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Architecture

- The microservice uses FastAPI for the web framework
- Data is fetched from an external social media API
- LRU caching is used to minimize API calls to the test server
- The application is designed to handle unsorted data and efficiently process it 