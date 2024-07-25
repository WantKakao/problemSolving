import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def process_commands(commands):
    min_heap = []
    max_heap = []
    entry_count = defaultdict(int)

    def add_value(x):
        heapq.heappush(min_heap, x)
        heapq.heappush(max_heap, -x)
        entry_count[x] += 1

    def remove_min():
        while min_heap:
            min_val = heapq.heappop(min_heap)
            if entry_count[min_val] > 0:
                entry_count[min_val] -= 1
                return

    def remove_max():
        while max_heap:
            max_val = -heapq.heappop(max_heap)
            if entry_count[max_val] > 0:
                entry_count[max_val] -= 1
                return

    for command in commands:
        op, num = command
        if op == 'I':
            add_value(num)
        elif op == 'D':
            if num == 1:
                remove_max()
            elif num == -1:
                remove_min()

    while min_heap and entry_count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap:
        return "EMPTY"

    min_val = min_heap[0]
    max_val = -max_heap[0]

    return f"{max_val} {min_val}"


def main():
    T = int(input())
    results = []

    for _ in range(T):
        k = int(input())
        commands = []
        for i in range(k):
            cmd, num = map(str, input().split())
            commands.append((cmd, int(num)))
        result = process_commands(commands)
        results.append(result)

    for result in results:
        print(result)


main()
