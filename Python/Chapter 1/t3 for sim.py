import os

#创建布局文件
os.chdir('d:\\test')
i=0
a=[]
#读取数据
name = [[],[]]
index=[0]
flag=[]
l=0
j=0
with open('d:\\test\\raw0.txt') as f:
    for line in f:
         for each in enumerate(line.split('\t')):
            name[each[0]].append(each[1])
            if each[1]=='\n':
                z=int((j+1)/2)
                index.append(z)
            j+=1
IDs,Ns = name
index.append(len(Ns)+1)
flag.append(len(Ns)+1)
for x in range(len(Ns)):
    str1=Ns[x]
    Ns[x]=str1.replace("\n"," ")


#写入
f=open("Gooooooo.xml",'w+')

#part3

for i in range(0,len(Ns)):
    if IDs[i]=="" :
        f.write('\n===============================================')
        continue
    else:
        f.write('\n\t<key ID="'+IDs[i]+'"    name="'+Ns[i]+'"  Sort="100" free="1" /> ')
f.write('\n')


f.close()
