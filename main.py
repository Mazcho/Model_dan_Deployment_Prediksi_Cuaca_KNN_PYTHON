import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier

#open file css
with open('style.css')as f:
    st.markdown(f'<style>{f.read()}<style>',unsafe_allow_html = True)

#call model
model = pickle.load(open("model.pkl","rb"))

#memanggil dataset
file_data = "prediksicuaca2.csv"
try:
    df = pd.read_csv(file_data)
except FileNotFoundError:
    st.error("File csv tidak ditemukan")


# Using "with" notation
with st.sidebar:
    logomain = Image.open('Assets/logo.png')
    st.image(logomain)
    menuapp = st.radio("MENU PREDIKSI CUACA",["Menu Utama","Analsis Cuaca","Dataset","App"])
if menuapp == "Menu Utama":
    #membuat container
    ct1 = st.container() 
    with ct1:   
        #insert header gambar
        headermenu = Image.open('Assets/weather-header-NEW-2.jpg')
        st.image(headermenu)
        st.header('Perubahan Cuaca Selama 3 tahun')
        st.write("By : Nicholaus verdhy Putranto || A11.2020.12447")
    st.divider()
    st.markdown(""" Perubahan cuaca adalah fenomena alam yang terus-menerus memengaruhi kondisi atmosfer di seluruh dunia. Cuaca dapat berubah dari satu hari ke hari berikutnya, dan ini dipengaruhi oleh berbagai faktor seperti suhu, tekanan udara, kelembaban, dan arah angin. Dalam cuaca, terdapat beragam kondisi yang dapat kita temui, seperti kabut (fog), hujan (rain), matahari (sun), gerimis (drizzle), dan salju (snow).

Kabut, misalnya, adalah kondisi di mana partikel air sangat kecil mengambang di udara dan mengurangi jarak pandang, sering terjadi di pagi hari saat suhu udara dingin. Hujan adalah turunnya butiran-butiran air dari atmosfer yang dapat muncul dalam berbagai intensitas, dari gerimis hingga hujan lebat. Matahari adalah sumber cahaya dan panas utama bagi planet kita yang mendukung kehidupan. Gerimis adalah hujan ringan yang terdiri dari tetesan air kecil, sering kali cukup untuk membuat permukaan tanah menjadi basah. Salju adalah kristal es yang turun dari langit dan dapat menciptakan pemandangan yang indah saat menutupi permukaan bumi.

Semua perubahan cuaca ini memiliki dampak yang berbeda pada kehidupan kita dan ekosistem di sekitar kita, dan pemahaman tentang fenomena cuaca ini penting untuk mengatasi tantangan yang terkait dengan perubahan iklim dan adaptasi di era modern ini.
                    """
                    )

#membuat analisis data
if menuapp=="Analsis Cuaca":
    st.header("ANALISIS CUACA 2012-2015")
    st.markdown("Dari dataset yang didapatkan dari pembuat, ada beberapa hal yang dapat diulas dari dataset Prediksi cuaca 2012-2015. Mulai dari yang pertama yaitu Analisis Frekuensi cuaca.")
    dataku=df["weather"].value_counts()
    st.bar_chart(dataku)
    st.markdown("Pada 3 tahun terahkir 2012-2015, cuaca yang sering dijumpai ialah hujan dan matahari. Dari kedua cuaca in menunjukkan bahwa 2 cuaca tersebut dominan di bulan bulan tertentu, sedangkan berkabut gerimis dan bersalju sangat jarang ")



#membuat isi datasets

