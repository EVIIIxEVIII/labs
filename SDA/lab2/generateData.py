import array
import random

def generate_random_ints(n, lower_bound=0, upper_bound=100):
	"""Generate a list of n random integers between lower_bound and upper_bound."""
	return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def main():
	n = 31
	data = generate_random_ints(n, 0, 10000)
	a = array.array('i', data)

	with open("data/31.bin", "wb") as f:
		a.tofile(f)

	n = 33
	data = generate_random_ints(n, 0, 10000)
	a = array.array('i', data)

	with open("data/33.bin", "wb") as f:
		a.tofile(f)

	n = 500
	data = generate_random_ints(n, 0, 10000)
	a = array.array('i', data)

	with open("data/500.bin", "wb") as f:
		a.tofile(f)

	n = 5000
	data = generate_random_ints(n, 0, 10000)
	a = array.array('i', data)

	with open("data/5000.bin", "wb") as f:
		a.tofile(f)

	n = 100000
	data = generate_random_ints(n, 0, 1000000)
	a = array.array('i', data)

	with open("data/100000.bin", "wb") as f:
		a.tofile(f)

	n = 10000000
	data = generate_random_ints(n, 0, 2147483646)
	a = array.array('i', data)

	with open("data/10000000.bin", "wb") as f:
		a.tofile(f)

if __name__ == "__main__":
	main()
