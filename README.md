# Prediksi_Cuaca_KNN_PYTHON
Halo! Selamat datang di Repository ku. jadi repo ini adalah tugas ahkir aku saat matakuliah permodelan. Akan tetapi model yang aku buat sebelumnya sangat buruk yang dimana model hanya bisa memprediksi kelas 3 dan 4, sedangkan ada 5 kelas pada data tersebut.

![image](https://github.com/Mazcho/Prediksi_Cuaca_KNN_PYTHON/assets/77985996/b51701d8-25e5-4c14-88d7-622de41a37e8)

Bisa kalian lihat sendiri, pada model yang pertama aku bikin 9 bulan yang lalu, model ini hanya bisa memprediksi sebesar 76% untuk kelas 3 dan 4. Hal ini disebabkan oleh yang namanya imbalance data, yang dimana jumlah data untuk tiap kelasnya tidak seimbang sama sekali.
pada dataset ini, jumlah kelas 3 dan 4 sangatlah tinggi.
Maka dari itu saya membuat model baru yang jauh lebih baik yaitu menggunakan metode oversampling, dimana data data kelas yang memiliki jumlah yang data sedikit , kita buat menjadi sama banyaknya/ mendekati jumlah data terbesarnya,
Dan hasil model KNN + Oversampling menjadi seperti dibawah ini

![image](https://github.com/Mazcho/Prediksi_Cuaca_KNN_PYTHON/assets/77985996/ff919c30-4886-467b-bbda-84ea31ecdf8c)

Akurasinya menjadi 75% untuk keseluruhan, tapi bisa kita lihat bahwa dari model 1 KNN dibandingkan dengan model 2 KNN + Oversampling hasilnya sangatlah ebrbeda
Model 2 mampu memprediksi keseluruhan kelas pada dataset yang diberikan

Untuk mencoba model ini bisa kunjungi link ini : https://prediksicuacaknnpython-mazcho.streamlit.app/
