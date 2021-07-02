import Methods




def opeselectmanager() :

    opeselect = int(input("quelle opé voulez vous faire ?  "))

    if opeselect == 1:
        Methods.methods.addition()
    elif opeselect == 2:
        Methods.methods.soustraction()
    elif opeselect == 3:
        Methods.methods.division()
    elif opeselect == 4:
        Methods.methods.multipcation()
