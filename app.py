
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
        """
        <div style="text-align:center;">
            <p>Please enter your password to continue.</p>
            <p style="font-size:13px; color:gray;">
                Clue: the most beautiful instrumental of an xdiz song (11 letters)
            </p>
        </div>
        """,
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
               a little bit of words for cepe
            </p>

            <h2 style="font-family:Georgia;">
                hii bess!!!
                hehe kayaknya aku lebih sering manggil kamu bess ya daripada cep/pe

                disclaimer aku gabisa nulis kata kata kek gini and sorry for my broken english *SUMPAH BES GRAMMAR SUSAH POLL

                our story began on 2nd march, anjayy. zuzurr nih dlu tkut bgt bakalan sendiri krna yah i don’t like odd number and i’m the only one math in here, but unexpectedly kita malah sering barengg. i think that you’re o.de to my life, krna klo kata gaon, o.de can match energy people around him. AND THAT’S YOU BESS!!!

                trimakasiee yaa bess udah menemani ku di hari-hari magang ituu. i was so happy spending time with you together. unexpected nya lagi kita sama sama INFP??? OMGG AND WE ARE N AND P GARIS KERAS????? sumpahh maaf banget yaa bess kalo aku sering ngasih pertanyaan “menurutmu”, pasti kmu muak yaaa, hehe. makasiii jugaa sudah menanggapi semua pertanyaan di kepala ku and you really answered exactly what i wanted to hear. i’m going to miss the days when we’re yapping 24/7 talked random topic, berisik di sekre, dan dangdutan di sekre itu </3. dann aku bener bener bakal kangenn beli cilok mansa dan bakwi fkh bareng kmu besss.

                jujur yaa bess, i really have to thank Allah for bringing you into my life when my life lagi ajur ajur nya karena s word or revisi ituu. makasii udah selalu nyemangatin aku with all your beautiful words, selalu bantu akuu meskipun kmu ga paham dengan topik ku. udah mau memberikan pendapat tentang skripsi ku itu dan makasii sudah menyediakan rumah mu untuk aku skripsian, PENGEN LAGI PLS MAIN KE RUMAH CEPE TPI BENER BENER MAIN:(((. makasii yaaa bess bener bener gatau lagi mau bilang apa selain makasii.

                ahh, this is the point that i could never forget. terima kasihh sudah mau menuruti keimpulsive an kuu *anjay kek judul albumnya xdiz. kayaknya banyak bgt ga sih main kita yg berawal dari impulsive though kitaa. thank you for always saying “gas” or “ayo” dan no word “wacana” from cepe, i really appriciated for it. mulai dari pergi ke mall pake seragam sma (eh sumpah tapi itu seru bgt plss, pdhl kita cuma muter muter doang di mall), terus tiba-tiba ke pantai pagi pagi?? ANJAY ITU MAH BELUM FULL MELEK DAH LANGSUNG GAS KE PANTAI, terus tiba tiba noraebang meanwhile kmu blom tau banyak lagu kpop. sumpahh terharu bangett, makasii yaaa bess dah mau nemenin aku meskipun i know it’s not your place. oh ya jadi keinget kalimat ini “we didn’t realize we were making memories, we just knew we were having fun” wkwkk.

                bess, i know so many things inside your head, so many expectations you have to live up to. but remember bess, don’t be so hard on yourself bcs it’s your first time living okee. you can share whatever’s on your mind with me, my chat is always open for you (but for know i prefer on tiktok wkwk). kalau kata xdiz “고생했어요, 그대여” and “겁먹을 필요 없어요”, wkwk tebak lirik apa. oh ya kalo kata seventeen “cheers to youth”, i really recommend this song to you bess. inget ya bess even if things sometimes don’t go your way you’ll not stop trying and not give up on yourself. don't forget to take care your health yaa bess, kesehatan nomor 1 plss.

                maafin aku yaa bes kalo selama temenan sama aku masih banyak kurangnya, kadang omongan ku yg kelewatan atau perlakuan ku yg kurang mengenakan. maaf banget kalau semisal aku tiba tiba diem atau ga ngajak ngobrol, idk what’s happening to me tpi pasti ada fasenya di mana aku tiba tiba diem dan ga mood berinteraksi. i’m really sorry for that :((

                duh i hate that the world giving words “come” and “go”, tapi mayb i’m just a small part of your life but the memories that we spent together semoga gapernah kamu lupain yaa bess. sangat sangat berharap we don’t lost contact and still chatting as much as we do, i’ll really sad if it happens. thank you bess for the memories we made. time flies so fast but memories will last forever. goodbye it’s bittersweet, but it’s not the end, i’ll see your face again.

                — cewe jungsu, elsa <3
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

    st.title("Thank you for reading my cringe letter bes!")
    st.write("disclaimer : this is my first time i've made a website like this, so sorry if it looks a little weird :(.")

    st.divider()

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()
