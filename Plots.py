import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.header("Plotting Graphs")

char_data = pd.DataFrame(np.random.randn(20, 3), columns=['line-1', 'line-2', 'line-3'])
st.subheader("Line plot")
st.line_chart(char_data)

st.subheader("Area plot")
st.area_chart(char_data)

st.subheader("Bar plot")
st.bar_chart(char_data)

st.header("Data visualization with matplotlib.")

st.subheader('Loading the dataframe')
df = pd.read_csv('C:/Users/achin/.streamlit/iris.csv')
st.dataframe(df)

st.subheader('Distribution plot with matplotlib')
fig = plt.figure(figsize=(15, 8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution plot with seaborn')
fig = plt.figure(figsize=(15, 8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader('Multiple graphs')
col1, col2 = st.columns(2)
with col1:
    col1.header('KDE = False')
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'], kde=False)
    st.pyplot(fig1)

with col2:
    col2.header('Histogram = False')
    fig2 = plt.figure()
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig2)

st.subheader('Changing style')
col1, col2 = st.columns(2)
with col1:
    col1.header('style, context')
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['sepal_length'])
    st.pyplot(fig1)

with col2:
    col2.header('theme')
    fig2 = plt.figure()
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(df['sepal_length'])
    st.pyplot(fig2)

st.header('Types of graphs')
st.subheader('Scatter plot')
fig, ax = plt.subplots(figsize=(15, 8))
ax.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

st.subheader('Count-plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data=df, x='species')
st.pyplot(fig)

st.subheader('box-plot')
fig = plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='species', y='petal_length')
st.pyplot(fig)

st.subheader('voilin-plot')
fig = plt.figure(figsize=(15, 8))
sns.violinplot(data=df, x='species', y='petal_length')
st.pyplot(fig)
