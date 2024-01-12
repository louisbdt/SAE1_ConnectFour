from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from random import *


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

def getPionJoueur(joueur: dict)-> dict:
    """
    Construit un pion avec la couleur du joueur et le renvoie

    :param joueur: Dictionnaire représentant le joueur
    :return: le pion créer avec la couleur du joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPionJoueur: Le paramètre ne correspond pas à joueur")
    pion = construirePion(joueur[const.COULEUR])
    return pion

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Affecte le plateau au joueur
    :param joueur: Dictionnaire représentant le joueur
    :param plateau: liste 2D représentant le plateau
    :return: renvoie rien
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur: Le paramètre ne correspond pas à joueur")
    if not type_plateau(plateau):
        raise TypeError("setPlateauJoueur: Le paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fn) -> None :
    """
    affecte la fonction en paramètre au joueur

    :param joueur: Dictionnaire représentant le joueur
    :param fn:  fonction callable
    :return: renvoie rien
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur: Le paramètre ne correspond pas à joueur")
    if not callable(fn):
        raise TypeError("setPlateauJoueur: Le second paramètre n'est pas une fonction")

    joueur[const.PLACER_PION] = fn
    return None


def _placerPionJoueur(joueur: dict) -> int:
    """
    Place un pion aléatoirement dans une colonne entre 0 et const.NB_COLUMNS -1

    :param joueur: Dictionnaire représentant le joueur
    :return: un entier représentant une colonne
    """

    num_col = randint(0, const.NB_COLUMNS - 1)
    plateau = joueur[const.PLATEAU]
    while plateau[0][num_col] != None:
        num_col = randint(0, const.NB_COLUMNS - 1)
    return num_col


def initialiserIAJoueur(joueur: dict, booleen: bool) -> None:
    """
    Initialise l'ordre des joueurs selon la valeur du booléen

    :param joueur: Dictionnaire représentant le joueur
    :param booleen: True si le joueur commence, False sinon
    :return: Rien
    """
    if not type_joueur(joueur):
        raise TypeError("initialiserIAJoueur : Le premier paramètre ne correspond pas à joueur")
    if type(booleen) != bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n'est pas un booléen")
    if booleen:
        setPlacerPionJoueur(joueur, _placerPionJoueur)
    if not booleen :
        setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None



     