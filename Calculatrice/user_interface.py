import Methods




def opeselectmanager() :

    #file = open("selopt", "r")  <----- note : Je voudrais utiliser le fichier selopt (Select option), mais je sais pas comment faire, et pour l'instant je vais devoir me résoudre à l'utilisation de la variable opeselect et des elif qu ej'ai mis en place
    LoopToken = 1
    ContiousToken = 0


    while LoopToken == 1:

        opeselect = int(input("""
     _________________________________________________________________________
    |                  Quelle option voulez vous choisir ?                    |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Opérations simples                                                   |
    |-2) Opérations avancées                                                  |
    |-3) Formules (En COURS DE DEV)                                           |
    |-4) Quitter ce programme                                                 |
    |_________________________________________________________________________|

        Votre réponse -- >   """))


        if opeselect == 4:
            LoopToken = 0
            exit()

        elif opeselect == 0:
            LoopToken + 1
            debug = int(input("""
     _________________________________________________________________________
    |                             DEBUG MENU                                  |
    |                                                                         |
    |                                                                         |
    |                                                                         |
    |-1) Tester la variable en cours de dev                                   |
    |-2) Quitter ce menu                                                      |
    |-3) Quitter le programme                                                 |
    |_________________________________________________________________________|

                    Votre réponse -- >   """))

            if debug == 1:
                LoopToken + 1
                Methods.methods.pytagore()
            if debug == 2:
                LoopToken = 1
            if debug == 3:
                LoopToken = 0
                exit()


        elif opeselect == 1:
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
    |-6) Quitter ce programme                                                 |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

            if OpSimp == 6:
                LoopToken = 0
                exit()
            elif OpSimp == 1:
                Methods.methods.addition()
                ContiousToken = 1
            elif  OpSimp == 2:
                Methods.methods.soustraction()
                ContiousToken = 1
            elif OpSimp == 3:
                Methods.methods.multiplication()
                ContiousToken = 1
            elif OpSimp == 4:
                Methods.methods.division()
                ContiousToken = 1
            elif OpSimp == 5:
                LoopToken = 1

            if ContiousToken == 1:
                LoopToken = 0
                nextop = str(input("""
     _________________________________________________________________________
    |                                                                         |
    | Voulez vous continuer avec une autre opération ?  Y/N                   |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

                if nextop == 'Y':
                    LoopToken = 1
                elif nextop == 'N':
                    LoopToken = 0
                    exit()

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
    |-5) Quitter ce programme                                                 |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

            if  OpAva == 5:
                LoopToken = 0
                exit()
            elif OpAva == 1:
                Methods.methods.puissances()
                ContiousToken = 1
            elif  OpAva == 2:
                Methods.methods.soustraction()
                ContiousToken = 1
            elif OpAva == 3:
                Methods.methods.multiplication()
                ContiousToken = 1
            elif OpAva == 4:
                LoopToken = 1

            if ContiousToken == 1:
                LoopToken = 0
                nextop = str(input("""
     _________________________________________________________________________
    |                                                                         |
    | Voulez vous continuer avec une autre opération ?  Y/N                   |
    |_________________________________________________________________________|

        Votre réponse -- >   """))

                if nextop == 'Y':
                    LoopToken = 1
                elif nextop == 'N':
                    LoopToken = 0
                    exit()

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
    |-3) Quitter ce programme                                                 |
    |_________________________________________________________________________|

        Votre réponse -- >   """))
