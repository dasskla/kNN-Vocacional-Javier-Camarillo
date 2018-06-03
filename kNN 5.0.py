import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import *
from collections import Counter
style.use('dark_background')

def suma(V):
    a=0
    i=0
    while(i<20): 
        a=a+V[i]
        #print(a)
        i=i+1
    return a/2     

def get_dist(v1,v2):
    dv=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    kv=[0,0,0]
    j=0
    while(j<20):
        i=0
        while(i<=2):       
            kv[i]=abs(v1[j][i]-v2[j][i])            
            i=i+1
        dv[j]=kv[0]+kv[1]+kv[2]
        j=j+1
    V_dist=suma(dv)
    return V_dist

def contestar(n):
    v=list()
    with open('Nv.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        i=0
        j=0
        for line in csv_reader:
            if i==n:                
                while (j+1<22):
                    if line[j]=='1':
                        v.append([1,0,0])
                    elif line[j]=='2':
                        v.append([0,1,0])
                    elif line[j]=='3':
                        v.append([0,0,1])
                    elif line[j]=='0':
                        v.append([0,0,0])
                    j+=1
                return v
            i+=1
                            
def medir_enc():
    i=0
    with open('Nv.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            i=i+1
    return i

def classify(n):
    with open('Nv.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        i=0
        for line in csv_reader:
            if(i==n):
                if line[0]=='Cc':
                    return 'Cc'
                if line[0]=='Ae':
                    return 'Ae'
                if line[0]=='Cv':
                    return 'Cv'
                if line[0]=='Fm':
                    return 'Fm'
            i+=1
            
def get_corx(sur):
    corx=0
    i=0
    while(i<20):
        
        if sur[i]==[1,0,0]:
            corx=corx
        elif sur[i]==[0,1,0]:
            corx=corx-0.5
        elif sur[i]==[0,0,1]:
            corx=corx+0.5
        i+=1
    return corx
def get_cory(sur):
    cory=0
    i=0
    while(i<20):
        
        if sur[i]==[1,0,0]:
            cory=cory+1
        elif sur[i]==[0,1,0]:
            cory=cory-(math.sqrt(3)/2)
        elif sur[i]==[0,0,1]:
            cory=cory-(math.sqrt(3)/2)
        
        i+=1
    return cory

def plot(cat,color,size,mark,modx,mody):
    i=0
    while(i<tamano):
        if sur_v[i].cat==cat:
            plt.scatter(sur_v[i].dist*modx,sur_v[i].dist*mody,size,color=color,marker=mark)
        i+=1

class survey():
    def __init__(self,mat):
        self.ans=mat

def insertionSort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            for j in range(i):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
    return lst

def mode(lst):
    counter=Counter(lst)
    cat=counter.most_common(1)
    return cat[0][0]

tamano=medir_enc()
preg=[0,0,0]
i=0

box=list()

while(i<tamano):
    
    ans=contestar(i)
    box.append(ans)
    i+=1
    
sur_v=list()

i=0
for obj in range(tamano):
    obj=survey(box[i])
    sur_v.append(obj)
    i=i+1

i=0

i=0
while(i<tamano):
    sur_v[i].cat=classify(i)
    i+=1

i=0
while(i<tamano):
    i+=1

i=0

v1=[[0,0,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],
    [1,0,0],[0,0,1],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1],[1,0,0]]
v2=[[1,0,0],[1,0,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],
    [1,0,0],[1,0,0],[1,0,0],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,0,0]]
v3=[[0,1,0],[0,1,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],
    [1,0,0],[0,0,1],[0,0,1],[1,0,0],[0,0,1],[0,1,0],[0,0,1],[1,0,0]]
v4=[[0,1,0],[1,0,0],[0,1,0],[1,0,0],[1,0,0],[0,1,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],
    [0,1,0],[0,0,1],[0,0,1],[1,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0]]

sur_x=survey
sur_x.ans=v4

dist_sum=0

i=0
while(i<tamano):
    sur_v[i].dist=get_dist(sur_x.ans,sur_v[i].ans)
    i+=1
    
i=0
while(i<tamano):
    sur_v[i].corx=sur_v[i].dist
    #sur_v[i].cory=get_cory(sur_v[i].ans)
    i+=1
print ('\n\n')


k=input('Introducir valor de k')
k=int(k)
i=0
dist_v=list()
while(i<tamano):
    dist_v.append(sur_v[i].dist)
    i+=1    
print (dist_v)

insertionSort(dist_v)

print ('distancias ordenadas \n', dist_v)
k_dist=list()
i=0
while(i<k):
    k_dist.append(dist_v[i])
    i+=1

print ('distancias k', k_dist)

k_cat=list()


i=0
while(i<tamano):
    j=0
    while(j<k):
        if sur_v[i].dist==k_dist[j]:
            k_cat.append(sur_v[i].cat)
        j+=1
    i+=1
print (k_cat)

sur_x.cat=mode(k_cat)
print(sur_x.cat)

if(sur_x.cat=='Ae'):
    print('Usted coincide con estudiantes de Aeroespacial')
elif(sur_x.cat=='Cc'):
    print('Usted coincide con estudiantes de Ciencias de la Computacion/Hardware')
elif(sur_x.cat=='Cv'):
    print('Usted coincide con estudiantes de Civil o Topografia')
elif(sur_x.cat=='Fm'):
    print('Usted coincide con estudiantes Fisico/Matematicos')

col_4='#D50000'

col_3='#78909C'
col_2='#B0BEC5'

col_1='#37474F'
labAe = mpatches.Patch(color=col_1,label='Aeroespacial')
labCv = mpatches.Patch(color=col_2,label='Civil')
labCc = mpatches.Patch(color=col_3,label='Sistemas')
labfM = mpatches.Patch(color=col_4,label='Fisico Matematico')
plt.legend(handles=[labAe,labCv,labCc,labfM])


plt.scatter(0+k_dist[0]-1,0,100,color='white',marker='x')
val=30

plot('Ae',col_1,val*16,'s',1,0)
plot('Cv',col_2,val*8,'s',1,0)
plot('Cc',col_3,val*4,'s',1,0)
plot('Fm',col_4,val,'s',1,0)

plt.show()
