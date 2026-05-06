import streamlit as st


st.markdown("Wilkommen")


st.title("das ist die Streamlit App")

firstname = st.text_input("Vorname")
lastname = st.text_input("Nachname")


st.text_area("deine Nachricht")


if st.button("Submit"):
    st.write(firstname + " " + lastname)

