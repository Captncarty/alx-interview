#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer,
don't print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

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
