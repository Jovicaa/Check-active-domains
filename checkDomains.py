import subprocess
import csv

def is_domain_active(domain):
    # Ping check
    command = f'ping -c 1 {domain}'
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if b'received' in result:
            return True
    except subprocess.CalledProcessError:
        pass

    # Run Nmap with the -sL flag to scan for hosts on the network
    # and the -p flag to specify the ports to scan (aiming at http/https defaults)
    command = f'nmap -sL -p 80, 443, 8080, 8443 -Pn {domain}'
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if b'open' in result:
            return True
    except subprocess.CalledProcessError:
        pass

    # Run Nmap with the -sT flag to perform a TCP connect scan
    command = f'nmap -sT -p 80, 443, 8080, 8443 {domain}'
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if b'open' in result:
            return True
    except subprocess.CalledProcessError:
        pass

    return False

# Load the list of domains from a CSV file
domains = []
with open('target_domains.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        domains.extend(row)

# Iterate over the domains and check if they're active
active_domains = []

for domain in domains:
    if is_domain_active(domain):
        active_domains.append(domain)

# Write the list of active domains to a response file
with open('active_domains.txt', 'w') as f:
    for domain in active_domains:
        f.write(f'{domain}\n')

print('Active domains list generated in active_domains.txt')
