from datetime import datetime


with open('timestamp', 'r') as timestamp:
    updated = datetime.fromisoformat(timestamp.readline())
    current = datetime.today()
    print((current - updated).days < 8)
