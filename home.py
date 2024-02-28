import streamlit as st
from menu import menu

st.set_page_config(
   page_title="AIEmpodera app",
   page_icon="🤖",
   layout="wide",
   initial_sidebar_state="expanded",
)

#   FUNCIONES
def confirmation():
    if st.session_state.name is not None:
        if st.session_state.password == "AIEmpodera":
            databaseUsers.append(st.session_state.name)
            st.write("Welcome, ", st.session_state.name, "!👋")
            print(databaseUsers)
        else :
            st.warning("Coloca una contraseña valida o un rol valido - ej: User")
    else:
        st.warning("Coloca tu nombre, no seas vago")

def set_role():
    # Función de devolución de llamada para guardar la selección de rol en el estado de la sesión
    st.session_state.role = st.session_state._role

# Inicializa st.session_state.role a None si "role" no está en st.session_state
if "role" not in st.session_state:
    st.session_state.role = None

# Recupera el rol del estado de la sesión para inicializar el widget
st.session_state._role = st.session_state.role

# Declaration of variables
databaseUsers = []

# introduction
st.title("Welcome to the new database of AIEmpodera! 👋")
st.write("Download the files you want to update")
st.write("\n")
st.write("First enter your name and password to verify you 👇")

# Confirmation methods
st.text_input("Your name", key='name')
st.text_input("Your password", key='password', type='password')
st.text_input("Ingresa tu rol:", key="_role", on_change=set_role,)

st.button("Sign Up", key='sign_button', on_click=confirmation)

# ¡Renderiza el menú dinámico!
menu()
