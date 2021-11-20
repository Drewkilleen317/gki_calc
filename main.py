#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:56:06 2021

@author: andrewkilleen
"""

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Glucose/Ketone Index Calculator",
                   page_icon="🦈", layout="centered",
                   initial_sidebar_state="collapsed", menu_items=None)

glucose_unit_options = ['ml/dL','mmol/L']
glucose_units = st.sidebar.radio('Glucose Units',glucose_unit_options)

#
# Set width of sidebar to 150 pixels
#__________________________________________________________________________
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 150px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 150px;
        margin-left: -150px;
    }
    </style>
    """,
    unsafe_allow_html=True,)

st.title("Glucose/Ketone Index Calculator")

col1, col2 = st.columns(2)

with col1:

    glucose_reading = st.number_input(label= "Glucose Reading ("+glucose_units+")",
                                      value = 95, format="%i")
    ketone_reading = st.number_input(label= "Ketone Reading (mmol/L)",
                                     value = 1.0, step=(0.1),format="%.1f")
    
    if glucose_units == "ml/dL" :
        gki = round(glucose_reading / 18 / ketone_reading,1)
    else:
        gki = round(glucose_reading  / ketone_reading,1)
    
    st.write("Your GKI is: {:.1f}".format(gki))
# =============================================================================
#     color_picked = st.color_picker('Pick')
#     st.write('You picked: ',color_picked)
# =============================================================================
   

with col2:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = gki,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "GKI", 'font': {'size': 20}},
        delta = {'reference': 9, 'increasing': {'color': "white"}},
        gauge = {
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
    fig.update_layout(paper_bgcolor = 'lightgray',
                      font = {'color': "black", 'family': "Arial"},
                      width=400,
                      height=400)
    
    fig.update_traces(gauge_axis_dtick=1)
    st.plotly_chart(fig,width=400,height=400)