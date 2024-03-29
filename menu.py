import streamlit as st

def authenticated_menu():
    # Muestra un menú de navegación para usuarios autenticados
    if st.session_state.role in ["Admin"] and st.session_state.name != '':
        st.sidebar.page_link("pages/admin_page.py", label="Mira la base de datos! 📀")
    elif st.session_state.role in ["User"] and st.session_state.name != '':
        st.sidebar.page_link("pages/user_page.py", label="Mira nuestros videos! 📹")
    elif st.session_state.role in ["Super-Admin"] and st.session_state.name != '':
        st.sidebar.page_link("pages/super_admin_page.py", label="🚷Solo para personal autorizado")

def unauthenticated_menu():
    # Muestra un menú de navegación para usuarios no autenticados
    st.sidebar.page_link("home.py", label="Iniciar sesión")

def menu():
    # Determina si un usuario está conectado o no, luego muestra el menú de navegación correcto
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
    else:
        authenticated_menu()

def menu_with_redirect():
    # Redirige a los usuarios a la página principal si no están conectados, de lo contrario, continúa para renderizar el menú de navegación
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("home.py")
    menu()
