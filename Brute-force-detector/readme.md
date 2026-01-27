# SSH Brute-Force Detection Tool (Python)

## 📌 Overview

This project is a **Python-based SOC automation tool** designed to detect **SSH brute-force attacks** by analyzing Linux authentication logs.
The script parses log entries, counts failed login attempts per IP address, and generates alerts when suspicious behavior exceeds a defined threshold.

This tool simulates a **real-world SOC detection use case** and demonstrates how Python can be used to automate log analysis and alerting.

---

## 🛡️ SOC Use Case

In Security Operations Centers (SOC), analysts frequently monitor authentication logs to identify brute-force attacks against SSH services.
Manually analyzing large log files is time-consuming and error-prone.

This tool automates:

* Log parsing
* Failed login correlation per IP
* Threshold-based alerting

---

## ⚙️ How the Tool Works

1. Reads a Linux authentication log file (`auth.log`)
2. Identifies failed SSH login attempts
3. Extracts source IP addresses
4. Counts failed attempts per IP using a dictionary
5. Triggers alerts if attempts exceed a defined threshold

---

## 🧠 Detection Logic

* **Indicator:** Repeated `Failed password` entries from the same IP
* **Threshold:** More than 3 failed attempts
* **Outcome:** Alert generated for suspected brute-force activity

---

## ▶️ How to Run

### Prerequisites

* Python 3.x
* Linux / macOS / WSL / Kali Linux

### Steps

```bash
cd brute_force_detector
python3 ssh_bruteforce.py
```

---

## 📊 Sample Output

```
--- SSH Brute-Force Detection Report ---
[ALERT] 10.0.0.5 → 4 failed attempts
[INFO]  10.0.0.7 → 1 failed attempt
```

---

## 🧩 Skills Demonstrated

* Python scripting
* Log file analysis
* Dictionary-based data aggregation
* Threshold-based detection logic
* SOC alerting fundamentals

---

---

## 🚀 Future Improvements

* Regex-based IP extraction
* Time-window based detection
* Export alerts to file (JSON / TXT)
* Integration with SIEM or alerting systems

---

## 📚 Learning Outcome

This project demonstrates how Python can be used to:
