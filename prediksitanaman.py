import streamlit as st

# Kamus kondisi prediksi untuk setiap tanaman
tanaman_conditions = {
    'Cabe': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'}
    ],
    'Terong': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'}
    ],
    'Toge': [
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'gambut'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'gambut'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'gambut'}
    ],
    'Tomat': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'lempung'}
    ],
    'Wortel': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'}
    ],
    'Kacang': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Cerah', 'suhu': 'Kurang dari 10 Derajat', 'tempat': 'greenhouse', 'tanah': 'lempung'},
        {'cuaca': 'Hujan', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'gambut'}
    ],
    'Seledri': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'liat'},
        {'cuaca': 'Berawan', 'suhu': 'Kurang dari 10 Derajat', 'tempat': 'pedesaan', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'},
        {'cuaca': 'Hujan', 'suhu': 'Lebih dari 30 Derajat', 'tempat': 'pedesaan', 'tanah': 'gambut'}
    ],
    'Bombai': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': 'Lebih dari 30 Derajat', 'tempat': 'perkotaan', 'tanah': 'vulkanik'}
    ],
    'Bawang merah': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'liat'},
        {'cuaca': 'Berawan', 'suhu': 'Kurang dari 10 Derajat', 'tempat': 'pedesaan', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'},
        {'cuaca': 'Hujan', 'suhu': 'Lebih dari 30 Derajat', 'tempat': 'pedesaan', 'tanah': 'gambut'}
    ],
    'Jahe': [
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'greenhouse', 'tanah': 'lempung'},
        {'cuaca': 'Berawan', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'}
    ],
    'Brokoli': [
        {'cuaca': 'Cerah', 'suhu': 'Kurang dari 10 Derajat', 'tempat': 'greenhouse', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'lempung'},
        {'cuaca': 'Hujan', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'gambut'}
    ],
    'Lengkuas': [
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'pedesaan', 'tanah': 'liat'},
        {'cuaca': 'Berawan', 'suhu': 'Lebih dari 30 Derajat', 'tempat': 'greenhouse', 'tanah': 'pasir'},
        {'cuaca': 'Cerah', 'suhu': '11-30 Derajat', 'tempat': 'perkotaan', 'tanah': 'lempung'}
    ]
}

# Fungsi prediksi berdasarkan plant_id, cuaca, suhu, tempat, dan tanah
def predict(plant_id, cuaca, suhu, tempat, tanah):
    if plant_id in tanaman_conditions:
        for condition in tanaman_conditions[plant_id]:
            if (cuaca == condition['cuaca'] and 
                suhu == condition['suhu'] and
                tempat == condition['tempat'] and 
                tanah == condition['tanah']):
                return True
    return False

