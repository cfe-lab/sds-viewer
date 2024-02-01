import time
from datetime import datetime


with open('timestamp', 'r') as timestamp:
    updated = float(timestamp.readline())
    current = time.time()
    print((current - updated) / 86400 < 8)
