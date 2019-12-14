#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:43:11 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

##Mine
##Para codificar datos categóricos ahora se utiliza:

from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])
## Para utilizar one hot encoder y crear variables dummy, 
##ya no hace falta utilizar previamente la función label enconder, 
##si no que para aplicar la dummyficación a la primera columna y
## dejar el resto de columnas como están, lo podemos hacer con:

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)
##Para hacer reemplazo de valores por la media, ahora se utiliza:

from sklearn.impute import SimpleImputer
# Reemplazar por medias
imputer = SimpleImputer(strategy="mean")
#medias en columnas 1,2
imputer = imputer.fit(X[:, 1:3])
# Cambiar valores por dichas nedias
X[:, 1:3] = imputer.transform(X[:, 1:3])


###Cambios de validación cruzada y training/testing

##La función sklearn.grid_search ha cambiado y ya no depende de ese paquete. 
##Ahora debe cargarse con

from sklearn.model_selection import GridSearchCV

###La función train_test_split ya no forma parte de sklearn.cross_validation, 
##ahora debe cargarse desde el paquete sklearn.model_selection

