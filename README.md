# Milestone 1: Ide Visualisasi Data

## Dataset yang anda pilih

NYC and Tokyo Check-in
https://www.kaggle.com/datasets/chetanism/foursquare-nyc-and-tokyo-checkin-dataset/data

## Deskripsi data

Dataset yang dipilih adalah dataset berjudul FourSquare - NYC and Tokyo Check-ins, diambil dari Foursquare dengan data yang berisi riwayat check-in di kota New York, Amerika Serikat dan Tokyo, Jepang yang dikumpulkan dalam rentang 10 bulan (dari 12 April 2012 sampai 16 February 2013) yang terpisah dalam 2 file (dataset_TSMC2014_NYC & dataset_TSMC2014_TKY). Tiap file dataset berisi 8 atribut, yakni userId, venueId, venueCategoryId, venueCategory, latitude, longitude,timezoneOffset, dan utcTimestamp, berikut penjelasan per atribut:
1. UserId adalah id pengguna dalam foursquare
2. VenueId adalah id dari suatu tempat
3. venueCategoryId adalah id kategori dari VenueId
4. venueCategory adalah representatif label (nama) dari kategori tempat berdasarkan venueCategoryId
5. latitude adalah titik koordinat lintang
6. longtitude adalah titik koordinat bujur
7. timezoneOffset adalah perbedaan waktu antara zona waktu tertentu dan Waktu UTC (Tokyo 540 menit lebih cepat dari UTC, Amerika Serikat -240 menit dibelakang UTC)
8. utcTimestamp adalah waktu check-in berdasarkan UTC.
Setiap aktivitas check-in dikaitkan dengan timestamp, koordinat GPS, dan lain-lainnya untuk menunjukkan spesifik aktivitas dari tiap tiap pengguna.

## Tuliskan ide cerita

Ide cerita ini bertujuan untuk memberikan wawasan mendalam tentang pola rutinitas kehidupan masyarakat perkotaan di New York dan Tokyo melalui informasi data check-in Foursquare.

 Menggunakan konversi timestamp UTC berdasarkan timezoneOffset, kita dapat melihat kapan pengguna di setiap kota aktif dan bagaimana perbedaan waktu tersebut mempengaruhi jam-jam sibuk mereka.

Melalui atribut venueCategory, kita dapat melihat tempat-tempat seperti restoran, taman, atau pusat perbelanjaan mana yang menarik banyak pengunjung di kedua kota.

Melalui informasi koordinat (latitude dan longitude), kita dapat menampilkan peta interaktif yang menggambarkan pergerakan dan distribusi aktivitas di dua kota tersebut. 

Dengan menggabungkan venueCategory, utcTimestamp, dan timezoneOffset, maka dapat disimpulkan waktu-waktu tertentu saat masyarakat lebih sering mengunjungi kategori tempat tertentu. Misalnya, restoran mungkin lebih ramai pada waktu makan siang atau makan malam, sementara taman mungkin lebih ramai pada akhir pekan. Ini menunjukkan bagaimana kategori tempat tertentu mempengaruhi frekuensi check-in berdasarkan waktu.

Dengan Visualiasi ini diharap dapat membantu kita dalam memahami perbedaan gaya hidup dan preferensi aktivitas masyarakat di dua kota tersebut yang memiliki waktu  yang berbeda. 

## Petanyaan visualisasi

1. Dimana saja tempat yang sering dikunjungi di kota New York dan Tokyo?
2. Pada waktu kapan saja tempat atau area tersebut mulai sibuk?
3. Dalam hitungan per waktu, kategori tempat apa yang orang sering kunjungi?(per hari, per bulan, per minggu, dll)
4. Apakah ada hubungan antara lokasi geografis dengan frekuensi kunjungan masyarakat?
5. Bagaimana perbedaan waktu kunjungan pada kategori tempat yg sama di kedua kota?