# Uses python3
'''
You are going to travel to another city that is located d miles away from your home city. Your car can travel
at most m miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop 1 , stop 2 , . . . , stop n from your home city. What is the minimum number of refills needed?

Problem Description
Input Format. The first line contains an integer d. The second line contains an integer m. The third line
specifies an integer n. Finally, the last line contains integers stop 1 , stop 2 , . . . , stop n .

Output Format. Assuming that the distance between the cities is d miles, a car can travel at most m miles
on a full tank, and there are gas stations at distances stop 1 , stop 2 , . . . , stop n along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
Constraints. 1 ≤ d ≤ 10 5 . 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop 1 < stop 2 < · · · < stop n < d.
'''
import sys


def compute_min_refills(distance, tank, stops):
    # print(distance, tank, stops)
    if tank >= distance: return 0
    if tank < stops[0] and tank < distance: return -1
    last_refill = 0
    count = 0

    for i, stop in enumerate(stops):
        # print("FOR: ",stop, i)
        if (last_refill + tank ) >= distance: return count
        if (last_refill + tank) < stop: return -1
        if (i+1) < len(stops) and (last_refill + tank) >= stops[i+1]:
            continue

        last_refill = stop
        count += 1

    if (last_refill + tank) >= distance:
        return count
    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
