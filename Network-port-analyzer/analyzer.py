import csv
from collections import Counter

PORT_SERVICES = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "53": "DNS",
    "80": "HTTP",
    "443": "HTTPS",
    "445": "SMB",
    "3389": "RDP"
}

SUSPICIOUS_PORTS = ["21", "22", "23", "445", "3389"]

port_counter = Counter()
src_ips = set()
dst_ips = set()

with open("sample_logs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        port = row["dst_port"]
        port_counter[port] += 1
        src_ips.add(row["src_ip"])
        dst_ips.add(row["dst_ip"])

print("\n=== Network Port Analysis Report ===\n")

print("Top Ports Used:")
for port, count in port_counter.most_common():
    service = PORT_SERVICES.get(port, "Unknown")
    print(f"Port {port} ({service}) -> {count} connections")

print("\nSuspicious Port Activity:")
for port in SUSPICIOUS_PORTS:
    if port in port_counter:
        print(f"ALERT: Port {port} ({PORT_SERVICES.get(port)}) detected")

print("\nUnique Source IPs:", len(src_ips))
print("Unique Destination IPs:", len(dst_ips))
