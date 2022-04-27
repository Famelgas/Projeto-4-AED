from sys import stdin, stdout
import time


grid = []



# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
	i = (low - 1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)


def quick_sort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		partition_index = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quick_sort(arr, low, partition_index - 1)
		quick_sort(arr, partition_index + 1, high)



def raster(file, A: int, B: int):
    for i in range(A):
        user_in = readln(file)
        for j in range(B):
            grid.append(int(user_in[j])) 

    quick_sort(grid, 0, len(grid) - 1)
    
    #outln("RASTER GUARDADO")
    return grid



def amplitude():
    return str(grid[len(grid) - 1] - grid[0])


def percent(num_percent: int, numbers: list):
    num_below = 0
    percent = 0
    percents = []
    for i in range(num_percent):
        for n in range(len(grid)):
            if grid[n] < numbers[i]:
                num_below += 1
            if grid[n] == numbers[i]:
                break
        percent = int((num_below / len(grid)) * 100)
        if min(numbers) > percent:
            percent = 0

        percents.append(percent)
        num_below = 0
        percent = 0

    output = ""
    for i in range(len(percents)):
        if i + 1 == len(percents):
            output += str(percents[i])
        else:
            output += str(percents[i]) + " "
    #outln(output)



def median():
    half = int(len(grid) / 2)
    if not len(grid) % 2:
        return int((grid[half - 1] + grid[half]) / 2)
    return grid[half]

        



def main(test_file):
    run_time = 0
    user_in = [""]
    with open(test_file, "r") as file:
        try:
            while True:
                user_in = readln(file)
                start_time = time.time()
                if user_in[0] == "RASTER":
                    raster(file, int(user_in[1]), int(user_in[2]))

                elif user_in[0] == "AMPLITUDE":
                    amplitude()
                    #outln(amplitude())

                elif user_in[0] == "PERCENTIL":
                    num_percent = int(user_in[1])
                    numbers = readln(file)
                    for i in range(len(numbers)):
                        numbers[i] = int(numbers[i])
                    percent(num_percent, numbers)
                        

                elif user_in[0] == "MEDIANA":
                    med = median()
                    #outln(str(median()))

                elif user_in[0] == "TCHAU":
                    break
                
                else:
                    break


                run_time += (time.time() - start_time)
        except EOFError:
            pass
    return run_time


def readln(file):
    return file.readline().rstrip().split(" ")


def outln(string):
    stdout.write(string.rstrip() + "\n")




if __name__=="__main__":
    test_files = ["test_10.txt", "test_50.txt", "test_100.txt", "test_250.txt", 
				"test_500.txt", "test_750.txt", "test_1000.txt", "test_5000.txt", "test_10000.txt", "test_25000.txt", 
                "test_50000.txt", "test_75000.txt",   "test_100000.txt", "test_200000.txt", 
                "test_300000.txt", "test_400000.txt", "test_500000.txt", "test_1000000.txt"]
    total_matrix_elm = [10, 50, 100, 250, 500, 750, 1000, 5000, 10000, 25000,
                        50000, 75000, 100000, 500000, 1000000]

    run_times = []

    for f in (test_files):
        run_time = main(f)
        print(run_time)
        run_times.append(main(f))

    with open("results.txt", "w") as file:
        for r in range(len(run_times)):
            file.write("Tempo " + str(total_matrix_elm[r]) + " casos: " + str(run_times[r]) + "\n")
	
