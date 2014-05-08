#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

PERCENTAGE = 0.8

OUTPUT_FOLDER  = "../../data/vectors_normalized/"
OUTPUT_TRAIN_G    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_gauss.data" 
OUTPUT_TEST_G     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_gauss.data" 
OUTPUT_TRAIN_M    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_xmin.data" 
OUTPUT_TEST_M     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_xmin.data" 
OUTPUT_TRAIN_N    = OUTPUT_FOLDER + "train_" + str(PERCENTAGE) + "_none.data" 
OUTPUT_TEST_N     = OUTPUT_FOLDER + "test_" + str(PERCENTAGE) + "_none.data" 

INPUT_FOLDER     = '../../data/train_test/'
IN_FILE_TRAIN = INPUT_FOLDER + "train_" + str(PERCENTAGE) + ".data" 
IN_FILE_TEST  = INPUT_FOLDER + "test_" + str(PERCENTAGE) + ".data" 
