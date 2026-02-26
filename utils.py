"""
Utility functions for echo server.
Provides logging and validation helpers.
"""

import datetime

def log_message(message: str) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {message}"

def validate_message(message: str) -> bool:
    if not message:
        return False
    if len(message) > 1024:
        return False
    return True
