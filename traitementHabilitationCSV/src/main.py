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
#############################################################################
#############################################################################

# Ouverture des fichiers Habilitations.csv et habilitation_etablissement.csv
racine = "C:/Users/5936005/Documents/ScriptPython/python-master/traitementHabilitationCSV/src/"
sourceHabilitations = open(racine+"Habilitations.csv", "r")
sourceHabilitationEtablissemet = open(racine+"Habilitations_etablissements.csv", "r") 

# Ouverture du fichier destinationHabilitations
destinationHabilitations = open(sourceHabilitations.name+".out", "w")
destinationHabilitationEtablissements = open(sourceHabilitationEtablissemet.name+".out", "w")
 
 
# Appeler la fonction de traitement
th.filtrer(sourceHabilitations, destinationHabilitations, sourceHabilitationEtablissemet, destinationHabilitationEtablissements)
 

# Fermeture du fichier destinationHabilitations
destinationHabilitations.close()
 
# Fermerture du fichier sourceHabilitations
sourceHabilitations.close()