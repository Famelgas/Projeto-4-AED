from sys import stdin, stdout
import random



grid = []


def raster(A: int, B: int):
	for i in range(A):
		user_in = readln()
		for j in range(B):
			grid.append(int(user_in[j])) 
	outln("RASTER GUARDADO")
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
	outln(output)







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
			med = median(grid, len(grid))
			#median = selection_algorithm(0, len(grid), len(grid) / 2)
			outln(str(med))

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