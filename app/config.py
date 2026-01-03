import os

# Application environment
ENV = os.getenv("ENV", "development")


TEST_MODE = os.getenv("TEST_MODE", "0") == "1"


BASE_URL = os.getenv("BASE_URL")