tanaman_rekomendasi = {
   'Cabe' : """Selamat atas keberhasilan Anda menanam cabai! Untuk memastikan tanaman terus tumbuh dengan baik, siram secara teratur untuk menjaga kelembapan tanah tanpa membuatnya terlalu basah. Pangkas daun yang tumbuh terlalu lebat untuk sirkulasi udara yang baik dan gunakan penopang untuk mendukung tanaman. Beri pupuk kaya nitrogen, fosfor, dan kalium, serta pupuk organik. Periksa tanaman secara rutin untuk hama dan penyakit, dan gunakan pestisida alami jika perlu. Pastikan tanaman mendapatkan sinar matahari penuh 6-8 jam sehari atau gunakan lampu tumbuh jika di dalam ruangan. Tambahkan mulsa untuk menjaga kelembapan tanah dan lakukan rotasi tanaman setiap musim. Panen cabai saat buahnya matang dengan gunting atau pisau tajam agar tidak merusak cabang. Dengan langkah-langkah ini, Anda akan mendapatkan hasil panen yang melimpah. Selamat bercocok tanam!""",
   'Terong' : """Selamat Tanaman anda akan tumbuh sehat dilahan yang sudah anda siapkan, kemudian untuk menanam terong dengan sukses, pilih bibit berkualitas dan sesuaikan dengan kondisi iklim setempat. Tanam di lahan yang subur, gembur, dan terkena sinar matahari penuh, dengan pH tanah antara 5.5-6.8. Jaga jarak tanam sekitar 60-70 cm antar tanaman dan 90 cm antar baris. Siram secara teratur tanpa menggenangi, beri pupuk nitrogen, fosfor, dan kalium berkala, serta bersihkan gulma. Kendalikan hama seperti kutu daun dan lalat buah dengan insektisida alami, dan cegah penyakit dengan menjaga kebersihan lahan. Panen terong saat buah mengkilap dan belum keras, simpan di tempat sejuk dan kering untuk masa simpan yang lebih lama.""",
   'Toge' : """Selamat anda akan berhasil menanam toge ditempat yang sudah anda siapkan, Setelah berhasil menanam tanaman toge, pastikan untuk menyiramnya secara teratur untuk menjaga kelembapan tanah, tempatkan di lokasi yang terkena sinar matahari sedang hingga terang, dan pastikan pot memiliki lubang drainase yang cukup. Berikan pupuk organik secara berkala, pemangkasannya jika tumbuh terlalu rapat, dan pantau tanda-tanda hama atau penyakit untuk ditangani dengan insektisida atau fungisida organik. Pemanenan secara teratur juga penting untuk menjaga kualitas tanaman toge.""",
   'Tomat' : """Selamat atas keberhasilan Anda menanam tomat! Untuk memastikan tanaman terus tumbuh dengan baik, siram secara teratur untuk menjaga kelembapan tanah tanpa membuatnya terlalu basah dan gunakan penyiraman dari bawah. Pangkas daun di bawah cabang buah pertama untuk sirkulasi udara yang baik dan gunakan penopang untuk mendukung tanaman. Beri pupuk kaya fosfor dan kalium, serta pupuk organik. Periksa tanaman secara rutin untuk hama dan penyakit, dan gunakan pestisida alami jika perlu. Pastikan tanaman mendapatkan sinar matahari penuh 6-8 jam sehari atau gunakan lampu tumbuh jika di dalam ruangan. Tambahkan mulsa untuk menjaga kelembapan tanah dan lakukan rotasi tanaman setiap musim. Panen tomat saat matang dengan gunting atau pisau tajam agar tidak merusak cabang. Dengan langkah-langkah ini, Anda akan mendapatkan hasil panen yang melimpah. Selamat bercocok tanam!""",
   'Wortel' : """Untuk menanam wortel dengan hasil optimal, pilih daerah dengan iklim sejuk hingga sedang dan cuaca stabil. Suhu ideal berkisar antara 15-21°C; suhu lebih rendah memperlambat pertumbuhan, sementara suhu di atas 27°C menurunkan kualitas. Tanam di tempat yang mendapat sinar matahari penuh setidaknya 6-8 jam per hari, dengan drainase baik untuk mencegah busuk akar. Tanah harus gembur, kaya bahan organik, dan pH 6-7, dengan tekstur liat berpasir atau lepas dan dalam untuk mendukung pertumbuhan akar yang lurus dan panjang. Hindari tanah berat, berbatu, atau padat yang dapat menyebabkan akar bercabang atau bentuk tidak beraturan. Olah tanah dengan baik sebelum menanam untuk hasil panen wortel berkualitas tinggi.""",
   'Kacang' : """Untuk menanam kacang panjang, pilihlah lokasi yang mendapatkan sinar matahari penuh untuk setidaknya enam hingga delapan jam sehari. Tanah yang ideal adalah yang kaya akan bahan organik dan memiliki drainase yang baik untuk mencegah genangan air. Pastikan suhu udara rata-rata harian berkisar antara 25°C hingga 30°C untuk memaksimalkan pertumbuhan. Penting juga untuk memperhatikan pola cuaca; hindari tanah yang terlalu basah atau terlalu kering, dan pastikan untuk menyiram tanaman secara teratur tetapi tidak berlebihan.""",
   'Seledri' : """Untuk menanam seledri, Anda membutuhkan kondisi cuaca yang sejuk hingga hangat dengan cahaya matahari yang cukup. Seledri tumbuh paling baik pada suhu sekitar 15-25 derajat Celsius dan membutuhkan tanah yang kaya akan bahan organik, dengan pH antara 6 hingga 7. Tanah yang lockernya baik memungkinkan akar seledri untuk berkembang dengan baik dan memungkinkan penyerapan air yang optimal. Pastikan tanah tersebut dapat mempertahankan kelembapan tanpa menjadi terlalu basah, untuk mencegah akar seledri membusuk. Idealnya, pilih lokasi yang terkena sinar matahari pagi atau sinar matahari yang terfilter, untuk memberikan kondisi tumbuh yang optimal bagi tanaman seledri Anda.""",
   'Bombai' : """Untuk menanam bawang bombay dengan baik, pilihlah lokasi yang terbuka dan terkena sinar matahari penuh. Bawang bombay tumbuh optimal pada suhu yang sejuk hingga sedang, sekitar 15°C hingga 25°C, dengan tanah yang kaya akan bahan organik dan memiliki drainase yang baik. Pastikan tanah tidak terlalu padat agar akar bawang dapat tumbuh dengan baik dan tanaman dapat menyerap nutrisi dengan optimal. Idealnya, tanam bawang bombay di musim semi hingga awal musim panas di daerah yang tidak terlalu lembab. Jaga kelembaban tanah agar tetap stabil tanpa terlalu basah atau kering secara berlebihan. Pemupukan secara teratur dengan pupuk organik ringan dapat membantu dalam pertumbuhan dan perkembangan tanaman bawang bombay.""",
   'Bawang merah' : """Meskipun cuaca berawan atau cerah, pastikan tanaman tetap mendapatkan cukup cahaya dengan memilih lokasi yang menerima sinar matahari maksimal dan menanam dengan jarak yang tidak terlalu rapat. Monitor suhu secara teratur untuk menjaga rentang optimal, dan gunakan penutup tanaman jika suhu turun terlalu rendah. Tanah vulkanik yang kaya mineral sebaiknya diperkaya dengan kompos atau pupuk kandang matang untuk meningkatkan kesuburan, dan pastikan drainase yang baik untuk mencegah genangan air. Lakukan penyiraman teratur tanpa berlebihan, dengan mempertimbangkan sistem pengairan tetes untuk menjaga kelembapan konsisten. Berikan pupuk secara teratur sesuai fase pertumbuhan, dengan pupuk kaya nitrogen pada fase awal dan fosfor serta kalium pada fase pembentukan umbi. Pemantauan rutin terhadap hama dan penyakit sangat penting, serta penggunaan pestisida organik atau kimia sesuai kebutuhan. Rotasi tanaman juga diperlukan untuk mencegah penumpukan patogen spesifik. Selain itu, gunakan mulsa untuk menjaga kelembapan tanah dan mengontrol gulma, serta lakukan penyiangan rutin. Dengan langkah-langkah ini, bawang merah Anda dapat tumbuh dengan baik dan menghasilkan panen yang berkualitas.""",
   'Jahe' : """Untuk memastikan pertumbuhan jahe optimal dalam kondisi cuaca berawan, suhu 11-30 derajat Celsius, di pedesaan dengan jenis tanah lempung, beberapa langkah perlu diperhatikan. Meskipun cuaca berawan, pastikan jahe tetap mendapatkan sinar matahari tidak langsung atau cahaya yang cukup dengan memilih lokasi yang memberikan pencahayaan maksimal. Monitor suhu secara teratur untuk menjaga rentang optimal, dan perlakukan tanaman dengan perhatian ekstra jika suhu turun di bawah 15 derajat Celsius. Tanah lempung yang baik sebaiknya diperkaya dengan pupuk organik atau kompos untuk meningkatkan kesuburan, serta pastikan drainase yang baik agar tidak ada genangan air yang dapat merusak akar jahe. Lakukan penyiraman secara teratur, terutama saat cuaca berawan untuk menjaga kelembapan tanah tetap stabil. Berikan pupuk secara berkala sesuai dengan kebutuhan jahe, dengan memastikan tanaman mendapatkan nutrisi yang cukup untuk pertumbuhan optimal. Pemantauan rutin terhadap hama dan penyakit sangat penting, serta gunakan pestisida organik jika diperlukan untuk mengendalikan serangan hama dan penyakit tanaman. Dengan mengikuti langkah-langkah ini, jahe Anda dapat tumbuh subur dan sehat di lingkungan pedesaan dengan tanah lempung, meskipun dalam kondisi cuaca berawan dan suhu variatif.""",
   'Brokoli' : """Setelah tanaman brokoli berhasil hidup, pastikan untuk terus memberikan perawatan yang tepat guna memastikan pertumbuhannya optimal. Monitor kondisi tanah secara teratur untuk memastikan kelembapan yang cukup namun tidak berlebihan, terutama pada tanah dengan drainase yang baik seperti lempung atau tanah liat yang dikombinasikan dengan bahan organik untuk nutrisi yang maksimal. Berikan pupuk secara berkala sesuai dengan kebutuhan tanaman, dengan fokus pada pupuk yang kaya nitrogen untuk pertumbuhan daun yang kuat dan pupuk kaya fosfor untuk pembentukan kepala brokoli yang baik. Jaga tanaman terbebas dari gulma dan pertahankan area sekitarnya untuk menghindari persaingan nutrisi. Lakukan pengendalian hama dan penyakit secara preventif dengan memantau tanaman secara rutin. Dengan memberikan perhatian yang tepat terhadap semua aspek ini, Anda dapat memastikan tanaman brokoli tetap sehat dan produktif, menghasilkan panen yang berkualitas tinggi.""",
   'Lengkuas' : """Pastikan tanaman lengkuas mendapatkan sinar matahari cukup, minimal 6-8 jam setiap hari. Tanam lengkuas di tanah yang kaya akan bahan organik dan memiliki drainase yang baik. Pastikan untuk memberikan penyiraman teratur agar tanah tetap lembab, tetapi tidak tergenang air. Pemupukan rutin dengan pupuk organik atau pupuk NPK dengan konsentrasi tinggi pada unsur nitrogen dan kalium juga sangat penting untuk mendukung pertumbuhan dan produksi lengkuas yang baik.""", 
}

