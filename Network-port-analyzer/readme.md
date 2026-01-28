# 🛡️ Day 3 – Network Port Analyzer (SOC Tool)

A beginner-friendly Python-based SOC tool that analyzes network traffic logs, maps destination ports to known services, and highlights potentially suspicious port activity. This project focuses on building strong fundamentals in networking, traffic analysis, and SOC-style reporting.

---

## 📌 Project Objective

This tool was created as part of my SOC Analyst learning roadmap (Day 3 – Networking & Ports) to:

* Understand how ports and services appear in network logs
* Practice analyzing traffic from a SOC perspective
* Identify high-risk ports commonly abused by attackers
* Generate a simple SOC-style summary report

---

## ⚙️ Features

* Parses network traffic from CSV log file
* Counts destination port usage
* Maps ports to common services
* Flags suspicious ports (SSH, RDP, SMB, FTP, Telnet)
* Displays unique source and destination IP counts

---

## 📂 Project Structure

```
day3-network-port-analyzer/
│
├── analyzer.py
├── sample_logs.csv
└── README.md
```

---

## 📄 Sample Log Format

```csv
timestamp,src_ip,dst_ip,src_port,dst_port,protocol
2026-01-01,192.168.1.10,8.8.8.8,55321,53,UDP
2026-01-01,10.0.0.5,192.168.1.20,44444,22,TCP
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/yourusername/day3-network-port-analyzer.git
cd day3-network-port-analyzer
```

2. Run the tool:

```
python analyzer.py
```

---

## 🖥️ Example Output

```
=== Network Port Analysis Report ===

Top Ports Used:
Port 53 (DNS) -> 1 connections
Port 22 (SSH) -> 1 connections
Port 3389 (RDP) -> 1 connections
Port 80 (HTTP) -> 1 connections
Port 445 (SMB) -> 1 connections

Suspicious Port Activity:
ALERT: Port 22 (SSH) detected
ALERT: Port 3389 (RDP) detected
ALERT: Port 445 (SMB) detected

Unique Source IPs: 5
Unique Destination IPs: 4
```

---

## 🔍 SOC Use Case

This tool simulates how a SOC Analyst:

* Reviews port activity
* Identifies risky services
* Gains quick visibility into traffic patterns
* Supports triage and investigation

---

## 🚀 Future Improvements

* Threshold-based alerting
* Top source IP detection
* Export report to text file
* Beaconing behavior detection
* Command-line argument support

---

## 👤 Author

Siddharth Kamble
SOC Analyst (L1) Aspirant

---

⭐ If you found this useful, consider giving the repository a star!
