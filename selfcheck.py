from datetime import datetime
from pytz import timezone


with open('timestamp', 'r') as timestamp:
    updated = datetime.fromisoformat(timestamp.readline())
    current = datetime.now(timezone('America/Vancouver'))
    print((current - updated).days < 8)
