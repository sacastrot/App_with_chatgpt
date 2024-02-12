# Importar la librería Streamlit
import streamlit as st

# Título de la app y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por COLOQUE AQUÍ SU NOMBRE")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, introduce tu nombre")

# Imprimir el mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
