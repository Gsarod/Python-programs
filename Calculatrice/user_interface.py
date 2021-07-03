import Methods, ope_select




def opeselectmanager() :

    #file = open("selopt", "r")  <----- note : Je voudrais utiliser le fichier selopt (Select option), mais je sais pas comment faire, et pour l'instant je vais devoir me résoudre à l'utilisation de la variable opeselect et des elif qu ej'ai mis en place
    LoopToken = 1

    while LoopToken == 1:

        opeselect = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Opérations simples                                                   |
    |-2) Opérations avancées                                                  |
    |-3) Formules                                                             |
    |_________________________________________________________________________|

        Votre réponse -- >   """))



        if opeselect == 1:
            LoopToken + 1
            OpSimp = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Addition                                                             |
    |-2) Soustraction                                                         |
    |-3) Multiplication                                                       |
    |-4) Division                                                             |
    |-5) Revenir au menu précedent                                            |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

            if OpSimp == 1:
                Methods.methods.addition()
            elif  OpSimp == 2:
                Methods.methods.soustraction()
            elif OpSimp == 3:
                Methods.methods.multiplication()
            elif OpSimp == 4:
                Methods.methods.division()
            elif OpSimp == 5:
                LoopToken = 1

        elif opeselect == 2:
            LoopToken + 1
            OpAva = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Calculs de puissances                                                |
    |-2) Modulus                                                              |
    |-3) Floor division                                                       |
    |-4) Revenir au menu précedent                                            |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

            if OpAva == 1:
                Methods.methods.addition()
            elif  OpAva == 2:
                Methods.methods.soustraction()
            elif OpAva == 3:
                Methods.methods.multiplication()
            elif OpAva == 4:
                LoopToken = 1

        elif opeselect == 3:
            LoopToken + 1
            Form = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Théorème de Pytagore (ENCORE EN DEV)                                 |
    |-2) Revenir au menu précedent                                            |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

            if Form == 1:
                Methods.methods.pytagore()
            elif  Form == 2:
                LoopToken = 1
