from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

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

def main():
    alignment = AlignIO.read(open("protein.fasta"), "fasta")
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    distanceMatrix = dm.matrix

    for index in range(len(distanceMatrix)):
        distanceMatrix[index] = distanceMatrix[index][:-1]

    file = open('simple.dnd', 'w')
    file.write(UPGMA(distanceMatrix, dm.names))
    file.close()

    tree = Phylo.read('simple.dnd', 'newick')
    tree.ladderize()
    Phylo.draw(tree)

main()
