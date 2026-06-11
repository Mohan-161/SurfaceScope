import nmap

def discover_hosts(network):

    scanner = nmap.PortScanner()

    print(f"\n[*] Scanning {network}...\n")

    scanner.scan(hosts=network, arguments='-sn')

    live_hosts = []

    for host in scanner.all_hosts():
        live_hosts.append(host)

    return live_hosts
