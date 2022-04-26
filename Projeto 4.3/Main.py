from sys import stdin, stdout



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



def raster(A: int, B: int):
    for i in range(A):
        user_in = readln()
        for j in range(B):
            grid.append(int(user_in[j])) 

    quick_sort(grid, 0, len(grid) - 1)
    
    outln("RASTER GUARDADO")
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
    outln(output)



def median():
    half = int(len(grid) / 2)
    if not len(grid) % 2:
        return int((grid[half - 1] + grid[half]) / 2)
    return grid[half]

        



def main():
    while True:
        user_in = readln()
        #start_time = time.time()
        if user_in[0] == "RASTER":
            raster(int(user_in[1]), int(user_in[2]))

        elif user_in[0] == "AMPLITUDE":
            outln(amplitude())

        elif user_in[0] == "PERCENTIL":
            num_percent = int(user_in[1])
            numbers = readln()
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
            percent(num_percent, numbers)
                 

        elif user_in[0] == "MEDIANA":
            outln(str(median()))

        elif user_in[0] == "TCHAU":
            break
        
        else:
            break



    return


def readln():
    return stdin.readline().rstrip().split(" ")


def outln(string):
    stdout.write(string.rstrip() + "\n")




if __name__=="__main__":
    main()