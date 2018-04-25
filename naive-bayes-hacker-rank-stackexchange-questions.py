# Hacker Rank - Stack Exchange Question Classifier
#!/usr/bin/env python
import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

arr=open('training.json', 'r+').read().strip().split("\n")
m=int(arr[0])
arr.pop(0)
j=[json.loads(unicode(arr[p],'latin-1')) for p in range(len(arr))]
q=[j[p]["question"] for p in range(len(j))]
e=[j[p]["excerpt"] for p in range(len(j))]
t=[j[p]["topic"] for p in range(len(j))]
dfx1=pd.DataFrame(e)
yarr=np.array(t)

arr1=open('eval.json', 'r+').read().strip().split("\n")
n=int(arr1[0])
arr1.pop(0)
j1=[json.loads(unicode(arr1[p],'latin-1')) for p in range(len(arr1))]
e1=[j1[p]["excerpt"] for p in range(len(j1))]
dfx2=pd.DataFrame(e1)

df=[dfx1,dfx2]
dfx=pd.concat(df)

v=CountVectorizer()
v.fit(dfx[0])
xarr=v.transform(dfx[0])

xtrain=xarr[:m]
xeval=xarr[m:m+n]
ytrain=yarr

clf = MultinomialNB()
clf.fit(xtrain, ytrain)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

pred=clf.predict(xeval)

a=" "
for p in pred:  a+=str(p)+"\n"
print(a.strip())
