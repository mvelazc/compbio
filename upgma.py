import sys
from Bio import Phylo
from Bio.Phylo import PhyloXMLIO

# A Quick Implementation of UPGMA (Unweighted Pair Group Method with Arithmetic Mean)

# lowest_cell:
#   Locates the smallest cell in the table
def lowest_cell(table):
    # Set default to infinity
    min_cell = float("inf")
    x, y = -1, -1

    # Go through every cell, looking for the lowest
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j

    # Return the x, y co-ordinate of cell
    return x, y


# join_labels:
#   Combines two labels in a list of labels
def join_labels(labels, a, b):
    # Swap if the indices are not ordered
    if b < a:
        a, b = b, a

    # Join the labels in the first index
    labels[a] = "(" + labels[a] + "," + labels[b] + ")"

    # Remove the (now redundant) label in the second index
    del labels[b]


# join_table:
#   Joins the entries of a table on the cell (a, b) by averaging their data entries
def join_table(table, a, b):
    # Swap if the indices are not ordered
    if b < a:
        a, b = b, a

    # For the lower index, reconstruct the entire row (A, i), where i < A
    row = []
    for i in range(0, a):
        row.append((table[a][i] + table[b][i])/2)
    table[a] = row

    # Then, reconstruct the entire column (i, A), where i > A
    #   Note: Since the matrix is lower triangular, row b only contains values for indices < b
    for i in range(a+1, b):
        table[i][a] = (table[i][a]+table[b][i])/2

    #   We get the rest of the values from row i
    for i in range(b+1, len(table)):
        table[i][a] = (table[i][a]+table[i][b])/2
        # Remove the (now redundant) second index column entry
        del table[i][b]

    # Remove the (now redundant) second index row
    del table[b]


# UPGMA:
#   Runs the UPGMA algorithm on a labelled table
def UPGMA(table, labels):
    # Until all labels have been joined...
    while len(labels) > 1:
        # Locate lowest cell in the table
        x, y = lowest_cell(table)

        # Join the table on the cell co-ordinates
        join_table(table, x, y)

        # Update the labels accordingly
        join_labels(labels, x, y)

    # Return the final label
    return labels[0]



## A test using an example calculation from http://www.nmsr.org/upgma.htm

# alpha_labels:
#   Makes labels from a starting letter to an ending letter
def alpha_labels(start, end):
    labels = []
    for i in range(ord(start), ord(end)+1):
        labels.append(chr(i))
    return labels
