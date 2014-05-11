#!/bin/bash

cd ./lr-knn-svm-comparison/

#python plot_with_out_no_zero.py
#python plot_with_out_with_zero.py
python plot_no_out_no_zero.py
python plot_no_out_with_zero.py
cd ..