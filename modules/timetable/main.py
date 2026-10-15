"""
Стартовая точка для запуска через CLI, Python shell
"""
from argparse import ArgumentParser

from datetime import datetime

from entrypoints.cli import create_event, get_event


parser = ArgumentParser()
parser.add_argument("-c" "--create", action="store_true")
parser.add_argument("-g" "--get", action="store_true")
parser.add_argument("--start", type=str)
parser.add_argument("--end", type=str)
parser.add_argument("title")
parser.add_argument("describe")


def main():
    args = parser.parse_args()
    if args.c__create:
        create_event(datetime.fromisoformat(args.start), datetime.fromisoformat(args.end), args.title, args.describe)

    elif args.g__get:
        events = get_event(datetime.fromisoformat(args.start), datetime.fromisoformat(args.end))
        print(events)


if __name__ == "__main__":
    main()

