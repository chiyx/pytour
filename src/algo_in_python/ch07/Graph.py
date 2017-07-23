#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Graph.py - 基本图类，采用邻接矩阵表示


class GraphError(ValueError):
    pass


class Graph:
    "邻接矩阵的实现"

    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            # 检查是否为方阵
            if len(x) != vnum:
                raise ValueError("Argument for 'Graph'")
        # copy
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        "顶点个数"
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError("Adj-Matrix does not support 'add_vertex'.")

    def add_edge(self, vi, vj, val=1):
        "添加边"
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(
                "{0} or {1} is not a valid vertex.".format(vi, vj))
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(
                "{0} or {1} is not a valid vertex.".format(vi, vj))
        return self._mat[vi][vj]

    def out_edges(self, vi):
        "获取某个顶点的所有出边"
        if self._invalid(vi):
            raise GraphError("{0} is not a valid vertex".format(vi))
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return ("[\n" + ",\n".join(map(str, self._mat)) + "\n]" +
                "\nUnconnected:" + str(self._unconn))


class GraphAL(Graph):
    "压缩的邻接矩阵（邻接表）实现"

    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for 'GraphAl'.")
        self._mat = [Graph._out_edges(mat[i], ) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        "增加新顶点： 安排一个新编号"
        self._mat.append([])
        self._vnum += 1
        # 返回顶点编号
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        "新增边"
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(
                "{0} or {1} is not a valid vertex.".format(vi, vj))
        row = self._mat[vi]
        i = 0
        while i < len(row):
            # 存在到vj的边，修改权值
            if row[i][0] == vj:
                row[i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        row.insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(
                "{0} or {1} is not a valid vertex.".format(vi, vj))
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edge(self, vi):
        if self._invalid(vi):
            raise GraphError("{0} is not a valid vertex.")
        return self._mat[vi]


def DFS_graph(graph, v0):
    "图的深度优先遍历的非递归算法, 该操作只遍历传入节点连通的部分"
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    dfs_seq = [v0]
    stack = []
    stack.append((0, graph.out_edges(v0)))
    while stack:
        i, edges = stack.pop()
        if i < len(edges):
            v, e = edges[i]
            stack.append((i + 1, edges))
            if not visited[v]:
                dfs_seq.append(v)
                visited[v] = 1
                stack.append((0, graph.out_edges(v)))
    return dfs_seq


def main():
    glaph = GraphAL()
    for i in range(0, 10):
        glaph.add_vertex()
    glaph.add_edge(1, 2)
    glaph.add_edge(1, 3)
    print(glaph)
    print("===== dfs_graph =====")
    dfs_seq = DFS_graph(glaph, 0)
    print(dfs_seq)

if __name__ == '__main__':
    main()
