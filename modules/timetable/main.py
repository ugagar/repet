"""
Стартовая точка для запуска через CLI, Python shell
"""
from argparse import ArgumentParser

from datetime import datetime

from timetable.entrypoints.cli import create_event, get_event


parser = ArgumentParser()
parser.add_argument("-c" "--create", action="store_true")
parser.add_argument("--start", type=datetime)
parser.add_argument("--end", type=datetime)
parser.add_argument("title")
parser.add_argument("describe")
parser.add_argument("-g" "--get", action="store_true")


def main():
    args = parser.parse_args()
    if args["create"]:
        create_event(args["start"], args["end"], args["title"], args["describe"])

    elif args["get"]:
        events = get_event(args["start"], args["end"])
        print(events)


if __name__ == "__main__":
    main()

