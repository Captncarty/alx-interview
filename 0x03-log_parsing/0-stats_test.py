#!/usr/bin/python3

import sys

def parse_log_line(line):
    """
    Read stdin line by line and parses
    """
    try:
        split_line = line.split()
        status = int(split_line[-2])
        file_size = int(split_line[-1])
        return status, file_size
    except (ValueError, IndexError):
        return None


def compute_metrics(total_files_size, status_code_line):
    """
    computes metrics from the log files and passes it to stdout
    """
    print("File size:", total_files_size)
    for status in sorted(status_code_line.keys()):
        print("{}: {}".format(status, status_code_line[status]))


def main():
    """
    runs program for every 10 lines or Ctrl+C and throws an exception
    """
    total_files_size = 0
    status_code_line = {}

    try:
        count_lines = 0
        for line in sys.stdin:
            log_data = parse_log_line(line)
            if log_data:
                status, file_size = log_data
                total_files_size += file_size
                status_code_line[status] = status_code_line.get(status, 0) + 1

                count_lines += 1
                if count_lines % 10 == 0:
                    compute_metrics(total_files_size, status_code_line)
                    print()

    except KeyboardInterrupt:
        compute_metrics(total_files_size, status_code_line)
        raise

