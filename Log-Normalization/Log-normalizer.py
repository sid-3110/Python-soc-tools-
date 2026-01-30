file = open("auth.log", "r")

print("🔧 Normalized Authentication Logs\n")

for line in file:
    parts = line.split()

    if "Failed password" in line:
        event_type = "FAILED_LOGIN"
        user = parts[3]
        ip = parts[-1]

    elif "Accepted password" in line:
        event_type = "SUCCESS_LOGIN"
        user = parts[3]
        ip = parts[-1]

    else:
        continue

    print(f"EVENT={event_type} | USER={user} | IP={ip}")

file.close()
