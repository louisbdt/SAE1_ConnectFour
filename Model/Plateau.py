from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Construit un tableau 2D vide qui représente le tableau

    :return: Retourne le tableau 2D
    """
    plateau = []
    for i in range(const.NB_LINES):
        plateau2 = []
        for j in range(const.NB_COLUMNS):
            plateau2.append(None)
        plateau.append(plateau2)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, numCol: int) -> int:
    """
    Place le pion dans la colonne passée en paramètre et retourne le numéro de ligne.

    :param plateau: Tableau 2D représentant le plateau
    :param pion: Dictionnaire qui représente l'objet pion
    :param numCol : Numéro de colonne ou l'on souhaite placer le pion
    :return: Numéro de ligne ou se trouve le pion, ou -1 si la colonne est pleine
    """
    if not type_plateau(plateau) :
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if not type_pion(pion) :
        raise TypeError ("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(numCol) != int :
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if numCol < 0 or numCol >= const.NB_COLUMNS:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {numCol} n’est pas correcte")

    if plateau[0][numCol] != None :
        return -1

    for numLigne in range(const.NB_LINES -1, -1, -1):
        if plateau[numLigne][numCol] is None :
            plateau[numLigne][numCol] = pion
            return numLigne

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Retourne les séries de 4 pions alignés horizontalement sur le plateau ou une liste vide s'il n'y en as pas

    :param plateau: Tableau 2D représentant le plateau
    :param couleur: Entier qui désigne la couleur du pion
    :return: Liste des séries de 4 pions alignés horizontalements
    """
    if not type_plateau(plateau) :
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0 :
        raise ValueError("detecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie= []
    for lignes in plateau:
        for i in range(len(lignes) - 3):
            if lignes[i] != None and lignes[i + 1] != None and lignes[i + 2] != None and lignes[i + 3] != None:
                serie_pion = [lignes[i], lignes[i + 1], lignes[i + 2], lignes[i + 3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
   """
    Retourne les séries de 4 pions alignés horizontalement sur le plateau ou une liste vide s'il n'y en as pas
   :param plateau: Tableau 2D représentant le plateau
   :param couleur: Entier qui désigne la couleur du pion
   :return: Liste des séries de 4 pions alignés verticalements
   """

   if not type_plateau(plateau):
       raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
   if type(couleur) != int:
       raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
   if couleur != 1 and couleur != 0:
       raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

   liste_serie = []
   for colonne in range(len(plateau[0])):
       for ligne in range(len(plateau) - 3):
           if (plateau[ligne][colonne] != None and plateau[ligne + 1][colonne] != None and plateau[ligne + 2][
               colonne] != None and plateau[ligne + 3][colonne] != None):
               serie_pion = [plateau[ligne][colonne], plateau[ligne + 1][colonne], plateau[ligne + 2][colonne],plateau[ligne + 3][colonne]]
               if (getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur):
                   liste_serie.extend(serie_pion)
   return liste_serie

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int)->list:
    """
        Retourne les séries de 4 pions alignés dans la diagonale directe du haut vers le bas sur le plateau
        :param plateau: Tableau 2D représentant le plateau
        :param couleur: Entier qui désigne la couleur du pion
        :return: Liste des séries de 4 pions alignés ou liste vide
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    liste_serie = []
    for lignes in range(len(plateau)-3):
        for colonnes in range(len(plateau[lignes])-3):
            if plateau[lignes][colonnes] != None and plateau[lignes+1][colonnes+1] != None and plateau[lignes+2][colonnes+2] != None and plateau[lignes+3][colonnes+3] !=  None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes+1][colonnes+1],plateau[lignes+2][colonnes+2],plateau[lignes+3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
    return liste_serie

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int)-> list:
    """
        Retourne les séries de 4 pions alignés dans la diagonale directe du haut vers le bas sur le plateau
        :param plateau: Tableau 2D représentant le plateau
        :param couleur: Entier qui désigne la couleur du pion
        :return: Liste des séries de 4 pions alignés ou liste vide
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    liste_serie = []
    for lignes in range(3,len(plateau)):
        for colonnes in range(len(plateau[lignes])-3):
            if plateau[lignes][colonnes] != None and plateau[lignes-1][colonnes+1] != None and plateau[lignes-2][colonnes+2] != None and plateau[lignes-3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes-1][colonnes+1],plateau[lignes-2][colonnes+2],plateau[lignes-3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
    return liste_serie

def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Récupère toutes les séries de 4 pions alignés et l'ajoute dans une liste

    :param plateau: Tableau 2D représentant le plateau
    :return: la liste des séries de 4 pions alignés
    """
    if not type_plateau(plateau) :
        raise TypeError("getPionsGagnantsPlateau : le paramètre n'est pas un plateau")
    liste = []

    #Récupération des gagnants jaune
    liste.extend(detecter4verticalPlateau(plateau,0))
    liste.extend(detecter4horizontalPlateau(plateau, 0))
    liste.extend(detecter4diagonaleDirectePlateau(plateau, 0))
    liste.extend(detecter4diagonaleIndirectePlateau(plateau, 0))

    #Récupération des gagnants rouge
    liste.extend(detecter4verticalPlateau(plateau, 1))
    liste.extend(detecter4horizontalPlateau(plateau, 1))
    liste.extend(detecter4diagonaleDirectePlateau(plateau, 1))
    liste.extend(detecter4diagonaleIndirectePlateau(plateau, 1))
    return liste

def isRempliPlateau(plateau: list) -> bool:
    """
    Renvoie True ou False si le plateau est rempli ou non

    :param plateau: Tableau 2D représentant le plateau
    :return: booléen True si le tableau est rempli, False sinon
    """
    if not type_plateau(plateau) :
        raise TypeError("isRempliPlateau : le paramètre n'est pas un plateau")

    pions_premiere_ligne = []
    for col in range(len(plateau[0])):
        if plateau[0][col] != None:
            pions_premiere_ligne.append(plateau[0][col])
        else:
            pions_premiere_ligne = []
    return len(pions_premiere_ligne) == const.NB_COLUMNS




def placerPionLignePlateau(plateau: list, pion: dict, numLigne: int, left: bool) -> tuple:
    """
    Cette fonction place le pion sur la ligne indiquée par la gauche si le booléen left vaut True ou par la droite sinon, en poussant les éventuels pions existants sur la ligne
    :param plateau: Tableau 2D représentant le plateau
    :param pion: Dictionnaire qui représente l'objet pion
    :param numLigne: Entier qui représente la ligne ou l'on souhaite placer le pion (entre 0 et const.NB_LINES - 1)
    :param left: booléen qui donne la coté ou l'on souhaite placer le pion (True = Gauche, False = Droite)
    :return: constitué de la liste des pions poussés (commençant par le pion ajouté) et un entier correspondant au numéro de ligne où se retrouve le dernier pion
        de la liste ou None si le dernier pion ne change pas de ligne. Si le dernier pion est éjecté du plateau, l’entier vaudra const.NB_LINES
    """

    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n'est pas un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n'est pas un pion")
    if type(numLigne) != int:
        raise TypeError("placerPionLignePlateau : le troisième paramètre n'est pas un entier")
    if numLigne < 0 or numLigne > const.NB_LINES - 1:
        raise ValueError(f"placerPionLignePlateau : Le troisième paramètre {numLigne} ne désigne pas une ligne ")
    if type(left) != bool:
        raise TypeError(" placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")

    lstPion = [pion]
    descente = None

    if left:
        i = 0
        while i < const.NB_COLUMNS and plateau[numLigne][i] is not None:
            lstPion.append(plateau[numLigne][i])
            i += 1

        for k in range(len(lstPion)-1):
            plateau[numLigne][k] = lstPion[k]

        descente = numLigne
        while descente + 1 < const.NB_LINES and plateau[descente + 1][len(lstPion) - 1] is None:
            plateau[descente + 1][len(lstPion) - 1] = plateau[descente][len(lstPion) - 1]
            plateau[descente][len(lstPion) - 1] = None
            descente += 1
    else:
        i = const.NB_COLUMNS - 1
        while i >= 0 and plateau[numLigne][i] is not None:
            lstPion.append(plateau[numLigne][i])
            i -= 1

        for k in range(min(len(lstPion), const.NB_COLUMNS)):
            plateau[numLigne][const.NB_COLUMNS - 1 - k] = lstPion[k]

        descente = numLigne
        while descente + 1 < const.NB_LINES and plateau[descente + 1][const.NB_COLUMNS - 1 - len(lstPion) + 1] is None:
            plateau[descente + 1][const.NB_COLUMNS - 1 - len(lstPion) + 1] = plateau[descente][const.NB_COLUMNS - 1 - len(lstPion) + 1]
            plateau[descente][const.NB_COLUMNS - 1 - len(lstPion) + 1] = None
            descente += 1

    return lstPion, descente

def encoderPlateau(plateau: list) -> str:
    """
    Encode le plateau sous forme de str (_ pour None , R pour rouge et J pour jaune)
    :param plateau: Tableau 2D représentant le plateau
    :return: Renvoie l'encodage du plateau en str
    """
    if not type_plateau(plateau) :
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau.")

    encodage = ""

    for ligne in plateau:
        for case in ligne:
            if case is None:
                encodage += "_"
            elif case['Couleur'] == 0:
                encodage += "J"
            elif case['Couleur'] == 1:
                encodage += "R"

    return encodage


def isPatPlateau(plateau: list, histogramme_plateaux: dict) -> bool:
    """
    Permet de déclarer si une partie est nulle, quand on rencontre 5 fois le meme plateau

    :param plateau: Tableau 2D représentant le plateau
    :param histogramme_plateaux: Dictionnaire représentant "L'histogramme des plateaux"
    :return: renvoie un booleen True si c'est la 5eme fois qu'on rencontre le plateau, False sinon
    """

    if not(type_plateau(plateau)):
        raise TypeError("isPatPlateau : le paramètre ne correspond pas à un plateau.")
    if type(histogramme_plateaux) != dict :
        raise TypeError("isPatPlateau : Le second paramètre n’est pas un dictionnaire ")

    clé = encoderPlateau(plateau)

    if clé in histogramme_plateaux:
        histogramme_plateaux[clé] += 1
        return histogramme_plateaux[clé] >= 5
    else:
        histogramme_plateaux[clé] = 1
        return False




