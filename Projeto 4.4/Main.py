from sys import stdin, stdout



grid = []


def counting_sort(arr, exp1):
	n = len(arr)
	# The output array elements that will have sorted arr
	output = [0] * (n)
	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(n):
		index = arr[i] // exp1
		count[index % 10] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the output array
	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]


def radix_sort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1 / exp > 1:
		counting_sort(arr, exp)
		exp *= 10



def raster(A: int, B: int):
    for i in range(A):
        user_in = readln()
        for j in range(B):
            grid.append(int(user_in[j])) 

    radix_sort(grid)
    
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