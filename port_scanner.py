import socket

print("=" * 40)
print("      Network Port Scanner")
print("=" * 40)

target = input("Enter IP Address: ")

#port = int(input("Enter Port Number: "))
#ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Alternate"
}

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    result = scanner.connect_ex((target, port))
    service = services.get(port, "Unknown Service")
    if result == 0:
       print(f"Port {port} is OPEN ({service})")
    else:
       print(f"Port {port} is CLOSED ({service})")

    scanner.close()