if menuapp == "Dataset":
    headerdataset = Image.open('Assets/headerdata.jpg')
    st.image(headerdataset)
    st.title("Tentang dataset : Prediksi Cuaca")
    st.markdown("Data set tentang 'Prediksi Cuaca' berisikan data yang mengenai time series dari tahun 2012 hingga tahun 2015. Tidak hanya waktunya saja, melainkan juga faktor faktor yang mempengaruhi hasil cuaca tersebut. Atribut tersebut diantaranya ada pengendapat, temperatur maksimal, temperatur minimal dan kecepatan angin. Dari hasil dataset yang ada, berisikan data sebanyak 1460 buah data dari tahun 2012 hingga 2015")
    st.dataframe(df,width=1500,height=500,hide_index=True)
    st.markdown("Berikut adalah Deskripsi dari atribut atribut yang ada pada dataset")
    dfdesk = pd.DataFrame([
        {"Atribut":"Date","Deskripsi":"Tanggal kejadian cuaca tersebut"},
        {"Atribut":"precipitation","Deskripsi":"Tingkat curah hujan pada hari itu"},
        {"Atribut":"temp_max","Deskripsi":"Temperatur maksimal pada hari itu"},
        {"Atribut":"temp_min","Deskripsi":"Temperatur minimal pada hari itu"},
        {"Atribut":"wind","Deskripsi":"Kecepatan angin di hari itu"},
        {"Atribut":"weather","Deskripsi":"Nama cuaca"},
        {"Atribut":"Prediciton","Deskripsi":"label dari nama cuaca"},
    ])
    st.dataframe(dfdesk,width=1500, height=280, hide_index=True)
    st.markdown("Dari dataset diatas, dataset ini tergolong dataset yang bersih, dimana tidak mengandung missing value sama sekali. Akan tetapi data ini mengandung data yang tidak seimbang yang dimana jumlah klasifikasi antar kelas jumlahnya tidak sama/ tidak seimbang. Bila tidak memiliki dataset, silahkan download di tombol ini !")
    @st.cache_data
    def convert_df(dataframe):
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)
    
    st.download_button(
            label="Download 'Prediksi Cuaca.csv' Data set",
            data=csv,
            file_name="Dataset Prediksi Cuaca.csv",
            mime="text/csv",
        )
    st.write("Link dataset di KAggle : https://www.kaggle.com/datasets/ananthr1/weather-prediction ")

#membuat app
if menuapp == "App":
    st.title("Halaman Prediksi cuaca hari ini")
    st.markdown("Halo! Sekarang kamu ada pada halaman prediksi cauca yang telah dibuat oleh penulis kode ini. Silahkan masukan aspek aspek yang ada kolom dibawah ini. Setelah kalian memasukkan data data yang dibutuhkan oleh prediksi cuaca ini, silahkan kalian tekan tombol prediksi cuaca. Nanti hasil prediksi akan muncul di sebelah kanan pada halaman ini. Selamat mencoba")
    col8,col9 = st.columns(2)
    with col8:
        precipitation = st.number_input("Masukan Curah Hujan : ",value=0.0, step=0.1)
        temp_max = st.number_input("Masukan Temperatur maksimal : ", value=0.0, step=0.1)
        temp_min = st.number_input("Masukan Temperatur minimal : ",value=0.0, step=0.1)
        wind     = st.number_input("Masukan tekanan Angin : ", value=0.0, step=0.1)
        prediksi_cuaca = ""
        if st.button("Prediksi Cuaca"):
            prediksi_cuaca = model.predict([[precipitation,temp_max,temp_min,wind]])
    with col9:
        if prediksi_cuaca==1:
            weather1 = Image.open('Assets/drizzel.png')
            st.title("Cuaca: Gerimis")
            st.image(weather1,width=300)
        elif prediksi_cuaca==2:
            weather2 = Image.open('Assets/snow.png')
            st.title("Cuaca: Bersalju")
            st.image(weather2,width=300)
        elif prediksi_cuaca==3:
            weather3 = Image.open('Assets/rain.png')
            st.title("Cuaca: Hujan")
            st.image(weather3,width=300)
        elif prediksi_cuaca==4:
            weather4 = Image.open('Assets/sun.png')
            st.title("Cuaca: Panas")
            st.image(weather4,width=300)
        elif prediksi_cuaca==5:
            weather5 = Image.open('Assets/fog.png')
            st.title("Cuaca: Berkabut")
            st.image(weather5,width=300)
            
        

