from modules.os_detector import detect_os
from modules.service_detector import detect_services
from modules.vuln_detector import detect_vulnerabilities

target = input("Enter Host IP to Scan: ")

# OS Detection
os_results = detect_os(target)

print("\nDetected Operating Systems:\n")

for os_name in os_results:
    print(os_name)

# Service Detection
service_results = detect_services(target)

print("\nDetected Services:\n")

for service in service_results:
    print(service)

# Vulnerability Detection
vuln_results = detect_vulnerabilities(target)

print("\nDetected Vulnerabilities:\n")

for vuln in vuln_results:
    print(vuln)
