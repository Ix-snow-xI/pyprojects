# Simple SOC Log Analyzer

A simple interactive tool for server log analysis. Written in Python while learning how to automate SOC tasks.

## Features
- Reading log files (protected against input errors).
- IP address search using Regular Expressions.
- IP encounter rate counting (identifying potential attacks/brute-force attacks).
- Interactive display of the top N active addresses.
- Graceful shutdown (exit gracefully with Ctrl+C).
## Technologies
- **Language:** Python 3
- **Modules:** `re`, `collections`, `sys`

## 💻 Как запустить
1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/Ix-snow-xI/pyprojects/parsers.git](https://github.com/Ix-snow-xI/pyprojects/parsers.git)
