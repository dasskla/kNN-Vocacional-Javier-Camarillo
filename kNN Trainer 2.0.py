import csv
import math

from collections import Counter


def suma(V):
    a=0
    i=0
    while(i<20): 
        a=a+V[i]
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
    
print (box[5])
sur_v=list()

i=0
for obj in range(tamano):
    obj=survey(box[i])
    sur_v.append(obj)
    i=i+1

i=0
for sur in box:
    sur_v[i].ans=sur
    sur_v[i].iden=i
    i+=1
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





    
k=input('Introducir valor de k')
k=int(k)
a=0
a_count=0
ae_data=list()
i=0
while(i<10):
    if(sur_v[i].cat=='Ae'):
        ae_data.append(sur_v[i].ans)
        i+=1
while(a<10):
    print('training#',a)
    i=0
    while(i<1+a):
        if(sur_v[i].cat=='Ae'):
            v1=(sur_v[i].ans)
            
        i+=1
    print('vamos en la encuesta',v1)

        
    sur_x=survey
    sur_x.ans=v1
    i=0
    while(i<tamano):
        sur_v[i].dist=get_dist(sur_x.ans,sur_v[i].ans)
        i+=1      
    i=0
    dist_v=list()
    while(i<tamano):
        if(sur_v[i].dist!=0):
            
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
    if(sur_x.cat=='Ae'):
        a_count+=1
        
    print(sur_x.cat)
    a+=1

b=0
b_count=0
cv_data=list()
i=0
while(j<10):
    if(sur_v[i].cat=='Cv'):
        cv_data.append(sur_v[i].ans)
        j+=1
    i+=1

while(b<10):
    print('training#',b)
    i=0
    j=0
    while(j<1+b):
        if(sur_v[i].cat=='Cv'):
            v1=(sur_v[i].ans)
            j+=1
        i+=1
    print('vamos en la encuesta',v1)
    sur_x.ans=v1
    i=0
    while(i<tamano):
        sur_v[i].dist=get_dist(sur_x.ans,sur_v[i].ans)
        i+=1        

    i=0
    dist_v=list()
    while(i<tamano):
        if(sur_v[i].dist!=0):
            
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
    if(sur_x.cat=='Cv'):
        b_count+=1
        
    print(sur_x.cat)
    b+=1
c=0
c_count=0
cc_data=list()
i=0
while(j<10):
    if(sur_v[i].cat=='Cc'):
        cc_data.append(sur_v[i].ans)
        j+=1
    i+=1

while(c<10):
    print('training#',c)
    i=0
    j=0
    while(j<1+c):
        if(sur_v[i].cat=='Cc'):
            v1=(sur_v[i].ans)
            j+=1
        i+=1
    print('vamos en la encuesta',v1)
    sur_x.ans=v1
    i=0
    while(i<tamano):
        sur_v[i].dist=get_dist(sur_x.ans,sur_v[i].ans)
        i+=1 

    i=0
    dist_v=list()
    while(i<tamano):
        if(sur_v[i].dist!=0):
            
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
    if(sur_x.cat=='Cc'):
        c_count+=1
        
    print(sur_x.cat)
    c+=1
    
print('Datos de entrenamiento: Aeroespacial(10 encuestas contra todas) = ',(a_count*10),'%')
print('Datos de entrenamiento: Civil(10 encuestas contra todas) = ',(b_count*10),'%')
print('Datos de entrenamiento: Sistemas(10 encuestas contra todas) = ',(c_count*10),'%')
print('Para "k"=',k)

