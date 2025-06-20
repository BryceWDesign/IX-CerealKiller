"""
Configuration for connecting IX-CerealKiller to the IX-Gibson API.
"""

# Gibson API endpoint
GIBSON_API_URL = "http://localhost:9000/api/query"

# Timeout for HTTP requests to Gibson
REQUEST_TIMEOUT_SECONDS = 5

# Number of retry attempts for failed connections
RETRY_ATTEMPTS = 3

# Time to wait between retries
RETRY_BACKOFF_SECONDS = 2
