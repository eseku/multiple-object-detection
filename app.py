import streamlit as st
from PIL import Image
from predict import  detecto_m
import matplotlib.pyplot as plt

def main():
     st.markdown("# Object Detector")
     st.markdown("#### A Simple Object detector using Detecto")
     st.markdown(" — -")
     # getting the image from the user
     uploaded_file = st.file_uploader("Choose an pic…”, type=”jpg")
     if uploaded_file is not None:
          st.image(uploaded_file, caption='Your Image.',use_column_width=True)
          st.success("#### And taraaaaa!")
          result = detecto_m(uploaded_file) # passing image to our function
          result = plt.plot() # plotting the result
          st.pyplot(result)
          st.balloons() #some fun ballons
# to run our module
if __name__=='__main__':
         main()