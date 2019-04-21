# -*- coding: utf-8 -*-
from pylab import*
from numpy import polynomial as P
#############Lecture des fichiers#############
liste_fichiers = [r"C:\Users\natha\Downloads\tp2019pb.txt"]
liste_size = [2001]
tt_masses = []
tab_dE1=[]
beta_gamma=[]
for rr in range(0, len(liste_fichiers)):
     nom_fichier = liste_fichiers[rr]
     nb_event = liste_size[rr]
     fd=open(nom_fichier, 'r')
     all_lignes = fd.readlines()
     c = 2.99792458*10**8
     nb = 0
     for l in range(0, int(len(all_lignes)/nb_event)):
     #initialisation
         lignes = all_lignes[l*nb_event:l*nb_event+nb_event]
         temps = []
         col1 = []
         col2 = []
         col3 = []
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
                
                 taille = len(col)
                 for j in range(0, taille):
                     moyenne=moyenne+col[j]
                 moyenne = moyenne/taille
                 v = min(indice_mini, abs(indice_mini-len(col)-1))-1
                 
                 t_m = 0.
                 v_m = 0.
                
                 for k in range(indice_mini-v, indice_mini+v):
                     t_m += (temps[k])*(col[k]-moyenne)
                     v_m += (col[k]-moyenne)
                 tt.append(t_m/v_m) 
print(tt)
        
