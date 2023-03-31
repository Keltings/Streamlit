import numpy as np
import altair as alt
import pandas as pd

####The very first thing to do when creating a Streamlit app 
# is to start by importing the streamlit library as st like so:
import streamlit as st

#This is followed by creating a header text for the app:
st.header('st.write')

# example 1

#Its basic use case is to display text and Markdown-formatted text:
st.write('Hello, *World!* : sunglasses:')

#example 2

#it can also be used to display other data formats such as numbers:
st.write(1234)

#example 3
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
#DataFrames can also be displayed as follows:
st.write(df)

#eaxmple 4
#You can pass in multiple arguments:
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

#example 5
#you can also display plots as well by passing it to a variable as follows:
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
st.write(c)