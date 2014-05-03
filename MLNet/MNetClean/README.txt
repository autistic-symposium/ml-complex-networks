The data goes to the following steps:
=====================================

1. Cleasing:
------------

Here we get all the outputs from MNet Network Analysis and we put together into vector files, separated by sammpling groups  (for further sampling analysis) and network type. It contains header. Missing values are completed with '-'.

2. Separating:
--------------

Here we get all the outputs from MNet Network Analysis and we put together into vector files for each newtowrk (all sampling results all togethere. We also add an additional column for the class. It does not cointa the above header. Missing values are completed with '0'.

3. Generating Final File:
-----------------------------

Here we read the vectors files from previous step and create a unique file for all the data. 

The file for the entire nets is here. The file "label.data" examplain each column.