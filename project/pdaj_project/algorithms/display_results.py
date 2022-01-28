import requests
import json
import matplotlib.pyplot as plt
import random

n = 10
m = 10
points = ["1,3", "3,2", "6,8", "9,6", "5,5"] #, "123,555", "345,543"]
url = 'http://localhost:8000/calculation/sequential'

json_data = {
	"n": n,
	"m": m,
	"points": points
}


def get_results(url, points):
	res = requests.post(url=url, json=json_data)
	data = json.loads(res.json())

	results = data["result"]
	time_in_s = data["time_in_s"]
	max_memory_in_MB = data["max_memory_in_MB"]
	return results, time_in_s, max_memory_in_MB


def random_color():
	return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])


def display_results(res, n, m, points):
	for i in range(0, n):
		for j in range(0, m):
			if (i, j) in read_points(points):
				print('*', end=" ")
			else:
				index = res[i * n + j]
				print(index, end=" ")
		print()


def show_table(res, n, m, points):
	random_colors = [random_color() for p in points]
	colors = []

	for i in range(0, n):
		row_colors = []
		for j in range(0, m):
			if (i, j) in read_points(points):
				row_colors.append((0, 0, 0))
			else:
				index = res[i * n + j]
				row_colors.append(random_colors[index])
		colors.append(row_colors)
	columns = range(0, n)
	fig, ax = plt.subplots()
	ax.set_axis_off()
	ax.table(cellColours=colors, colWidths=[0.02 for x in columns], cellLoc ='center', loc ='upper left')
	plt.show()


def read_points(points):
	point_list = []
	for p in points:
		x, y = p.split(',')
		x, y = int(x), int(y)
		point_list.append((x, y))
	return point_list


def main():
	results, time_in_s, max_memory_in_MB = get_results(url, points)
	print(f"Time is {time_in_s}s")
	print(f"Max memory is {max_memory_in_MB}MB")
	display_results(results, n, m, points)
	show_table(results, n, m, points)


if __name__ == "__main__":
	main()
