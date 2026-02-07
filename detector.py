# detector.py
import time

class RansomwareDetector:
    def __init__(self):
        # Stores recent file activity events
        # Each event: (timestamp, process, directory, extension_changed, cpu_usage)
        self.events = []

        # Time window for early detection
        self.TIME_WINDOW = 30  # seconds

        # Thresholds
        self.FILE_THRESHOLD = 20
        self.DIR_THRESHOLD = 3
        self.EXT_THRESHOLD = 10
        self.CPU_THRESHOLD = 70

        # Trusted processes (whitelist)
        self.trusted_processes = [
            "word.exe",
            "excel.exe",
            "chrome.exe",
            "explorer.exe"
        ]

    # -------------------------------
    # Add file system event
    # -------------------------------
    def add_event(self, process, directory, extension_changed=False, cpu_usage=0):
        current_time = time.time()
        self.events.append(
            (current_time, process, directory, extension_changed, cpu_usage)
        )
        self._clean_old_events()

    # -------------------------------
    # Remove events outside time window
    # -------------------------------
    def _clean_old_events(self):
        now = time.time()
        self.events = [
            event for event in self.events
            if now - event[0] <= self.TIME_WINDOW
        ]

    # -------------------------------
    # RULE 1: High file modification rate
    # -------------------------------
    def rule_high_file_rate(self):
        return len(self.events) >= self.FILE_THRESHOLD

    # -------------------------------
    # RULE 2: Multiple directory access
    # -------------------------------
    def rule_multiple_directories(self):
        directories = set(event[2] for event in self.events)
        return len(directories) >= self.DIR_THRESHOLD

    # -------------------------------
    # RULE 3: Unknown process
    # -------------------------------
    def rule_unknown_process(self):
        processes = set(event[1] for event in self.events)
        for process in processes:
            if process not in self.trusted_processes:
                return True
        return False

    # -------------------------------
    # RULE 4: Rapid extension change
    # -------------------------------
    def rule_extension_change(self):
        count = sum(1 for event in self.events if event[3])
        return count >= self.EXT_THRESHOLD

    # -------------------------------
    # RULE 5: High CPU usage
    # -------------------------------
    def rule_high_cpu_with_files(self):
        for event in self.events:
            if event[4] >= self.CPU_THRESHOLD:
                return True
        return False

    # -------------------------------
    # RISK LEVEL CALCULATION
    # -------------------------------
    def get_risk_level(self):
        file_count = len(self.events)
        directories = set(event[2] for event in self.events)

        if file_count >= 20 and len(directories) >= 3:
            return "HIGH"
        elif file_count >= 10 or len(directories) >= 2:
            return "MEDIUM"
        else:
            return "LOW"

    # -------------------------------
    # FINAL RANSOMWARE DECISION
    # -------------------------------
    def detect_ransomware(self):
        rule1 = self.rule_high_file_rate()
        rule2 = self.rule_multiple_directories()
        rule4 = self.rule_extension_change()
        rule5 = self.rule_high_cpu_with_files()

        # Strong ransomware signal
        if rule1 and rule2:
            return True

        # Extended detection
        if rule1 and (rule4 or rule5):
            return True

        return False
