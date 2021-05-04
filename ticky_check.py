#!/usr/bin/env python3
import csv
import re
import operator
import sys


def parse_line(data):
    # Finds relevant data in the system logs
    reg = re.search(r'ticky: (\w*) (.*) \((.*)\)', data)
    return reg.groups()


def read_data(filename, errors, user_stats):
    # opens the file passed to the function and goes through line by line
    with open(filename, 'r') as f:
        for line in f.readlines():
            # calls regex function and processes the data into dictionaries if it matches
            parsed_line = parse_line(line)
            if parsed_line is None:
                continue
            log_type, message, username = parsed_line[0], parsed_line[1], parsed_line[2]
            if log_type == 'ERROR':
                try:
                    errors.get(message)
                    errors[message] += 1
                except:
                    errors[message] = 1
                try:
                    user_stats[username]['ERROR'] += 1
                except:
                    user_stats[username] = {'INFO': 0, 'ERROR': 1}
            else:
                try:
                    user_stats[username]['INFO'] += 1
                except:
                    user_stats[username] = {'INFO': 1, 'ERROR': 0}

    return errors, user_stats


def create_error_csv(errors):
    # Takes the sorted dictionary and adds it to a readable csv format
    with open('error_message.csv', '+w') as error_log:
        csv_file = csv.writer(error_log)
        csv_file.writerow(['Error', 'Count'])
        for item in errors:
            csv_file.writerow(item)


def create_user_stats_csv(user_stats):
    # Takes the sorted dictionary and adds it to a readable csv format
    with open('user_statistics.csv', '+w') as user_log:
        csv_file = csv.writer(user_log)
        csv_file.writerow(['Username', 'INFO', 'ERROR'])
        for i, item in enumerate(user_stats):
            csv_file.writerow([item[0], item[1]["INFO"], item[1]["ERROR"]])


def main():
    errors = {}
    user_stats = {}
    log_filename = sys.argv[1]
    errors, user_stats = read_data(log_filename, errors, user_stats)
    errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
    user_stats = sorted(user_stats.items(), key=operator.itemgetter(0))
    create_error_csv(errors)
    create_user_stats_csv(user_stats)


if __name__ == '__main__':
    main()
