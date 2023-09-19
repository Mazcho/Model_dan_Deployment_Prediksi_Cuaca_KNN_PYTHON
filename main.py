import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

#open file css
with open('style.css')as f:
    st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html = True)

#call model
model = pickle.load(open("model.pkl","rb"))


# Using "with" notation
with st.sidebar:
    st.image('Assets\logo.png',width=200)
    menuapp = st.radio("Pilih salahsatu",["Menu Utama","Analsis Cuaca","Dataset","App"])
if menuapp == "Menu Utama":
    #membuat container
    ct1 = st.container()
    with ct1:   
        #insert header gambar
        st.image('Assets\weather-header-NEW-2.jpg')
        st.header('Perubahan Cuaca Selama 3 tahun')
        st.write("By : Nicholaus verdhy Putranto || A11.2020.12447")
    st.divider()
    st.markdown(""" Cuaca di Australia antara tahun 2012 hingga 2015 telah menjadi topik yang sangat penting dan perhatian. Selama periode ini, Australia mengalami berbagai variasi cuaca yang mencolok. Di beberapa wilayah, kekeringan yang parah menjadi masalah serius, dengan pasokan air yang menipis dan tanah yang retak akibat kurangnya hujan. Hal ini memicu kebakaran hutan yang merusak serta mengganggu kehidupan manusia dan satwa liar.

Namun, ada juga sisi lain dari koin cuaca Australia. Beberapa wilayah di timur negara ini mengalami musim hujan yang berlimpah, yang menyebabkan banjir hebat dan kerusakan infrastruktur. Cuaca yang ekstrem ini mencerminkan tantangan yang dihadapi Australia dalam mengelola dan beradaptasi dengan perubahan iklim global.

Periode ini juga memicu perdebatan yang berkembang tentang perlunya tindakan perlindungan lingkungan dan mitigasi perubahan iklim untuk menghadapi masalah cuaca ekstrem yang semakin sering terjadi di Australia.
                    """
                    )

#membuat isi

if menuapp == "Dataset":
    st.title("Tentang dataset")


#membuat app
if menuapp == "App":
    st.title("Halaman Prediksi cuaca hari ini")
    st.markdown("Halo! Sekarang kamu ada pada halaman prediksi cauca yang telah dibuat oleh penulis kode ini. Silahkan masukan aspek aspek yang ada kolom dibawah ini. Setelah kalian memasukkan data data yang dibutuhkan oleh prediksi cuaca ini, silahkan kalian tekan tombol prediksi cuaca. Nanti hasil prediksi akan muncul di sebelah kanan pada halaman ini. Selamat mencoba")
    col8,col9 = st.columns(2)
    with col8:
        precipitation = st.number_input("Masukan Kadar Pengendapan : ",value=0.0, step=0.1)
        temp_max = st.number_input("Masukan Temperatur maksimal : ", value=0.0, step=0.1)
        temp_min = st.number_input("Masukan Temperatur minimal : ",value=0.0, step=0.1)
        wind     = st.number_input("Masukan tekanan Angin : ", value=0.0, step=0.1)
        prediksi_cuaca = ""
        if st.button("Prediksi Cuaca"):
            prediksi_cuaca = model.predict([[precipitation,temp_max,temp_min,wind]])
    with col9:
        if prediksi_cuaca==1:
            st.title("Cuaca: Gerimis")
            st.image("Assets/drizzel.png",width=300)
        elif prediksi_cuaca==2:
            st.title("Cuaca: Bersalju")
            st.image("Assets/snow.png",width=300)
        elif prediksi_cuaca==3:
            st.title("Cuaca: Hujan")
            st.image("Assets/rain.png",width=300)
        elif prediksi_cuaca==4:
            st.title("Cuaca: Panas")
            st.image("Assets/sun.png",width=300)
        elif prediksi_cuaca==5:
            st.title("Cuaca: Berkabut")
            st.image("Assets/fog.png",width=300)
            
        

