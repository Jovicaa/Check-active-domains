# **Python Domain Status Checker**

## **Overview**
This script is a Python program that checks the active status of a list of domains by performing a series of network scans and ping checks. It uses the `subprocess` module to execute external commands, such as `nmap` and `ping`, to determine if each domain is reachable and hosts an open port. The script loads the list of domains from a CSV file, iterates over them, and appends the active domains to a new list. Finally, it writes the list of active domains to a text file named `active_domains.txt`. The script is designed to be run on a command line or as a scheduled task to periodically check the status of a large number of domains.

---

## **Script Description**
This script is a Python-based tool that checks the availability of a list of target domains by performing a combination of ICMP echo requests (ping) and network scanning using Nmap. The script is designed to detect active targets, even in cases where ICMP is blocked, by utilizing Nmap's TCP SYN scan (`-sL`) and TCP connect scan (`-sT`) methods.

---

## **Usage Instructions**
To use this script, follow these steps:

1. **Replace** `'CHANGE_TARGET_LIST.csv'` with the actual path to your CSV file containing the list of domains to scan.
2. **Run** the script using a Python interpreter or your preferred method.
3. **Generate** a list of active domains in a file named `active_domains.txt`.

---

## **Script Features**
- **Performs ICMP echo requests (ping)** to determine if a target is alive.
- **Uses Nmap's TCP SYN scan (`-sL`) and TCP connect scan (`-sT`)** methods to detect open ports and active targets, even if ICMP is blocked.
- **Supports scanning for multiple ports and protocols**.
- **Generates a list of active domains** in a text file for easy analysis and reporting.

---

## **Dependencies**
- **Python 3.x**
- **Nmap** (must be installed on the system and accessible from the command line)

---

## **Limitations**
- This script is designed for use with **domains that have open ports and are reachable via the internet**. It may not be effective for scanning private IP addresses or internal networks.
- The script assumes that **Nmap is installed and configured correctly** on the system. You may need to adjust the Nmap command-line options or flags based on your specific needs and requirements.
