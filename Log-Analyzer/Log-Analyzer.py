total_logs = 0
failed_logins = 0
successful_logins = 0
ip_activity = {}

file = open("auth.log", "r")

for line in file:
    total_logs += 1

    parts = line.split()
    ip = parts[-1]

    # Track IP frequency
    if ip in ip_activity:
        ip_activity[ip] += 1
    else:
        ip_activity[ip] = 1

    # Count login types
    if "Failed password" in line:
        failed_logins += 1
    elif "Accepted password" in line:
        successful_logins += 1

file.close()

print("📊 Log Analysis Summary\n")
print("Total log entries:", total_logs)
print("Failed logins:", failed_logins)
print("Successful logins:", successful_logins)

print("\nIP Activity:")
for ip in ip_activity:
    print(ip, "→", ip_activity[ip], "events")
