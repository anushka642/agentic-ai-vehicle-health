class AlertAgent:
    def send_email(self, vehicle_id, issue):
        print("📧 EMAIL ALERT")
        print(f"To: customer{vehicle_id}@example.com")
        print("Subject: Vehicle Failure Alert")
        print(f"Message: Potential issue detected - {issue}")
        print("-" * 40)

    def send_sms(self, vehicle_id, issue):
        print("📱 SMS ALERT")
        print(f"To: +91-9XXXXXXXX{vehicle_id}")
        print(f"Message: Alert! {issue}. Please schedule service.")
        print("-" * 40)
