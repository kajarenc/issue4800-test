import streamlit as st


def get_rating(rating_text):
    if rating_text == "Accepted":
        return "🟢"
    elif rating_text == "Reasonable":
        return "🟠"
    else:
        return "🔴"


y = st.selectbox("TEST SELECTBOX", ["Accepted", "Reasonable", "ANOTHER_VALUE"])

rating = get_rating(y)

# JUST SPACING
for i in range(10):
    st.write("")

with st.expander(label=f"{rating} foo"):
    st.markdown("bar")