#!/usr/bin/python
# vim : set fileencoding=utf-8 :
 
#
# filtrecours.py
#
# Traitement des fichier habilitation.csv et habilitation_etablissement.csv pour 
# utilisation dans le batch de migration
#

'''
Created on 21 avr. 2013

@author: Thomas
'''
import rechercheBefAId.rechercheBefIId as rb

def lireConf():
    
    conf = open("traitementBefAId.conf",'r')
    tab = {}
    for ligne in conf:
        donnees = ligne.rstrip('\n\r').split("=")
        tab[donnees[0].strip()] = donnees[1].strip()
    
    racine = tab["racine"]
    befAIdV2 = tab["befAIdV2"]
    befAIdV3 = tab["befAIdV3"]
    isFastMethode = tab["isFastMethode"]
    conf.close()
    
    return racine, befAIdV2, befAIdV3, isFastMethode

#############################################################################
#############################################################################


racine, befAIdV2, befAIdV3, isFastMethode = lireConf()
# Ouverture des fichiers Habilitations.csv et habilitation_etablissement.csv
sourceBefAIdV2 = open(racine+befAIdV2, "r")
sourceBefAIdV3 = open(racine+befAIdV3, "r") 
 
 
# Appeler la fonction de traitement
rb.rechercheBef(sourceBefAIdV2, sourceBefAIdV3, isFastMethode)


 

# Fermeture des fichiers
sourceBefAIdV2.close()
sourceBefAIdV3.close()
 
