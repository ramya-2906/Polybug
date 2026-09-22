import streamlit as st
import google.generativeai as genai
from prompts import get_polybug_prompt
from styles import CUSTOM_CSS

st.set_page_config(page_title="PolyBug", page_icon="🐞", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 34px; color: #1e293b;'>🐞 PolyBug - AI Bug Finder & Explainer Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6; margin-top: -10px;'>Paste code in any language, I will find bugs for you! ✨</p>", unsafe_allow_html=True)

api_key = st.text_input("🔑 Enter your Gemini API Key:", type="password", placeholder="AIzaSy...")
code_input = st.text_area("💻 Paste your code here in any language:", height=250, placeholder="for i in range(5)\n print(i)")

if st.button("🔍 Find Bugs Now"):
    if not api_key or not code_input:
        st.warning("Please enter API key and code!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-3.5-flash-lite")

            prompt = get_polybug_prompt(code_input)
            with st.spinner("Analyzing code..."):
                res = model.generate_content(prompt)

                if "No Bugs Found" in res.text:
                    st.markdown("<h3 style='text-align:center; background:#dcfce7; color:#15803d; padding:10px; border-radius:12px;'>✅ No Bugs Found! Clean Code ✨</h3>", unsafe_allow_html=True)
                else:
                    count = res.text.count("**Bug")
                    if count == 0:
                        count = 1
                    if count == 1:
                        badge_text = "🐞 1 Bug Found!"
                    else:
                        badge_text = f"🐞 {count} Bugs Found!"
                    st.markdown(f"<h3 style='text-align:center; background:#fee2e2; color:#b91c1c; padding:10px; border-radius:12px;'>{badge_text}</h3>", unsafe_allow_html=True)

                st.markdown(res.text)

            st.success("Done! ✨")

        except Exception as e:
            st.error(f"Error: {e}")