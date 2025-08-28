import streamlit as st

# Import semua halaman
from sidebar_page import sidebar_menu
from home_page import home_page, home_after_login  
from login_page import login_page
from admin_dashboard import admin_dashboard
from manajemen_user import manajemen_user_page
from upload_page import upload_surveilans_page, upload_posbindu_page, hasil_spm_page

def main():
    # --- Inisialisasi session state ---
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "show_login" not in st.session_state:
        st.session_state.show_login = False
    if "username" not in st.session_state:
        st.session_state.username = "Guest"
    if "role" not in st.session_state:
        st.session_state.role = "user"
    if "tambah_user_mode" not in st.session_state:
        st.session_state.tambah_user_mode = False

    # --- Styling sidebar ---
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            background-color: #E3F2FD;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Kalau belum login ---
    if not st.session_state.logged_in:
        if st.session_state.show_login:
            login_page()
        else:
            home_page()

    # --- Kalau sudah login ---
    else:
        st.sidebar.markdown(
            f"👤 Login sebagai: `{st.session_state.username}` ({st.session_state.role})"
        )

        # Tentukan menu sesuai role
        menu = sidebar_menu(role=st.session_state.role)

        if menu == "Home":
            home_after_login()

        elif menu == "Dashboard":
            admin_dashboard()

        elif menu == "Unggah Surveilans":
            # ✅ kirim username
            upload_surveilans_page(st.session_state.username)

        elif menu == "Unggah Posbindu":
            # ✅ kirim username
            upload_posbindu_page(st.session_state.username)

        elif menu == "Hasil SPM":
            hasil_spm_page()

        elif menu == "Manajemen User":
            if st.session_state.role == "admin":
                manajemen_user_page()
            else:
                st.warning("⚠️ Anda tidak memiliki akses ke Manajemen User.")

        elif menu == "Logout":
            st.session_state.clear()
            st.success("✅ Berhasil logout.")
            st.rerun()


if __name__ == "__main__":
    main()