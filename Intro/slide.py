# st.slider allows the display of a slider input widget.
#importing the streamlit library
import streamlit as st
import pandas as pd
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

#collect user input about the age of users.
# collect user input about the age of users.
# The following three integers 0, 130, 25 represents 
# the minimum, maximum and default values, respectively.
age = st.slider('How old are you?', 0, 130, 25)
st.write('I am', age, 'years old')

st.subheader('Range slider')

#The range slider allow selection of a 
# lower and upper bound value pair.

#The first input argument displays the 
# text just above the range slider widget
values = st.slider(
    # The following three arguments 0.0, 100.0, (25.0, 75.0) 
    # represents the minimum and maximum values while the last 
    # tuple denotes the default values 
    #to use as the selected lower (25.0) and upper (75.0) bound values.
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('Range time slider')

#allows selection of a lower and upper bound value pair of datetime.
#The first input argument displays the text just above the range 
# time slider

#The default values for the lower and upper 
# bound value pairs of datetime are set to 11:30 
# and 12:45, respectively.
appointment = st.slider(
    'Schedule your appointment:',
    value=(time(11, 30), time(12, 45)))
st.write('You are sheduled for:', appointment)

st.subheader("Datetime Slider")


#The datetime slider allows selection of a datetime.
#Thee first input argument displays the text just above the 
# datetime slider widget 

#The default value for the datetime was set using the 
# value option to be January 1, 2020 at 9:30
start_time = st.slider("When do you start?",
                      value=datetime(2020, 1, 1, 9, 30),
                      format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)

