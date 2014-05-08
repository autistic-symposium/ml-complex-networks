#!/bin/bash 


./run_p2p.sh > op2p &
./run_products.sh > opro &
./run_road.sh > oroad & 
./run_signed.sh > orsig14 &
./run_social_II.sh > osocial2 & 
./run_social_I.sh > osocial1 & 
./run_webgraphs.sh > oweb &
./run_wiki.sh > owiki &
./run_yeast.sh > oyeast &
