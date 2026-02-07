import os
import time

BASE_DIR = "test_files"
EXTENSION = ".locked"

def fake_ransomware():
    print("☠️ Fake ransomware started...")

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if not file.endswith(EXTENSION):
                old_path = os.path.join(root, file)
                new_path = old_path + EXTENSION

                os.rename(old_path, new_path)
                print(f"Encrypted: {old_path}")

                time.sleep(0.2)  # very fast

    print("☠️ Fake ransomware finished.")

if __name__ == "__main__":
    fake_ransomware()
