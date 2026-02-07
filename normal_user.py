import time
import os

BASE_DIR = "test_files/Documents"

def normal_user_activity():
    files = os.listdir(BASE_DIR)

    print("👤 Normal user started working...")

    for file in files[:3]:  # user edits only 3 files
        file_path = os.path.join(BASE_DIR, file)

        with open(file_path, "a") as f:
            f.write("\nUser added some text.")

        print(f"Edited file: {file}")
        time.sleep(5)  # slow, human-like delay

    print("✅ Normal user finished work.")

if __name__ == "__main__":
    normal_user_activity()
