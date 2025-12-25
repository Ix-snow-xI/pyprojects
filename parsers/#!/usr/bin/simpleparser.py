#!/usr/bin/env python3
import re
import sys
from collections import Counter
def main():
    log_input=input('choose log file: ')
    logline=[]
    while True:
        try:
            with open(log_input, "r", encoding="utf-8") as file:
                for line in file:
                    if re.findall(r"\d+\.\d+\.\d+\.\d+",line):
                        logline.extend(re.findall(r"\d+\.\d+\.\d+\.\d+",line))
                break
        except FileNotFoundError:
            print("log file not found.")
            continue
    counter = Counter(logline)
    while True:
        log_output = int(input('which top ips you want to see? (n): '))
        try:
            if log_output:
                print(counter.most_common(log_output))
            if not log_output:
                print("you didn't mention top values.")
        except KeyboardInterrupt:
            sys.exit(0)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("exiting the parser.")
        sys.exit(0)
