#!/usr/bin/python3
import sys


class Line(object):
    def __init__(self, line: str) -> None:
        object.__init__(self)
        self.line = line
        parts = self.line.split()
        self.airline = parts[0]
        self.destination = parts[1]
        self.passengers = int(parts[2])

    def __str__(self) -> str:
        return self.line


def main():
    # Read content and parse
    lines: list[Line] = []
    for line_str in sys.stdin:
        processed_line_str = line_str.strip()
        if processed_line_str == '':
            break
        lines.append(Line(processed_line_str))

    # -------------------------------------------------------------------------
    # How many flights are there to "Frankfurt"?
    # -------------------------------------------------------------------------

    to_Frankfurt = list(filter(
        lambda line: line.destination == 'Frankfurt',
        lines
    ))

    print(len(to_Frankfurt))

    # -------------------------------------------------------------------------
    # Which flight has the most passengers?
    # -------------------------------------------------------------------------

    max_passengers = sorted(
        lines,
        key=lambda line: line.passengers,
        reverse=True
    )
    if len(max_passengers):
        print(max_passengers[0])
    else:
        print('The file is empty!')

    # -------------------------------------------------------------------------
    # Find the first flight with passengers less than 100.
    # -------------------------------------------------------------------------

    flights = list(filter(
        lambda line: line.passengers < 100,
        lines
    ))
    if len(flights):
        print(flights[0])
    else:
        print('There is no flight with passengers less than 100.')

    # -------------------------------------------------------------------------
    # Name the airline with the most total number of passengers. Print out 
    # the total number of passengers carried by the airline as well.
    # -------------------------------------------------------------------------

    airlines = {}
    for line in lines:
        if line.airline not in airlines:
            airlines[line.airline] = 0
        airlines[line.airline] += line.passengers
    max_airlines = sorted(
        airlines.items(),
        key=lambda airline: airline[1],
        reverse=True,
    )
    if len(max_airlines):
        print(*max_airlines[0])
    else:
        print('The file is empty!')


if __name__ == '__main__':
    main()
