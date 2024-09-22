import subprocess
import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def run_command(command, output_file):
    """Runs a command and writes its output to a file."""
    with open(output_file, 'w') as f:
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            f.write(result.stdout + '\n' + result.stderr)
        except Exception as e:
            f.write(f"Error running command: {e}\n")

def main(ctf_name, ip_address, web_address):
    # Define directory to store results
    output_dir = f"./{ctf_name}"
    os.makedirs(output_dir, exist_ok=True)

    # Define the commands (customize based on your needs)
    commands = [
        f"nmap -sS -p- -Pn --min-rate 99999 --scan-delay 0 --version-all  --osscan-guess --script=vuln  -system-dns  {ip_address}",  # Service version detection
        f"dirb http://{web_address}",  # Directory brute-forcing
        #f"nikto -h http://{web_address}",  # Web vulnerability scan
        #f"curl http://{web_address}"  # Simple web request
    ]

    # Output file names
    output_files = [
        f"{output_dir}/nmap_output.txt",
        f"{output_dir}/dirb_output.txt",
        #f"{output_dir}/nikto_output.txt",
        #f"{output_dir}/curl_output.txt"
    ]

    # Execute commands in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:
        for command, output_file in zip(commands, output_files):
            executor.submit(run_command, command, output_file)

if __name__ == "__main__":
    # Argument parser for parameters
    parser = argparse.ArgumentParser(description='Automate CTF solving tasks.')
    parser.add_argument('-ctf', required=True, help='CTF name')
    parser.add_argument('-ip', required=True, help='Target IP address')
    parser.add_argument('-web',  help='Web address for scanning')
    
    args = parser.parse_args()

    main(args.ctf, args.ip, args.web)
