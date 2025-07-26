import streamlit as st
import pandas as pd

st.title("📝 User Input Form")

# Input fields
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
email = st.text_input("Enter your email")
favorite_color = st.selectbox("Pick your favorite color", ["Red", "Blue", "Green", "Yellow", "Other"])

submit = st.button("Submit")

# Show table after submit
if submit:
    data = {
        "Field": ["Name", "Age", "Email", "Favorite Color"],
        "Value": [name, age, email, favorite_color]
    }
    df = pd.DataFrame(data)
    st.subheader("🎉 Your Information Summary")
    st.table(df)
else:
    st.info("Fill out the form and hit submit!")

st.write("hello")
st.write("hi")