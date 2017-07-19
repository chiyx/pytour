#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Graph.py - 基本图类，采用邻接矩阵表示


class GraphError(ValueError):
    pass


class Graph:

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
