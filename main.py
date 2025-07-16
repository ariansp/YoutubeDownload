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

# 💖 Header
st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">
            🎀 Web Bundaku Sayang 🎀
        </h1>
        <p style="color: #d96aa7;">Download video YouTube dengan penuh cinta 💌</p>
    </div>
    """,
    unsafe_allow_html=True
)

url = st.text_input("🌸 Masukkan URL video YouTube bunda di sini:")

# Folder for downloads
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

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
                    label="💌 Klik ini, bund!",
                    data=file,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"❌ Gagal mendownload videonya bund 😢\n\n**Error:** {e}")
