import json
import random

class SchedulingAgent:
    def book_service(self):
        slots = json.load(open("data/service_slots.json"))["slots"]
        slot = random.choice(slots)
        print(f"Scheduling Agent: Service booked at {slot}")
        return slot
