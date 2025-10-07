def get_coords_from_gpx(gpx):
    if gpx.find("trkpt")!=1:
        return None,None
    
    gpx=gpx.split("lon")
    latqone=gpx[0].find('"')
    latqtwo=gpx[0].rfind('"')
    lonqone=gpx[1].find('"')
    lonqtwo=gpx[1].rfind('"')
    latlon=''
    latlon+=gpx[1][lonqone+1:lonqtwo]
    latlon+=','
    latlon+=gpx[0][latqone+1:latqtwo]    
    return latlon