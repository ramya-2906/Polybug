import streamlit as st
import requests
from prompts import get_polybug_prompt
from styles import CUSTOM_CSS

st.set_page_config(page_title="PolyBug", page_icon="🐞", layout="centered")

# Hide Streamlit Buttons
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stToolbar"] {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 34px; color: #1e293b;'>🐞 PolyBug - AI Bug Finder & Explainer Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6; margin-top: -10px;'>Paste code in any language, I will find bugs for you! ✨ No API Key Needed!</p>", unsafe_allow_html=True)

code_input = st.text_area("💻 Paste your code here in any language:", height=250, placeholder="for i in range(5)\n print(i)")

if st.button("🔍 Find Bugs Now"):
    if not code_input:
        st.warning("Please paste your code!")
    else:
        try:
            prompt = get_polybug_prompt(code_input)
            API_URL = "https://text.pollinations.ai/openai"
            payload = {
                "model": "openai",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1500
            }
            with st.spinner("Analyzing code..."):
                response = requests.post(API_URL, json=payload, timeout=30)
                response.raise_for_status()
                data = response.json()
                result_text = data['choices'][0]['message']['content']

                if "No Bugs Found" in result_text:
                    st.markdown("<h3 style='text-align:center; background:#dcfce7; color:#15803d; padding:10px; border-radius:12px;'>✅ No Bugs Found! Clean Code ✨</h3>", unsafe_allow_html=True)
                else:
                    count = result_text.count("**Bug")
                    if count == 0:
                        count = 1
                    badge_text = f"🐞 {count} Bug{'s' if count > 1 else ''} Found!"
                    st.markdown(f"<h3 style='text-align:center; background:#fee2e2; color:#b91c1c; padding:10px; border-radius:12px;'>{badge_text}</h3>", unsafe_allow_html=True)

                st.markdown(result_text)

            st.success("Done! ✨")

        except Exception as e:
            st.error(f"Error: {e}. Please wait 15 seconds and try again.")
