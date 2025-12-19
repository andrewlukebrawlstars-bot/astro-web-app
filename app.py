import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Astronomie", page_icon="🌌")

st.title("🌌 Aplicație Web de Astronomie")

st.sidebar.header("Meniu")
optiune = st.sidebar.selectbox(
    "Alege funcția",
    (
        "Distanță unghiulară",
        "Legea a III-a a lui Kepler",
        "Forță gravitațională",
        "Simulare orbită"
        "Calcule suplimentare"
    )
)

# ------------------------------
if optiune == "Distanță unghiulară":
    st.header("⭐ Distanță unghiulară între două stele")

    ra1 = st.number_input("RA1 (grade)")
    dec1 = st.number_input("DEC1 (grade)")
    ra2 = st.number_input("RA2 (grade)")
    dec2 = st.number_input("DEC2 (grade)")

    if st.button("Calculează"):
        ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
        cos_d = (math.sin(dec1)*math.sin(dec2) +
                 math.cos(dec1)*math.cos(dec2)*math.cos(ra1 - ra2))
        d = math.degrees(math.acos(cos_d))
        st.success(f"Distanța unghiulară: {d:.4f}°")

# ------------------------------
elif optiune == "Legea a III-a a lui Kepler":
    st.header("🪐 Legea a III-a a lui Kepler")

    a = st.number_input("Semiaxa mare a (UA)", min_value=0.0)

    if st.button("Calculează perioada"):
        a_m = a * 1.496e11
        G = 6.674e-11
        M = 1.989e30

        T = 2 * math.pi * math.sqrt(a_m**3 / (G * M))
        T_ani = T / (60*60*24*365)

        st.success(f"Perioada orbitală: {T_ani:.3f} ani")

# ------------------------------
elif optiune == "Forță gravitațională":
    st.header("🌍 Forță gravitațională")

    m1 = st.number_input("Masa 1 (kg)", min_value=0.0)
    m2 = st.number_input("Masa 2 (kg)", min_value=0.0)
    r = st.number_input("Distanța (m)", min_value=0.0)

    if st.button("Calculează forța"):
        G = 6.674e-11
        F = G * m1 * m2 / r**2
        st.success(f"Forța: {F:.3e} N")

# ------------------------------
elif optiune == "Simulare orbită":
    st.header("📈 Orbită circulară")

    r = st.number_input("Raza orbitei (UA)", min_value=0.0)

    if st.button("Desenează"):
        t = np.linspace(0, 2*math.pi, 500)
        x = r * np.cos(t)
        y = r * np.sin(t)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.scatter(0, 0)
        ax.set_aspect("equal")
        ax.set_xlabel("x (UA)")
        ax.set_ylabel("y (UA)")
        ax.set_title("Orbită planetară")

        st.pyplot(fig)
elif optiune == "Calculuri suplimentare":
    st.header("⚡ Calculuri suplimentare")

    st.subheader("1️⃣ Viteza orbitală")
    G = 6.674e-11
    M = st.number_input("Masa corpului central (kg)", min_value=0.0, value=1.989e30)
    r = st.number_input("Raza orbitei (m)", min_value=0.0, value=1.496e11)

    if st.button("Calculează viteza orbitală"):
        v = (G * M / r) ** 0.5
        st.success(f"Viteza orbitală: {v:.2f} m/s")

    st.subheader("2️⃣ Timp pentru unghi parcurs")
    T = st.number_input("Perioada orbitală (s)", min_value=0.0, value=3.154e7)
    theta = st.number_input("Unghi parcurs (grade)", min_value=0.0, max_value=360.0, value=90.0)

    if st.button("Calculează timp parțial"):
        t_parțial = theta / 360 * T
        st.success(f"Timpul pentru {theta}°: {t_parțial:.2f} s")

    st.subheader("3️⃣ Forță gravitațională între mai multe corpuri")
    st.markdown("Introduceți două mase și distanța dintre ele:")

    m1 = st.number_input("Masa 1 (kg)", min_value=0.0, value=5.972e24)
    m2 = st.number_input("Masa 2 (kg)", min_value=0.0, value=7.348e22)
    r_force = st.number_input("Distanța (m)", min_value=0.0, value=3.844e8)

    if st.button("Calculează forța"):
        F = G * m1 * m2 / r_force**2
        st.success(f"Forța gravitațională: {F:.3e} N")




