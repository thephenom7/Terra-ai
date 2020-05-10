import pandas as pd
filenames = ['total_acc_x_train.txt', 'total_acc_y_train.txt', 'total_acc_z_train.txt']
frames=[]
sdf=pd.read_csv('total_acc_z_train.txt')
for file in filenames:
   frames.append(pd.read_csv(file)) 
df = pd.concat(frames, axis=1)
df.to_csv('/home/akshayaksh/Desktop/INTERNSHIP/output.txt', sep='\t')



