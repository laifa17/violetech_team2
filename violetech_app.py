import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="AI & Big Data Masterclass", 
                   page_icon="🤖", 
                   layout="wide")

# --- CSS Custom untuk Efek Visual & Background ---
background_css = """
<style>
    /* Background utama */
    .stApp {
        background: linear-gradient(135deg, #4c3c92, #8a3dff, #d36cf2);
        color: white;
        animation: fadeIn 3s ease-in-out;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.8);
        color: white;
        border-right: 3px solid #ffffff40;
        transition: 0.3s ease-in-out;
    }

    /* Efek Animasi */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    .stTitle, .stMarkdown, .stImage {
        animation: fadeIn 2s ease-in-out;
    }

    /* Stiker animasi */
    .stSticker {
        width: 120px;
        height: auto;
        transition: transform 0.3s ease;
    }
    .stSticker:hover {
        transform: scale(1.1);
    }

    /* Penambahan font dan efek pada text */
    .stTitle {
        font-family: 'Arial', sans-serif;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        animation: slideInFromLeft 1s ease-in-out;
    }

    .stMarkdown {
        font-family: 'Verdana', sans-serif;
        font-size: 16px;
        text-align: justify;
        line-height: 1.7;
        color: #f5f5f5;
    }

    @keyframes slideInFromLeft {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }

    /* Gaya tombol */
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        padding: 10px 25px;
        border-radius: 50px;
        border: none;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #f57c00;
    }
</style>
"""

