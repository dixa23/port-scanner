import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP address: ")

print("-" * 50)
print("Scanning target:", target)
print("Time started:", datetime.now())
print("-" * 50)

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            service = services.get(port, "Unknown Service")
            output = f"Port {port} open - {service}"
            print(output)
            open_ports.append(output)

        s.close()

    except:
        pass


with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))


with open("scan_results.txt", "w") as file:
    for port in open_ports:
        file.write(port + "\n")


print("\nScan completed.")
print("Results saved to scan_results.txt")