# response.py

def respond_to_risk(risk_level, process_name="unknown.exe"):
    """
    Take action based on calculated risk level
    """

    if risk_level == "LOW":
        print("\n✅ LOW RISK")
        print("System behavior is normal.")
        print("No action required.")

    elif risk_level == "MEDIUM":
        print("\n⚠️ MEDIUM RISK")
        print(f"Suspicious behavior detected from: {process_name}")
        print("User alerted. System under observation.")

    elif risk_level == "HIGH":
        print("\n🚨 HIGH RISK – RANSOMWARE DETECTED 🚨")
        print(f"Malicious process identified: {process_name}")
        isolate_system()

    else:
        print("\n❓ Unknown risk level")


def isolate_system():
    print("\n🔒 SYSTEM ISOLATION INITIATED")
    print("• Network disconnected (simulated)")
    print("• Malicious process terminated (simulated)")
    print("• File system access blocked (simulated)")
    print("System secured to prevent data loss.\n")
