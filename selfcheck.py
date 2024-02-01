from datetime import datetime


with open('timestamp', 'r') as timestamp:
    updated = datetime.fromtimestamp(float(timestamp.readline()))
    current = datetime.utcnow()
    print((current - updated).days < 8)
