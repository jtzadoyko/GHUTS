# -*- coding: utf-8 -*-
# @Author: jtzdoyko
# @Date:   2020-10-18 19:39:37
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2020-10-18 20:05:11
from math import ceil


def batchLoading( list_arg:list, bsize:int = 5 ):
	"""
	ARGS
	:: list_arg - iterable object which should be proccess via batch loads
	:: bsize - size of each batch that should be evaluated
	"""

	BATCH_ITERS =  ceil( len(list_arg) / bsize )

	print( "LOADING bsize of {}, executing {} iterations on list".format(bsize, BATCH_ITERS) )


	for i in range(BATCH_ITERS):
		if BATCH_ITERS - i - 1 != 0:
			print("TOTAL ITEMS: {} \t CURRENT_BATCH: {} \t START_INDEX: {} \t END_INDEX: {}".format(len(list_arg), i, i * bsize, (i + 1) * bsize))
			print( list_arg[i * bsize:(i + 1) * bsize] )
		else:
			print("TOTAL ITEMS: {} \t CURRENT_BATCH: {} \t START_INDEX: {} \t END_INDEX: {}".format(len(list_arg), i, i * bsize, len(list_arg)))
			print( list_arg[i * bsize:None] )

my_list = ['val1','val2','val3','val4','val5','val6','val7','val8','val9','val10']
batchLoading(my_list, bsize = 2)
batchLoading(my_list, bsize = 6)