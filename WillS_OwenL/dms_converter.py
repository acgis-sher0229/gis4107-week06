def dmstodd(dms):
    dd=""
    ddlon=""
    ddlat=""
    if dms[len(dms)-2:len(dms)]=="/n":
        dms=dms[0:len(dms)-2]
    dms=dms.split(" ")
    if len(dms)!=8:
        return None,None
    dms[0]=float(dms[0])
    dms[1]=float(dms[1])
    dms[2]=float(dms[2])
    dms[4]=float(dms[4])
    dms[5]=float(dms[5])
    dms[6]=float(dms[6]) 
    if dms[0]>180 or dms[0]<0 or dms[1]<0 or dms[1]>59 or dms[2]<0 or dms[2]>59 or dms[4]>90 or dms[4]<0 or dms[5]<0 or dms[5]>59 or dms[6]<0 or dms[6]>59:
        return None,None
    elif dms[3].lower()!="e" and dms[3].lower()!="w":
        return None,None
    elif dms[7].lower()!="n" and dms[7].lower()!="s":
        return None,None 
    ddlon=dms[0]+(dms[1]/60)+(dms[2]/3600)
    ddlat=dms[4]+(dms[5]/60)+(dms[6]/3600)
    if dms[3].lower()=='w':
        ddlon=-1*ddlon         
    if dms[7].lower()=='s':
        ddlat=-1*ddlat
    ddlat=round(ddlat,6)
    ddlon=round(ddlon,6)        
    dd=str(ddlon)+","+str(ddlat)
    return dd