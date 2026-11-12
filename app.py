
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# 1. KONFIGURASI WEBSITE
# =========================

st.set_page_config(
    page_title="My Private Dashboard",
    page_icon="🔐",
    layout="wide"
)

# Password disimpan di Streamlit Secrets
PASSWORD_BENAR = st.secrets["APP_PASSWORD"]

# Inisialisasi halaman
if "halaman" not in st.session_state:
    st.session_state.halaman = "login"


# =========================
# 2. HALAMAN LOGIN
# =========================

if st.session_state.halaman == "login":

    st.markdown(
        "<h1 style='text-align:center;'>Welcome</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "Please enter your password to continue."
        "</p>",
        unsafe_allow_html=True
    )

    with st.form("login_form"):
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        submit = st.form_submit_button(
            "Unlock",
            use_container_width=True
        )

        if submit:
            if password == PASSWORD_BENAR:
                st.session_state.halaman = "surat"
                st.rerun()
            else:
                st.error("Incorrect password!")


# =========================
# 3. HALAMAN SURAT
# =========================

elif st.session_state.halaman == "surat":

    st.markdown(
        """
        <div style="
            max-width:650px;
            margin:50px auto;
            padding:40px;
            background:#faf7f0;
            border-radius:15px;
            color:#333333;
            line-height:1.8;
        ">
            <p style="text-align:right; color:#888888;">
                A LITTLE MESSAGE FOR YOU
            </p>

            <h2 style="font-family:Georgia;">
                Dear You,
           
                Ada sedikit pesan yang ingin aku sampaikan
                melalui halaman ini.
            
                Terima kasih sudah meluangkan waktu untuk
                membuka halaman ini. Semoga kamu menikmati
                pesan kecil ini.


            <p><i>Warm regards,</i></p>
            <h3>Someone</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue to Dashboard →",
                 use_container_width=True):

        st.session_state.halaman = "dashboard"
        st.rerun()


# =========================
# 4. HALAMAN DASHBOARD
# =========================

elif st.session_state.halaman == "dashboard":

    st.title("My Data Dashboard")
    st.write("Welcome to your personal data dashboard!")

    st.divider()

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()
