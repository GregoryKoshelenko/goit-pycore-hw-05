import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log['level'] for log in logs))

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
        if level in counts:
            print(f"{level:<16} | {counts[level]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # python task3.py example.log INFO
        print("Використання: python task3.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
