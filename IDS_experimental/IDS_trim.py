import pandas as pd

## columns 0,1,4,5,23,35 are selected

df = pd.read_csv("/home/vinay/Downloads/Network-Intrusion-Detection-master/NSL-KDD/kddtrain.csv", header=None)

print(df.head())

columnsList = [0,1,4,5,23,35,41,42]
df_mod = df.iloc[:,columnsList]
print(df_mod.head())

col_names = ["duration","protocolType","srcBytes","dstBytes","srvCount","dst_host_same_src_port_rate","attackType","attackNumber"]

df_mod.columns = col_names

df_mod.to_csv("kddtrain_trim.csv")

#print(df.cloumns)
