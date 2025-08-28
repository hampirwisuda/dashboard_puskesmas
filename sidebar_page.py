import streamlit as st

def sidebar_menu(role="user"):
    if role == "admin":
        menu = [
            "Home",
            "Dashboard"
        ]
    else:  # role user biasa
        menu = [
            "Home",
            "Unggah Surveilans",
            "Unggah Posbindu",
            "Hasil SPM",
            "Logout"
        ]

    choice = st.sidebar.radio("", menu)
    return choice