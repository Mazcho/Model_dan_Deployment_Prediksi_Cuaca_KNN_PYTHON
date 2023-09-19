import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

#insert header gambar
st.image('Assets\weather-header-NEW-2.jpg')

#open file css
with open('style.css')as f:
    st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html = True)


# Using "with" notation
with st.sidebar:
    st.image('Assets\logo.png',width=200)
    menuapp = st.radio("Pilih salahsatu",["Menu Utama","Analsis Cuaca","Dataset","App"])
if menuapp == "Menu Utama":
    #membuat container
    ct1 = st.container()
    with ct1:
        st.header('Perubahan Cuaca Selama 3 tahun')
        st.write("By : Nicholaus verdhy Putranto || A11.2020.12447")
    st.divider()
    st.markdown(""" Dalam kurun waktu 2012 hingga 2015, perubahan cuaca yang ada
                    """
                    )

#membuat isi

if menuapp == "makan":
    st.write("Kuy")
#tab

