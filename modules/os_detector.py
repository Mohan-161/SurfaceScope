import nmap

def detect_os(target):

    scanner = nmap.PortScanner()

    print(f"\n[*] Detecting OS on {target}\n")

    scanner.scan(
        hosts=target,
        arguments='-Pn -O'
    )

    os_results = []

    for host in scanner.all_hosts():
        if 'osmatch' in scanner[host]:
            for osmatch in scanner[host]['osmatch']:
                os_results.append(osmatch['name'])

    if not os_results:
        os_results.append(
            "OS Detection Failed (Insufficient fingerprint data)"
        )

    return os_results
