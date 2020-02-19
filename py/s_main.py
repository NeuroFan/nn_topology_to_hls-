#!/usr/bin/python
from c_nn import *

# PATH_NN_OBJECT = '../topology_example.json'
PATH_NN_OBJECT = '../topology_8_16_12_8_4.json'
PATH_TEST_DATA = '../topology_example_test.json'

if __name__ == "__main__":
	# load neural network object
	obj = nn(PATH_NN_OBJECT)

	# parse configuration
	obj.parse_configuration()
	
	# show configuration
	obj.show_configuration()
	print

	# update configuration
	obj.update_configuration_max_execution(32)
	# print

	# apply data type configuration 
	obj.set_dtype("float")
	# obj.set_dtype_fixed(16, 7)
	# obj.set_dtype_fixed_LUT_input(12, 4)
	# obj.set_dtype_fixed_LUT_output(16, 7)

	# select interface
	obj.set_interface("s_axis")
	# obj.set_interface("s_axilite")

	# set test data object
	# obj.set_test_file(PATH_TEST_DATA)

	# set relevant paths
	obj.set_path_output("hls/main")
	# obj.set_path_testbench("hls/main")

	# show configuration
	obj.show_configuration()
	print

	# generate implementation and testbench
	obj.generate_implementation()
	# obj.generate_testbench()