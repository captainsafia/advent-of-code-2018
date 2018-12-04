Another day, another Advent of Code challenge! As per usual, you can read the problem statement for today's challenge here.

I'm solving each of these problems using a different programming language. I've already used Python and JavaScript and have wondered what language I can use next. It's a little bit later in the day as I'm working on this and I've been working all day and don't have the mental capacity to try a new language. So for this challenge, I'm breaking the rule and working with a programming language I've already used in these challenges: Python.

So, in this challenge, we'd like to determine the area of overlapping assignments given a list of positions and dimensions. The first thing I wanted to do here was to write a function that would determine all the child coordinates within the range of a rectangle.

```python
def increments(claim):
    return [
        (x, y)
        for x in range(claim["x"], claim["x"] + claim["width"])
        for y in range(claim["y"], claim["y"] + claim["height"])
    ]
```

The next thing I needed to do was parse the input file. Although I usually stay far away from it, I decided to use a regular expression to parse the inputs. I copy-pasted some of the data into [Regexr](https://regexr.com) and played around with the values until I eventually got a regular expression to parse things out. Finally, I set up an iterator to run through each inch increment within a rectangle and increase the value of the overlapped area by 1. Running through the areas inch by inch allows us to to only count overlaps that involve multiple rectangles only once.

For the second part of the puzzle, I needed to determine the ID of the claim that did not share an area with any other claims. I did this by searching through each inch of each claim for the areas that were not shared. Here's what the end result looked like.

```python
import re


def increments(claim):
    return [
        (x, y)
        for x in range(claim["x"], claim["x"] + claim["width"])
        for y in range(claim["y"], claim["y"] + claim["height"])
    ]


with open("areas.txt") as claims:
    regex = "^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)"
    parsed_claims = []
    overlap = 0
    for claim in claims.readlines():
        m = re.search(regex, claim)
        parsed_claims.append(
            {
                "id": m.group(1),
                "x": int(m.group(2)),
                "y": int(m.group(3)),
                "width": int(m.group(4)),
                "height": int(m.group(5)),
            }
        )
    overlaps = {}
    for claim in parsed_claims:
        for increment in increments(claim):
            if increment in overlaps:
                overlaps[increment] += 1
            else:
                overlaps[increment] = 1
    overlapped_area = 0
    for overlap in overlaps.values():
        if overlap > 1:
            overlapped_area += 1
    print(overlapped_area)

    for claim in parsed_claims:
        if all(overlaps[increment] == 1 for increment in increments(claim)):
            print(claim)
```
