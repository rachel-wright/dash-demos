# colors
purple = '#645375'
green = '#616F56'
gold = '#CB9856'
dkblue = '#055588'
ltblue = '#3E8FC4'
red = '#8B2034'


def agecolor(age):
    if age=='<30': 
        return ltblue
    elif age=='30-59': 
        return green
    elif age=='60+': 
        return gold
    else:
        return red

def bucolor(bu):
    if bu=='TCE': 
        return ltblue
    elif bu=='DMIT': 
        return dkblue
    elif bu=='P&I': 
        return purple
    elif bu=='Corporate': 
        return green
    else:
        return gold

def bucolors(bulist):
    colors = []
    for bu in bulist:
        colors.append(bucolor(bu))
    return colors
