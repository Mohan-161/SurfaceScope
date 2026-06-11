import nmap

def detect_vulnerabilities(target):

    scanner = nmap.PortScanner()

    print(f"\n[*] Checking vulnerabilities on {target}\n")

    scanner.scan(
        hosts=target,
        arguments='-Pn -sV -p 1514,1515'
    )

    vulnerabilities = []

    for host in scanner.all_hosts():

        for proto in scanner[host].all_protocols():

            for port in scanner[host][proto]:

                service = scanner[host][proto][port]['name']
                product = scanner[host][proto][port].get('product', '')
                version = scanner[host][proto][port].get('version', '')

                vulnerabilities.append(
                    f"Port {port}: {service} {product} {version}"
                )

    if not vulnerabilities:
        vulnerabilities.append(
            "No services identified"
        )

    return vulnerabilities
