#!/bin/bash

cd ./normalization/normalization_with_outlier-T/
python plot_normalization.py
cd ../normalization/normalization_with_outlier-F/
python plot_normalization.py
cd ..