# Password Spraying Analysis using Python

This project analyzes authentication logs to identify password spraying
behavior by correlating IP addresses with multiple targeted user accounts.

## What This Tool Does
- Parses authentication logs
- Extracts usernames and source IPs
- Groups login attempts by IP address
- Identifies how many unique users each IP attempts to authenticate as

## Why This Matters
Password spraying attacks use a small number of attempts across many user
accounts to evade brute-force detection.

This project focuses on **behavior analysis**, not alerting.

## Example Log Format
Failed password for root from 10.0.0.9
Failed password for admin from 10.0.0.9
Failed password for test from 10.0.0.9


## Example Output
10.0.0.9 → attempted users: 3
Users: {'root', 'admin', 'test'}


## Skills Demonstrated
- Python log parsing
- Authentication attack analysis
- SOC behavior-based analysis
- Understanding of password spraying techniques
