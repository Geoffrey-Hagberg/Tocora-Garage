# Tocora Garage
# An almost one-page Python program to generate an unbounded poem
# Adapted from Nick Montfort's "Taroko Gorge"
#
# Geoffrey Hagberg
# Latest draft: 23 October 2024, Tocora Lane, Madison, Wisconsin
#
# x() splits a string into a list      c() is just random.choice()
# f() picks a fresh value from a list  p() prints a line and pauses
# scene() -- glimpses of scenery at speed
# route() -- a car (a) on a road (b)
# mile() -- brief markers of travel

import time,random,sys
def x(s): return s.split(',')
def c(l): return random.choice(l)
a=x('911,Z4,Forester,370Z,E36 M3,E46 M3,Exige,MR2,Focus ST,Veloster N,Miata,NB,FRS,S2000'+\
   ',Badger,Owl,Dog,Clammy,Tarmac,Slotus,Red Hot,Beluga,FRZ'+\
   ',Porsche,BMW,Subaru,Mazda,Nissan,Lotus,Toyota,Honda,Ford,Hyundai,Scion')
b_n=x("Observatory,Garfoot,78,JJ,Blue Mounds,J,Forshaug,Greenwald,F,Zwettler,K,Ridgeview,HH,H,T,Pike's Peak,Dugway")
b_w=x("H,K,Mill Dam,HK,Burma,Star Valley,F,Clay Hill,Sandy Rock,78,A,Spring Valley,JG,Britt Valley,G")
b_s=x("G,JG,Lee Valley,Tyvand,78,Hay Hollow,39,H,Gould Hill,Yankee Hollow,Sawmill,A,C")
b_r=x("tarmac,dust,dirt,pavement,asphalt,road,route,turn,bank,county highway,backroad,hill,slope,off-camber curve,blind curve")
g=x('cars,crew,friends,drivers,convoy,group')

def f(v):
    l=globals()[v]
    i=c(l[:-1])
    l.remove(i)
    globals()[v]=l+[i]
    return i

def p(s=''):
    print(s)
    sys.stdout.flush()
    time.sleep(1.2)

def scene():
    j=x('green,gold,brown,bare,full,new,snowy,leaf,grass,branch,hill,tree,limb,side,slope')+\
      x(',drift,driftless,creek,river,stream,bridge,crane,eagle,valley,marsh,wetland,glade,glen,field,clearing,forest,woodland,treeline,prairie')+\
      x(',farmhouse,barn,stable,shed,cow,horse,squirrel,cyclist,biker,traffic,farm,corn,tractor,truck,mailbox,flag,house,church,silo,crop')
    t=c([1,2,3,4])
    while len(j)>t:
        j.remove(c(j))
    v=' '+c(x('drift,slide,get loose,get tail-happy,understeer,oversteer,body roll,soar,fly,apex,climb')+\
            x(',third gear, second gear,full throttle,floor it,coast,lift off,power out,track out,turn in,trail brake'))
    w=c(x('blue,gray,white,gold,red,purple,darkening,brightening,sunset,sunrise,noon,night,clear,clouded,overcast,stormy,snowy,rainy,foggy,misty,high,low,heavy,light,cold,warm,breezy,still,gusty'))
    return v+' past '+' '.join(j)+' under '+w+' skies'

def route():
    v=c(x('lead,guide,pace,run,race,follow,tail,track,hunt,chase,course,wind,command,trail,sweep,range,passe,swerve,cut'))
    u=f('a')
    b=c(['b_n','b_w','b_s','b_r'])
    h=u+' '+v+'s'
    return h+' on '+f(f'{b}')

def mile():
    if random.randint(0,10) == 10:
        return c(x('Deer!,Gravel!'))
    else:
        return 'The '+f(c(x('g')))+' '+c(x('roar,hum,purr,rumble,whoosh,linger,rest,shift,slow,accelerate,push,hold'))+','

p()
p('Anyone up for a cruise?')
p('Got a route we can try!')
p()
while True:
    p(route()+',')
    m=c([0]*2+[1,2])
    for n in range(0,m):
        p(mile())
    p(route()+'.')
    p()
    p(scene()+' --')
    p()