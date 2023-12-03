
import collections
from typing import List


class BackTracking:
    def numIsilands(self, grid: List[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c)not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

    def solution(self, state):
        column = len(state[0])
        raw = len(state)
        res = set()

        def findTarget(target, r, c):
            print("current="+state[r][c]+" r = " +
                  str(r) + " c = "+str(c)+" target="+target)
            if state[r][c] == target:
                print("state[r][c]="+state[r][c] + " target="+target)
                return

            if state[r][c].isdigit():
                if state[r][c] == "1":
                    if (state[r+1][c] == "1" or state[r+1][c] == "3" or state[r+1][c] == "4" or state[r+1][c] == "7") and r+1 < raw:
                        if state[r+1][c] not in res:
                            res.add((r+1, c))
                        findTarget(target, r+1, c)
                    if (state[r-1][c] == "1" or state[r-1][c] == "5" or state[r-1][c] == "6" or state[r+1][c] == "7") and r-1 >= 0:
                        if state[r-1][c] not in res:
                            res.add((r-1, c))
                        findTarget(target, r-1, c)

                if state[r][c] == "2":
                    if (state[r][c+1] == "2" or state[r][c+1] == "3" or state[r][c+1] == "4" or state[r][c+1] == "7") and c+1 < column:
                        if state[r][c+1] not in res:
                            res.add((r, c+1))
                        findTarget(target, r, c+1)
                    if (state[r][c-1] == "2" or state[r][c-1] == "2" or state[r][c-1] == "5" or state[r][c-1] == "7") and c-1 >= 0:
                        if state[r][c-1] not in res:
                            res.add((r, c-1))
                        findTarget(target, r, c-1)

                if state[r][c] == "3":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and c+1 < column:
                        if state[r][c+1] not in res:
                            res.add((r, c+1))
                        findTarget(target, r, c+1)
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and r+1 < raw:
                        if state[r+1][c] not in res:
                            res.add((r+1, c))
                        findTarget(target, r+1, c)

                if state[r][c] == "4":
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and c-1 >= 0:
                        if state[r][c-1] not in res:
                            res.add((r, c-1))
                        findTarget(target, r, c-1)
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and r+1 < raw:
                        if state[r+1][c] not in res:
                            res.add((r+1, c))
                        findTarget(target, r+1, c)

                if state[r][c] == "5":
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and c-1 >= 0:
                        if state[r][c-1] not in res:
                            res.add((r, c-1))
                        findTarget(target, r, c-1)
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and r-1 >= 0:
                        if state[r-1][c] not in res:
                            res.add((r-1, c))
                        findTarget(target, r-1, c)

                if state[r][c] == "6":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and c+1 < column:
                        if state[r][c+1] not in res:
                            res.add((r, c+1))
                        findTarget(target, r, c+1)
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and r-1 >= 0:
                        if state[r-1][c] not in res:
                            res.add((r-1, c))
                        findTarget(target, r-1, c)

                if state[r][c] == "7":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and c+1 < column:
                        if state[r][c+1] not in res:
                            res.add((r, c+1))
                        findTarget(target, r, c+1)
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and c-1 >= 0:
                        if state[r][c-1] not in res:
                            res.add((r, c-1))
                        findTarget(target, r, c-1)
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and r+1 < raw:
                        if state[r+1][c] not in res:
                            res.add((r+1, c))
                        findTarget(target, r+1, c)
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and r-1 >= 0:
                        if state[r-1][c] not in res:
                            res.add((r-1, c))
                        findTarget(target, r-1, c)

            if c+1 < column:
                findTarget(target, r, c+1)
            if c-1 >= 0:
                findTarget(target, r, c-1)
            if r+1 < raw:
                findTarget(target, r+1, c)
            if r-1 >= 0:
                findTarget(target, r-1, c)

        for r in range(raw):
            for c in range(column):
                if not state[r][c].isdigit() and state[r][c].islower():
                    findTarget(state[r][c].upper(), r, c)


if __name__ == "__main__":
    tp = BackTracking()
    state = ["a224C22300000",
             "0001643722B00",
             "0b27275100000",
             "00c7256500000",
             "0006A45000000"]
    tp.solution(state)
