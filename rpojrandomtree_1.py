#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:30:32 2021

@author: thiago
"""
#bibliotecas de análise
import numpy as np
import pandas as pd

#bibliotecas de visualização
import seaborn as sns
import matplotlib.pyplot as plt

#árvore de decisão
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#    etapas

#    Definição do Problema
#    Espera-se que você consiga fazer uma análise sobre quais variáveis tiveram maior influência na 
#    probabilidade de sobrevivência (ou seja, que tipo de pessoa teve mais chance de escapar com vida).
#    Após analisar os dados, espera-se também que você seja capaz de construir um modelo que dê a previsão 
#    de sobrevivência para um passageiro qualquer que seja fornecido como input.

#    Obtenção dos Dados
#inserção dos documentos de treino e teste
treino = pd.read_csv('/home/thiago/Downloads/train.csv')
teste = pd.read_csv('/home/thiago/Downloads/test.csv')

#    Exploração dos Dados
#    Checklist de informações
#    PassengerId;
#    Survived; (0 = N, 1 = S)
#    Pclass(1,2,3)
#    Name;
#    Sex;
#    Age;
#    SibSp: cônjuges e irmãos;
#    Parch: Pais e filhos;
#    Ticket;
#    Fare;
#    Cabin;
#    Embarked (C, Q, S).

print(treino.dtypes)
display(treino.head())
treino.describe()
treino.hist(figsize=(10,8))

fig, (axis1, axis2, axis3) = plt.subplots(1, 3, figsize = (12, 4))

#influências de dados com poucos fatores de variação
sns.barplot(x = 'Sex', y = 'Survived', data=treino, ax=axis1)
sns.barplot(x = 'Pclass', y = 'Survived', data=treino, ax=axis2)
sns.barplot(x = 'Embarked', y = 'Survived', data=treino, ax=axis3)

#Observações importantes:
# As mulheres sobreviveram mais que os homens nos dados
# A classe maior influencia positivamente na sobrevivência
# Os embarcados em C sobreviveram mais que os embarcados em Q ou S

#influências de dados com mais fatores de variação (idade)

fator_idade = sns.FacetGrid(treino, col='Survived')
fator_idade.map(sns.distplot, 'Age')

#Observações importantes:
#Considerando dados desse plot, crianças acabam sobrevivendo mais que adultos

#    Preparação dos Dados
# guardar as variáveis treino e teste para depois
treino_dps = treino.shape[0]
teste_dps = teste.shape[0]

#a coluna Survived não pode ser usada
target = treino.Survived.copy()
treino.drop(['Survived'], axis=1, inplace=True)

#juntar treino e teste em um DataFrame
#identificar a relevância e a quantia dos dados
#será que dados como Nome, Ticket, Id e Cabine são necessários?
#será que os dados sem valor devem ser zerados ou devo excluir as colunas?
#será que posso atribuir a mediana ou a moda?

df_tt= pd.concat(objs=[treino, teste], axis=0).reset_index(drop=True)
df_tt.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df_tt.isnull().sum()
idade_mediana = df_tt['Age'].median()
df_tt['Age'].fillna(idade_mediana, inplace=True)
preco_mediana = df_tt['Fare'].median()
df_tt['Fare'].fillna(preco_mediana, inplace=True)
embarque_valor = df_tt['Embarked'].value_counts()[0]
df_tt['Embarked'].fillna(embarque_valor, inplace=True)

#converter as variáveis não numéricas em números
df_tt['Sex'] = df_tt['Sex'].map({'male': 0, 'female': 1})
embarcados_zeroeum = pd.get_dummies(df_tt['Embarked'], prefix='Embarked')
df_tt = pd.concat([df_tt, embarcados_zeroeum], axis=1)
df_tt.drop('Embarked', axis=1, inplace=True)

#recuperar treino e teste
treino = df_tt.iloc[:treino_dps]
teste = df_tt.iloc[treino_dps:]

#modelagem

#iniciação do modelo Decision Tree
tree_model = DecisionTreeClassifier(max_depth=25)
tree_model.fit(treino, target)

# verificar a acurácia do modelo
acc_tree = round(tree_model.score(treino, target) * 100, 2)
print("Acurácia do modelo de Árvore de Decisão: {}".format(acc_tree))

y_pred_tree = tree_model.predict(teste)
print(y_pred_tree)
resultado = pd.DataFrame({
        "Survived": y_pred_tree
        })

acc_tree = round(tree_model.score(treino, target) * 100, 2)
print("Acurácia do modelo de Árvore de Decisão: {}".format(acc_tree))

#    Avaliação
#print(aprendizado)