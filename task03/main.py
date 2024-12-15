import sys
import os
from collections import Counter
from tabulate import tabulate


def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message.strip()}


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line) for line in file if parse_log_line(line) is not None]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to read the file. {e}")
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    table = [(level, count) for level, count in counts.items()]
    print(tabulate(table, headers=["Рівень логування", "Кількість"], tablefmt="grid"))


def display_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        return 

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        display_logs(filtered_logs, level)

if __name__ == "__main__":
    main()