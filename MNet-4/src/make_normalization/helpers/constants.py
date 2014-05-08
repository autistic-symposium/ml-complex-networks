#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "4.1"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


# Definition of some paths
PATH_2_INPUT = "../../data/" 
PATH_2_OUTPUT = "../../output/"
PATH_2_GRAPH_SAMPLED = "graphs_sampled/" 
PATH_2_GRAPH_GLOBAL = "graphs_global/" 
PATH_2_FEATURES_SAMPLED = "vector_sampled/"  
PATH_2_FEATURES_GLOBAL = "vector_global/" 


# How many samples to be sampled, this is a deprecated
# feature since we introduced checking in the mhrw
NUM_SAMPLES = 1

# MHRW sampling, given by order
ORDER_SAMPLING = [100, 300, 500, 1000, 2000]
MIN_SIZE       = [50, 150, 250,  500, 1000]

# Files we want for each network.
# This could be automatized, but we want to be able
# to select some files manually, it can be automatized in the
# future if time allows it.

NETWORK_FILES_UN_YEAST  = ["1.dat", '2.dat', '3.dat']
NETWORK_FILES_UN_ATLAS = ['1.dat', '2.dat', '3.dat', '4.dat', '5.dat', '6.dat', '7.dat', '8.dat']
NETWORK_FILES_UN_CARBON = ['out.foodweb-baydry', 'out.foodweb-baywet']
NETWORK_FILES_UN_METABOLIC = ['1.dat', '2.dat', '3.dat', '4.dat', '5.dat', '6.dat', '7.dat', '8.dat', '9.dat', '10.dat', '11.dat', '12.dat', '13.dat', '14.dat', '15.dat', '16.dat', '17.dat', '18.dat', '19.dat', '20.dat', '21.dat', '22.dat', '23.dat', '24.dat', '25.dat', '26.dat', '27.dat', '28.dat', '29.dat', '30.dat', '31.dat', '32.dat', '33.dat', '34.dat','35.dat','36.dat','37.dat','38.dat','39.dat', '40.dat','41.dat','42.dat','43.dat' ]
NETWORK_FILES_UN_CELLULAR = ['1.dat', '2.dat', '3.dat', '4.dat', '5.dat', '6.dat', '7.dat', '8.dat', '9.dat', '10.dat', '11.dat', '12.dat', '13.dat', '14.dat', '15.dat', '16.dat', '17.dat', '18.dat', '19.dat', '20.dat', '21.dat', '22.dat', '23.dat', '24.dat', '25.dat', '26.dat', '27.dat', '28.dat', '29.dat', '30.dat', '31.dat', '32.dat', '33.dat', '34.dat','35.dat','36.dat','37.dat','38.dat','39.dat', '40.dat','41.dat','42.dat','43.dat' ]
NETWORK_FILES_DIR_SOCIAL_II = ["out.advogato", "out.dbpedia-occupation", "out.munmun_twitter_social", "out.petster-friendships-hamster", "out.petster-hamster", "out.slashdot-zoo", "out.ucidata-gama", "out.ucidata-zachary", "out.youtube-groupmemberships", "wiki-Vote.txt", "soc-Slashdot0902.txt", "soc-Slashdot0811.txt", "soc-Epinions1.txt"]
NETWORK_FILES_DIR_SOCIAL = ["twitter", "gplus", "facebook"]  
NETWORK_FILES_UN_AUTO = ["as20000102.txt", "oregon1_010331.txt", "oregon1_010407.txt", "oregon1_010414.txt", "oregon1_010421.txt", "oregon1_010428.txt", "oregon1_010505.txt", "oregon1_010512.txt", "oregon1_010519.txt", "oregon1_010526.txt", "oregon2_010331.txt", "oregon2_010407.txt", "oregon2_010414.txt", "oregon2_010421.txt", "oregon2_010428.txt", "oregon2_010505.txt", "oregon2_010512.txt", "oregon2_010519.txt", "oregon2_010526.txt"]
NETWORK_FILES_DIR_AUTO = ["as-caida20040105.txt", "as-caida20040202.txt", "as-caida20040301.txt", "as-caida20040405.txt", "as-caida20040503.txt", "as-caida20040607.txt", "as-caida20040705.txt", "as-caida20040802.txt", "as-caida20040906.txt", "as-caida20041004.txt", "as-caida20041101.txt", "as-caida20041206.txt", "as-caida20050103.txt", "as-caida20050207.txt", "as-caida20050307.txt", "as-caida20050404.txt", "as-caida20050502.txt", "as-caida20050606.txt", "as-caida20050704.txt", "as-caida20050801.txt", "as-caida20050905.txt", "as-caida20051003.txt", "as-caida20051107.txt", "as-caida20051205.txt", "as-caida20060102.txt", "as-caida20060109.txt", "as-caida20060116.txt", "as-caida20060123.txt", "as-caida20060130.txt", "as-caida20060206.txt", "as-caida20060213.txt", "as-caida20060220.txt", "as-caida20060227.txt", "as-caida20060306.txt", "as-caida20060313.txt", "as-caida20060320.txt", "as-caida20060327.txt", "as-caida20060403.txt", "as-caida20060410.txt", "as-caida20060417.txt", "as-caida20060424.txt", "as-caida20060501.txt", "as-caida20060508.txt", "as-caida20060515.txt", "as-caida20060522.txt", "as-caida20060529.txt", "as-caida20060605.txt", "as-caida20060612.txt", "as-caida20060619.txt", "as-caida20060626.txt", "as-caida20060703.txt", "as-caida20060710.txt", "as-caida20060717.txt", "as-caida20060724.txt", "as-caida20060731.txt", "as-caida20060807.txt", "as-caida20060814.txt", "as-caida20060821.txt", "as-caida20060828.txt", "as-caida20060904.txt", "as-caida20060911.txt", "as-caida20060918.txt", "as-caida20060925.txt", "as-caida20061002.txt", "as-caida20061009.txt", "as-caida20061016.txt", "as-caida20061023.txt", "as-caida20061030.txt", "as-caida20061106.txt", "as-caida20061113.txt", "as-caida20061120.txt", "as-caida20061127.txt", "as-caida20061204.txt", "as-caida20061211.txt", "as-caida20061218.txt", "as-caida20061225.txt", "as-caida20070101.txt", "as-caida20070108.txt", "as-caida20070115.txt", "as-caida20070122.txt", "as-caida20070129.txt", "as-caida20070205.txt", "as-caida20070212.txt", "as-caida20070219.txt", "as-caida20070226.txt", "as-caida20070305.txt", "as-caida20070312.txt", "as-caida20070319.txt", "as-caida20070326.txt", "as-caida20070402.txt", "as-caida20070409.txt", "as-caida20070416.txt", "as-caida20070423.txt", "as-caida20070430.txt", "as-caida20070507.txt", "as-caida20070514.txt", "as-caida20070521.txt", "as-caida20070528.txt", "as-caida20070604.txt", "as-caida20070611.txt", "as-caida20070618.txt", "as-caida20070625.txt", "as-caida20070702.txt", "as-caida20070709.txt", "as-caida20070716.txt", "as-caida20070723.txt", "as-caida20070730.txt", "as-caida20070806.txt", "as-caida20070813.txt", "as-caida20070820.txt", "as-caida20070827.txt", "as-caida20070903.txt", "as-caida20070910.txt", "as-caida20070917.txt", "as-caida20070924.txt", "as-caida20071001.txt", "as-caida20071008.txt", "as-caida20071015.txt", "as-caida20071022.txt", "as-caida20071029.txt", "as-caida20071105.txt", "as-caida20071112.txt"]
NETWORK_FILES_DIR_CITATION = ["cit-HepPh.txt", "cit-HepTh.txt"]#,  "cit-Patents.txt"]  
NETWORK_FILES_UN_COLLABORATION = ["ca-AstroPh.txt", "ca-CondMat.txt", "ca-GrQc.txt", "ca-HepPh.txt", "ca-HepTh.txt", "out.dblp-cite", "out.dbpedia-producer",  "out.github", "out.opsahl-collaboration", "out.subelj_cora"] 
NETWORK_FILES_UN_COMMUNICATION = ["email-Enron.txt"]
NETWORK_FILES_DIR_COMMUNICATION = ["email-EuAll.txt"]
NETWORK_FILES_UN_GROUND = ["com-amazon.ungraph.txt", "com-dblp.ungraph.txt",  "com-youtube.ungraph.txt"]#"com-lj.ungraph.txt", "com-orkut.ungraph.txt"]
NETWORK_FILES_DIR_LOCATION = ["loc-brightkite_edges.txt", "loc-gowalla_edges.txt"] 
NETWORK_FILES_DIR_MEME = ["higgs-mention_network.edgelist", "higgs-reply_network.edgelist", "higgs-retweet_network.edgelist" ] 
NETWORK_FILES_DIR_ONLINECOM = ["flickrEdges.txt" ] 
NETWORK_FILES_DIR_P2P = ["p2p-Gnutella04.txt", "p2p-Gnutella05.txt", "p2p-Gnutella06.txt", "p2p-Gnutella08.txt", "p2p-Gnutella09.txt", "p2p-Gnutella24.txt", "p2p-Gnutella25.txt", "p2p-Gnutella30.txt", "p2p-Gnutella31.txt" ] 
NETWORK_FILES_DIR_PRODUCTS = ["amazon0302.txt", "amazon0312.txt", "amazon0505.txt", "amazon0601.txt"] 
NETWORK_FILES_UN_ROAD = ["roadNet-CA.txt", "roadNet-PA.txt", "roadNet-TX.txt","out.opsahl-openflights", "out.opsahl-powergrid", "out.opsahl-usairport", "out.subelj_euroroad"]
NETWORK_FILES_DIR_SIGNED = ["soc-sign-epinions.txt", "soc-sign-Slashdot081106.txt", "soc-sign-Slashdot090216.txt", "soc-sign-Slashdot090221.txt"]#, "wikiElec.ElecBs3.txt"]
NETWORK_FILES_DIR_WEBGRAPHS = ["web-NotreDame.txt", "web-Stanford.txt"]#
NETWORK_FILES_DIR_WIKI = [ "wiki-Vote.txt"]#, "wikiElec.ElecBs3.txt"]
