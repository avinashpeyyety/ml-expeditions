# Hacker Rank - Quora Answer classifier Challenge
import pandas as pd
data='5 23\n2LuzC +1 1:2101216030446 2:1.807711 3:1 4:4.262680 5:4.488636 6:87.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.891820 12:0 13:1 14:0 15:0 16:0 17:1 18:1 19:0 20:2 21:2.197225 22:0.000000 23:0.000000\nLmnUc +1 1:99548723068 2:3.032810 3:1 4:2.772589 5:2.708050 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:4.727388 12:5 13:1 14:0 15:0 16:1 17:1 18:0 19:0 20:9 21:2.833213 22:0.000000 23:0.000000\nZINTz -1 1:3030695193589 2:1.741764 3:1 4:2.708050 5:4.248495 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.091042 12:1 13:1 14:0 15:0 16:0 17:1 18:1 19:0 20:5 21:2.564949 22:0.000000 23:0.000000\ngX60q +1 1:2086220371355 2:1.774193 3:1 4:3.258097 5:3.784190 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.258097 12:0 13:1 14:0 15:0 16:0 17:1 18:0 19:0 20:5 21:2.995732 22:0.000000 23:0.000000\n5HG4U -1 1:352013287143 2:1.689824 3:1 4:0.000000 5:0.693147 6:0.000000 7:0.000000 8:0.000000 9:0 10:1 11:1.791759 12:0 13:1 14:1 15:0 16:1 17:0 18:0 19:0 20:4 21:2.197225 22:0.000000 23:0.000000\n2\nPdxMK 1:340674897225 2:1.744152 3:1 4:5.023881 5:7.042286 6:0.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.367296 12:0 13:1 14:0 15:0 16:0 17:0 18:0 19:0 20:12 21:4.499810 22:0.000000 23:0.000000\nehZ0a 1:2090062840058 2:1.939101 3:1 4:3.258097 5:2.995732 6:75.000000 7:0.000000 8:0.000000 9:0 10:0 11:3.433987 12:0 13:1 14:0 15:0 16:1 17:0 18:0 19:0 20:3 21:2.639057 22:0.000000 23:0.000000'
                                             
#data=sys.stdin.read()
arr=data.strip().split("\n")
n=int(arr[0].strip().split()[0])
m=int(arr[0].strip().split()[1])
l=int(arr[n+1])
train_f,evl_f=[],[]
for p in range(n):  train_f.append(arr[1+p])
for q in range(l):  evl_f.append(arr[n+2+q])
train_g,evl_g=[],[]
for r in range(n):  train_g.append(list(train_f[r].split()))
for t in range(l):  evl_g.append(list(evl_f[t].split()))
train_x=[[list(p.split(':'))[1] for p in s[2:]] for s in train_g]
train_y=[list(train_f[s].split())[1] for s in range(len(train_f))]
train_ind=[list(train_f[s].split())[0] for s in range(len(train_f))]
evl_x=[[list(p.split(':'))[1] for p in s[1:]] for s in evl_g]
evl_ind=[list(evl_f[s].split())[0] for s in range(len(evl_f))]

df_train_x=pd.DataFrame(train_x)
df_train_y=pd.DataFrame(train_y)
df_evl_x=pd.DataFrame(evl_x)

# Running a Decision tree model
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(df_train_x, df_train_y)
predictions = tree_reg.predict(df_evl_x).astype(int)

out=zip(evl_ind, predictions)
q=""
for p in range(len(out)):  
  q+=str(out[p][0])+" "+"%+d"%(out[p][1])+"\n"
print(q.strip())
