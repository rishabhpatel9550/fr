import streamlit as st

# Page config
st.set_page_config(page_title="Name Combiner", layout="centered")

# Custom CSS for colorful UI
st.markdown("""
    <style>
    body {
        background-color: #FF0000
        ;
    }
    .stApp {
        background: linear-gradient(to right, #e0f7fa, #fce4ec);
        color: #800080;
    }
    .stTextInput>div>div>input {
        background-color: #0G00FF"!important;
        color: #11111 !important;
    }
    .combiner-box {
        padding: 1em;
        border-radius: 10px;
        background-color: #fce4ec"!important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("💞 Name Combiner Tool")

# Input section
st.markdown("Enter two names to mix and match their sounds. Great for couple names!")

with st.container():
    name1 = st.text_input("First Name", placeholder="e.g., Brad")
    name2 = st.text_input("Second Name", placeholder="e.g., Angelina")

# Name combination logic
def combine_names(n1, n2):
    if not n1 or not n2:
        return []
    n1, n2 = n1.strip(), n2.strip()
    half1 = n1[:len(n1)//2]
    half2 = n2[len(n2)//2:]
    reverse1 = n1[::-1][:3]
    reverse2 = n2[::-1][:3]
    return [
        half1 + half2,
        n1[:3] + n2[-3:],
        reverse1 + reverse2,
        n1[:len(n1)//2+1] + n2[len(n2)//2-1:]
    ]

# Display combinations
if name1 and name2:
    combos = combine_names(name1, name2)
    st.markdown("### 💡 Suggested Names:")
    with st.container():
        for combo in combos:
            st.success(combo.capitalize())

# Advertisement section
st.markdown("---")
st.markdown("### 📢 Ad Space")
st.markdown("""
<div style='text-align:center; padding: 10px; border: 2px dashed #aaa; background-color: #rrggbb; border-radius: 10px;'>
✨ <b>Promote your brand here!</b> ✨<br>
Great spot for couple-themed products or events.
</div>
""", unsafe_allow_html=True)
