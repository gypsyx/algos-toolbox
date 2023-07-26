from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    if not segments:
        return    
    points = []
    index = 0
    segments = sorted(segments,)
    valid_index = -1

    # write your code here
    while index < len(segments):
        ref_segment = segments[index]

        for i in range(index, len(segments)):
            current_segment = segments[i]
            
            if current_segment.start >= ref_segment.start and current_segment.start <= ref_segment.end:
                valid_index = i
            else:
                break

        points.append(segments[valid_index].start)
        index = valid_index + 1
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
