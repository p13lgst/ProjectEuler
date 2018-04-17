def main():
	grid = formatGrid(open('11.txt').readlines())
	print(getMults(grid))

def formatGrid(grid):
	newGrid = []
	for i in grid:
		line = []
		for j in i.split():
			line.append(int(j))
		newGrid.append(line)
	return newGrid

def getMults(grid):
	return max([multH(grid), multV(grid), multD1(grid), multD2(grid)])

def multH(grid):
	maxMult = 0
	for i in grid:
		for j in range(len(i) - 3):
			mult = i[j]*i[j+1]*i[j+2]*i[j+3]
			if mult > maxMult:
				maxMult = mult
	return maxMult

def multV(grid):
	maxMult = 0
	for i in range(len(grid) - 3):
		for j in range(len(grid)):
			mult = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
			if mult > maxMult:
				maxMult = mult
	return maxMult

def multD1(grid):
	maxMult = 0
	for i in range(len(grid) - 3):
		for j in range(len(grid) - 3):
			mult = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
			if mult> maxMult:
				maxMult = mult
	return maxMult

def multD2(grid):
	maxMult = 0
	for i in range(len(grid) - 3):
		for j in range(3, len(grid)):
			mult = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
			if mult> maxMult:
				maxMult = mult
	return maxMult

if __name__ == '__main__':
	main()
