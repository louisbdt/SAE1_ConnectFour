from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur: int) -> dict:
    """
    Construit un dictionnaire représentant un joueur avec une couleur, un plateau, et une fonction permettant de le faire jouer
    :param couleur: Entier représentant une couleur
    :return: le dictionnaire représentant le joueur
    """
    if type(couleur) != int:
        raise TypeError("construireJoueur: Le paramètre n'est pas un entier")
    if couleur != 0 and couleur != 1:
        raise ValueError(f"construireJoueur: L'entier donné {couleur} n'est pas une couleur")

    if couleur == const.JAUNE:
        joueur = {const.COULEUR: const.JAUNE, const.PLATEAU: None, const.PLACER_PION: None}
    if couleur == const.ROUGE:
        joueur = {const.COULEUR: const.ROUGE, const.PLATEAU: None, const.PLACER_PION: None}

    return joueur

def getCouleurJoueur(joueur: dict) -> int:
    """
    Renvoie la couleur du joueur
    :param joueur: Dictionnaire représentant le joueur
    :return: renvoie la couleur du joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getCouleurJoueur: Le paramètre ne correspond pas à joueur")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    """
    Renvoie la liste plateau contenu dans le dictionnaire joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: Renvoie le plateau contenu dans le dictionnaire joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPlateauJoueur: Le paramètre ne correspond pas à joueur")
    return joueur[const.PLATEAU]


def getPlacerPionJoueur(joueur: dict):
    """
    Renvoie la fonction contenue dans le dictionnaire joueur

    :param joueur: Dictionnaire représentant le joueur
    :return: renvoie la fonction contenue dans le dictionnaire
    """
    if not type_joueur(joueur):
        raise TypeError("getPlacerPionJoueur: Le paramètre ne correspond pas à joueur")
    return joueur[const.PLACER_PION]

 