class FeedbackAgent:
    def generate_rca(self, data, slot):
        print("RCA Agent: Generating report")
        print(f"Mileage: {data['mileage']}")
        print(f"Issue: Engine overheating suspected")
        print(f"Service Slot: {slot}")
