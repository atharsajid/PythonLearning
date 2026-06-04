# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("Attempt", attempt + 1 , " - Wait Time -", wait_time)
    time.sleep(wait_time)
    attempt += 1
    wait_time *= 2

