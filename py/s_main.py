#!/usr/bin/python3
import argparse
from c_nn import *

# PATH_NN_OBJECT = '../topology_example.json'
PATH_NN_OBJECT = '../topology_8_16_12_8_4.json'
PATH_TEST_DATA = '../topology_example_test.json'


############### DEFAULT MODE ###############
def mode_default(pathOut, pathNN, pathTest, ii, dtype, interface):
    # load neural network object
    obj = nn(pathNN)
    
    # parse configuration
    obj.parse_configuration()
    
    # show starting configuration
    obj.show_configuration()

    # update configuration
    obj.update_configuration_max_execution(int(ii))

    # update configuration
    obj.set_dtype(dtype)

    # select interface
    obj.set_interface(interface)
    
    # set test data object
    obj.set_test_file(pathTest)
    
    # set relevant paths
    obj.set_path_output(pathOut)
    obj.set_path_testbench(pathOut+"/tb")

    # show final configuration
    obj.show_configuration()

    # generate sources for the output nn
    obj.generate_implementation()


############### INTERACTIVE MODE ###############
def mode_interactive(pathOut, pathNN, pathTest, ii, dtype, interface):
    print("TODO Not yet implemented")


############### ARGUMENT PARSER  ###############
parser = argparse.ArgumentParser(
  description="Noisy sinusoid generation/testing helper script")

parser.add_argument(
  '--topology', dest='topology',
  default="topology.json",
  help='path to the JSON description of the topology')

parser.add_argument(
  '--dtype', dest='dtype',
  default="float",
  help='base data type for the neural network')

parser.add_argument(
  '--interface', dest='interface',
  default="s_axilite",
  choices=["s_axis","s_axilite"],
  help='interface to the neural network, either memory mapped or streaming')

parser.add_argument(
  '--output', dest='output',
  default="out",
  help='output path for the generated topology')

parser.add_argument(
  '--mode', dest='mode',
  default="default",
  choices=["default","interactive"],
  help='mode in which to explore neural network topology')

parser.add_argument(
  '--ii', dest='ii',
  default="32",
  help='target iteration interval')

parser.add_argument(
  '--test', dest='test',
  default=None,
  help='path to the JSON file with test vectors')

############### ACQUIRE ARGUMENTS ###############
args = parser.parse_args()
arg_topology  = args.topology
arg_dtype     = args.dtype
arg_interface = args.interface
arg_output    = args.output
arg_mode      = args.mode
arg_ii        = args.ii
arg_test      = args.test

print("Running script with the following arguments")
print("- topology  = " + args.topology)
print("- dtype     = " + args.dtype)
print("- interface = " + args.interface)
print("- output    = " + args.output)
print("- mode      = " + args.mode)

if arg_mode == "interactive":
    mode_interactive(
        arg_output,      # path output (generated)
        arg_topology,    # path nn input topology
        arg_test,        # path nn test vector
        arg_ii,          # initiation interval
        arg_dtype,       # network's base data type
        arg_interface)   # network's interface
else:
    mode_default(
        arg_output,      # path output (generated)
        arg_topology,    # path nn input topology
        arg_test,        # path nn test vector
        arg_ii,          # initiation interval
        arg_dtype,       # network's base data type
        arg_interface)   # network's interface
