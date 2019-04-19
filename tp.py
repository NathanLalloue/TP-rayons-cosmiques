# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#bite
for col in [col1, col2, col3, col4]:
            indice_mini=0
            for j in range(1,len(col)):
                if col[j]<col[indice_mini]:
                    indice_mini=j
            moyenne = 0.
            taille  = len(col)-300
            for j in range(0, taille):
                moyenne=moyenne+col[j]
            moyenne =moyenne/taille
            v = min(indice_mini, abs(indice_mini-len(col)-1))-1
code_source

            t_m = 0.
            v_m = 0.
            for k in range(indice_mini-v, indice_mini+v):
                if(1==1):
                    t_m += (temps[k])*(col[k]-moyenne)
                    v_m += (col[k]-moyenne)
            tt.append(t_m/v_m)
            
            #bite
