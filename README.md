# Multithreaded Network Port Scanner

A Python-based multithreaded network port scanner that detects open ports on a target system and identifies commonly running services.
The tool helps in understanding basic network security concepts and how exposed services can be discovered through port scanning.

## Features

* Scans target systems for open ports
* Identifies common network services such as HTTP, SSH, FTP, etc.
* Uses multithreading to perform faster scanning
* Displays open ports along with service information
* Saves scan results to a file for further analysis

## Technologies Used

* Python
* Socket Programming
* Multithreading
* Networking Concepts

## Project Structure

port-scanner
│
├── port_scanner.py
├── scan_results.txt
└── README.md

## How to Run

1. Make sure Python is installed on your system.

2. Run the scanner using:

python port_scanner.py

3. Enter the target IP address or domain name when prompted.

Example:

scanme.nmap.org

## Example Output

Scanning target: scanme.nmap.org

Port 22 open - SSH
Port 80 open - HTTP
Port 443 open - HTTPS

Scan completed.
Results saved to scan_results.txt

## Project Purpose

This project demonstrates how network scanning tools work by identifying open ports and active services on a system.
It highlights how attackers and security analysts analyze network exposure to detect potential security risks.

## Author

Diksha Patil
