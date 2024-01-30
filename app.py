# -*- codin:utf-8 -*-

import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px 

def load_data():
    df=pd.read_csv('./data/df.csv') 
    return df

def main():
    st.title("My First Deply streamlit & Plotly")
    df=load_data()
    #st.dataframe(df)
    
    #Frequency of Orders by Days of week
    target=df.order_dow.value_counts()
    colors=sns.color_palette('hls',len(target.index)).as_hex()
    fig=go.Figure()
    fig.add_trace(
        go.Bar(x=target.index,y=target,
                marker={'color':colors,
                   'line':{'color':'black','width':3},
                   'pattern':{'shape':'/'}})
    )

    fig.update_layout(go.Layout(title={'text':'Frequency of Orders by Days of Week',
                                  'font':{'color':'blue','size':30}},
                            xaxis={'title':{'text':'Days of Week'},
                                   'gridwidth':1,'showgrid':True},
                            yaxis={'title':{'text':'Frequency'},
                                   'gridwidth':1,'showgrid':True},

    ))
    st.plotly_chart(fig,use_container_width=True)
    
    #Frequency of Orders by Hour of Day
    target=df.order_hour_of_day.value_counts()
    fig=go.Figure()
    fig.add_trace(
        go.Bar(x=target.index,y=target,
            marker={'color':px.colors.qualitative.Dark24,
                   'line':{'color':'black','width':3},
                   'pattern':{'shape':'/'}})
    )

    fig.update_layout(go.Layout(title={'text':'Frequency of Orders by Hour of Day',
                                  'font':{'color':'blue','size':30}},
                            xaxis={'title':{'text':'Hour_of_Day'},
                                   'gridwidth':1,'showgrid':True},
                            yaxis={'title':{'text':'Frequency'},
                                   'gridwidth':1,'showgrid':True},
                            margin=dict(l=23,r=23,b=23)

    ))
    st.plotly_chart(fig,use_container_width=True)
      
      
if __name__ == '__main__':
    main()
    
