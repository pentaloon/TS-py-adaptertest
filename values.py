class Test(object):
	def __str__(self):
		return self.__class__.__name__

	def numeric_test(self):
		return 100

	def string_test(self):
		return 'test result PASSED'
		
	def numeric_string_test(self):
		return 'the value of PI is 3.14'

	def numeric_string_pattern_test(self):
		return '768.82'
		
	def numbers_list_test(self):
		return [1.0, 2.0, 3.0, 4.0, 5.0]
		
	def numpy_array_test(self):
		import numpy as np
		values={1.01, 2.20, 3.54, 4.31, 5.26} # a set, need to convert to list
		return np.array(list(values))