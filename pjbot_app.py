import streamlit as st
import openai
import os
from fpdf import FPDF

# API-avain
openai.api_key = os.getenv("OPENAI_API_KEY")

# UI-asetukset
st.set_page_config(page_title="PJBOT", layout="wide")

# Game Boy -ulkoasu
st.markdown('<style>body { background-color: #C4D6B0; color: #333; font-family: monospace; }</style>', unsafe_allow_html=True)

# Pyrio-hahmo
st.image("assets/pyrio.png", width=100, caption="Pyrio sanoo: Tsekkaa nämä!")

# Aihelista (esimerkkejä)
aiheet = [
    {"otsikko": "Nuoret ja tekoäly", "kuvaus": "AI kiinnostaa nuoria enemmän kuin koskaan."},
    {"otsikko": "TikTok-trendit kouluissa", "kuvaus": "Nopeasti leviävä someilmiö."},
    {"otsikko": "Mikroasuminen", "kuvaus": "Minimalismi kiinnostaa suurkaupungeissa."}
]

# Tallennus
valitut = []

st.title("📋 PJBOT – Ajankohtaiset aiheet")
for i, a in enumerate(aiheet, 1):
    st.markdown(f"### {i}. {a['otsikko']}")
    st.write(a["kuvaus"])
    if st.button(f"💾 Tallenna aihe {i}", key=f"btn_{i}"):
        valitut.append(a)

# Näytetään tallennetut ja PDF-vienti
if valitut:
    st.subheader("✅ Tallennetut aiheet")
    for v in valitut:
        st.markdown(f"- {v['otsikko']}")
    if st.button("📄 Lataa PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="PJBOT – Tallennetut aiheet", ln=True)
        for i, a in enumerate(valitut, 1):
            pdf.cell(200, 10, txt=f"{i}. {a['otsikko']} - {a['kuvaus']}", ln=True)
        pdf_path = "/mnt/data/pjbot_aiheet.pdf"
        pdf.output(pdf_path)
        with open(pdf_path, "rb") as f:
            st.download_button("Lataa PDF-tiedosto", f, file_name="pjbot_aiheet.pdf")
