import sys
from Bio import Phylo
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.Phylo import PhyloXMLIO

def closest_relation(table):
    max_value = 0
    x, y = -1, -1
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] > max_value:
                max_value = table[i][j]
                x, y = i, j

    return x, y

def update_labels(labels, x, y):
    if y < x:
        x, y = y, x
    labels[x] = "(" + labels[x] + "," + labels[y] + ")"
    del labels[y]

def update_table(table, x, y):
    if y < x:
        x, y = y, x
    row = []
    for i in range(0, x):
        row.append((table[x][i] + table[y][i])/2)
    table[x] = row
    for i in range(x+1, y):
        table[i][x] = (table[i][x]+table[y][i])/2
    for i in range(y+1, len(table)):
        table[i][x] = (table[i][x]+table[i][y])/2
        del table[i][y]
    del table[y]

def UPGMA(table, labels):
    while len(labels) > 1:
        x, y = closest_relation(table)
        update_table(table, x, y)
        update_labels(labels, x, y)
    return labels[0]

def main():
    with open('phylotest.txt') as f:
        lines = f.read().splitlines()

    size = len(lines)
    comp = []
    labels = []

    for i in range(size):
        lines[i] = lines[i].split()
        labels.append(lines[i][0])
        comp.append([])

    for k in range(size):
        seq1 = Seq(lines[k][1])
        for index, item in enumerate(lines):
            if index > k:
                seq2 = Seq(lines[index][1])
                comp[index].append(int(pairwise2.align.globalxx(seq1, seq2)[0][2]))

    f = open('simple.dnd', 'w')
    f.write(UPGMA(comp, labels))
    f.close()

    tree = Phylo.read('simple.dnd', 'newick')
    Phylo.draw(tree)



main()
