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
flag=0
proc1=int(0)
count=int(0)


            
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

quan=sum(end)//proc
print("XXXXXXXXXXX QUANTUM TIME IS",quan,"XXXXXXXXXXX")

def judge(inner,wic):
    for i in req:
        if wic<=start1[i]:
            return int(req.index(i)+1)
        else:
            pass

if sum(start)==0:                                                                       
    for i in range(proc):
        req.append(i)

    while(sum(end)!=0):
        re=req[0]
        a=start[req[0]]
        bup=end[req[0]]
        b=end.index(bup)
        if bup<=quan:
            req.remove(req[0])
            com+=a+bup
            comp[b]=com
            end.remove(bup)
            end.insert(b,0)
    
            
        elif bup>quan:
            ori=bup-quan
            com+=quan
            end.remove(bup)
            end.insert(b,ori)
            req.remove(req[0])
            req.append(re)


elif sum(start)!=0:
    key=list(now.keys())
    val=list(now.values())
    start.sort()
    for i in start:
        if i in val:
            a=int(key[val.index(i)])
            req.append(a)
            now.pop(key[val.index(i)])
            key.remove(key[val.index(i)])
            val.remove(val[val.index(i)])
   

    while(sum(end)!=0):
        re=req[0]
        a=start1[req[0]]
        bup=end[req[0]]
        b=end.index(bup)
        
        if bup<=quan:
            
            if flag==0:
                com+=a+bup
            else:
                com+=bup
            comp[req[0]]=com
            end[req[0]]=0
            req.remove(req[0])
           
            

        elif bup>quan:
            com+=quan
            if com>=start1[req[-1]]:
                
                ori=bup-quan
                if flag==0:
                    end[req[0]]=ori+start1[req[0]]
                else:
                    end[req[0]]=ori
                req.remove(req[0])
                req.append(re)
                print(req)
                
                
            elif com<start1[req[-1]]:
                
                ori=bup-quan
                if flag==0:
                    end[req[0]]=ori+start1[req[0]]
                else:
                    end[req[0]]=ori
                req.remove(req[0])
                to=judge(re,com)
                req.insert(to,re)
                
        flag=1

        
print("{}     {}      {}      {}         {}         {}".format("Process","ArrivalTime","Burst Time","Completion time","Turnarround Time","Waiting Time"))
                
for i in range(proc):
    turnarround.append(comp[i]-start1[i])
    waiting.append(turnarround[-1]-end1[i])


for i in range(proc):
    print("  {}               {}              {}                {}                      {}                      {}".format(i,start1[i],end1[i],comp[i],turnarround[i],waiting[i]))



print("The average turnarround time is",(sum(turnarround)/proc))
print("The average waiting time is",(sum(waiting)/proc))
