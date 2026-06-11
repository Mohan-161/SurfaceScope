import nmap

def scan_ports(target):

    scanner = nmap.PortScanner()

    print(f"\n[*] Scanning ports on {target}\n")

    scanner.scan(
        hosts=target,
        ports="1-65535"
    )

    results = []

    for host in scanner.all_hosts():

        for proto in scanner[host].all_protocols():

            ports = scanner[host][proto].keys()

            for port in ports:

                state = scanner[host][proto][port]['state']

                if state == "open":

                    results.append(port)

    return results
