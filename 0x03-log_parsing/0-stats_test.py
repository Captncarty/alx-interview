#!/usr/bin/python3

import sys

def parse_log_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None

def print_metrics(total_file_size, lines_by_status_code):
    print("Total file size:", total_file_size)
    for status_code in sorted(lines_by_status_code.keys()):
        print(f"{status_code}: {lines_by_status_code[status_code]}")

def main():
    total_file_size = 0
    lines_by_status_code = {}

    try:
        line_count = 0
        for line in sys.stdin:
            log_data = parse_log_line(line)
            if log_data:
                status_code, file_size = log_data
                total_file_size += file_size
                lines_by_status_code[status_code] = lines_by_status_code.get(status_code, 0) + 1

                line_count += 1
                if line_count % 10 == 0:
                    print_metrics(total_file_size, lines_by_status_code)
                    print(line_count)
                    print()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Printing final metrics:")
    
    print_metrics(total_file_size, lines_by_status_code)

if __name__ == "__main__":
    main()

