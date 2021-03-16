proc=int(input("Enter the number of process: "))                                           #
start=[]
end=[]
start1=[]
req=[]
now={}
end1=[]
quan=float(0)
com=int(0)
comp=[]
turnarround=[]
waiting=[]
flag=int(0)
flag1=int(0)
proc1=int(0)


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in range(proc):
    print("FOR PROCESS NO:",str(i))
    arr=int(input("Enter the arrival time of process: "))
    bur=int(input("Enter the burst time of the process: "))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    start.append(arr)
    end.append(bur)
    start1.append(arr)
    comp.append(0)
    end1.append(bur)
    a=str(i)
    now[a]=arr

start.sort()
key=list(now.keys())
val=list(now.values())
for i in start:
    if i in val:
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
print(req)

while(len(req)!=0):
    re=req[0]
    bup=end[req[0]]
    count=int(1)
    if count+bup<=len(req):
        flag1=1
    if start[req[0]]>0 and flag==0:
        com+=start[req[0]]
        flag=1
    for i in range(1,bup+1):
        
        if count>=len(req):
            com+=1
            comp[req[0]]=com
            end[req[0]]=0
            flag1=0
            print(req)
        elif count>=len(req) and req[-1]==req[0]:
            end[req[0]]=0
            com+=1
            comp[req[0]]=com
            flag1=0
       
        elif count!=len(req):
            if i+1==start1[req[count]] and count>=end[req[count]]:
                ori=bup-i
                end[req[0]]=ori
                if com<start1[req[-1]]:
                    req.remove(req[0])
                    to=judge(re,com)
                    req.insert(to,re)
                    for j in req:
                        if j==re:
                            break
                        elif end[j]>end[req[req.index(j)+1]]:
                            ui=req.index(j)
                            ui2=req.index(j)+1
                            val=req[req.index(j)+1]
                            req.remove(req[req.index(j)+1])
                            req.remove(j)
                            req.insert(ui2,j)
                            req.insert(ui,val)
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
        fell=int(1)
        comp[req[0]]=com
        end[req[0]]=0
        req.remove(req[0])
        if len(req)!=0:
            for j in req:
                if len(req)==1:
                    break
                elif req.index(j)==-1:
                    break
                elif fell==len(req):
                    break
                
                elif end[j]>end[req[req.index(j)+1]]:
                    ui=req.index(j)
                    ui2=req.index(j)+1
                    val=req[req.index(j)+1]
                    req.remove(req[req.index(j)+1])
                    req.remove(j)
                    req.insert(ui2,j)
                    req.insert(ui,val)
                    fell+=1
                else:
                    fell+=1
        
    elif count>=len(req):
        fell=int(1)
        req.remove(req[0])
        if len(req)!=0:
            for j in req:
                if len(req)==1:
                    break
                elif req.index(j)==-1:
                    break
                elif fell==len(req):
                    break
                
                elif end[j]>end[req[req.index(j)+1]]:
                    ui=req.index(j)
                    ui2=req.index(j)+1
                    val=req[req.index(j)+1]
                    req.remove(req[req.index(j)+1])
                    req.remove(j)
                    req.insert(ui2,j)
                    req.insert(ui,val)
                    fell+=1
                else:
                    fell+=1
print(comp)
print("{}     {}      {}      {}         {}         {}".format("Process","ArrivalTime","Burst Time","Completion time","Turnarround Time","Waiting Time"))
                
for i in range(proc):
    turnarround.append(comp[i]-start1[i])
    waiting.append(turnarround[-1]-end1[i])


for i in range(proc):
    print("  {}               {}              {}                {}                      {}                      {}".format(i,start1[i],end1[i],comp[i],turnarround[i],waiting[i]))



print("The average turnarround time is",(sum(turnarround)/proc))
print("The average waiting time is",(sum(waiting)/proc))

