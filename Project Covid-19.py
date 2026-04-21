# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:16:33 2020

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#------------------------ EXERCICIO 1 -----------------------------------------
                    
confirmados= pd.read_csv ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
mortes= pd.read_csv ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
recuperados= pd.read_csv ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")

print (confirmados.head())
print (mortes.head())
print (recuperados.head())

#------------------------ EXERCICIO 2 -----------------------------------------

def indexar1 (x):
    x_apagar= x.melt (id_vars=['Province/State','Country/Region','Lat','Long'],value_name = 'Confirmados', var_name = 'Date')
    x_apagar= x_apagar.set_index (['Province/State','Country/Region','Date'])
    return x_apagar

def indexar2 (x):
    x_apagar= x.melt (id_vars=['Province/State','Country/Region','Lat','Long'],value_name = 'Mortes', var_name = 'Date')
    x_apagar= x_apagar.set_index (['Province/State','Country/Region','Date'])
    return x_apagar


def indexar3 (x):
    x_apagar= x.melt (id_vars=['Province/State','Country/Region','Lat','Long'],value_name = 'Recuperados', var_name = 'Date')
    x_apagar= x_apagar.set_index (['Province/State','Country/Region','Date'])
    return x_apagar



Confirmados= indexar1(confirmados)
Mortes= indexar2(mortes)
Recuperados= indexar3(recuperados)

print(Confirmados)
print(Mortes)
print(Recuperados)

#------------------------ EXERCICIO 3 -----------------------------------------
A = Confirmados.groupby(['Country/Region']).last()

B = Mortes.groupby(['Country/Region']).last()

C = Recuperados.groupby(['Country/Region']).last()

#----------------------- EXERCICIO 4 ------------------------------------------

M= A.join(B['Mortes'])
final= M.join(C['Recuperados'])

final['Active Cases'] = A['Confirmados'] - B['Mortes']     
print (final) 



#------------------------ EXERCICIO 5 -----------------------------------------

Ordenado = final.sort_values(by=['Active Cases'], ascending=True)
print(Ordenado)

#------------------------ EXERCICIO 6 -----------------------------------------

pop= pd.read_csv('Pop.csv')
comum=[]
paises= pop[['Region, subregion, country or area *','2020']]

paisespopulacao=paises['Region, subregion, country or area *'].unique()
final= final.reset_index()
paisesfinal= final['Country/Region'].unique()


for n in paisesfinal:
    if n not in paisespopulacao:
        del n
    else:
        comum.append(n)

paises = paises.loc[paises['Region, subregion, country or area *'].isin(comum)]        
paises=paises.set_index('Region, subregion, country or area *')  
paises=paises.sort_values(by=['Region, subregion, country or area *'],ascending=True)

final = final.loc[final['Country/Region'].isin(comum)]      
final=final.set_index('Country/Region')  
final=final.sort_values(by=['Country/Region'],ascending=True)

final=final.join(paises['2020'])        

#------------------------ EXERCICIO 7 -----------------------------------------

Ordenado = Ordenado.sort_values(by=['Active Cases'], ascending=True) 
                            
x= Ordenado['Confirmados'].head(15)
y= Ordenado['Mortes'].head(15)


plt.xlabel('Confirmados')
plt.ylabel('Mortes')
plt.scatter (x,y,color='yellow')
plt.scatter (y,x,color='orange')
plt.show()

#------------------------ EXERCICIO 8 -----------------------------------------

p = np.poly1d(np.polyfit(x, y, deg=2))
print (p)

plt.plot(x,y,".")
plt.plot(x,p(x),"-")
plt.show()

#------------------------ EXERCICIO 9 -----------------------------------------

final=final.reset_index()

def convert(a):
    for x in range (len(a['2020'])):
        y=int(a.at[x,'2020'].replace(' ',''))
        a.at[x,'2020']=y
    return a

final=convert(final)

final=final.set_index('Country/Region')


#------------------------ EXERCICIO 10 ----------------------------------------

final['Casos por milhão']=final['Confirmados']/final['2020']
final['Casos por milhão']=final['Casos por milhão']/1000
print(final)  

#------------------------ EXERCICIO 11 ----------------------------------------

final['Casos por milhão']=final['Mortes']/final['2020']
final['Casos por milhão']=final['Casos por milhão']/1000
print(final)  
