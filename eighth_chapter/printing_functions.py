def print_function(*inputs):
	"""打印inputs中的内容，每个内容之间间隔一个空格"""
	answer = ''
	for i in inputs:
		answer += (i + ' ')
	return answer