import sys
import math
import csv
import numpy as np
global n_inter, m_data, n_data, n_cluster
global data, centroid_data,new_cluster_centroid
global input_file, centroi_file, output_file
global cluster_id
import csv
from sklearn.decomposition import PCA


def config(args = ["YeastGene.csv","YeastGene_Initial_Centroids.csv",7,"output_k_means.txt"]):
    global n_inter, m_data, n_data, n_cluster
    global data, centroid_data, new_cluster_centroid
    global input_file, centroi_file, output_file
    data = []
    centroid_data = []
    input_file = args[0]
    centroi_file = args[1]
    n_inter = args[2]
    output_file = args[3]


    m_data = 0
    n_data = 0
    with open(input_file, 'rb') as f:
        f = csv.reader(f,delimiter = ',')
        for line in f:

            m_data += 1


            n_data = len(line)


            vec = [float(i) for i in line]

            data.append(vec)


    print("Input configuration " + str(m_data) + " objects " + str(n_data) + " - dimenion, ")

    n_cluster = 0
    with open(centroi_file,'rb') as f:
        f = csv.reader(f, delimiter=',')
        for line in f:

            n_cluster += 1

            vec = [float(i) for i in line]


            centroid_data.append(vec)

    print ("Input configuration: " + str(n_cluster) + " clusters")

def euclide_dist(a_list,b_list):
    return math.sqrt(sum((a_list[i]-b_list[i])**2 for i in range(min(len(a_list),len(b_list)))))


def execute():
    #**-------------------Fill in here------------------------**        
    # Repeat for nIteration times:
    # for a_iter in range(n_inter):
            # Find the minimum distance and assign object to new cluster

            # Calculate new centroid of each cluster by calculating the total sum of all objects in a cluster
            # then divide it by number of objects in that cluster

            # Update the centroid matrix for next iteration
    global clusters


    for i in range(0,n_inter):

        clusters = [[] for i in range(n_cluster)]

        for each_entry in data:
            cluster_distance = [euclide_dist(each_entry, centroid) for centroid in centroid_data]

            new_cluster = cluster_distance.index(min(cluster_distance))

            clusters[new_cluster].append(each_entry)



        for each_cluster in clusters:


            new_centroid = [-1 for i in range(0,n_data)]

            for n in range(0,n_data):
                temp_point = [each[n] for each in each_cluster]
                new_centroid[n] = sum(temp_point)/len(each_cluster)

            centroid_data.append(new_centroid)
            del(centroid_data[0])

    sklearn_pca = PCA(n_components=2)
    transf = sklearn_pca.fit_transform(data)


    csvfile = open('test.csv', 'wb')
    csvwriter = csv.writer(csvfile)

    for i in clusters:

        for item in i:


            csvwriter.writerow(item+[clusters.index(i)+1])

    csvfile.close()


def output():
    global n_inter, m_data, n_data, n_cluster
    global data, centroid_data, new_cluster_centroid
    global input_file, centroi_file, output_file,cluster_id
    with open(output_file,'w') as f:
        f.write("New Centroid: \n")             #
        # for i in range(n_cluster):
        #     f.write("Cluster " + str(i) + " : ")
        #     for j in range(n_data):
        #         f.write(str(new_cluster_centroid[i][j]) + ' ')
        for i in range(0, len(centroid_data)):
            f.write("Cluster" + " " + str(i + 1) + ":" + str(centroid_data[i]))
            f.write('\n')
        f.write('\n')
        f.write('cluster ID: \n')
        for i in clusters:
            for each in i:
                f.write(str(each))
                f.write(" ")
                f.write(str(clusters.index(i)+1))
                f.write("\n")

        # for i in range(m_data):
        #     f.write(str(cluster_id[i]) + ' ')

    f.close()


def main():
    arg = sys.argv[1:]
    if len(arg) > 3:
        arg[2] = int(arg[2])
        config(arg)
    else:
        config()
    execute()
    output()

main()



