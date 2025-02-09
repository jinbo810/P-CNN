import numpy as np
import pylab
import pickle as p

import sys
caffe_root = '../'
sys.path.insert(0, caffe_root + 'python')
import caffe

caffe.set_mode_gpu()

def f23(conv4_3):
	model_def = 'deploy23.prototxt'
	#model_weights = 'test.caffemodel'

	net = caffe.Net(model_def,
		            #model_weights,
		            caffe.TEST)
	#構造相同的維度
	net.blobs['conv4_3'].data[...] = conv4_3

	net.forward()

	output = net.blobs['relu4_3'].data
	
	return output