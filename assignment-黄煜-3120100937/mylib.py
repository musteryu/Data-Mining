import numpy as np
import matplotlib.pyplot as plt
import math

def fget_vctr(path, posi):
	f = open(path, 'r')
	lines = f.readlines()
	f.close()
	return [ float(item) for item in lines[posi * 2 + 1].split(' ') ]


def fget_mtrx(path):
	f = open(path, 'r')
	lines = f.readlines()
	f.close()
	matrix = []

	for line in lines:
		if line[0] != ' ':
			matrix.append( [ float(item) for item in line.split(' ') ] )

	return matrix


def my_hist(vector, min_edge = None, max_edge = None, bucket_size = 10, flat_edge = False, title = 'histrogram', **kwargs):
	# kwargs are other param that could be used in the pyplot.hist() method.

	min_edge = min_edge if min_edge else min(vector)
	max_edge = max_edge if max_edge else max(vector)

	if flat_edge: 
		# Flat the edge to the nearest integral multiple
		min_edge = min_edge // bucket_size * bucket_size 
		max_edge = math.ceil(max_edge / bucket_size ) * bucket_size


	bins = (max_edge - min_edge) / bucket_size
	plt.hist(vector, bins, (min_edge, max_edge), **kwargs)
	plt.title(title);


def get_normal_param(vector):
	# param vector could be python list or numpy array
	if type(vector) == list:
		np_vctr = np.array(vector)
	else:
		np_vctr = vector

	# estimation by maximum likehood function
	ex = np.mean(np_vctr)
	var = np.var(np_vctr)
	return ex, var


def get_uniform_param(vector):
	# param vector could be python list or numpy array
	if type(vector) == list:
		np_vctr = np.array(vector)
	else:
		np_vctr = vector

	# estimation by maximum likehood function
	a = np_vctr.min()
	b = np_vctr.max()
	return a,b

def my_DCT_compression(vector, threshold = 0):
	vector = np.array(vector)
	k = len(vector)
	u = []

	for i in range(k):
		ai = np.sqrt(1/k) if  i == 0 else np.sqrt(2/k)
		if i == 0:
			cos_vector = np.array([1] * k).reshape(k, 1)
		else:
			cos_vector = np.cos( np.arange(i,(2*k+1)*i,2*i)/(2*k) ).reshape(k, 1)
		u.append( float(ai * vector.dot(cos_vector)) )

	dimension = 100
	for i in range(k-1, -1, -1):
		if abs(u[i]/u[0]) < threshold:
			u[i] = 0
		else:
			dimension = i + 1
			break
	return u, dimension
