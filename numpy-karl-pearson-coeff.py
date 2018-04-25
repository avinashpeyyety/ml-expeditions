# Karl pearson Coefficient
import numpy as np
import decimal
data='Physics Scores 15 12 8 8 7 7 7 6 5 3\nHistory Scores 10 25 17 11 13 17 20 13 9 15'

data=sys.stdin.read()
arr=data.strip().split("\n")
arr1=arr[0].strip().split()
arr2=arr[1].strip().split()
arr1.pop(0)
arr1.pop(0)
arr2.pop(0)
arr2.pop(0)
arr3=[int(q) for q in arr1]
arr4=[int(q) for q in arr2]
p=round(Decimal(np.corrcoef(arr3, arr4)[0,1]),3)
print(str(p))
