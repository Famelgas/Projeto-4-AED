from sys import stdin, stdout
import random
import time


grid = []


def raster(A: int, B: int):
	for i in range(A):
		user_in = readln()
		for j in range(B):
			grid.append(int(user_in[j])) 
	# outln("RASTER GUARDADO")
	return grid



def amplitude():
	return str(max(grid) - min(grid))


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
	#outln(output)







a, b = None, None;

# Returns the correct position of
# pivot element
def partition(arr, l, r) :

	lst = arr[r]; i = l; j = l;
	while (j < r) :
		if (arr[j] < lst) :
			arr[i], arr[j] = arr[j],arr[i];
			i += 1;
		
		j += 1;

	arr[i], arr[r] = arr[r],arr[i];
	return i;

# Picks a random pivot element between
# l and r and partitions arr[l..r]
# around the randomly picked element
# using partition()
def random_partition(arr, l, r) :
	n = r - l + 1;
	pivot = random.randrange(1, 100) % n;
	arr[l + pivot], arr[r] = arr[r], arr[l + pivot];
	return partition(arr, l, r);

# Utility function to find median
def median_util(arr, l, r, k, a1, b1) :

	global a, b;
	
	# if l < r
	if (l <= r) :
		
		# Find the partition index
		partition_index = random_partition(arr, l, r);
		
		# If partition index = k, then
		# we found the median of odd
		# number element in arr[]
		if (partition_index == k) :
			b = arr[partition_index];
			if (a1 != -1) :
				return;
				
		# If index = k - 1, then we get
		# a & b as middle element of
		# arr[]
		elif (partition_index == k - 1) :
			a = arr[partition_index];
			if (b1 != -1) :
				return;
				
		# If partition_index >= k then
		# find the index in first half
		# of the arr[]
		if (partition_index >= k) :
			return median_util(arr, l, partition_index - 1, k, a, b);
			
		# If partition_index <= k then
		# find the index in second half
		# of the arr[]
		else :
			return median_util(arr, partition_index + 1, r, k, a, b);
			
	return;

# Function to find Median
def median(arr, n) :
	global a;
	global b;
	a = -1;
	b = -1;
	
	# If n is odd
	if (n % 2 == 1) :
		median_util(arr, 0, n - 1, n // 2, a, b);
		ans = b;
		
	# If n is even
	else :
		median_util(arr, 0, n - 1, n // 2, a, b);
		ans = (a + b) // 2;
	
	return ans







def main(test_file):
	run_time = 0
	with open(test_file, "r") as file:
		try:
			while True:
				user_in = readln()
				start_time = time.time()
				if user_in[0] == "RASTER":
					raster(int(user_in[1]), int(user_in[2]))

				elif user_in[0] == "AMPLITUDE":
					amplitude()
					#outln(amplitude())

				elif user_in[0] == "PERCENTIL":
					num_percent = int(user_in[1])
					numbers = readln()
					for i in range(len(numbers)):
						numbers[i] = int(numbers[i])
					percent(num_percent, numbers)
						

				elif user_in[0] == "MEDIANA":
					med = median(grid, len(grid))
					#outln(str(med))

				elif user_in[0] == "TCHAU":
					break
				
				else:
					break
				run_time += (time.time() - start_time)
		except EOFError:
			pass
	return run_time



def readln():
	return stdin.readline().rstrip().split(" ")


def outln(string):
	stdout.write(string.rstrip() + "\n")



if __name__=="__main__":
	test_files = ["test_1000.txt", "test_5000.txt", "test_10000.txt", "test_25000.txt", 
                "test_50000.txt", "test_75000.txt",   "test_100000.txt"] #, "test_200000.txt", 
                # "test_300000.txt", "test_400000.txt", "test_500000.txt", "test_600000.txt", 
                # "test_700000.txt", "test_800000.txt", "test_900000.txt", "test_1000000.txt"]
		
	total_matrix_elm = [1000, 5000, 10000, 25000, 50000, 75000, 
                        100000] #, 200000, 300000, 400000, 500000, 
                        #600000, 700000, 800000, 900000, 1000000]

	with open("results.txt", "w") as file:
		for f in range(len(test_files)):
			run_time = main(test_files[f])
			file.write("Tempo " + str(total_matrix_elm[f]) + " casos: " + str(run_time) + "\n")
	
