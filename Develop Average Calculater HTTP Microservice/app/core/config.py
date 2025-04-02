import os

WINDOW_SIZE: int = int(os.getenv("WINDOW_SIZE", 10))
TEST_SERVER_TIMEOUT: float = float(os.getenv("TEST_SERVER_TIMEOUT", 0.5)) # 500 ms is set

QUALIFIER_URLS: dict[str, str] = {
    "p": os.getenv("PRIMES_URL", "http://20.244.56.144/evaluation-service/primes"),
    "f": os.getenv("FIBO_URL", "http://20.244.56.144/evaluation-service/fibo"),
    "e": os.getenv("EVEN_URL", "http://20.244.56.144/evaluation-service/even"),
    "r": os.getenv("RAND_URL", "http://20.244.56.144/evaluation-service/rand"),
}


