import matplotlib.pyplot as plt
import numpy as np
import json

net = ['BIO', 'INFO', 'TECH', 'SOCIAL', 'BIO']
dd = ['100 Sets', '200 Sets', '300 Sets']
cc = 'b', 'r', 'g'
dset1 = ['test_all_neat100', 'test_all_neat200', 'test_all_neat300']
dset2 = ['train_all_neat100', 'train_all_neat200', 'train_all_neat300']

for n in net:
	fig = plt.figure()
	plt.title('Cross-Validation for ' + n + ' network - SVM - "1-against-all" - 80/20', fontsize=12);
	with open("conf.json") as json_file:
				s = json.load(json_file)
	plt.rcParams.update(s)
	for i,d in enumerate(dset1):
		testfile = "./svm/" + n + '_' + d + "_.data"
		x,y = np.loadtxt(testfile, delimiter = ',', unpack=True)
		plt.hist(x, bins=20, histtype='stepfilled', normed=True, color=cc[i], alpha=0.3, label=dd[i])
	ax = fig.add_subplot(111)
	ax.set_xlabel('Accuracy')
	ax.set_ylabel('Number of Sets')		
	outputfile = n + '_test_.png'
	plt.legend(loc=2,prop={'size':14})
	plt.savefig(outputfile)

	plt.cla()
	plt.clf()