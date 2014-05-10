

import matplotlib.pyplot as plt
import numpy as np
import json


testfile = "./ALL_NO_CV_test.data"
datatest = np.loadtxt(testfile, delimiter = ',')



with open("conf.json") as json_file:
		s = json.load(json_file)
 
plt.rcParams.update(s)
plt.plot(datatest[0], label='N=500', marker='o');
plt.plot(datatest[1], label='N=1000',marker='o');
plt.plot(datatest[2], label='N=1500', marker='o');
plt.plot(datatest[3], label='N=2000',marker='o');
plt.plot(datatest[4], label='N=5000',marker='o');
plt.plot(datatest[5], label='All together',marker='*');

#plt.title('SVM');
plt.ylim([0.8,1.05])
plt.xlim([-0.5, 5.5])

ax = plt.gca()
ax.xaxis.set_visible(False)
plt.title('Test Set Results - SVM')
plt.annotate('"1-vs-the-rest", unormalized', xy=(0,0.99), xytext=(-0.2, 1.03), arrowprops=dict(facecolor='red'), color='red',fontsize=9)
plt.annotate('"1-against-1",  xmin ', xy=(1,0.96), xytext=(1.2, 0.91), arrowprops=dict(facecolor='black'), fontsize=9)
plt.annotate('"1-vs-the-rest", Gauss.', xy=(2,1.0), xytext=(2.2, 1.04), arrowprops=dict(facecolor='black'), fontsize=9)
plt.annotate('1-against-1", xmin', xy=(3, 0.96), xytext=(3, 0.93), arrowprops=dict(facecolor='black'), fontsize=9)
plt.annotate('"1-vs-the-rest", Gauss.  ', xy=(4,1.0), xytext=(4.3, 1.03), arrowprops=dict(facecolor='black'), fontsize=9)
plt.annotate('"1-against-1", unormalized', xy=(5,0.92), xytext=(4.5, 0.89), arrowprops=dict(facecolor='red'), color='red',fontsize=9)
ax.set_ylabel('Accuracy')
plt.legend(loc=4,prop={'size':10});
plt.savefig('test.png')
