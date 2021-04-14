class coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance (self, other):
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5
c = coordinate(3,4)
zero = coordinate(0,0)
print(c.distance(zero))
print(coordinate.distance(c, zero))

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result
print(merge([1,5,12,18,19,20],[2,3,4,17]))

def merge_sort(L):
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L)//2
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)
print(merge_sort([1,5,4,8,9,20,10]))