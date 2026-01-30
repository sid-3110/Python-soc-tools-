# Authentication Log Normalization using Python

This project focuses on normalizing raw Linux authentication logs into a
structured, consistent format suitable for SOC analysis and SIEM pipelines.

## What This Tool Does
- Parses raw authentication logs
- Identifies login success and failure events
- Extracts usernames and source IPs
- Outputs normalized, machine-readable log entries

## Why Log Normalization Matters
Before detection and alerting, logs must be cleaned and standardized.
This project demonstrates how SOC tools prepare raw logs for analysis
and correlation.

## Example Input
Failed password for root from 10.0.0.5
Accepted password for admin from 10.0.0.8


## Example Output
EVENT=FAILED_LOGIN | USER=root | IP=10.0.0.5
EVENT=SUCCESS_LOGIN | USER=admin | IP=10.0.0.8


## Skills Demonstrated
- Python log parsing
- Log normalization concepts
- SOC / SIEM fundamentals
- Data preparation for detection pipelines