# Menampilkan CSS di dalam Streamlit
st.markdown(background_css, unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("📌 Navigasi Cepat")
menu = st.sidebar.radio("📖 Pilih Halaman:", ["About Us", "Big Data", "Machine Learning", "AI", "Tes Pengetahuan"])
st.sidebar.markdown("---")

# Halaman About Us
if menu == "About Us":
    st.markdown("<h1 class='stTitle'>📖 About Us</h1>", unsafe_allow_html=True)
    
    # Gambar Hero
    st.image("https://cdn1-production-images-kly.akamaized.net/GQNghQqz0t7NGpXQOz0HzzY80GY=/1200x900/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3430556/original/038776400_1618548270-group-people-working-out-business-plan-office_1303-15861.jpg", use_container_width=True)

    st.write("""
    *Selamat datang di AI & Big Data Masterclass!* 🚀
    
    Di sini, kami memberikan materi yang mendalam tentang dua bidang yang paling revolusioner dalam dunia teknologi saat ini: *Artificial Intelligence (AI)* dan *Big Data*. Kami berkomitmen untuk membekali Anda dengan keterampilan dan pengetahuan yang diperlukan untuk memahami dan berkontribusi pada dunia digital yang terus berkembang ini.

    ## Apa yang Anda Dapatkan dari Masterclass Ini?
    - *Pemahaman Mendalam*: Kami membahas konsep-konsep dasar hingga aplikasi terkini dalam AI dan Big Data.
    - *Penerapan Nyata*: Anda akan mempelajari bagaimana teknologi ini digunakan di berbagai industri seperti kesehatan, keuangan, e-commerce, dan lainnya.
    - *Interaktivitas*: Materi dipecah dalam format yang mudah dipahami, dengan pertanyaan kuis untuk menguji pemahaman Anda.

    *Kenapa Belajar AI dan Big Data?*
    
    - *AI* membantu perusahaan membuat keputusan lebih cepat dan lebih akurat dengan analisis data besar.
    - *Big Data* memberikan wawasan baru dengan memproses volume informasi yang sangat besar.
    
    Dengan keterampilan ini, Anda akan memiliki keunggulan kompetitif di dunia yang semakin mengandalkan teknologi.
    
    ## Misi Kami
    Masterclass ini bertujuan untuk:
    - Membantu Anda memahami dasar-dasar AI dan Big Data.
    - Memberikan keterampilan praktis yang dapat digunakan untuk karier di teknologi, analitik data, dan kecerdasan buatan.
    - Menyediakan wawasan tentang bagaimana AI dan Big Data mengubah berbagai industri.

    Terima kasih telah bergabung, dan mari kita mulai perjalanan pembelajaran ini! 🎓
    """)

    st.success("📚 *Jelajahi materi di sidebar atau gunakan pencarian untuk menemukan topik yang Anda inginkan!* 🚀")
    st.divider()

# Halaman Big Data
if menu == "Big Data":
    st.markdown("<h1 class='stTitle'>📊 Big Data</h1>", unsafe_allow_html=True)
    st.image("https://www.coregistros.com/wp-content/uploads/2016/07/big-data-bbdd-data-base-bases-de-datos.jpg", use_container_width=True)
    
    with st.expander("📦 *Apa Itu Big Data?*"):
        st.write("""
        Big Data adalah kumpulan data dalam jumlah *sangat besar* yang dihasilkan dari berbagai sumber seperti media sosial, sensor IoT, transaksi e-commerce, dan banyak lagi.
        
        Teknologi Big Data memungkinkan untuk menganalisis dan mengolah data dalam volume besar secara efisien untuk mendapatkan wawasan yang dapat diambil dari data tersebut.
        """)

    st.markdown("### 📊 *Karakteristik Big Data (5V)*")
    st.write("""
    - *📦 Volume*: Data dalam jumlah besar yang memerlukan penyimpanan dan pengolahan yang efisien.  
    - *⚡ Velocity*: Data yang terus berkembang dan harus diproses secara real-time atau mendekati real-time.  
    - *🔀 Variety*: Berbagai format data seperti teks, gambar, video, dan data sensor.  
    - *✔ Veracity*: Keakuratan dan konsistensi data yang perlu diperhatikan untuk analisis yang tepat.  
    - *💰 Value*: Data yang memiliki potensi untuk memberikan wawasan atau keuntungan bagi organisasi.
    """)
    
    st.markdown("### 🧮 *Penerapan Big Data dalam Industri*")
    st.write("""
    ✅ *Kesehatan* → Big Data digunakan untuk menganalisis data medis dalam jumlah besar untuk menemukan pola penyakit dan merancang perawatan yang lebih baik.  
    ✅ *E-commerce* → Platform e-commerce menganalisis perilaku belanja pelanggan untuk memberikan rekomendasi produk yang lebih personal.  
    ✅ *Keuangan* → Big Data digunakan untuk mendeteksi pola transaksi yang mencurigakan dalam upaya pencegahan penipuan.  
    ✅ *Transportasi* → Analisis Big Data memungkinkan optimasi lalu lintas dan pengelolaan armada kendaraan.
    """)

# Halaman Machine Learning
if menu == "Machine Learning":
    st.markdown("<h1 class='stTitle'>🤖 Machine Learning</h1>", unsafe_allow_html=True)
    st.image("https://repararelpc.es/wp-content/uploads/2020/10/machine-learning-3.jpg", use_container_width=True)

    with st.expander("📚 *Apa Itu Machine Learning?*"):
        st.write("""
        Machine Learning (ML) adalah cabang dari kecerdasan buatan yang memungkinkan komputer untuk *belajar dari data* tanpa diprogram secara eksplisit.
        
        Pada dasarnya, ML menggunakan algoritma untuk menganalisis data, memahami pola, dan membuat keputusan berdasarkan data tersebut.
        """)

    st.markdown("### 🧠 *Jenis-jenis Machine Learning*")
    st.write("""
    - *Supervised Learning*: Model dilatih dengan menggunakan data berlabel, sehingga komputer dapat belajar dan membuat prediksi berdasarkan data tersebut.  
    - *Unsupervised Learning*: Model berusaha menemukan pola atau struktur dalam data yang tidak memiliki label.  
    - *Reinforcement Learning*: Model belajar dari interaksi dengan lingkungan dan mendapatkan umpan balik berupa penghargaan atau hukuman.
    """)

# Halaman AI
if menu == "AI":
    st.markdown("<h1 class='stTitle'>🧠 Kecerdasan Buatan (AI)</h1>", unsafe_allow_html=True)
    st.image("https://cms-cmp.cbncloud.co.id/api/media/public/info/promo/images/VC-Blog-2024-Machine-Learning-di-Kehidupan-Nyata-Model%2C-Kasus-Penggunaan-dan-Pengoperasiannya-01%281%29.jpg", use_container_width=True)

    with st.expander("🤖 *Apa Itu AI?*"):
        st.write("""
        AI adalah bidang ilmu yang bertujuan untuk membuat mesin berpikir dan bertindak layaknya manusia.
        
        Dengan kemampuan untuk *mengolah data, **membuat keputusan otomatis, dan **belajar dari pengalaman*, AI telah merevolusi berbagai bidang.
        """)

    st.markdown("### 🚀 *Penerapan AI di Dunia Nyata*")
    st.write("""
    ✅ *Kesehatan* → AI digunakan untuk mendiagnosis penyakit dan merancang perawatan.  
    ✅ *E-commerce* → AI memberikan rekomendasi produk berdasarkan data perilaku pelanggan.  
    ✅ *Keuangan* → Deteksi penipuan dalam transaksi bank dan perencanaan keuangan otomatis.  
    ✅ *Transportasi* → Kendaraan otonom menggunakan AI untuk mengenali dan menavigasi lingkungan sekitar.
    """)

# Halaman Tes Pengetahuan
if menu == "Tes Pengetahuan":
    st.markdown("<h1 class='stTitle'>📝 Tes Pengetahuan</h1>", unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        st.write("### ✅ Jawab pertanyaan berikut:")

        q1 = st.radio("1. Apa kepanjangan dari AI?", ["Artificial Intelligence", "Automated Intelligence", "Advanced Information"])
        q2 = st.radio("2. Apa tujuan utama Machine Learning?", ["Mengolah data", "Membuat program", "Belajar dari data tanpa program eksplisit"])
        q3 = st.radio("3. Apa yang termasuk karakteristik Big Data?", ["Volume, Variety, Velocity", "Video, Voice, Virtual", "Valuable, Vivid, Vast"])
        q4 = st.radio("4. Bagaimana AI bekerja?", ["Menggunakan algoritma dan data", "Berdasarkan insting", "Mengikuti emosi manusia"])
        q5 = st.radio("5. Contoh penerapan AI di dunia nyata adalah?", ["Mobil otonom", "Kalkulator biasa", "Mesin ketik"])
        q6 = st.radio("6. Apa itu Big Data?", ["Data dalam jumlah kecil", "Data dalam jumlah besar", "Data yang tidak terstruktur"])
        q7 = st.radio("7. Apa tujuan dari Machine Learning?", ["Menganalisis data", "Belajar dari data", "Menulis kode manual"])
        q8 = st.radio("8. Jenis Machine Learning yang membutuhkan label pada data adalah?", ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"])
        q9 = st.radio("9. Apa itu Veracity dalam Big Data?", ["Keakuratan data", "Kecepatan data", "Kuantitas data"])
        q10 = st.radio("10. Apa yang digunakan AI dalam mobil otonom?", ["Data sensor", "Peta manual", "Driver manusia"])

        submitted = st.form_submit_button("Kirim Jawaban")

    if submitted:
        correct_answers = {
            "q1": "Artificial Intelligence", 
            "q2": "Belajar dari data tanpa program eksplisit", 
            "q3": "Volume, Variety, Velocity", 
            "q4": "Menggunakan algoritma dan data", 
            "q5": "Mobil otonom", 
            "q6": "Data dalam jumlah besar", 
            "q7": "Belajar dari data", 
            "q8": "Supervised Learning", 
            "q9": "Keakuratan data", 
            "q10": "Data sensor"
        }

        user_answers = {
            "q1": q1, 
            "q2": q2, 
            "q3": q3, 
            "q4": q4, 
            "q5": q5, 
            "q6": q6, 
            "q7": q7, 
            "q8": q8, 
            "q9": q9, 
            "q10": q10
        }

        st.markdown("### 📊 Hasil Jawaban Anda:")
        for key, user_answer in user_answers.items():
            if user_answer == correct_answers[key]:
                st.markdown(f"✅ *{user_answer}* (Benar!)")
            else:
                st.markdown(f"❌ *{user_answer}* (Salah! Jawaban yang benar: *{correct_answers[key]}*)")

st.divider()
st.success("📚 *Terus belajar dan tingkatkan pemahamanmu tentang AI & Big Data!* 🚀")