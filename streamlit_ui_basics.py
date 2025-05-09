# Import streamlit package
import streamlit as st
from streamlit import multiselect

# Page header
st.title("Welcome to Streamlit")

# Page subheader
st.subheader("Welcome to Streamlit")

# Page text
st.text("Example text")

# Page Markdown
st.markdown("Example markdown")

# Create a button
if st.button("Click me!"):
    st.success("You clicked me!")

# Example slider
slider_value = st.slider("Select a number:", 1, 100)
st.write("You selected:", slider_value)

#Example checkbox
checkbox_value = st.checkbox("Check me to continue")
st.write("You checked: ", checkbox_value)

# Example selectbox
selectbox_value = st.selectbox("Select a number", [1,2,3,4,5])
st.write("You selected:", selectbox_value)

# Example radio button
radio_value = st.radio("Select a number", [1,2,3,4,5])
st.write("You selected:", radio_value)

# Example multiselect
multiselect_value = st.multiselect("Select a number", [1,2,3,4,5])
st.write("You selected:", multiselect_value)

# Example text input
text_input_value = st.text_input("Enter some text")
st.write("You entered:", text_input_value)

# Example password input
password_input_value = st.text_input("Enter some password", type="password")
st.write("You entered:", password_input_value)

# Example number input
number_input_value = st.number_input("Enter a number")
st.write("You entered:", number_input_value)

# Example date input
date_input_value = st.date_input("Select a date")
st.write("You selected:", date_input_value)

# Example time input
time_input_value = st.time_input("Select a time")
st.write("You selected:", time_input_value)

# Example color picker
color_picker_value = st.color_picker("Pick a color")
st.write("You picked:", color_picker_value)

# Example file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size)
    st.write(uploaded_file.read())