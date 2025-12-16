from agents.data_agent import DataAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.customer_agent import CustomerAgent
from agents.scheduling_agent import SchedulingAgent
from agents.feedback_agent import FeedbackAgent
from agents.ueba_agent import UebaAgent
from agents.alert_agent import AlertAgent


data_agent = DataAgent()
diag_agent = DiagnosisAgent()
cust_agent = CustomerAgent()
sched_agent = SchedulingAgent()
fb_agent = FeedbackAgent()
ueba = UebaAgent()
alert_agent = AlertAgent()


ueba.log("System started")

data = data_agent.get_latest_data()

vehicle_id = int(data.get("vehicle_id", -1))

prediction = diag_agent.predict_failure(data)


if prediction == 1:
    ueba.log("Failure predicted")

    issue = "Engine overheating suspected"

    cust_agent.notify_user()

    alert_agent.send_email(vehicle_id, issue)
    alert_agent.send_sms(vehicle_id, issue)


    slot = sched_agent.book_service()
    fb_agent.generate_rca(data, slot)

else:
    ueba.log("Vehicle healthy")

print("Workflow completed.")
