from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def matches_previous_segments(left, matching_segments):
    for seg in matching_segments:
        if left < seg.start or left > seg.end:
            return False
    return True


def optimal_points(segments):
    if not segments:
        return    
    points = []
    index = 0
    segments = sorted(segments,)

    # write your code here
    while index < len(segments):
        ref_segment = segments[index]
        # segments whose left end falls within the ref segment's width
        matches = []

        while index < len(segments):
            current_segment = segments[index]
            if (
                current_segment.start >= ref_segment.start and 
                current_segment.start <= ref_segment.end and
                matches_previous_segments(current_segment.start, matches)
            ):
                matches.append(current_segment)
                index += 1
            else:
                break
        
        points.append(segments[index-1].start)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
