from Bio import Phylo
from Bio import AlignIO
from difflib import SequenceMatcher
from Bio.Phylo.TreeConstruction import DistanceCalculator

def closest_relation(table):
    min_cell = float("inf")
    x, y = -1, -1
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j
    return x, y

def update_labels(labels, a, b):
    if b < a:
        a, b = b, a
    labels[a] = "(" + labels[a] + "," + labels[b] + ")"
    del labels[b]

def update_table(table, a, b):
    if b < a:
        a, b = b, a
    row = []
    for i in range(0, a):
        row.append((table[a][i] + table[b][i])/2)
    table[a] = row

    for i in range(a+1, b):
        table[i][a] = (table[i][a]+table[b][i])/2

    for i in range(b+1, len(table)):
        table[i][a] = (table[i][a]+table[i][b])/2
        del table[i][b]
    del table[b]

def UPGMA(table, labels):
    while len(labels) > 1:
        x, y = closest_relation(table)
        update_table(table, x, y)
        update_labels(labels, x, y)
    return labels[0]

def pairwise(seq1, seq2):
    score = 0
    max_score = 0
    score = sum(l1 == l2 for l1, l2 in zip(seq1, seq2))
    max_score = len(seq1)
    if max_score == 0:
        return 1
    return 1 - (score * 1.0 / max_score)


def main():
    sequences = []
    matrix = []
    names = []

    with open('protein.txt') as file:
        for line in file:
            sequences.append(line.split())
            matrix.append([])

    for index in range(len(sequences)):
        for j in range(len(sequences)):
            if j > index:
                matrix[j].append(pairwise(sequences[index][1], sequences[j][1]))
        names.append(sequences[index][0])

    file = open('simple.dnd', 'w')
    file.write(UPGMA(matrix, names))
    file.close()

    tree = Phylo.read('simple.dnd', 'newick')
    tree.ladderize()
    Phylo.draw(tree)

main()
