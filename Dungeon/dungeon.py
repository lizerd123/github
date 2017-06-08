from random import randint as ri
inv=[]
print("   _____ _                   _       _    _____ _        _     ")
print("  / ____| |                 ( )     ( )  / ____| |      | |    ")
print(" | (___ | |__   ___  _ __   |/ _ __ |/  | (___ | |_ __ _| |__  ")
print("  \___ \| '_ \ / _ \| '_ \    | '_ \     \___ \| __/ _` | '_ \ ")
print("  ____) | | | | (_) | |_) |   | | | |    ____) | || (_| | |_) |")
print(" |_____/|_| |_|\___/| .__/    |_| |_|   |_____/ \__\__,_|_.__/ ")
print("                    | | ")                                        
print("                    |_| ")
st=1
sa=0
money=120
weapon="your an idiot"
item="your an idiot"
magic="your an idiot"
print (money)
print ("I better get some weapons items and magic")
Inventory_Blacksmith=["wooden sword","Axe","longsword","knife","hammer","torch"]
r = ri(0,5)
print (Inventory_Blacksmith[r:r+3])

print ("  ,                {} ")
print ("  / \, | ,        .--.")
print (" |    =|= >      /.--.\ ")
print ("  \ /` | `       |====|")
print ("   `   |         |`::`| ") 
print ("       |     .-;`\..../`;_.-^-._ ")
print ("       /\/  /  |...::..|`   :   `| ")
print ("      |:'\ |   /'''::''|   .:.   | ")
print ("       \ /\;-,/\   ::  |..:::::..| ")
print ("       |\ <` >  >._::_.| ':::::' | ")
print ("       | `  `  /   ^^  |   ':'   | ")
print ("       |       |       \    :    / ")
print ("       |       |        \   :   /  ")
print ("       |       |___/\___|`-.:.-` ")
print ("       |        \_ || _/    ` ")
print ("       |        <_ >< _> ")
print ("       |        |  ||  | ")
print ("       |        |  ||  | ")
print ("       |       _\.:||:./_ ")
print ("       |      /____/\____\ ")

buy = raw_input("what to buy?")
if buy == "wooden sword":
    inv.append("wooden sword")
    money=money-25
    weapon="wooden sword"
if buy == "Axe":
    inv.append("Axe")
    money=money-60
    weapon="Axe"
if buy == "longsword":
    inv.append("longsword")
    money=money-60
    weapon="longsword"
if buy == "knife":
    inv.append("knife")
    money=money-30
    weapon="knife"
if buy == "hammer":
    inv.append("hammer")
    money=money-60
    weapon="hammer"
if buy == "torch":
    inv.append("torch")
    money=money-30
    weapon="torch"
if len(inv) < 1:
    inv.append("FOOL")
print(money)
print(inv)
print("              __  ")
print("            .'  `'. ")
print("           /  _    | ")
print("           #_/.\==/.\ ")
print("          (, \_/  \_/ ")
print("           |    -' |")
print("           \   '=  /")
print("           /`-.__.'")
print("        .-'`-.___|__")
print("       /    \       `.")
 
Inventory_Shopkeep=["Potion","attack potion","defence potion"]
print (Inventory_Shopkeep)
buy = raw_input("what to buy?")
if buy == "firebomb":
    inv.append("firebomb")
    money=money-30
    item="firebomb"
if buy == "Potion":
    inv.append("Potion")
    money=money-30
    item="Potion"
if buy == "attack potion":
    inv.append("attack potion")
    money=money-30
    item="attack potion"
if buy == "defence potion":
    inv.append("defence potion")
    money=money-30
    item="defence potion"
if len(inv) < 2:
    inv.append("FOOL")    
print(money)
print(inv)

print("      :     *  ( .*) *     ")
print("     .:.  .(* ) .*  ) .   ")
print("    .:M:.   (.*( * )       ")
print("    ͡° ͜ʖ ͡°     /")
print("  .::.^.::..../")     
print(" .::::.::::  ")    
print(" :: :::::  ")                                               
print(" `  :::::")
print("    :::::         ")    
print("    :::::       ")       
print("    :::::     ")                  
print("   .:::::.  ")              
print("   ::::::: ")          
print("   `':::'' ")

Inventory_wizard=["energy","magic weapon","heal","stoneflesh"
]
r = ri(0,5)
print (Inventory_wizard[r:r+3])
buy = raw_input("what to buy?")
if buy == "energy":
    magic="energy"
    inv.append("energy")
    money=money-25
if buy == "magic weapon":
    inv.append("magic weapon")
    money=money-30
    magic="magic weapon"
if buy == "heal":
    inv.append("heal")
    money=money-60
    magic="heal"
if buy == "stoneflesh":
    inv.append("stoneflesh")
    money=money-60
    magic="stoneflesh"
if buy == "thorns":
    inv.append("thorns")
    money=money-30
    magic="thorns"
if len(inv) < 3:
    inv.append("FOOL")
print(inv)
from random import randint as ri
mg=0
eh = ri(150, 280)
mh = 200
de=1
if weapon == "Axe":
    st = 1.8
if weapon == "longsword":
    st = 1.6
if weapon == "knife":
    st = 1.1
if weapon == "hammer":
    st = 1.7
if weapon == "wooden sword":
    st = 1
if weapon == "torch":
    st = 1.4
if item == "potion":
    mh=mh+30
if item == "potion":
    mh=mh+30
if item == "attack potion":
    st=st+.6
if item == "defence potion":
    de=de+.4
if magic == "energy":
    mg=5
if magic == "magic weapon":
    st=st+.6
if magic == "heal":
    mh=mh+30
if magic == "magic weapon":
    st=st+.6
if magic == "stoneflesh":
    de=de+.2
if magic == "thorns":
    cd=.5
    
print("  \_/")
print(" '-0-'")
print(" --0-- ")
print(" .-0-. ")
    
while eh>0:
    if mh>0:
        counter = 0
        ed=ri(9,30)
        print (" I can attack counter or use skill")
        if sa < 40:
          print ("I'm too tired to use a skill")
        move = input("move ")
        if move == "attack":
            at=ri(9,15)
            eh=eh-st*at+mg
            print ("enemy")
            print (eh)
            print ("the attack was successful")
        if move == ("inventory"):
          print ("I have") (inv)
        if move == ("skill") and sa > 40:
          if weapon == "Axe":
            eh = eh-st*2*at+mg
            mh = mh-20
            sa=0
            print("the attack was powerful but left your wrist injujred")
          if weapon == "longsword":
             ed = 0
             sa=0
             print("You were too far for the enemy to attack")
          if weapon == "knife":
            slash = ri(1,5)
            if slash == 1:
              eh = eh-40
              sa=0
              print("you slash at the enemy dealing heavy dammage")
            else:
              print("you miss the enemy")
          if weapon == "hammer":
            de = + .5
            sa=0
            print("you feel far more fortified")
          if weapon == "wooden sword":
            st = st-.75
            mh = mh + .1*mh
            sa=0
            print("somehow snaping your flimsy sword makes you feel better")
          if weapon == "torch":
            mg = 10
            sa=0
            print("you light the enemy ablaze")
        if move == "counter":
            counter = 1
        ea = ri(0,4)
        if ea > 0:
            mh=mh-ed/de
            print ("me")
            print (mh)
            if counter == 1:
                eh=eh-st*ed*1.25+mg
                print ("enemy")
                print (eh)
        if ea == 0:
            if counter ==1:
                print("the counter fails")
                mh=mh-ri(10,20)
                print(mh)
        print ("enemy")
        print (eh)
        sa = sa +10
    