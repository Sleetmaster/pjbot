# 🟢 PJBOT – Asennus- ja käyttöohje

## 1. Lataa ja pura ZIP
Pura tämä paketti omalle koneellesi tai vie GitHubiin.

## 2. Streamlit Cloud -julkaisu (suositus)
- Mene: https://streamlit.io/cloud
- Kirjaudu sisään GitHub-tililläsi
- Klikkaa "New app" ja valitse tämä repo
- Main file path: pjbot_app.py

### Lisää salainen avain:
- Avaa "Advanced settings"
- Lisää:
  OPENAI_API_KEY = "sk-oma-api-avain"

## 3. Paikallinen käyttö koneella
Asenna riippuvuudet:
> pip install -r requirements.txt

Käynnistä sovellus:
> streamlit run pjbot_app.py

Sovellus avautuu selaimessa osoitteessa http://localhost:8501
