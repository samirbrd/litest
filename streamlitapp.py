# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 06:12:53 2020

@author: Administrator
"""


import streamlit as st
import numpy as np
import pandas as pd


st.title('My first app')
st.write("Here's my first attempt at writing some text")
path_string="C:\\users\\administrator\\google drive\\autotrading\\"
file_string=path_string+'strategyposition.csv'
df_position=pd.read_csv(file_string)
add_selectbox = st.sidebar.selectbox(
    'Position in timeframe?',
    ('5 min', '15 min', '30 min','60 min','Daily','Total')
)
if add_selectbox=='5 min':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[0]== '5']
elif add_selectbox=='15 min':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[0:2]== '15'] 
elif add_selectbox=='30 min':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[0:2]== '30']
elif add_selectbox=='60 min':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[0:2]== '60']
elif add_selectbox=='Daily':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[0]== 'D']    
elif add_selectbox=='Total':
    df_filter=df_position
total_position=df_filter['Position'].sum()

st.write('Total Position Size is '+str(total_position))
st.write(df_filter)

