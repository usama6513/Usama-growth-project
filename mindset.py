#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth mindset",project_icon="⌛")
st.title("Growth mindset AI project")

st.header("🏈 Welcome to your GROWTH journey!")
st.write("Embrace challenges,learn from mistakes,and unlock fully potential. This AI- powered app helps you to build a growth mindset with reflection, challenges and achievements! ")

#quote section
st.header("Today's Growth mindset Quote")
st.write("❝Success is not final,Failure is not fatal: it is the courage to continue that counts.❞- wins and churchill",)

st.header("🏍 whats your challenge today?")
user_input=st.text_input("Describe a challenge you are facing:")


#condition
if user_input:
    st.success(f"💪you are facing: {user_input},keep pushing towords your goals🥉")
else:
    st.warning("Tell us about your challenge to get started!")

    #reflexing
    st.header("Reflect on your learning")
    reflection=st.text_area("describe your reflections here")

    if reflection:
        st.success(f"✨Great insight! your reflection:{reflection}")
    else:
        st.info("reflecting on past experience help you grow! share your difficulties")


        #achievements
        st.header("🏆 Celebrate Your Wins!")
        acheivement= st.text_input("Share something that you have recently accomplished:")


        if acheivement:
            st.success(f"🌷 Amazing! you acheived: {acheivement}")
        else:
            st.info("Big or Small acheivement counts! share one now! 😍")


            #footer
            st.write("- - -")
            st.write("💫 keep believing in yourself.Growth is the journey, not destination!✨")
            st.write("**⛔ Created by Usama Sharif**")






               