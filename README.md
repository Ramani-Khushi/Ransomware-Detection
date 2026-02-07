# 🛡️ Ransomware Detection & Response System

## 📌 Project Overview
This project simulates how ransomware can be detected using **behavior-based analysis**.
Instead of signatures, it observes how fast files are modified.

## 👥 Team Structure
- Person 1: Detection Logic
- Person 2: Risk Scoring
- Person 3: Visualization
- Person 4: Integration & Presentation

## ⚙️ How It Works
1. Monitor file modification events
2. Count number of files modified per second
3. Assign risk level:
   - LOW → Normal user activity
   - MEDIUM → Suspicious behavior
   - HIGH → Ransomware detected
4. Automatically trigger response actions

## 🚨 Risk Levels
- **LOW** → No action
- **MEDIUM** → Alert + Monitoring
- **HIGH** → System isolation (simulated)

## 📊 Visualization
A graph shows:
- Normal user → slow increase
- Ransomware → sharp spike

## ▶️ How to Run
```bash
python main.py
# Ransomware-Detection
A simulated ransomware detection and response system using behavioral analysis
