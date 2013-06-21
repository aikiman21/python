'''
Created on 5 juin 2013

@author: 5936005
'''

def rechercheBef(sourceBefAIdV2, sourceBefAIdV3, fastMethode):
    tabBefV2 = createTabBefAId(sourceBefAIdV2,'V2')
    tabBefV3 = createTabBefAId(sourceBefAIdV3,'V3')

    if fastMethode.strip().upper() == 'TRUE': 
        isBefV2InV3Fast(tabBefV2,tabBefV3)
    else:
        isBefV2InV3Complete(tabBefV2, tabBefV3)
    
    

def createTabBefAId(srcBefAId,src):
    
    # convertit le file input entableau
    tab = []
    srcBefAId.readline()
    for ligne in srcBefAId:
        donnees = ligne.rstrip('\n\r').split(";")
        tab.append([donnees[0],src])
     
    return tab

def isBefV2InV3Fast(tabBefV2,tabBefV3):
    
    tabBefV2.extend(tabBefV3)
    
    tabBefV2.sort()
    
    i=0
    while i < len(tabBefV2):
            
        if i+1<len(tabBefV2) and tabBefV2[i][0] == tabBefV2[i+1][0]:
            i+=1
        elif tabBefV2[i][1] == 'V2':
            print('le beneficiare {} est inexistant'.format(tabBefV2[i][0]))
            tabBefV2.remove(tabBefV2[i])
            i-=1
        i+=1
        
    

def isBefV2InV3Complete(tabBefV2,tabBefV3):
      
      
    for ligneV2 in tabBefV2:
        #i+=1
          
        #print(str(i)+"/"+str(len(tabBefV2)))
        test = False
        for ligneV3 in tabBefV3:
            if ligneV2[0] == ligneV3[0]:
                test = True
                break
                      
        if test == False:
            print('le beneficiare {} est inexistant'.format(ligneV2[0]))    
              
              
   
                