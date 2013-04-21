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

def filtrer(srcHabilitations, dstHabilitations, srcHabilitationsEtab, dstHabilitationsEtab):
    
    
    tabHab = initHabilitationsCsvOut(srcHabilitations, dstHabilitations)
    tabHabEta = initHabilitationsEtabCsvOut(srcHabilitationsEtab, dstHabilitationsEtab)
        
    print("Fichier d'habilitation initial:")    
    print(tabHab)
    print("Fichier de définition du périmètre géographique initial:")
    print(tabHabEta)
    
    # recherche les doublons et les extraits
    doublonListe = searchDoublonHabilitations(tabHab)
    
    # ajoute les id aux habilitations
    ajoutID(doublonListe[0])
    
    tabHabEta.extend(convertHabToHabEtab(doublonListe[1]))
    
    # recherche doublon habilitation_etablissements
    searchDoublonHabilitationsEtablissement(tabHabEta)
    
    verifExistenceUtilisateur(doublonListe[0],tabHabEta)
    
    # Ecriture des donnees
    ecritureDonnee(doublonListe[0],dstHabilitations, tabHabEta, dstHabilitationsEtab)
    
    print("Fichier d'habilitation final:")
    print(tabHab)
    print("Fichier de définition du périmètre géographique final:")
    print(tabHabEta)
    
def searchDoublonHabilitations(liste): # recherche les doublons de la liste, les supprimes de la liste et ajoutes à la liste des doublons
    listeDoublon=[] # liste de doublon
    liste.sort() # liste trié
    i=0
    while i<len(liste)-1:
        if liste[i][0] == liste[i+1][0]: # si l'index 0 de l'elt suivant est identique au courant, on supprime l'élément de la liste et on l ajoute dans la liste des doublons
            listeDoublon.append(liste[i+1])
            liste.remove(liste[i+1]) 
        else: # gestion des triplets
            i=i+1
    return [liste,listeDoublon]

def ajoutID(liste):
    """ ajout d'un ID à chaque entrée de la liste """
    i=0
    for item in liste:
        i=i+1
        item.insert(0,str(i))
        
def searchDoublonHabilitationsEtablissement(liste): # recherche les doublons de la liste, les supprimes de la liste et ajoutes à la liste des doublons
    liste.sort() # liste trié
    i=0
    while i<len(liste)-1:
        if liste[i][0] == liste[i+1][0] and liste[i][1] == liste[i+1][1]: # si l'index 0 de l'elt suivant est identique au courant, on supprime l'élément de la liste et on l ajoute dans la liste des doublons
            liste.remove(liste[i+1])
        else:
            i=i+1
    return liste

def initHabilitationsCsvOut(srcHabilitations, dstHabilitations):
    # Lit l'en-t�te, �limine la fin de ligne, et extrait les 
    # champs s�par�s par un point-virgule
    entete = srcHabilitations.readline().rstrip('\n\r').split(";")
 
    # D�termine l'index des diff�rents champs qui nous sont utiles
    usernameidx = entete.index("username")
    profilidx = entete.index("profil")
    campusidx = entete.index("campus")
    etabidx = entete.index("etab")


    # Ecrit l'en-t�te
    dstHabilitations.write(entete[1]+";"+entete[2]+";"+entete[3]+";"+entete[4]+"\n")
    # convertit le file input entableau
    tab = []
    for ligne in srcHabilitations:
        donnees = ligne.rstrip('\n\r').split(";")
        tab.append([donnees[usernameidx], donnees[profilidx], donnees[campusidx], donnees[etabidx]])
     
    return tab

def initHabilitationsEtabCsvOut(srcHabilitationsEtab, dstHabilitationsEtab):
    # Lit l'en-t�te, �limine la fin de ligne, et extrait les 
    # champs s�par�s par un point-virgule
    entete = srcHabilitationsEtab.readline().rstrip('\n\r').split(";")
 
    # D�termine l'index des diff�rents champs qui nous sont utiles
    usernameidx = entete.index("username")
    campusidx = entete.index("campus")


    # Ecrit l'en-t�te
    dstHabilitationsEtab.write(entete[0]+";"+entete[1]+"\n")
    # convertit le file input entableau
    tab = []
    for ligne in srcHabilitationsEtab:
        donnees = ligne.rstrip('\n\r').split(";")
        tab.append([donnees[usernameidx], donnees[campusidx]])
     
    return tab

def convertHabToHabEtab(tabHab):
    tabHabEta = []
    for item in tabHab:
        tabHabEta.append([item[0],item[len(item)-1]])
                          
    return tabHabEta

def verifExistenceUtilisateur(tabHab,tabHabEta):
    for item in tabHabEta:
        test = True
        for itemb in tabHab:
            if item[0] == itemb[1]:
                test = False
        if test:
            print("[ERROR] L'utilisateur "+item[0]+" est inexistant dans le fichier d'habilitation")


def ecritureDonnee(tabHab,dstHabilitations, tabHabEta, dstHabilitationsEtab):
# Ecriture des donnees
    for ligne in tabHab:  
        # Ecriture des donn�es dans le fichier destinationHabilitations
        dstHabilitations.write("%s\n" % (";".join(ligne)))
        
    for ligne in tabHabEta:  
        # Ecriture des donn�es dans le fichier destinationHabilitations
        dstHabilitationsEtab.write("%s\n" % (";".join(ligne)))
    
#############################################################################
#############################################################################

# Ouverture des fichiers Habilitations.csv et habilitation_etablissement.csv
racine = "C:/Users/Thomas/Documents/python/"
sourceHabilitations = open(racine+"inTest.csv", "r")
sourceHabilitationEtablissemet = open(racine+"inTest2.csv", "r") 

# Ouverture du fichier destinationHabilitations
destinationHabilitations = open(sourceHabilitations.name+".out", "w")
destinationHabilitationEtablissements = open(sourceHabilitationEtablissemet.name+".out", "w")
 
 
# Appeler la fonction de traitement
filtrer(sourceHabilitations, destinationHabilitations, sourceHabilitationEtablissemet, destinationHabilitationEtablissements)
 
 
# Fermeture du fichier destinationHabilitations
destinationHabilitations.close()
 
# Fermerture du fichier sourceHabilitations
sourceHabilitations.close()