
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
        accessed = []
        path = {}
        result = []
        reachedTarget = set()
        reachList = []
        def findTarget(target, r, c, path):
            if r >= raw or r < 0 or c >= column or c < 0 or state[r][c] == 0 or (r, c) in accessed:
                return False
            else:
                if state[r][c] != target and state[r][c].isdigit():
                    path.append((r, c))
                    accessed.append((r, c))
            print("current="+state[r][c]+" r = " +
                  str(r) + " c = "+str(c) + " target="+target)
            if state[r][c] == target:
                result.append(path)
                reachedTarget.add(target)
                reachList.append(target)
                print("reached target "+target)
                return True
            if state[r][c].isdigit():
                if state[r][c] == "1":
                    findTarget(target, r+1, c, path)
                    findTarget(target, r-1, c, path)

                elif state[r][c] == "2":
                    findTarget(target, r, c+1,  path)
                    findTarget(target, r, c-1,  path)

                elif state[r][c] == "3":
                    findTarget(target, r, c+1,  path)
                    findTarget(target, r+1, c,  path)

                elif state[r][c] == "4":
                    findTarget(target, r, c-1,  path)
                    findTarget(target, r+1, c, path)

                elif state[r][c] == "5":
                    findTarget(target, r, c-1,  path)
                    findTarget(target, r-1, c,  path)

                elif state[r][c] == "6":
                    findTarget(target, r, c+1,  path)
                    findTarget(target, r-1, c,  path)

                elif state[r][c] == "7":
                    findTarget(target, r, c+1,  path.copy())
                    findTarget(target, r, c-1,  path.copy())
                    findTarget(target, r+1, c, path.copy())
                    findTarget(target, r-1, c,  path.copy())

        for r in range(raw):
            for c in range(column):
                # print("this cell is "+state[r][c])
                if not state[r][c].isdigit() and state[r][c].islower():
                    accessed.clear()
                    path = []
                    if c+1 < column and state[r][c] != 0:
                        if not findTarget(state[r][c].upper(), r, c+1, path):
                            path = []
                        else:
                            continue
                    if c-1 >= 0 and state[r][c] != 0:
                        if not findTarget(state[r][c].upper(), r, c-1, path):
                            path = []
                        else:
                            continue
                    if r+1 < raw and state[r][c] != 0:
                        if findTarget(state[r][c].upper(), r+1, c, path):
                            path = []
                        else:
                            continue
                    if r-1 >= 0 and state[r][c] != 0:
                        if findTarget(state[r][c].upper(), r-1, c, path):
                            path = []
                        else:
                            continue
        merged_result = set().union(*result)
        for index,i in enumerate(result):
            print(f"{reachList[index]}:{len(i)}:{i}")
        if len(reachedTarget) >= 1:
            print(f"{len(merged_result)}")
            return len(merged_result)
        else:
            print(f"{-len(merged_result)}")
            return -len(merged_result)


if __name__ == "__main__":
    tp = BackTracking()
    # state = ["a224C22300000",
    #          "0001643722B00",
    #          "0b27275100000",
    #          "00c7256500000",
    #          "0006A45000000"]
    # state = ["A0000b0000",
    #          "0000000000",
    #          "0000000000",
    #          "0000a00000",
    #          "0000000000",
    #          "0c00000000",
    #          "01000000B0",
    #          "0C00000000"]
    # -48
    state = ["00p2400003777z24",
             "1a406P0001000101",
             "1064000001000101",
             "1006774001032501",
             "1000001001010001",
             "1000001001064035",
             "6227276A0622Z250"]  # -48 40
    # state = ["3277222400000000",
    #          "1000032A40000000",
    #          "1000010110000000",
    #          "1Q2227277q000000",
    #          "1000010110000000",
    #          "1000062a50000000",
    #          "6222222500000000"]  # 40 36

    tp.solution(state)
