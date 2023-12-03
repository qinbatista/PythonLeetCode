
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
        accessed = set()

        def findTarget(target, r, c, pre_r, pre_c):
            print("current="+state[r][c]+" r = " + str(r) + " c = "+str(c) +
                  " pre_r = "+str(pre_r) + " pre_c="+str(pre_c)+" target="+target)
            if state[r][c] == target:
                print("find target")
                return True
            if state[r][c] == 0:
                return False
            if state[r][c].isdigit():
                if state[r][c] == "1":
                    if (state[r+1][c] == "1" or state[r+1][c] == "3" or state[r+1][c] == "4" or state[r+1][c] == "7") and r+1 < raw and r+1 != pre_r and (r+1, c) not in accessed:
                        accessed.add((r+1, c))
                        if findTarget(target, r+1, c, r, c):
                            res.add((r+1, c))
                    if (state[r-1][c] == "1" or state[r-1][c] == "5" or state[r-1][c] == "6" or state[r+1][c] == "7") and r-1 >= 0 and r-1 != pre_r and (r-1, c) not in accessed:
                        accessed.add((r-1, c))
                        if findTarget(target, r-1, c, r, c):
                            res.add((r-1, c))
                elif state[r][c] == "2":
                    if (state[r][c+1] == "2" or state[r][c+1] == "3" or state[r][c+1] == "4" or state[r][c+1] == "7") and c+1 < column and c+1 != pre_c and (r, c+1) not in accessed:
                        accessed.add((r, c+1))
                        if findTarget(target, r, c+1, r, c):
                            res.add((r, c+1))
                    if (state[r][c-1] == "2" or state[r][c-1] == "2" or state[r][c-1] == "5" or state[r][c-1] == "7") and c-1 >= 0 and c-1 != pre_c and (r, c-1) not in accessed:
                        accessed.add((r, c-1))
                        if findTarget(target, r, c-1, r, c):
                            res.add((r, c-1))
                elif state[r][c] == "3":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and c+1 < column and c+1 != pre_c and (r, c+1) not in accessed:
                        accessed.add((r, c+1))
                        if findTarget(target, r, c+1, r, c):
                            res.add((r, c+1))
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and r+1 < raw and r+1 != pre_r and (r+1, c) not in accessed:
                        accessed.add((r+1, c))
                        if findTarget(target, r+1, c, r, c):
                            res.add((r+1, c))
                elif state[r][c] == "4":
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and c-1 >= 0 and c-1 != pre_c and (r, c-1) not in accessed:
                        accessed.add((r, c-1))
                        if findTarget(target, r, c-1, r, c):
                            res.add((r, c-1))
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and r+1 < raw and r+1 != pre_r and (r+1, c) not in accessed:
                        accessed.add((r+1, c, r, c))
                        if findTarget(target, r+1, c, r, c):
                            res.add((r+1, c,))
                elif state[r][c] == "5":
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and c-1 >= 0 and c-1 != pre_c and (r, c-1) not in accessed:
                        accessed.add((r, c-1))
                        if findTarget(target, r, c-1, r, c):
                            res.add((r, c-1))
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and r-1 >= 0 and r-1 != pre_r and (r-1, c) not in accessed:
                        accessed.add((r-1, c))
                        if findTarget(target, r-1, c, r, c):
                            res.add((r-1, c))
                elif state[r][c] == "6":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and c+1 < column and c+1 != pre_c and (r, c+1) not in accessed:
                        accessed.add((r, c+1))
                        if findTarget(target, r, c+1, r, c):
                            res.add((r, c+1))
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and r-1 >= 0 and r-1 != pre_r and (r-1, c) not in accessed:
                        accessed.add((r-1, c))
                        if findTarget(target, r-1, c, r, c):
                            res.add((r-1, c))
                elif state[r][c] == "7":
                    if (state[r][c+1] == "2" or state[r][c+1] == "4" or state[r][c+1] == "5" or state[r][c+1] == "7") and (r, c+1) not in accessed:
                        if findTarget(target, r, c+1, r, c):
                            res.add((r, c+1))
                    if (state[r][c-1] == "2" or state[r][c-1] == "3" or state[r][c-1] == "6" or state[r][c-1] == "7") and (r, c-1) not in accessed:
                        if findTarget(target, r, c-1, r, c):
                            res.add((r, c-1))
                    if (state[r+1][c] == "1" or state[r+1][c] == "5" or state[r+1][c] == "6" or state[r+1][c] == "7") and (r+1, c) not in accessed:
                        if findTarget(target, r+1, c, r, c):
                            res.add((r+1, c))
                    if (state[r-1][c] == "1" or state[r-1][c] == "3" or state[r-1][c] == "4" or state[r-1][c] == "7") and (r-1, c) not in accessed:
                        if findTarget(target, r-1, c, r, c):
                            res.add((r-1, c))

            # if state[r-1][c] == target or state[r+1][c] == target or state[r][c-1] == target or state[r][c+1] == target:
            if c+1 < column:
                if state[r][c+1] == target:
                    print("find target="+target)
                    return True
            if c-1 >= 0:
                if state[r][c-1] == target:
                    print("find target="+target)
                    return True
            if r+1 < raw:
                if state[r+1][c] == target:
                    print("find target="+target)
                    return True
            if r-1 >= 0:
                if state[r-1][c] == target:
                    print("find target="+target)
                    return True
            else:
                return False
        for r in range(raw):
            for c in range(column):
                if not state[r][c].isdigit() and state[r][c].islower():
                    accessed.clear()
                    if c+1 < column:
                        findTarget(state[r][c].upper(), r, c+1, r, c)
                    if c-1 >= 0:
                        findTarget(state[r][c].upper(), r, c-1, r, c)
                    if r+1 < raw:
                        findTarget(state[r][c].upper(), r+1, c, r, c)
                    if r-1 >= 0:
                        findTarget(state[r][c].upper(), r-1, c, r, c)


if __name__ == "__main__":
    tp = BackTracking()
    state = ["a224C22300000",
             "0001643722B00",
             "0b27275100000",
             "00c7256500000",
             "0006A45000000"]
    tp.solution(state)
