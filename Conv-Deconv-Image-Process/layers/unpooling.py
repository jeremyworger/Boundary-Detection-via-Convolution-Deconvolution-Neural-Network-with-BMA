'''
Created on Mar 7, 2016

@author: Wuga
'''

import numpy as np
import theano
from theano.tensor.signal import downsample
from theano import tensor as T
from theano.tensor.nnet import conv

class ReverseMaxPooling(object):
    
    def __init__(self, input, mask, poolsize=(2, 2), ignore_border=True):
        self.input = input
        self.poolsize = poolsize
        self.ignore_border = ignore_border
        
        mask_pooled_out = downsample.max_pool_2d(
            input=mask,
            ds=self.poolsize,
            ignore_border=self.ignore_border
        )
        
        self.output = T.grad(None, wrt=mask, known_grads={mask_pooled_out: input})
#         s1 = self.poolsize[0]
#         s2 = self.poolsize[1]
#         recovered= self.input.repeat(s1, axis=2).repeat(s2, axis=3)
#         if recovered.shape == mask.shape:            
#             output= recovered#*mask
#         else:
#             output= recovered[:,:,:-1,:-1]#*mask
#         self.output=output
        self.input = input

# M=np.array([[[[1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
# [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
# [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
# [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
# [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]]]])
# print M.shape   
# X=np.random.rand(1,1,5,5)
# print X
# input = T.dtensor4('input')
# mask = T.dtensor4('mask')
# layer=ReverseMaxPooling(input, mask)
# f= theano.function([input,mask],layer.output)
# print f(X,M)