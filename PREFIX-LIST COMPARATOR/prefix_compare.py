import re

def extract_ips_from_file(file_path):
    try:
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()
        prefixes = re.findall(r'\d+\.\d+\.\d+\.\d+/\d+', content)
        return set(prefixes)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)

def main():
    print("Enter the two IP list filenames (example: bangalore-ips.txt):")

    file1 = input("Enter first filename: ").strip()
    file2 = input("Enter second filename: ").strip()

    if not (file1.endswith(".txt") and file2.endswith(".txt")):
        print("Both filenames must end with .txt")
        exit(1)

    ips1 = extract_ips_from_file(file1)
    ips2 = extract_ips_from_file(file2)

    print(f"\nExtracted {len(ips1)} IPs from '{file1}'")
    print(f"Extracted {len(ips2)} IPs from '{file2}'")

    only_in_file1 = ips1 - ips2
    only_in_file2 = ips2 - ips1
    not_common = only_in_file1.union(only_in_file2)

    print(f"\nIPs only in {file1} (missing in {file2}) — {len(only_in_file1)} IPs:\n")
    for ip in sorted(only_in_file1):
        print(ip)

    print(f"\nIPs only in {file2} (missing in {file1}) — {len(only_in_file2)} IPs:\n")
    for ip in sorted(only_in_file2):
        print(ip)

    print(f"\nIPs not common to both files (total {len(not_common)} IPs):\n")
    for ip in sorted(not_common):
        print(ip)

if __name__ == "__main__":
    main()
