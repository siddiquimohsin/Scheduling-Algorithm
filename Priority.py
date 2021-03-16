proc=int(input("Enter the Number of process: "))
start=[]
end=[]
start1=[]
req=[]
end1=[]
waiting=[]
turnarround=[]
prio={}
prio1=[]
now={}
comp=[]
com=int(0)
flag=int(0)
flag1=int(0)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in range(proc):
    print("FOR PROCESS NO: ",str(i))
    arr=int(input("Enter the arrival time: "))
    bur=int(input("Enter the burst time: "))
    pro=int(input("Enter the priority: "))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    start.append(arr)
    end.append(bur)
    start1.append(arr)
    comp.append(0)
    end1.append(bur)
    a=str(i)
    now[a]=arr
    prio[a]=pro
    prio1.append(pro)

                
start.sort()
key=list(now.keys())
val=list(now.values())
for i in start:
    if flag==0:
        if i in val:
            a=int(key[val.index(i)])
            req.append(a)
            now.pop(key[val.index(i)])
            key.remove(key[val.index(i)])
            val.remove(val[val.index(i)])
            flag=1
    elif flag==1:
        if i in val and i==start[req[-1]] and prio[str(req[-1])]>prio[key[val.index(i)]]:
            a=int(key[val.index(i)])
            req.insert(req[-1],a)
            now.pop(key[val.index(i)])
            key.remove(key[val.index(i)])
            val.remove(val[val.index(i)])
        else:
            a=int(key[val.index(i)])
            req.append(a)
            now.pop(key[val.index(i)])
            key.remove(key[val.index(i)])
            val.remove(val[val.index(i)])


def judge(inner,wic):
    for i in req:
        if wic<=start1[i]:
            return int(req.index(i)+1)
        else:
            pass
           
while(len(req)!=0):
    re=req[0]
    bup=end[req[0]]
    count=int(1)
    if count+bup<=len(req):
        flag1=1
    for i in range(1,bup+1):
        
        if count>=len(req):
            com+=1
            comp[req[0]]=com
            end[req[0]]=0
            flag1=0
        elif count>=len(req) and req[-1]==req[0]:
            end[req[0]]=0
            com+=1
            comp[req[0]]=com
            flag1=0
    
       
        elif count!=len(req):
            if i==start1[req[count]] and prio[str(req[0])]>prio[str(req[count])]:
                ori=bup-i
                com+=1
                end[req[0]]=ori
                if com<start1[req[-1]]:
                    req.remove(req[0])
                    to=judge(re,com)
                    req.insert(to,re)
                    count+=1
                    flag1=0
                    break
                else:
                    req.remove(req[0])
                    req.append(re)
                    count+=1
                    flag1=0
                    break
            else:
                com+=1
                count+=1
    if flag1==1:
        comp[req[0]]=com
        end[req[0]]=0
        req.remove(req[0])
    elif count>=len(req):
        req.remove(req[0])

print("{}     {}      {}      {}         {}         {}            {}".format("Process","ArrivalTime","Burst Time","Priority","Completion time","Turnarround Time","Waiting Time"))
                
for i in range(proc):
    turnarround.append(comp[i]-start1[i])
    waiting.append(turnarround[-1]-end1[i])


for i in range(proc):
    print("  {}               {}              {}                {}                {}                      {}                      {}".format(i,start1[i],end1[i],prio1[i],comp[i],turnarround[i],waiting[i]))



print("The average turnarround time is",(sum(turnarround)/proc))
print("The average waiting time is",(sum(waiting)/proc))







    
