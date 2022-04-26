from math import sqrt
import random


def gera_testes(test_file, total_matrix_elm):
    lines = int(sqrt(total_matrix_elm))
    file = open(test_file, "w")
    file.write('RASTER ' + str(lines) + ' ' + str(lines) + '\n')
    for s in range(lines):
        for j in range(lines):
            if j < lines - 1:
                file.write(str(random.randint(0, 100)) + ' ')
            else:
                file.write(str(random.randint(0, 100)) + '\n')
    file.write('PERCENTIL ' + str(total_matrix_elm) + '\n')
    for k in range(total_matrix_elm):
        if k < total_matrix_elm - 1:
            file.write(str(random.randint(0, 100)) + ' ')
        else:
            file.write(str(random.randint(0, 100)) + '\n')
    file.write('MEDIANA\n')
    file.write('AMPLITUDE\n')
    file.write('TCHAU')

    return



if __name__=="__main__":
    test_files = ["test_1000.txt", "test_5000.txt", "test_10000.txt", "test_25000.txt", 
                "test_50000.txt", "test_75000.txt",   "test_100000.txt", "test_200000.txt", 
                "test_300000.txt", "test_400000.txt", "test_500000.txt", "test_600000.txt", 
                "test_700000.txt", "test_800000.txt", "test_900000.txt", "test_1000000.txt"]
    total_matrix_elm = [1000, 5000, 10000, 25000, 50000, 75000, 
                        100000, 200000, 300000, 400000, 500000, 
                        600000, 700000, 800000, 900000, 1000000]

    for i in range(len(test_files)):
        gera_testes(test_files[i], total_matrix_elm[i])
