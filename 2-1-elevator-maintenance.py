def sanitize(x):
	return map(int, x.split("."))

def solution(l):
	return sorted(l, cmp=lambda x,y: cmp(sanitize(x), sanitize(y)))