#rekomendasi gagal
tanaman_rekomendasi_gagal = {
    'Cabe' :"""Mohon maaf, prediksi kami menunjukkan bahwa kondisi saat ini mungkin tidak cocok untuk pertumbuhan cabai. Untuk mencoba lagi, pastikan tanah tetap lembab namun tidak terlalu basah. Lakukan penyiraman secara teratur pagi atau sore hari, terutama saat cuaca panas. Cabai membutuhkan sinar matahari penuh setidaknya enam jam sehari, jadi pastikan tanaman ditempatkan di tempat yang terkena cahaya langsung. Gunakan pupuk organik secara teratur untuk meningkatkan kesuburan tanah. Jika tumbuh di dalam ruangan, pastikan untuk menyediakan ventilasi yang baik. Dengan perawatan yang tepat, Anda dapat meningkatkan peluang berhasil menanam cabai di masa mendatang.""",
    'Terong' : """Jika tanaman terong gagal tumbuh, langkah-langkah untuk memperbaikinya meliputi pengecekan dan penyesuaian pH tanah, perbaikan struktur tanah dengan kompos, penggunaan bibit berkualitas, pengaturan penyiraman untuk menghindari genangan atau kekurangan air, pemupukan yang tepat dengan pupuk seimbang, pengendalian hama dan penyakit secara teratur, serta memastikan tanaman mendapatkan sinar matahari yang cukup dan kondisi lingkungan yang sesuai. Evaluasi kondisi secara menyeluruh dan memodifikasi pendekatan sebelum mencoba menanam kembali dapat membantu meningkatkan kesuksesan dalam menanam terong.""",
    'Toge' : """Jika Anda mengalami kegagalan dalam menanam tanaman toge, perlu untuk memeriksa kondisi tanah, aspek sinar matahari, pola penyiraman, pemupukan, dan kebersihan tempat tanam. Pastikan tanah memiliki drainase yang baik dan cukup subur, serta tanaman mendapatkan cukup sinar matahari. Atur pola penyiraman agar sesuai dengan kebutuhan tanaman toge, dan pastikan menggunakan pupuk yang tepat untuk memberikan nutrisi yang cukup. Selain itu, pastikan wadah atau tempat tanam bersih dari hama dan penyakit sebelum menanam kembali. Dengan mengevaluasi dan menyesuaikan faktor-faktor ini, Anda dapat meningkatkan peluang keberhasilan pada percobaan berikutnya dalam menanam tanaman toge.""",
    'Tomat' : """Jika tanaman tomat Anda gagal tumbuh, evaluasi kondisi tanah, pastikan pH antara 6.0-6.8, dan tambahkan kompos atau pupuk organik untuk meningkatkan kesuburan. Periksa apakah tanaman mendapatkan cukup sinar matahari, setidaknya 6-8 jam per hari, dan pindahkan ke lokasi yang lebih terang jika diperlukan. Pastikan penyiraman dilakukan dengan benar, menjaga kelembapan tanah tanpa membuatnya terlalu basah, dan pastikan drainase baik untuk menghindari genangan air. Periksa tanaman dari hama dan penyakit, gunakan pestisida alami jika diperlukan, dan cek kualitas benih yang digunakan. Jika ditanam di pot, pastikan ukurannya cukup besar dan memiliki lubang drainase yang memadai. Hindari penggunaan pupuk berlebihan dan lakukan rotasi tanaman setiap musim untuk mencegah penumpukan hama dan penyakit di tanah. Dengan langkah-langkah ini, Anda dapat meningkatkan peluang keberhasilan menanam tomat di musim berikutnya.""",
    'Wortel' : """Jika kondisi cuaca, suhu, tempat, dan tanah tidak sesuai untuk menanam wortel, ada beberapa rekomendasi yang bisa dipertimbangkan. Wortel biasanya membutuhkan tanah yang lembab tetapi tidak tergenang air, dengan suhu optimal antara 15-20 derajat Celsius dan kecenderungan untuk menghindari tanah yang berpasir atau tanah yang terlalu berat. Jika kondisi di lokasi Anda tidak mendukung hal ini, pertimbangkan untuk menanam wortel dalam wadah atau pot yang memungkinkan Anda mengontrol drainase dan komposisi tanah. Pilihlah varietas wortel yang tahan terhadap suhu ekstrem atau mencoba menanam di musim semi atau musim gugur di daerah yang lebih sejuk. Pastikan untuk memberikan perlindungan tambahan seperti penutup barikade atau mulsa untuk mempertahankan kelembaban tanah yang sesuai.""",
    'Kacang' : """Untuk menanam kacang panjang, kondisi cuaca yang ideal adalah matahari penuh dengan suhu antara 24-32 derajat Celsius. Tanah yang cocok adalah yang kaya akan bahan organik, dengan drainase yang baik untuk mencegah genangan air. Jika tanah di lokasi Anda kurang sesuai, pertimbangkan untuk menambahkan kompos atau bahan organik lainnya untuk meningkatkan kesuburan tanah. Pastikan untuk menyediakan cukup ruang bagi tanaman untuk merambat dan berkembang dengan baik.""",
    'Seledri' : """Untuk menanam seledri, idealnya memilih lokasi yang terkena sinar matahari parsial hingga penuh dan memiliki udara cukup lembab. Seledri tumbuh optimal pada suhu antara 15 hingga 20 derajat Celsius, namun dapat bertahan pada suhu sedikit lebih tinggi dengan penyiraman yang cukup. Tanah yang cocok untuk seledri adalah tanah yang kaya akan bahan organik dan memiliki drainase yang baik, dengan pH sekitar 6 hingga 6,5. Jika kondisi cuaca atau suhu di area Anda tidak mendukung, pertimbangkan untuk menanam seledri di pot atau wadah yang bisa dipindahkan ke tempat yang lebih sesuai dengan kebutuhannya.""",
    'Bombai' : """Untuk menanam bawang bombai, penting untuk memperhatikan beberapa faktor lingkungan. Bawang bombai membutuhkan cuaca yang relatif sejuk hingga hangat dengan sinar matahari penuh. Suhu ideal untuk pertumbuhan bawang bombai berkisar antara 15°C hingga 25°C. Jika suhu terlalu panas, pertumbuhan bawang bombai bisa terhambat. Pastikan tanah yang digunakan memiliki drainase yang baik dan kaya akan bahan organik. Bawang bombai juga lebih baik ditanam di tanah yang memiliki pH netral hingga sedikit asam.
                    Jika kondisi lingkungan tidak sesuai, pertimbangkan menggunakan wadah atau pot untuk menanam bawang bombai di tempat yang lebih terkendali. Ini memungkinkan Anda untuk mengatur tanah dengan lebih baik, memastikan drainase yang optimal, dan memindahkan pot sesuai dengan perubahan cuaca. Jika tanah di area Anda terlalu lempung atau memiliki drainase yang buruk, tambahkan kompos atau pasir untuk meningkatkan kondisi tanah. Pastikan juga bawang bombai mendapatkan sinar matahari yang cukup, minimal enam jam sinar matahari langsung setiap hari untuk pertumbuhan yang maksimal.""",
    'Bawang merah' : """Untuk mengatasi tantangan pertumbuhan bawang merah dalam kondisi cuaca hujan, suhu di atas 30 derajat Celsius, di perkotaan dengan tanah pasir, langkah-langkah spesifik perlu dipertimbangkan. Pastikan untuk mengelola drainase dengan baik karena tanah pasir cenderung cepat mengering setelah hujan. Selain itu, dalam suhu yang tinggi seperti di atas 30 derajat Celsius, tanaman bawang merah dapat mengalami stres panas, sehingga perlindungan dari sinar matahari langsung atau penggunaan jaring naungan bisa membantu. Pemantauan kelembapan tanah sangat penting; meskipun hujan turun, perlu untuk memberikan penyiraman tambahan agar tanah tetap lembab namun tidak tergenang air. Di lingkungan perkotaan, upayakan untuk menempatkan tanaman bawang merah di area yang teduh dari polusi udara dan cahaya langsung yang berlebihan. Pemupukan rutin dengan pupuk organik atau buatan diperlukan untuk meningkatkan kesuburan tanah yang biasanya rendah dalam tanah pasir. Pengendalian hama dan penyakit juga harus diperhatikan dengan lebih teliti karena kondisi yang lembap dapat meningkatkan risiko serangan jamur. Dengan merencanakan perawatan yang sesuai dan mengambil langkah-langkah perlindungan yang tepat, Anda dapat meningkatkan kemungkinan keberhasilan pertumbuhan bawang merah di kondisi lingkungan yang tidak ideal tersebut.""",
    'Jahe' : """Jika tanaman jahe Anda tidak hidup atau tidak subur, pertama-tama periksa kondisi tanah secara menyeluruh. Pastikan tanah memiliki drainase yang baik dan kaya akan bahan organik. Jahe membutuhkan tanah yang lembab namun tidak tergenang air. Selain itu, pastikan tanaman mendapatkan cukup cahaya matahari tidak langsung atau pencahayaan yang cukup untuk fotosintesis yang optimal. Jika suhu terlalu tinggi, pertimbangkan untuk memberikan naungan atau penutup sementara untuk mengurangi stres panas pada tanaman. Lakukan juga pemupukan rutin dengan pupuk yang sesuai untuk fase pertumbuhan jahe, dan perhatikan untuk mengendalikan hama dan penyakit yang dapat mempengaruhi kesehatan tanaman. Dengan memperbaiki faktor-faktor ini, Anda dapat meningkatkan peluang jahe tumbuh subur dan sehat.""",
    'Brokoli' : """Jika tanaman brokoli tidak hidup atau tidak subur, pertama-tama periksa kondisi lingkungan tempat tumbuhnya. Pastikan tanaman mendapatkan cahaya matahari yang cukup, setidaknya 6-8 jam per hari, atau pertimbangkan untuk menambah pencahayaan dengan lampu grow light jika ditanam di dalam ruangan. Selain itu, perhatikan suhu lingkungan yang optimal antara 15-25 derajat Celsius; suhu yang terlalu tinggi atau rendah dapat menghambat pertumbuhan brokoli. Perbaiki drainase tanah agar tidak terlalu basah atau tergenang air, terutama jika tanah terlalu liat atau berat. Pemupukan secara teratur dengan pupuk organik atau pupuk yang mengandung nitrogen, fosfor, dan kalium sesuai dengan kebutuhan tanaman brokoli juga diperlukan. Pantau secara rutin untuk mengendalikan hama dan penyakit, dan lakukan tindakan preventif seperti penyiangan gulma dan perawatan tanaman yang tepat. Dengan memperbaiki faktor-faktor ini, Anda dapat meningkatkan kesehatan dan produktivitas tanaman brokoli.""",
    'Lengkuas' : """Periksa kondisi tanah untuk memastikan pH-nya sesuai dengan kebutuhan lengkuas, yang idealnya antara 6-7. Jika tanah terlalu asam atau alkalis, itu dapat menghambat penyerapan nutrisi oleh tanaman. Selain itu, pastikan tanah memiliki drainase yang baik; lengkuas tidak menyukai tanah yang terlalu basah. Jika lingkungan terlalu teduh atau tidak mendapatkan cukup sinar matahari, pertimbangkan untuk memindahkan tanaman ke lokasi yang lebih terbuka. Gunakan pupuk khusus lengkuas yang mengandung nutrisi lengkap dan lakukan aplikasi secara teratur sesuai dengan petunjuk kemasan.""",
}


