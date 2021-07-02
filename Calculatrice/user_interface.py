import Methods




def opeselectmanager() :

    #file = open("selopt", "r")  <----- note : Je voudrais utiliser le fichier selopt (Select option), mais je sais pas comment faire, et pour l'instant je vais devoir me résoudre à l'utilisation de la variable opeselect et des elif qu ej'ai mis en place

    opeselect = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |-1) Addition                                                             |
    |-2) Soustraction                                                         |
    |-3) Multiplication                                                       |
    |-4)Division                                                              |
    |_________________________________________________________________________|

    Votre réponse -- >   """)) #sers à donner une meilleure allure au fichier

    if opeselect == 1:                      # \
        Methods.methods.addition()          # |
    elif opeselect == 2:                    # |
        Methods.methods.soustraction()      # | Sert à pouvoir choisir entre les différents opérations
    elif opeselect == 3:                    # |
        Methods.methods.division()          # |
    elif opeselect == 4:                    # |
        Methods.methods.multipcation()      # /
