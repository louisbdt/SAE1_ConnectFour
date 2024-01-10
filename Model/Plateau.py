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
    :return: Liste des séries de 4 pions
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
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(
                        serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(
                        serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie


