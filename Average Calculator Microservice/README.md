# Average Calculator Microservice

A REST API microservice that calculates the average of numbers fetched from third-party servers.

## Features

- REST API endpoint at `/numbers/{number_id}` where `number_id` can be:
  - `p`: Prime numbers
  - `f`: Fibonacci numbers
  - `e`: Even numbers
  - `r`: Random numbers
- Fetches numbers from third-party APIs
- Maintains a sliding window of numbers (size: 10)
- Calculates the average of stored numbers
- Ensures stored numbers are unique
- Ignores responses taking longer than 500ms or encountering errors
- Fast response time, never exceeding 500ms

## Installation

1. Install Python 3.8 or higher
2. Clone this repository
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Service

To start the server on port 9876:

```bash
python server.py
```

The service will be available at http://localhost:9876

## API Endpoint

### GET `/numbers/{number_id}`

- `number_id`: Type of numbers to fetch (`p`, `f`, `e`, `r`)

#### Response Format

```json
{
  "windowPrevState": [],
  "windowCurrState": [1, 3, 5, 7],
  "numbers": [1, 3, 5, 7],
  "avg": 4.00
}
```

- `windowPrevState`: State of the window before the current request
- `windowCurrState`: Current state of the window after the request
- `numbers`: Numbers received from the third-party server
- `avg`: Average of numbers in the current window state 