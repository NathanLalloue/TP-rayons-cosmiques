import numpy as np
liste_fichiers = [r"C:\Users\natha\Downloads\tp2019pb.txt"]
liste_size = [2001]
tt_masses = []
tab_dE1=[]
beta_gamma=[]
vtest=[]
for rr in range(0, len(liste_fichiers)):
    nom_fichier = liste_fichiers[rr]
    nb_event = liste_size[rr]
    fd=open(nom_fichier, 'r')
    all_lignes = fd.readlines()
    c = 2.99792458*10**8
    nb = 0
    for l in range(0, int(len(all_lignes)/nb_event)):
         lignes = all_lignes[l*nb_event:l*nb_event+nb_event]
         temps = []
         col1 = []
         col2 = []
         col3 = []
         col4 = []
         for i in range(0,nb_event):
             temps.append(i*2.*10.**-10)
             tab = lignes[i].split('\t')
             col1.append(float(tab[1]))
             col2.append(float(tab[2]))
             col3.append(float(tab[3]))
         tab_mini=[]
         tab_largeur = []
         tt=[]
         for col in [col1, col2, col3]:
             indice_mini=0
             for j in range(1,len(col)):
                 if col[j]<col[indice_mini]:
                     indice_mini=j
             moyenne = 0.
             if nom_fichier==r"D:\Téléchargement\tp2019-4":
                 taille=len(col)-2650
             else:
                 taille = len(col)-650
             for j in range(0, taille):
                 moyenne=moyenne+col[j]
             moyenne =moyenne/taille
             v = min(indice_mini, abs(indice_mini-len(col)-1))-1
             t_m =[]
             v_m =[]
             for k in range(0, len(col)):
                 t_m.append(temps[k])
                 v_m.append(col[k]-moyenne)
             vtest.append(v_m)        
             tt.append(t_m[v_m.index(min(v_m))])
         if tt[0]<tt[1] and tt[1]<tt[2]:
             beta1 = (22.75*10**(-2))/(1.*c*(tt[1]-tt[0]))
             beta2 = (5.5*10**(-2) )/(1.*c*(tt[2]-tt[1]-(17.5*10**(-2)/(beta1*c))))    
             beta3 = beta1
             if beta2>0. and beta2<beta3 and beta1<1.:
                 gamma1 = 1./np.sqrt((1.-beta1**2.))
                 gamma2 = 1./np.sqrt((1.-beta2**2.))
                 mec2 = 0.511 #Mev
                 Pi = np.pi
                 dx = 1.5#cm
                 Z = 82.
                 A = 207.2 #g/mol
                 z = -1.
                 M= 105.66
                 I = 823.*10**(-6)
                 K= 0.307075
                 dE1=6.24*10**12*dx*10**(-2)*(4*np.pi/(9.11*10**(-31)*9*10**16))*(Z*11.35*10**3*6.022*10**(23)/(A*10**(-3)*beta1**2))*((((1.6*10**-19)**2)/(4*np.pi*8.854*10**-12))**2)*(np.log(abs((2*mec2*beta1**2)/(I*(1-beta1**2))))-beta1**2)
                 mc2 = (dE1)/(gamma1-gamma2)
                 if mc2>0:
                     tt_masses.append(mc2)
                     nb = nb+ 1
                     
print("nombre d'evenements avant selection :", int(len(all_lignes)/nb_event))              
print("nombre d'evenements apres selection :", nb)
print("masse moyenne du muon :", np.mean(tt_masses))
        
