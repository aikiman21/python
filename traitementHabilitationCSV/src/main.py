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

import traitementHabilitations.traitementHabilitations as th

def lireConf():
    
    conf = open("traitementHabilitations.conf",'r')
    tab = {}
    for ligne in conf:
        donnees = ligne.rstrip('\n\r').split("=")
        tab[donnees[0].strip()] = donnees[1].strip()
    
    racine = tab["racine"]
    fichierHabilitation = tab["fichierHabilitation"]
    fichierHabilitationEtablissement = tab["fichierHabilitationEtablissement"]
    conf.close()
    
    return racine, fichierHabilitation, fichierHabilitationEtablissement

#############################################################################
#############################################################################


racine, fichierHabilitation, fichierHabilitationEtablissement = lireConf()
# Ouverture des fichiers Habilitations.csv et habilitation_etablissement.csv
sourceHabilitations = open(racine+fichierHabilitation, "r")
sourceHabilitationEtablissemet = open(racine+fichierHabilitationEtablissement, "r") 

# Ouverture du fichier destinationHabilitations
destinationHabilitations = open(sourceHabilitations.name+".out", "w")
destinationHabilitationEtablissements = open(sourceHabilitationEtablissemet.name+".out", "w")
 
 
# Appeler la fonction de traitement
th.filtrer(sourceHabilitations, destinationHabilitations, sourceHabilitationEtablissemet, destinationHabilitationEtablissements)
 

# Fermeture du fichier destinationHabilitations
destinationHabilitations.close()
 
# Fermerture du fichier sourceHabilitations
sourceHabilitations.close()

