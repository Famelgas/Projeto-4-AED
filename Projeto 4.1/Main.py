from sys import stdin, stdout
import random
import time


grid = []


def raster(file,A: int, B: int):
	for i in range(A):
		user_in = readln(file)
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


def partition(arr, l, r) :

	lst = arr[r]; i = l; j = l;
	
	# vai trocando os elementos para que o indice da particao
	# esteja onde queremos para ser devolvido
	while (j < r) :
		if (arr[j] < lst) :
			arr[i], arr[j] = arr[j],arr[i];
			i += 1;
		
		j += 1;

	arr[i], arr[r] = arr[r],arr[i];
	return i;


# esolhe um pivot entre l e r e divide o array ao meio 
# nesse pivot
def random_partition(arr, l, r) :
	n = r - l + 1;
	pivot = random.randrange(1, 100) % n;
	arr[l + pivot], arr[r] = arr[r], arr[l + pivot];
	return partition(arr, l, r);


def median_util(arr, l, r, k, a1, b1) :

	global a, b;
	
	# if l < r
	if (l <= r) :
		
		# encontrar o index da particao
		partition_index = random_partition(arr, l, r);
		
		# se o indice da particao for igual ao k, entao
		# encontramos a mediana
		if (partition_index == k) :
			b = arr[partition_index];
			if (a1 != -1) :
				return;
				
		# se index = k - 1 entao temos a e b no meio
		# logo a mediana sera a media dos dois
		elif (partition_index == k - 1) :
			a = arr[partition_index];
			if (b1 != -1) :
				return;
				
		# se o index for maior que k entao a mediana estara 
		# na primeira metade do array
		if (partition_index >= k) :
			return median_util(arr, l, partition_index - 1, k, a, b);
			
		# se o index for menor que k entao a mediana estara
		# na segunda metade do array
		else :
			return median_util(arr, partition_index + 1, r, k, a, b);
			
	return;

def median(arr, n) :
	global a;
	global b;
	a = -1;
	b = -1;
	
	# impar
	if (n % 2 == 1) :
		median_util(arr, 0, n - 1, n // 2, a, b);
		ans = b;
		
	# par
	else :
		median_util(arr, 0, n - 1, n // 2, a, b);
		ans = (a + b) // 2;
	
	return ans







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



def readln(file):
	return file.readline().rstrip().split(" ")


def outln(string):
	stdout.write(string.rstrip() + "\n")



if __name__=="__main__":
	test_files = ["test_10.txt", "test_50.txt", "test_100.txt", "test_250.txt", 
				"test_500.txt", "test_750.txt", "test_1000.txt", "test_5000.txt", "test_10000.txt", "test_25000.txt", 
                "test_50000.txt", "test_75000.txt",   "test_100000.txt"]
	total_matrix_elm = [10, 50, 100, 250, 500, 750, 1000, 5000, 10000, 25000,
                        50000, 75000, 100000]

	run_times = []

	for f in (test_files):
		run_time = main(f)
		print(run_time)
		run_times.append(main(f))

	with open("results.txt", "w") as file:
		for r in range(len(run_times)):
			file.write("Tempo " + str(total_matrix_elm[r]) + " casos: " + str(run_times[r]) + "\n")
	
