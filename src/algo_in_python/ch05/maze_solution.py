#! /usr/bin/env python3
# coding = utf-8

# maze_solution.py - 求解迷宫问题的算法

import random

# 代表4个方向的增量
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def generateMaze(weight, height):
    """ 生成一个(weight * height)的迷宫

        args:
            weight: 迷宫的宽
            height: 迷宫的高
    """
    maze = []
    for i in range(height + 1):
        mazeRow = []
        for j in range(weight + 1):
            # 四周是围墙
            if i == 0 or i == height or j == 0 or j == weight:
                mazeRow.append(1)
            # 入口和出口设置为0
            elif (i == 1 and j == 1) or \
                    (i == (height - 1) and j == (weight - 1)):
                mazeRow.append(0)
            # 其他设置为随机值
            else:
                value = random.randint(0, 2)
                mazeRow.append(value % 2)
        maze.append(mazeRow)
    return maze


def print_path(end, pos, stack):
    for elem in stack:
        print(elem[0], '-->')
    print(pos, '-->')
    print(end)


def mark(maze, pos):
    "给迷宫maze的位置pos标2表示 “到过了”"
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    "检查迷宫的位置pos是否可行"
    return maze[pos[0]][pos[1]] == 0


def find_path_rec(maze, pos, end):
    """ 基于递归的解法

        args:
            maze: 迷宫
            pos: 当前位置
            end: 出口
    """
    # 标记当前位置已走过
    mark(maze, pos)
    # 判断当前位置是否为出口
    if pos == end:
        print(pos, end=' ')
        return True
    # 否则按4个方向顺序探查
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            # 如果从这个nextp可达出口
            if find_path_rec(maze, nextp, end):
                print(pos, end=' ')
                return True
    return False


def maze_solver(maze, start, end):
    "基于栈的回溯解法"
    if start == end:
        print(start)
        return True
    stack = []
    mark(maze, start)
    # 入口和方向0序对入栈
    stack.append((start, 0))
    # 当栈不空时,走不通回退继续
    while stack:
        pos, nxt = stack.pop()
        # 依次检测未探测方向
        for i in range(nxt, 4):
            # 算出下一位置
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            # 找到出口，打印路径
            if nextp == end:
                print_path(end, pos, stack)
                return True
            # 遇到未探测的新位置
            if passable(maze, nextp):
                # 原位置和下一方向入栈
                stack.append((pos, i + 1))
                mark(maze, nextp)
                # 新位置入栈
                stack.append((nextp, 0))
                # 退出内循环，下次迭代将以新栈顶为当前位置继续
                break
    print('No path found.')
    return False


if __name__ == '__main__':
    weight, height = 13, 11
    maze = generateMaze(weight, height)
    # rs = find_path_rec(maze, (1, 1), (height - 1, weight - 1))
    rs = maze_solver(maze, (1, 1), (height - 1, weight - 1))
    print(rs)
    for row in maze:
        print(row)
    # print(maze[height][weight])
