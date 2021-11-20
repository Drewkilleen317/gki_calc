#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:56:06 2021

@author: andrewkilleen
"""

import streamlit as st
#import datetime
import plotly.graph_objects as go

glucose_unit_options = ['ml/dL','mmol/L']
glucose_units = st.sidebar.radio('Glucose Units',glucose_unit_options)
st.title("GKI Calculator")
#st.markdown('Use this Streamlit app to calculate your Glucose/Ketone Index ')

col1, col2 = st.columns(2)

with col1:
#    glucose_units = st.radio("Glucose Units:",('ml/dL','mmol/L'))
    glucose_reading = st.number_input(label= "Glucose Reading", value = 95, format="%i")
    ketone_reading = st.number_input(label= "Ketone Reading", value = 1.0, step=(0.1),format="%.1f")
    
    if glucose_units == "ml/dL" :
        gki = round(glucose_reading / 18 / ketone_reading,1)
    else:
        gki = round(glucose_reading  / ketone_reading,1)
    
    st.write("Your GKI is: {:.1f}".format(gki))
   

with col2:
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = gki,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "GKI", 'font': {'size': 20}},
#    delta = {'reference': 6, 'increasing': {'color': "white"}},
    gauge = {
#        'value':{'color':'black'},
        'axis': {'tick0':1,'range': [0, 9], 'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "red"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "black",
        'steps': [
            {'range': [0, 1], 'color': 'white'},
            {'range': [1, 3], 'color': 'darkgreen'},
            {'range': [3, 6], 'color': 'green'},
            {'range': [6, 9], 'color': 'lightgreen'},]}))

    fig.update_layout(paper_bgcolor = 'lightgray', font = {'color': "black", 'family': "Arial"})
    fig.update_traces(gauge_axis_dtick=1)
    st.plotly_chart(fig)