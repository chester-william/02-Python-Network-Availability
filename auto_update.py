
import time
from app import update_machine_status

while True:
    update_machine_status()
    print("Status updated")
    time.sleep(10)
