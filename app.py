
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Bragg Law Simulator", layout="wide")

st.title("🔬 محاكي قانون براج والحيود السيني")
st.write("غيّري المسافة بين المستويات البلورية وشاهدي تغير زاوية الحيود.")

wavelength = st.slider("الطول الموجي λ (Å)", 0.5, 2.5, 1.5406, 0.0001)
d = st.slider("المسافة بين المستويات d (Å)", 1.0, 5.0, 2.0, 0.01)
n = st.selectbox("رتبة الحيود n", [1, 2, 3])

ratio = n * wavelength / (2 * d)

if ratio <= 1:
    theta = np.degrees(np.arcsin(ratio))
    st.metric("زاوية براج θ", f"{theta:.2f}°")
    st.metric("زاوية القمة 2θ", f"{2*theta:.2f}°")

    angles = np.linspace(0, 150, 2000)
    peak = np.exp(-0.5 * ((angles - 2*theta) / 1.0)**2)

    fig, ax = plt.subplots()
    ax.plot(angles, peak)
    ax.set_xlabel("Diffraction angle 2θ (degrees)")
    ax.set_ylabel("Illustrative intensity")
    ax.set_title("Bragg diffraction peak")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("لا يوجد حل لهذه القيم. زيدي d أو قللي λ أو رتبة الحيود.")
