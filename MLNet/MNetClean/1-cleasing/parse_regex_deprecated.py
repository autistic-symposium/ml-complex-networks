def aaa():

    NET_NAMES = ["flickr"]
    FILES = ["flickrEdges.txt"]
    net_names_sets = set(NET_NAMES)

    SNAP_FILE = "SNAP.dat"

     '''
       Split the file into all the words (cleaning spaces)
    '''
    with open(fraw, "r") as f:
        all_words = re.split('\W+', f.read())
        print(all_words)

  
    '''
       Find the indices where the networks start.
    '''
    index_nets = []
    for i_word, word in enumerate(all_words):
    	if word in net_names_sets:
            net_names_sets.remove(word)
            index_nets.append(i_word)
    index_nets.append(i_word)
 

    ''' 
	Separate for each network
    '''
    all_unique_net = []
    for i_index in range(0, len(index_nets)-1):
        where_to_start = index_nets[i_index]
        where_to_stop = index_nets[i_index + 1]
        all_unique_net.append(all_words[where_to_start:where_to_stop])
    
   
     '''
      Extracting features
    '''
    feature_vector = []
    for i in range(len(all_unique_net)):
	net = all_unique_net[i]
        feat_aux = []

        for j in range(len(net)-4):
            wor = net[j]
            if wor == "Nodes": 
        	if net[j+1] != 'in':
			feat_aux.append(net[j+1])
		else:
			feat_aux.append(net[j+4])   
            elif wor == "Edges": 
        	if net[j+1] != 'in':
			feat_aux.append(net[j+1])
		else:
			feat_aux.append(net[j+4])   
    
            elif wor == "Average": 
		feat_aux.append(net[j+3] +'.' + net[j+4])  

            elif wor == "Number": 
		feat_aux.append(net[j+3])  

            elif wor == "Fraction": 
		feat_aux.append(net[j+4] +'.' + net[j+5])  
 
            elif wor == "Diameter": 
		feat_aux.append(net[j+4])

            elif wor == "90": 
                feat_aux.append('.'.join(net[j+4:]))
      
    	feature_vector.append(feat_aux)
    

    '''
	Get data from VECTOR files
    '''
    feature_vector_VECTOR = []
    for i, net_here in enumerate(FILES):	
        f_local = open(net_here + '_VECTOR.dat', "r")
        lines = f_local.readlines()
        f_local.close()
        feature_vector_VECTOR_aux = []
        for j in range(4):
	    feature_vector_VECTOR_aux.append(lines[j].split()[1])
        feature_vector_VECTOR.append(feature_vector_VECTOR_aux)
  

    '''
       Saving output file
    '''
    out_file = open("GLOBAL_FEATURES_VECTOR.dat", 'w')
    out_file.write("# Nones, Edges, Ave. Clust. Coeff., Num. Triangles, Fraction Closed Triangles, Diamter, 90-perc eff. diameter, Assortativity, Transitivity\n\n")

    for f in range(len(feature_vector)):
        out_file.write(NET_NAMES[f] + ' ')
        for i in  range(len(feature_vector[f])):
            out_file.write(str(feature_vector[f][i]) + ' ')
	
        for i in range(2, 4):
            out_file.write(str(feature_vector_VECTOR[f][i]) + ' ')

        out_file.write('\n') 



    out_file.close()