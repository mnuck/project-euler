#!/usr/bin/env python

import heapq
import sys

if len(sys.argv) != 2:
    print "Data file on the command line, yo"
    exit()

with open(sys.argv[1], 'r') as f:
    raw_file = f.read()

raw_lines = raw_file.split('\n')[:-1]

vertex_count = len(raw_lines)
forest = range(vertex_count) # kruskal's forest of sets
edges = list()

complete_weight = 0
for (u, line) in enumerate(raw_lines):
    elements = line.split(',')
    for (v, weight) in enumerate(elements):
        if '-' == weight:
            continue
        heapq.heappush(edges, (int(weight), u, v))
        complete_weight += int(weight)

complete_weight /= 2 # because (u,v) === (v,u)

mst_weight = 0
while edges and len(set(forest)) > 1:
    (weight, u, v) = heapq.heappop(edges)
    if forest[u] != forest[v]:
        mst_weight += weight
        forest = [x if x != forest[v] else forest[u]
                  for x in forest]

print complete_weight - mst_weight
