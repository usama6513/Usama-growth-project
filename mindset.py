import streamlit as st

st.set_page_config(page_title="Growth Mindset Quiz", page_icon="🧠")

st.title("🧠 Growth Mindset Quiz")
st.subheader("Kya aapki soch Growth Mindset wali hai ya Fixed Mindset wali?")

st.write("Har sawal ka jawab honestly do. End mein aapko apni mindset ka analysis milega.")

# Define questions and answers
quiz = [
    {
        "question": "Agar tum fail ho jao to tum kya sochoge?",
        "options": {
            "Yeh subject mere bas ka nahi hai.": 0,
            "Mujhe samajhne mein thoda waqt lagega.": 1,
        }
    },
    {
        "question": "Tum kisi mushkil problem ko kaise dekhte ho?",
        "options": {
            "Mushkil cheezen stress deti hain.": 0,
            "Mushkil ka matlab hai seekhne ka moka.": 1,
        }
    },
    {
        "question": "Jab kisi aur ko success milti hai to?",
        "options": {
            "Lagta hai mein kabhi aisa nahi kar sakta.": 0,
            "Unse inspire hota hoon aur seekhta hoon.": 1,
        }
    },
    {
        "question": "Agar teacher tumhe feedback de to?",
        "options": {
            "Criticism se bura lagta hai.": 0,
            "Feedback se improvement hoti hai.": 1,
        }
    },
    {
        "question": "Tum mehnat ke baare mein kya sochti ho?",
        "options": {
            "Agar talent ho to mehnat ki zarurat nahi.": 0,
            "Mehnat se talent develop hota hai.": 1,
        }
    },
]

# Quiz logic
score = 0
responses = []

with st.form("quiz_form"):
    for i, q in enumerate(quiz):
        st.write(f"**Q{i+1}. {q['question']}**")
        response = st.radio("", list(q["options"].keys()), key=i)
        responses.append(q["options"][response])
    submitted = st.form_submit_button("Submit Quiz")

# Result
if submitted:
    score = sum(responses)
    st.subheader("📊 Result")

    if score >= 4:
        mindset = "🌱 Growth Mindset"
        tips = [
            "Keep embracing challenges.",
            "Mistakes = opportunities to grow.",
            "Appreciate effort, not just result!",
        ]
    elif score >= 2:
        mindset = "🌀 Mixed Mindset"
        tips = [
            "You're on the way! Reflect on setbacks and reframe your thinking.",
            "Focus more on learning than proving yourself.",
        ]
    else:
        mindset = "🧱 Fixed Mindset"
        tips = [
            "Try to see mistakes as learning chances.",
            "Believe that you can improve with effort.",
            "Growth comes when you step out of comfort zone.",
        ]

    st.success(f"Aapka Mindset hai: **{mindset}**")
    st.write("### Tips to Improve:")
    for tip in tips:
        st.markdown(f"- {tip}")

    result_text = f"Mera mindset result: {mindset}! Tum bhi ye quiz karo: [Growth Mindset Quiz](your_app_link)"
    st.write("👇 Copy & share this message:")
    st.code(result_text)
