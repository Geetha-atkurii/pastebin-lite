import time
import os
from fastapi import Request

def now_ms(request: Request) -> int:
    """
    Returns current time in milliseconds.
    Uses deterministic time when TEST_MODE=1.
    """
    if os.getenv("TEST_MODE") == "1":
        header = request.headers.get("x-test-now-ms")
        if header:
            return int(header)
    return int(time.time() * 1000)