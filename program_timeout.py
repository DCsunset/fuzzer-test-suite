import matplotlib.pyplot as plt
import pandas as pd
import glob
import numpy as np
import os
 
timeout_file_name = "timeout.txt"
timeout_list = []
for file in glob.glob("./data/*.txt"):
    data = []
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.split(" ", 1)
        data.append(line)
    
    #data = pd.read_csv(file, sep=",", header=None)
    df = pd.DataFrame(data)
    timeout = df[0].nunique() # shape is not correct, we need the distingush time stamp of lines
    f.close()

    file_name = file[0:-4] + "_timeout.txt"
    timeout_list.append([file_name, timeout])           

f = open("timeout.txt", "a")
for timeout in timeout_list:
    for e in timeout:
        f.write(str(e) + ",")
    f.write('\n')
f.close()

x = [timeout[0][7:-19] for timeout in timeout_list]
y = [timeout[1]*5/60 for timeout in timeout_list]
fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
ax.barh(ind, y, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
for i, v in enumerate(y):
    v = int(v)
    ax.text(int(v + 3), i - 0.25, str(v), color='blue', fontweight='bold')
plt.title('Timeout in Various Programs')
plt.xlabel('Timeout in Hours')
plt.ylabel('Programs')      
plt.xlim(-0.5,50) 
plt.show()
plt.savefig(os.path.join('timeout.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial pictures