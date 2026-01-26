Failed_attempts = {}

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split()[-1]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print(failed_attempts)

THRESHOLD = 3

for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        print(f"ALERT 🚨 Brute-force detected from {ip} ({count} attempts)")

print("\n--- SSH Brute-Force Detection Report ---")

for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        print(f"[ALERT] {ip} → {count} failed attempts")
    else:
        print(f"[INFO] {ip} → {count} failed attempts")
