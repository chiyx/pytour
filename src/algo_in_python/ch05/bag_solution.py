#! /usr/bin/env python3
# coding = utf-8

# bag_solution - 简单背包问题的递归求解方式

count = 0


def bag_rec(weight, wlist, n):
    """简单背包问题的递归求解方式
    假设用knap(weight, n) 表示n件物品相对于总重量weight的背包问题，
    在考虑它是否有解时，通过考虑一件物品的选与不选，可以把原问题划分为
    2种情况：
        1. 如果不选最后一件物品，其重量为wlist[n-1], 那么knap(weight, n-1)的解也是原问题的解
        2. 如果选最后一件物品，那么如果knap(weight - wlist[n-1], n - 1)有解，其解加上最后一件物品就是原问题的解
    Args:
        weight: 剩余重量
        wlist: 物品对应的重量列表
        n: 剩余的物品数
    """
    # 总量已经等于0，说明有解
    global count
    count += 1
    print(weight, wlist, n)
    if weight == 0:
        return True
    # 剩余重量小于0或者剩余重量大于0时说明无解
    if weight < 0 or (weight > 0 and n < 1):
        return False
    # 选择当前物品，并递归求knap(weight - wlist[n -1], n -1)
    if bag_rec(weight - wlist[n - 1], wlist, n - 1):
        print('Item ' + str(n) + ":", wlist[n - 1])
        return True
    # 不选当前物品，递归求解knap(weight, n - 1)
    if bag_rec(weight, wlist, n - 1):
        return True
    else:
        return False

if __name__ == '__main__':
    bag_rec(50, [10, 20, 30, 40], 4)
    print(count)
