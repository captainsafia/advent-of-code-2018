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

