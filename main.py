import streamlit as st
import yt_dlp
import os
import uuid

# 🌸 Custom theme setup
st.set_page_config(
    page_title="💖 Web Bundaku Sayang 💖",
    page_icon="🌷",
    layout="centered"
)

# 💖 Header + Langkah
st.markdown(
    """
    <style>
    .langkah-box {
        background-color: #fff0f5;
        border-left: 5px solid #ff69b4;
        padding: 1rem;
        border-radius: 10px;
        font-family: 'Comic Sans MS', cursive;
        color: #800080;
        margin-bottom: 20px;
    }
    </style>
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">
            🎀 Web Bundaku Sayang 🎀
        </h1>
        <p style="color: #d96aa7;">Download video YouTube dengan penuh cinta 💌</p>
    </div>

    <div class="langkah-box">
        <b>💡 Cara download video, Bunda:</b><br><br>
        1️⃣ Bunda <b>"Salin"</b> link dari YouTube Bunda 💖<br>
        2️⃣ Bunda <b>"Tempel"</b> link-nya di kotak bawah ini ✨<br>
        3️⃣ Bunda tekan <b>Enter</b> atau klik pojok kanan bawah 📥<br>
        4️⃣ Bunda <i>tunggu sebentar ya cantik...</i> 🧸<br>
        5️⃣ Kalau sudah selesai & muncul tulisan <b>"Klik ini, Bund!"</b>, tinggal klik itu aja yaa 💿💌<br>
        6️⃣ Udah selesai ya Bund, <b style="color:#ff69b4;">Love you 💕</b><br>
    </div>
    """,
    unsafe_allow_html=True
)

# 🌷 URL input
url = st.text_input("🌸 Tempel disini ya Bund:")

# 📁 Folder for downloads
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# 🚀 Auto-download
if url:
    with st.spinner("⏳ Video sedang didownload... tunggu sebentar ya Bund.. 💕"):
        try:
            video_id = str(uuid.uuid4())
            output_path = os.path.join(download_dir, f"{video_id}.%(ext)s")

            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': output_path,
                'quiet': True,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            st.success("✅ Video Bunda berhasil didownload! Klik tombol di bawah ini yaa~ 🧸💿")
            with open(filename, "rb") as file:
                st.download_button(
                    label="💌 Klik ini, Bund!",
                    data=file,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Gagal mendownload videonya bund 😢\n\n**Error:** {e}")
