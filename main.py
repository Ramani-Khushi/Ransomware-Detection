from detector import RansomwareDetector
from response import respond_to_risk
from visualize import plot_file_activity
from datetime import datetime

# Initialize detector
detector = RansomwareDetector()

# Log file
log_file = open("logs.txt", "a")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] {message}\n")

print("===================================")
print(" RANSOMWARE DETECTION DEMO SYSTEM ")
print("===================================")

print("\nSelect activity type:")
print("1. Normal User Activity")
print("2. Ransomware Attack Simulation")

choice = input("Enter choice (1 or 2): ")

directories = ["Documents", "Desktop", "Downloads"]

if choice == "1":
    log("Normal user activity started")
    for i in range(5):
        detector.add_event(
            process="explorer.exe",
            directory="Documents",
            extension_changed=False,
            cpu_usage=10
        )
    process = "explorer.exe"

elif choice == "2":
    log("Ransomware simulation started")
    for i in range(25):
        detector.add_event(
            process="unknown.exe",
            directory=directories[i % 3],
            extension_changed=True,
            cpu_usage=85
        )
    process = "unknown.exe"

else:
    print("Invalid choice")
    exit()

# Risk evaluation
risk = detector.get_risk_level()
print(f"\n📊 Calculated Risk Level: {risk}")
log(f"Risk level calculated: {risk}")

# Response
respond_to_risk(risk, process)
log(f"Response executed for risk level: {risk}")

# Visualization
plot_file_activity(detector.events)
log("Graph displayed")

log_file.close()