# Test table data and corresponding labels
M_labels = ['IOLG_BACSU/3-125', 'NTDC_BACSU/2-118', 'Q79H45_BORPE/11-128', 'YJHC_ECOLI/2-118', 'Q8DNU5_STRR6/2-118', 'YTET_BACSU/2-129', 'GFO_ZYMMO/84-208', 'G5EB60_EMENI/13-129', 'Q5K7F9_CRYNJ/77-228', 'A0A0D1E5T6_USTMA/88-238', 'Q5KM75_CRYNJ/97-249', 'Q5KKC8_CRYNJ/57-215', 'YEAH_SCHPO/36-187', 'YB64_SCHPO/14-166', 'O26961_METTH/4-122', 'Q74AT7_GEOSL/5-121', 'Q55548_SYNY3/24-140', 'Q66GR2_ARATH/11-137', 'IOLX_BACSU/5-125', 'BIEA_RAT/9-124', 'P72782_SYNY3/11-129', 'YHHX_ECOLI/3-123', 'IOLW_BACSU/14-131', 'YDGJ_ECOLI/5-122', 'YM94_YEAST/4-127', 'Q8YPE5_NOSS1/12-131', 'Y816_SYNY3/7-126', 'Y4OX_SINFN/6-128', 'Q7N4K9_PHOLL/5-123', 'Q6LRK0_PHOPR/18-136', 'Q882M7_PSESM/5-123', 'A8AFX3_CITK8/10-126', 'B4EXX9_PROMH/6-122', 'Q9EWP2_STRCO/7-124', 'Q9HWG5_PSEAE/5-122', 'YCJS_ECOLI/10-130', 'WBPB_PSEAE/2-129', 'O25390_HELPY/1-127', 'YGJR_ECOLI/2-121', 'YCEM_ECOLI/4-121', 'YFII_BACSU/13-144', 'Y4HM_SINFN/18-148']   #A through G
M = [[], [0.4943820224719101], [0.4887640449438202, 0.5056179775280899], [0.4943820224719101, 0.4775280898876404, 0.4662921348314607], [0.4943820224719101, 0.4550561797752809, 0.4719101123595506, 0.1910112359550562], [0.5842696629213483, 0.5955056179775281, 0.5898876404494382, 0.6067415730337078, 0.5730337078651686], [0.5224719101123596, 0.5393258426966292, 0.5168539325842696, 0.5, 0.4831460674157303, 0.6067415730337078], [0.6123595505617978, 0.5449438202247191, 0.5561797752808989, 0.5561797752808989, 0.5393258426966292, 0.6123595505617978, 0.6179775280898876], [0.7415730337078652, 0.702247191011236, 0.7696629213483146, 0.752808988764045, 0.7415730337078652, 0.7415730337078652, 0.7808988764044944, 0.7415730337078652], [0.7247191011235955, 0.7359550561797753, 0.7640449438202247, 0.7359550561797753, 0.7415730337078652, 0.7303370786516854, 0.752808988764045, 0.7078651685393258, 0.3764044943820225], [0.7359550561797753, 0.752808988764045, 0.752808988764045, 0.7415730337078652, 0.7359550561797753, 0.7359550561797753, 0.7752808988764045, 0.7191011235955056, 0.4662921348314607, 0.3426966292134831], [0.7865168539325843, 0.7808988764044944, 0.8033707865168539, 0.7865168539325843, 0.7921348314606742, 0.8033707865168539, 0.8146067415730337, 0.7696629213483146, 0.5561797752808989, 0.4943820224719101, 0.4887640449438202], [0.752808988764045, 0.7191011235955056, 0.7752808988764045, 0.7415730337078652, 0.7359550561797753, 0.7640449438202247, 0.7359550561797753, 0.7078651685393258, 0.5168539325842696, 0.5337078651685394, 0.5224719101123596, 0.6235955056179776], [0.752808988764045, 0.7359550561797753, 0.7865168539325843, 0.7584269662921348, 0.7359550561797753, 0.7808988764044944, 0.752808988764045, 0.7247191011235955, 0.5224719101123596, 0.5056179775280899, 0.5337078651685394, 0.6235955056179776, 0.4044943820224719], [0.4887640449438202, 0.4662921348314607, 0.5280898876404494, 0.4550561797752809, 0.5, 0.6348314606741573, 0.5561797752808989, 0.550561797752809, 0.7191011235955056, 0.7359550561797753, 0.7303370786516854, 0.7808988764044944, 0.747191011235955, 0.7584269662921348], [0.5112359550561798, 0.4831460674157303, 0.5, 0.5112359550561798, 0.4943820224719101, 0.6123595505617978, 0.5449438202247191, 0.5280898876404494, 0.7303370786516854, 0.7415730337078652, 0.7247191011235955, 0.7808988764044944, 0.7078651685393258, 0.7415730337078652, 0.4213483146067416], [0.5168539325842696, 0.4719101123595506, 0.4943820224719101, 0.4887640449438202, 0.5, 0.5730337078651686, 0.5561797752808989, 0.5561797752808989, 0.752808988764045, 0.7303370786516854, 0.7415730337078652, 0.7808988764044944, 0.752808988764045, 0.7584269662921348, 0.4213483146067416, 0.398876404494382], [0.5449438202247191, 0.5561797752808989, 0.5561797752808989, 0.5449438202247191, 0.5393258426966292, 0.601123595505618, 0.5842696629213483, 0.5955056179775281, 0.7303370786516854, 0.7247191011235955, 0.7247191011235955, 0.7696629213483146, 0.7359550561797753, 0.7640449438202247, 0.5561797752808989, 0.5674157303370786, 0.5393258426966292], [0.5, 0.5112359550561798, 0.5168539325842696, 0.449438202247191, 0.4550561797752809, 0.5955056179775281, 0.5393258426966292, 0.5337078651685394, 0.7078651685393258, 0.7247191011235955, 0.7303370786516854, 0.747191011235955, 0.7191011235955056, 0.747191011235955, 0.4831460674157303, 0.4550561797752809, 0.5112359550561798, 0.550561797752809], [0.5842696629213483, 0.5674157303370786, 0.5674157303370786, 0.5674157303370786, 0.5674157303370786, 0.601123595505618, 0.5674157303370786, 0.5955056179775281, 0.7696629213483146, 0.7696629213483146, 0.7640449438202247, 0.8258426966292135, 0.7865168539325843, 0.7808988764044944, 0.5168539325842696, 0.5337078651685394, 0.5280898876404494, 0.5842696629213483, 0.5337078651685394], [0.550561797752809, 0.5112359550561798, 0.4887640449438202, 0.5056179775280899, 0.4943820224719101, 0.6292134831460674, 0.5224719101123596, 0.550561797752809, 0.752808988764045, 0.7640449438202247, 0.7640449438202247, 0.8202247191011236, 0.7696629213483146, 0.7921348314606742, 0.5, 0.4775280898876404, 0.5168539325842696, 0.5842696629213483, 0.5168539325842696, 0.4887640449438202], [0.5730337078651686, 0.550561797752809, 0.5561797752808989, 0.5449438202247191, 0.5337078651685394, 0.5898876404494382, 0.5674157303370786, 0.5955056179775281, 0.7865168539325843, 0.7415730337078652, 0.747191011235955, 0.797752808988764, 0.7752808988764045, 0.7808988764044944, 0.5112359550561798, 0.5280898876404494, 0.5449438202247191, 0.5674157303370786, 0.5112359550561798, 0.5393258426966292, 0.5337078651685394], [0.550561797752809, 0.5168539325842696, 0.4775280898876404, 0.5168539325842696, 0.5056179775280899, 0.601123595505618, 0.5449438202247191, 0.5898876404494382, 0.7359550561797753, 0.752808988764045, 0.7584269662921348, 0.8146067415730337, 0.7415730337078652, 0.7640449438202247, 0.4943820224719101, 0.5280898876404494, 0.5056179775280899, 0.5674157303370786, 0.5224719101123596, 0.5224719101123596, 0.4662921348314607, 0.5], [0.5617977528089888, 0.5393258426966292, 0.5112359550561798, 0.550561797752809, 0.5280898876404494, 0.601123595505618, 0.5280898876404494, 0.5786516853932584, 0.7640449438202247, 0.752808988764045, 0.752808988764045, 0.8146067415730337, 0.752808988764045, 0.7808988764044944, 0.5056179775280899, 0.4887640449438202, 0.5393258426966292, 0.5786516853932584, 0.5056179775280899, 0.5112359550561798, 0.4382022471910112, 0.4438202247191011, 0.4101123595505618], [0.5280898876404494, 0.5674157303370786, 0.5786516853932584, 0.5449438202247191, 0.5337078651685394, 0.6404494382022472, 0.5449438202247191, 0.5898876404494382, 0.7865168539325843, 0.7247191011235955, 0.7584269662921348, 0.8033707865168539, 0.7359550561797753, 0.7696629213483146, 0.5224719101123596, 0.550561797752809, 0.5617977528089888, 0.5730337078651686, 0.5561797752808989, 0.5898876404494382, 0.5280898876404494, 0.4831460674157303, 0.5561797752808989, 0.5449438202247191], [0.5561797752808989, 0.5224719101123596, 0.5, 0.5280898876404494, 0.5, 0.6067415730337078, 0.5168539325842696, 0.5393258426966292, 0.7415730337078652, 0.7303370786516854, 0.7359550561797753, 0.7808988764044944, 0.752808988764045, 0.7359550561797753, 0.5280898876404494, 0.4887640449438202, 0.5056179775280899, 0.601123595505618, 0.5168539325842696, 0.5280898876404494, 0.4775280898876404, 0.4887640449438202, 0.4943820224719101, 0.4887640449438202, 0.5168539325842696], [0.5, 0.4775280898876404, 0.5224719101123596, 0.5280898876404494, 0.5056179775280899, 0.6292134831460674, 0.5112359550561798, 0.5730337078651686, 0.747191011235955, 0.7415730337078652, 0.752808988764045, 0.7865168539325843, 0.7415730337078652, 0.7359550561797753, 0.4887640449438202, 0.449438202247191, 0.5337078651685394, 0.5730337078651686, 0.5168539325842696, 0.5168539325842696, 0.5056179775280899, 0.4943820224719101, 0.4887640449438202, 0.5168539325842696, 0.4887640449438202, 0.3146067415730337], [0.5561797752808989, 0.5786516853932584, 0.5674157303370786, 0.5898876404494382, 0.5842696629213483, 0.6235955056179776, 0.601123595505618, 0.6123595505617978, 0.797752808988764, 0.7696629213483146, 0.7865168539325843, 0.8370786516853932, 0.7808988764044944, 0.797752808988764, 0.5674157303370786, 0.5561797752808989, 0.5842696629213483, 0.6292134831460674, 0.5786516853932584, 0.6123595505617978, 0.5898876404494382, 0.6179775280898876, 0.6123595505617978, 0.601123595505618, 0.5955056179775281, 0.5955056179775281, 0.5955056179775281], [0.601123595505618, 0.5730337078651686, 0.5786516853932584, 0.6067415730337078, 0.5898876404494382, 0.6179775280898876, 0.6460674157303371, 0.601123595505618, 0.7584269662921348, 0.752808988764045, 0.7696629213483146, 0.8258426966292135, 0.7415730337078652, 0.7752808988764045, 0.601123595505618, 0.5449438202247191, 0.5786516853932584, 0.6179775280898876, 0.5955056179775281, 0.5955056179775281, 0.5449438202247191, 0.5898876404494382, 0.5786516853932584, 0.5786516853932584, 0.5955056179775281, 0.6067415730337078, 0.6123595505617978, 0.6123595505617978], [0.601123595505618, 0.5337078651685394, 0.5674157303370786, 0.6067415730337078, 0.5786516853932584, 0.5898876404494382, 0.6067415730337078, 0.5955056179775281, 0.752808988764045, 0.7640449438202247, 0.7696629213483146, 0.8202247191011236, 0.7696629213483146, 0.7696629213483146, 0.5955056179775281, 0.5449438202247191, 0.5393258426966292, 0.6123595505617978, 0.5955056179775281, 0.5730337078651686, 0.5617977528089888, 0.6067415730337078, 0.5730337078651686, 0.5730337078651686, 0.601123595505618, 0.5617977528089888, 0.6123595505617978, 0.5842696629213483, 0.2865168539325843], [0.6123595505617978, 0.5786516853932584, 0.601123595505618, 0.6123595505617978, 0.5842696629213483, 0.651685393258427, 0.6348314606741573, 0.6067415730337078, 0.7247191011235955, 0.7247191011235955, 0.7359550561797753, 0.797752808988764, 0.7584269662921348, 0.7752808988764045, 0.5786516853932584, 0.5337078651685394, 0.5730337078651686, 0.6348314606741573, 0.5898876404494382, 0.5955056179775281, 0.550561797752809, 0.6067415730337078, 0.5842696629213483, 0.5898876404494382, 0.601123595505618, 0.5842696629213483, 0.5842696629213483, 0.601123595505618, 0.3146067415730337, 0.297752808988764], [0.6292134831460674, 0.5842696629213483, 0.5561797752808989, 0.6179775280898876, 0.5955056179775281, 0.6235955056179776, 0.6179775280898876, 0.5786516853932584, 0.752808988764045, 0.752808988764045, 0.7696629213483146, 0.8258426966292135, 0.752808988764045, 0.7640449438202247, 0.6123595505617978, 0.5112359550561798, 0.5674157303370786, 0.6179775280898876, 0.5842696629213483, 0.5674157303370786, 0.5280898876404494, 0.6235955056179776, 0.5898876404494382, 0.5674157303370786, 0.5955056179775281, 0.5786516853932584, 0.601123595505618, 0.601123595505618, 0.3033707865168539, 0.3539325842696629, 0.2752808988764045], [0.6460674157303371, 0.5730337078651686, 0.5730337078651686, 0.6348314606741573, 0.6067415730337078, 0.6292134831460674, 0.6123595505617978, 0.6067415730337078, 0.752808988764045, 0.747191011235955, 0.7752808988764045, 0.8258426966292135, 0.752808988764045, 0.7584269662921348, 0.6123595505617978, 0.5393258426966292, 0.5898876404494382, 0.6292134831460674, 0.6123595505617978, 0.550561797752809, 0.5449438202247191, 0.5955056179775281, 0.5730337078651686, 0.5674157303370786, 0.5898876404494382, 0.5730337078651686, 0.5955056179775281, 0.6067415730337078, 0.3314606741573034, 0.3370786516853933, 0.2921348314606742, 0.2752808988764045], [0.6123595505617978, 0.5561797752808989, 0.5730337078651686, 0.5842696629213483, 0.5730337078651686, 0.651685393258427, 0.6235955056179776, 0.5786516853932584, 0.7584269662921348, 0.7359550561797753, 0.7584269662921348, 0.8089887640449438, 0.7640449438202247, 0.8033707865168539, 0.5561797752808989, 0.5056179775280899, 0.5561797752808989, 0.6404494382022472, 0.5842696629213483, 0.5786516853932584, 0.5561797752808989, 0.5955056179775281, 0.5842696629213483, 0.5674157303370786, 0.6292134831460674, 0.5561797752808989, 0.5393258426966292, 0.6292134831460674, 0.4269662921348315, 0.398876404494382, 0.3707865168539326, 0.4044943820224719, 0.4101123595505618], [0.6348314606741573, 0.5674157303370786, 0.601123595505618, 0.6067415730337078, 0.601123595505618, 0.6460674157303371, 0.651685393258427, 0.6179775280898876, 0.7696629213483146, 0.752808988764045, 0.7808988764044944, 0.8314606741573034, 0.7808988764044944, 0.7921348314606742, 0.5955056179775281, 0.5393258426966292, 0.5674157303370786, 0.6573033707865168, 0.5842696629213483, 0.5898876404494382, 0.5561797752808989, 0.6179775280898876, 0.5898876404494382, 0.5674157303370786, 0.6460674157303371, 0.5842696629213483, 0.5955056179775281, 0.6404494382022472, 0.4269662921348315, 0.449438202247191, 0.4157303370786517, 0.449438202247191, 0.4325842696629213, 0.348314606741573], [0.4887640449438202, 0.4662921348314607, 0.5224719101123596, 0.5449438202247191, 0.5112359550561798, 0.6123595505617978, 0.5168539325842696, 0.5393258426966292, 0.7359550561797753, 0.7303370786516854, 0.752808988764045, 0.8089887640449438, 0.752808988764045, 0.7865168539325843, 0.4382022471910112, 0.4606741573033708, 0.5112359550561798, 0.5842696629213483, 0.5393258426966292, 0.550561797752809, 0.5056179775280899, 0.5393258426966292, 0.5224719101123596, 0.4775280898876404, 0.5337078651685394, 0.5, 0.4943820224719101, 0.5786516853932584, 0.5786516853932584, 0.5842696629213483, 0.5561797752808989, 0.5674157303370786, 0.6123595505617978, 0.5955056179775281, 0.5898876404494382], [0.6123595505617978, 0.5674157303370786, 0.5842696629213483, 0.6123595505617978, 0.6179775280898876, 0.6460674157303371, 0.651685393258427, 0.6460674157303371, 0.7808988764044944, 0.7640449438202247, 0.752808988764045, 0.8314606741573034, 0.7808988764044944, 0.7808988764044944, 0.5955056179775281, 0.5730337078651686, 0.6067415730337078, 0.651685393258427, 0.6067415730337078, 0.6123595505617978, 0.5730337078651686, 0.6123595505617978, 0.5955056179775281, 0.601123595505618, 0.6573033707865168, 0.6123595505617978, 0.6123595505617978, 0.651685393258427, 0.6460674157303371, 0.6573033707865168, 0.651685393258427, 0.6460674157303371, 0.6629213483146068, 0.6629213483146068, 0.6573033707865168, 0.5280898876404494], [0.6179775280898876, 0.550561797752809, 0.5955056179775281, 0.6348314606741573, 0.6235955056179776, 0.651685393258427, 0.6460674157303371, 0.6179775280898876, 0.7921348314606742, 0.7752808988764045, 0.7584269662921348, 0.797752808988764, 0.797752808988764, 0.7752808988764045, 0.6067415730337078, 0.5898876404494382, 0.601123595505618, 0.6460674157303371, 0.5786516853932584, 0.5898876404494382, 0.601123595505618, 0.5955056179775281, 0.6123595505617978, 0.6235955056179776, 0.6404494382022472, 0.5674157303370786, 0.601123595505618, 0.6797752808988764, 0.6123595505617978, 0.6348314606741573, 0.651685393258427, 0.6179775280898876, 0.6404494382022472, 0.6685393258426966, 0.651685393258427, 0.5617977528089888, 0.398876404494382], [0.550561797752809, 0.5056179775280899, 0.5168539325842696, 0.5168539325842696, 0.5168539325842696, 0.6179775280898876, 0.5337078651685394, 0.5730337078651686, 0.7865168539325843, 0.7640449438202247, 0.7584269662921348, 0.797752808988764, 0.7640449438202247, 0.7865168539325843, 0.5168539325842696, 0.5, 0.5280898876404494, 0.6067415730337078, 0.5112359550561798, 0.550561797752809, 0.5, 0.5674157303370786, 0.5449438202247191, 0.5393258426966292, 0.5674157303370786, 0.5112359550561798, 0.4943820224719101, 0.6179775280898876, 0.5617977528089888, 0.5786516853932584, 0.5955056179775281, 0.5842696629213483, 0.5786516853932584, 0.5449438202247191, 0.6067415730337078, 0.4943820224719101, 0.5674157303370786, 0.5898876404494382], [0.5056179775280899, 0.5168539325842696, 0.5280898876404494, 0.5337078651685394, 0.5168539325842696, 0.5898876404494382, 0.5393258426966292, 0.5449438202247191, 0.752808988764045, 0.7415730337078652, 0.7696629213483146, 0.8089887640449438, 0.752808988764045, 0.7415730337078652, 0.5168539325842696, 0.4943820224719101, 0.4719101123595506, 0.5842696629213483, 0.5393258426966292, 0.5224719101123596, 0.5112359550561798, 0.5280898876404494, 0.5561797752808989, 0.5112359550561798, 0.5280898876404494, 0.5280898876404494, 0.5393258426966292, 0.5842696629213483, 0.5617977528089888, 0.5561797752808989, 0.5561797752808989, 0.5617977528089888, 0.5786516853932584, 0.5561797752808989, 0.5786516853932584, 0.5224719101123596, 0.6348314606741573, 0.6067415730337078, 0.5280898876404494], [0.5674157303370786, 0.5786516853932584, 0.5786516853932584, 0.6179775280898876, 0.6067415730337078, 0.651685393258427, 0.5617977528089888, 0.6404494382022472, 0.797752808988764, 0.7921348314606742, 0.7921348314606742, 0.8146067415730337, 0.8258426966292135, 0.8089887640449438, 0.5561797752808989, 0.550561797752809, 0.5674157303370786, 0.6292134831460674, 0.5674157303370786, 0.601123595505618, 0.5393258426966292, 0.5730337078651686, 0.5561797752808989, 0.5393258426966292, 0.5842696629213483, 0.5449438202247191, 0.5561797752808989, 0.5730337078651686, 0.6404494382022472, 0.6067415730337078, 0.6404494382022472, 0.6235955056179776, 0.6348314606741573, 0.6292134831460674, 0.6460674157303371, 0.5449438202247191, 0.6292134831460674, 0.5730337078651686, 0.5898876404494382, 0.6067415730337078], [0.601123595505618, 0.6123595505617978, 0.5955056179775281, 0.6292134831460674, 0.6067415730337078, 0.6404494382022472, 0.5617977528089888, 0.6404494382022472, 0.7752808988764045, 0.7584269662921348, 0.7696629213483146, 0.797752808988764, 0.7752808988764045, 0.7921348314606742, 0.6067415730337078, 0.5393258426966292, 0.601123595505618, 0.6292134831460674, 0.5955056179775281, 0.6235955056179776, 0.5730337078651686, 0.5730337078651686, 0.6067415730337078, 0.5280898876404494, 0.5898876404494382, 0.5730337078651686, 0.550561797752809, 0.6348314606741573, 0.6573033707865168, 0.6629213483146068, 0.6292134831460674, 0.6348314606741573, 0.6460674157303371, 0.6404494382022472, 0.6629213483146068, 0.5617977528089888, 0.6348314606741573, 0.6404494382022472, 0.5786516853932584, 0.5786516853932584, 0.4775280898876404]]

path = 'E:\\Win10Docs\\compbio\\compbio\\UPGMA\\simple.dnd'
f = open('path', 'w')
f.write(UPGMA(M, M_labels))
f.close()

tree = Phylo.read('path', 'newick')
tree.ladderize()
Phylo.draw(tree)
# UPGMA(M, M_labels) should output: '((((A,D),((B,F),G)),C),E)'
