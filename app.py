import requests
import streamlit as st
import streamlit_lottie as stl

st.set_page_config(page_title="Chep's Personal Python Website", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/styles.css")

#load assets
lottie_coding = load_lottieurl("https://lottie.host/36a2ea3b-8cf6-4346-b687-59f58b42e8ea/mEn0IFXk5n.json")
lottie_coding_two = load_lottieurl("https://lottie.host/c0f7fb70-59f7-423a-9230-c177c6fa5d58/tVYUSIktUx.json")



#header section
with st.container():
    st.write("##")
    st.header("Hi, my name is Conor Chepenik :boom:")
    st.title("I'm A Developer, Father, & Bitcoiner based in Boston")
    st.write("I am fueled by a passion to leverage open-source technologies that can transform peer-to-peer value transfers. My goal is to help others see why value for value is so important. My ultimate vision is an internet subsidized by users, not ads. In this future, creators directly engage their audience for support, not corporate sponsors. I also believe in the power of compounding so I've committed to writing daily, for life or until Medium goes out of business.")
    st.markdown("[My Medium](https://medium.com/@chepenikconor)")

#What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
                        """
            On my YouTube channel I am creating tutorials for people who:
            - Are looking for a way to leverage open source software in their day-to-day work.
            - Enjoy reads of quality articles focused on Bitcoin, Nostr, Satire, Comedy, and anything else that peaks my interest.
            - Chatting with individuals who I find interesting and who are doing things that improve the world.
            - Want to use software to enable value transfer between individuals without the need for a middleman.

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
    with right_column:
        stl.st_lottie(lottie_coding, height=500, key="coding")

#projects
with st.container():
    st.write("---")
    st.header("Featured Podcasts")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("img/powerofsub.png", width=200)
    with text_column:
        st.subheader("Learn About The Power Of Subtraction")
        st.write(
            """
                - See why shoes are vital to foot health  
                - How to choose the right shoes for you
                - Why everything is downstream of money
            """
        )
        st.markdown("[Watch video](https://youtu.be/FD5UME_fTHs)")
    with image_column:
        st.image("img/binmucker.png", width=200)
    with text_column:
        st.subheader("Texas Slim & The Beef Initative")
        st.write(
            """
                - What Beef & Bitcoin have in common
                - Why you should shake a Rancher's hand
                - How The Beef Initiative is changing the world
            """
        )
        st.markdown("[Watch Video](https://youtu.be/PT4yHzxq1oo)")

#contact
with st.container():
    st.write("---")
    st.header("Get in touch with me :)")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/eab4c130f00412b3d328a87920ac3ad3" method="POST" />
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        stl.st_lottie(lottie_coding_two, height=369, key="notcoding")