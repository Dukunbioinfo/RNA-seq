import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
FPKM = pd.read_csv(r'D:\transcriptLevelAnalysis\quautity\all.FPKM',sep='\t',index_col=0)
diff = pd.read_csv(r'D:\transcriptLevelAnalysis\quautity\DEproteinRNA.csv',header=None)
diff = list(diff[0])
diffFPKM = FPKM.loc[diff,]
diffnew = []
index = diffFPKM.index
value = diffFPKM.values
for i in value:
    tmp = []
    std = np.std(i)
    mean = np.mean(i)
    for j in i:
        tmp.append((j-mean)/std)
    diffnew.append(tmp)
newCol = []
for i in diffFPKM.columns:
    newCol.append(i[:-11])
diffNewPD = pd.DataFrame(diffnew,index = index ,columns= newCol)
diffNewPD.columns=['S12_EH','S13_R','S14_EH','S15_R','S16_R','S17_R','S18_EH','S20_R','S21_EH','S22_EH']

import seaborn as sbn
sbn.set()
g=sbn.clustermap(diffNewPD,standard_scale=True)

plt.subplots_adjust(right=0.7,bottom = 0.2)
ax = g.ax_heatmap
label_x = ax.get_xticklabels()
plt.setp(label_x, rotation=45, horizontalalignment='right',size=12)
label_y = ax.get_yticklabels()
plt.setp(label_y,  size=8)
plt.savefig(r'C:\Users\dklly\Desktop\PARmrna_cluster.svg',dpi=100)
plt.show()
