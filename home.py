import streamlit as st
from menu import menu

st.set_page_config(
   page_title="AIEmpodera app",
   page_icon="🤖",
   layout="wide",
   initial_sidebar_state="expanded",
)

# Inicializa st.session
if "role" not in st.session_state:
    st.session_state.role = None

if "selectRole" not in st.session_state:
    st.session_state.selectRole = None

#   FUNCIONES
def confirmation():
    if st.session_state.name != '' and st.session_state.password == "AIEmpodera":
        selected_role_index = st.session_state.selectRole
        if selected_role_index is not None:
            set_role(roles[selected_role_index])
    elif st.session_state.password != "AIEmpodera":
        st.warning("Place the correct pasword")
    else:
        st.warning("Put your name, don't be lazy")

def set_role(role):
    # Función de devolución de llamada para guardar la selección de rol en el estado de la sesión
    st.session_state.role = role

# Recupera el rol del estado de la sesión para inicializar el widget
st.session_state._role = st.session_state.role

# Declaration of variables
roles = ['User', 'Admin', 'Super-Admin']

# introduction
st.title("Welcome to the new database of AIEmpodera! 👋")
st.write("\n")
st.write("First enter your name and password to verify you 👇")

# Confirmation methods
st.text_input("Your name", key='name')
st.text_input("Your password", key='password', type='password')
selected_role_index = st.selectbox("Choose your role", range(len(roles)), format_f