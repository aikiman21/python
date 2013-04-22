'''
Created on 21 avr. 2013

@author: Thomas

Méthodes utilisées pour le traitement des fichiers habilitation.csv et habilitation_etablissement.csv en vue d'une utilisation dans le batch de migration
'''

def filtrer(srcHabilitations, dstHabilitations, srcHabilitationsEtab, dstHabilitationsEtab):
    
    
    tabHab = initHabilitationsCsvOut(srcHabilitations, dstHabilitations)
    tabHabEta = initHabilitationsEtabCsvOut(srcHabilitationsEtab, dstHabilitationsEtab)
        
    print("Nombre d'entrée du fichier d'habilitation initial:")    
    print(len(tabHab))
    print("Nombre d'entrée du fichier de définition du périmètre géographique initial:")
    print(len(tabHabEta))
    # recherche les doublons et les extraits
    tabHab,listeDoublon = searchDoublonHabilitations(tabHab)
    # ajoute les id aux habilitations
    ajoutID(tabHab)
    tabHabEta.extend(convertHabToHabEtab(listeDoublon))
    # recherche doublon habilitation_etablissements
    searchDoublonHabilitationsEtablissement(tabHabEta)
    
    verifExistenceUtilisateur(tabHab,tabHabEta)
    
    # Ecriture des donnees
    ecritureDonnee(tabHab,dstHabilitations, tabHabEta, dstHabilitationsEtab)
    print("Nombre d'entrée du fichier d'habilitation final:")
    print(len(tabHab))
    print("Nombre d'entrée du fichier de définition du périmètre géographique final:")
    print(len(tabHabEta))
    
def searchDoublonHabilitations(liste): # recherche les doublons de la liste, les supprimes de la liste et ajoutes à la liste des doublons
    listeDoublon=[] # liste de doublon
    liste.sort() # liste trié
    i=0
    while i<len(liste)-1:
        if liste[i][0] == liste[i+1][0]: # si l'index 0 de l'elt suivant est identique au courant, on supprime l'élément de la liste et on l ajoute dans la liste des doublons
            listeDoublon.append(liste[i+1][0:])
            liste.remove(liste[i+1]) 
        else: # gestion des triplets
            i=i+1
    return liste,listeDoublon

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
    usernameidx = entete.index("LoginAD")
    profilidx = entete.index("Profil")
    campusidx = entete.index("Campus")
    etabidx = entete.index("Etablissement")


    # Ecrit l'en-t�te
    dstHabilitations.write(entete[0]+";"+entete[1]+";"+entete[2]+";"+entete[3]+";"+entete[4]+"\n")
    # convertit le file input entableau
    tab = []
    for ligne in srcHabilitations:
        donnees = ligne.rstrip('\n\r').split(";")
        tab.append([donnees[usernameidx].upper(), donnees[profilidx], donnees[campusidx], donnees[etabidx]])
     
    return tab

def initHabilitationsEtabCsvOut(srcHabilitationsEtab, dstHabilitationsEtab):
    # Lit l'en-t�te, �limine la fin de ligne, et extrait les 
    # champs s�par�s par un point-virgule
    entete = srcHabilitationsEtab.readline().rstrip('\n\r').split(";")
 
    # D�termine l'index des diff�rents champs qui nous sont utiles
    usernameidx = entete.index("Login")
    campusidx = entete.index("Etablissement")

    # Ecrit l'en-t�te
    dstHabilitationsEtab.write(entete[0]+";"+entete[1]+"\n")
    # convertit le file input entableau
    tab = []
    for ligne in srcHabilitationsEtab:
        donnees = ligne.rstrip('\n\r').split(";")
        tab.append([donnees[usernameidx].upper(), donnees[campusidx]])
     
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