# Fungsi rekomendasi berdasarkan hasil prediksi
def get_rekomendasi(plant_id, success):
    if success:
        return tanaman_rekomendasi.get(plant_id, "Rekomendasi belum tersedia untuk tanaman ini.")
    else:
        return tanaman_rekomendasi_gagal.get(plant_id, "Rekomendasi belum tersedia untuk tanaman ini.")

# Judul aplikasi
st.title("Prediksi Keberhasilan Tanaman")
st.write('Masukkan kondisi saat ini untuk mendapatkan rekomendasi atau saran perbaikan untuk tanaman Anda.')


# Pilihan tanaman
tanaman = st.selectbox("Pilih Tanaman", list(tanaman_conditions.keys()))

# Input kondisi
cuaca = st.selectbox("Pilih Cuaca", ["Cerah", "Berawan", "Hujan"])
suhu = st.selectbox("Pilih Suhu", ["Kurang dari 10 Derajat", "11-30 Derajat", "Lebih dari 30 Derajat"])
tempat = st.selectbox("Pilih Tempat", ["pedesaan", "perkotaan", "greenhouse"])
tanah = st.selectbox("Pilih Jenis Tanah", ["liat", "lempung", "gambut", "pasir", "vulkanik"])

# Tombol prediksi
if st.button("Prediksi Tanaman"):
    is_successful = predict(tanaman, cuaca, suhu, tempat, tanah)
    
    if is_successful:
        st.success("Tanaman Anda diprediksi akan tumbuh dengan baik!")
        st.info(get_rekomendasi(tanaman, True))
    else:
        st.error("Tanaman Anda diprediksi mungkin tidak akan tumbuh.")
        st.warning(get_rekomendasi(tanaman, False))

