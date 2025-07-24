import streamlit as st
from AreaCalculator import area_of_circle, area_of_rectangle, area_of_triangle
from langchain_helper import explain_area_formula

if st.checkbox("Want to know how it works?"):
    st.info(explain_area_formula(shape))


st.title("🧮 Area Calculator")

shape = st.selectbox("Choose a shape", ["Circle", "Rectangle", "Triangle"])

if shape == "Circle":
    radius = st.number_input("Enter radius", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of Circle: {area_of_circle(radius):.2f}")

elif shape == "Rectangle":
    length = st.number_input("Enter length", min_value=0.0)
    width = st.number_input("Enter width", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of Rectangle: {area_of_rectangle(length, width):.2f}")

elif shape == "Triangle":
    base = st.number_input("Enter base", min_value=0.0)
    height = st.number_input("Enter height", min_value=0.0)
    if st.button("Calculate"):
        st.success(f"Area of Triangle: {area_of_triangle(base, height):.2f}")
