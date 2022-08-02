import streamlit as st
import streamlit_option_menu as som
import Functions as ft


st.set_page_config(page_title='EmancipaTIC', layout='wide', page_icon="./IMG/descarga.jpg")



#Sidebar option 
with st.sidebar:
    selected = som.option_menu("EmancipaTIC", ['Home', 'Reporting','Prediction'], 
        icons=['house'], menu_icon="cast", default_index=0)
    selected

if selected == 'Home':
    ft.home()
elif selected == 'Reporting':
    ft.reporting()
elif selected == 'Prediction':
    ft.prediction()