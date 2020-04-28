import matplotlib.pyplot as plt
import json
import numpy as np
import glob
from datetime import datetime

try:
    envi = os.environ['envi']
except:
    envi = "development"
finally:
    print("Environment: %s" %(envi))

if envi=='colab':
  dirPath = r"/content/drive/My Drive/save_model/stage_1_"
else:
  dirPath = r"./stage_1_"

lista = glob.glob(dirPath+"*.json")
arr = []
for k in range(len(lista)):
  s = lista[k].replace(dirPath,"")
  s = s.replace(".json","")
  arr.append(int(s))
arr.sort()

#print(arr)
eps = []
for z in range(len(arr)):
  with open(dirPath+str(arr[z])+'.json') as outfile:
    param = json.load(outfile)
    eps.append(param.get('epsilon'))
#print(eps)

plt.plot(arr,eps)
plt.ylabel('Epsilon')
plt.xlabel('Iteration Number')
plt.title("error vs numero de repeticiones")
now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")
#print(date_time)
plt.savefig(dirPath+'plot'+date_time+'.png')
plt.show()