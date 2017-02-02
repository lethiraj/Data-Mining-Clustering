import sys
import math
import csv
input_file = None
output_file = None
mData = 0
nData = 0
data = []
link_matrix = []

def config(args = ["test.csv","output_H_cluster.txt"]):
    global input_file, output_file, mData, nData
    global count, data
    input_file = args[0]
    output_file = args[1]
    with open (input_file, 'r') as f:
        f = csv.reader(f, delimiter=',')
        for line in f:
            nData = len(line)
            mData += 1
            vec_line = [float(i) for i in line]
            data.append(vec_line)


def p(matrix):
    for list in matrix:
        print(list)


def execute():

    distance = []
    infinity = float('inf')


    for i in range(mData):
        temp_row = [euclide_dist(data[i],data[j]) for j in range(mData)]
        temp_row[i] = float('inf')
        distance.append(temp_row)


    for iterations in range(mData-1):

        i1 = 0
        i2 = 0

        min_so_far = float('inf')


        for i in distance:
            if min(i) < min_so_far:
                min_so_far = min(i)
                i1 = distance.index(i)
                i2 = i.index(min_so_far)

        first_cluster = list(distance[i1])
        second_cluster = list(distance[i2])

        for i in range(len(distance[i1])):
            distance[i1][i] = infinity
            distance[i2][i] = infinity
            distance[i][i1] = infinity
            distance[i][i2] = infinity



        newRow = [min(x, y) for x, y in zip(first_cluster, second_cluster)]
        newRow[i1] = infinity
        newRow[i2] = infinity
        newRow.append(infinity)

        for i in range(len(distance)):
            distance[i].append(newRow[i])

        distance.append(newRow)


        print("TO MERGE : ", (i1 + 1, i2 + 1, iterations + 1 + mData))
        link_matrix.append((i1+1,i2+1,iterations+1+mData))



def euclide_dist(a_list,b_list):
    return math.sqrt(sum((a_list[i]-b_list[i])**2 for i in range(min(len(a_list),len(b_list)))))

def output():
    with open(output_file,'w') as f:
        f.write("Linkage: \n")
        for i in link_matrix:
            f.write(str(i))
            f.write('\n')
    f.close()

def main():
    arg = sys.argv[1:]
    if len(arg) > 1:
        config(arg)
    else:
        config()
    execute()
    output()

main()

