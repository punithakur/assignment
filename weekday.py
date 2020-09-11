import calendar as c

def check_date(d):
    wek={'Mon':0,'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}
    for i in d.keys():
        date=i.split("-")
        ckd=c.weekday(int(date[0]),int(date[1]),int(date[2]))
        if ckd==0:
            wek['Mon']+=d[i]
        elif ckd==1:
            wek['Tue']+=d[i]
        elif ckd==2:
            wek['Wed']+=d[i]
        elif ckd==3:
            wek['Thu']+=d[i]
        elif ckd==4:
            wek['Fri']+=d[i]
        elif ckd==5:
            wek['Sat']+=d[i]
        elif ckd==6:
            wek['Sun']+=d[i]


    th=(wek['Mon']+wek['Sun'])/2
    tu=((wek['Mon']+th)/2)-1
    we=((wek['Mon']+th)/2)+1
    fr=((th+wek['Sun'])/2)-1
    st=((th+wek['Sun'])/2)+1

    if wek['Tue']==0:
        wek['Tue']=int(tu)
    if wek['Wed']==0:
        wek['Wed']=int(we)
    if wek['Thu']==0:
        wek['Thu']=int(th)
    if wek['Fri']==0:
        wek['Fri']=int(fr)
    if wek['Sat']==0:
        wek['Sat']=int(st)
    

    return wek


date={'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
#date={'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}

print(check_date(date))
        
        
        
        
