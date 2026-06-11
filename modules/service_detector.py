import nmap

def detect_services(target):

    scanner = nmap.PortScanner()

    print(f"\n[*] Detecting Services on {target}\n")

    scanner.scan(
        hosts=target,
        arguments='-Pn -sV -p 1514,1515'
    )

    services = []

    for host in scanner.all_hosts():

        for proto in scanner[host].all_protocols():

            for port in scanner[host][proto]:

                service = scanner[host][proto][port]['name']

                product = scanner[host][proto][port]['product']

                version = scanner[host][proto][port]['version']

                services.append(
                    (port, service, product, version)
                )

    return services
