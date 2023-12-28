import streamlit as st
from streamlit_option_menu import option_menu
from t5_model import t5_correct
from LT_model import language_tool_detect
def streamlit_menu():
        selected = option_menu(
            menu_title=None,  # required
            options=["T5 Model", "Language Tool"],
            icons=["robot", "robot"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal")
        return selected

selected = streamlit_menu()

if selected == "T5 Model":
    st.subheader(f"Grammar corrector with {selected}")
    sentence = st.text_area("Enter Text", '')
    submit = st.button('Correct one')

    if submit:
        corrected = t5_correct(sentence)
        st.text(corrected)

if selected == "Language Tool":
    st.subheader(f"Grammar corrector with {selected}")
    sentence = st.text_area("Enter Text", '')
    submit = st.button('Correct one')

    if submit:
        corrected = language_tool_detect(sentence)
        st.text(corrected)