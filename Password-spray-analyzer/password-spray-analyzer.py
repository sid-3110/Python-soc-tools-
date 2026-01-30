ip_users = {}

file = open("auth.log", "r")

for line in file:
    if "Failed password" in line:
        parts = line.split()
        user = parts[3]      # username
        ip = parts[-1]       # IP address

        if ip not in ip_users:
            ip_users[ip] = set()

        ip_users[ip].add(user)

file.close()

print("🔍 Password Spraying Analysis\n")

for ip in ip_users:
    users = ip_users[ip]
    print(ip, "→ attempted users:", len(users))
    print("Users:", users)
    print()
