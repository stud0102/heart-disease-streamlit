import streamlit as st
import pickle

# Wczytanie modelu
filename = "model.sv"
model = pickle.load(open(filename, 'rb'))

# Słowniki dla zmiennych kategorycznych
sex_d = {0: "Kobieta", 1: "Mężczyzna"}
cp_d = {0: "ASY", 1: "ATA", 2: "NAP", 3: "TA"}
resting_d = {0: "LVH", 1: "Normal", 2: "ST"}
exang_d = {0: "Nie", 1: "Tak"}
st_d = {0: "Down", 1: "Flat", 2: "Up"}

def main():
    st.set_page_config(page_title="Heart Disease Predictor")

    st.title("Heart Disease Prediction App")
   

    left, right = st.columns(2)

    with left:
        age = st.slider("Wiek", min_value=20, max_value=100, value=45)
        sex = st.radio("Płeć", options=list(sex_d.keys()), format_func=lambda x: sex_d[x])
        resting_bp = st.slider("Ciśnienie spoczynkowe (RestingBP)", 80, 200, 120)
        cholesterol = st.slider("Cholesterol", 100, 600, 200)
        fasting_bs = st.radio("Cukier na czczo > 120mg/dl", options=[0, 1], format_func=lambda x: "Tak" if x else "Nie")

    with right:
        cp = st.radio("Typ bólu w klatce piersiowej", options=list(cp_d.keys()), format_func=lambda x: cp_d[x])
        rest_ecg = st.radio("Wynik EKG spoczynkowego", options=list(resting_d.keys()), format_func=lambda x: resting_d[x])
        max_hr = st.slider("Maksymalne tętno (MaxHR)", 60, 220, 150)
        ex_ang = st.radio("Ból przy wysiłku fizycznym?", options=list(exang_d.keys()), format_func=lambda x: exang_d[x])
        oldpeak = st.slider("Oldpeak (ST depresja)", 0.0, 6.0, 1.0, step=0.1)
        slope = st.radio("Nachylenie ST", options=list(st_d.keys()), format_func=lambda x: st_d[x])

    # Dane do predykcji
    data = [[age, sex, cp, resting_bp, cholesterol, fasting_bs, rest_ecg,
             max_hr, ex_ang, oldpeak, slope]]

    prediction = model.predict(data)
    confidence = model.predict_proba(data)

    st.subheader("Czy ta osoba jest zagrożona chorobą serca?")
    st.subheader("❌ Tak" if prediction[0] == 1 else "✅ Nie")
    st.write("Pewność predykcji: {:.2f}%".format(confidence[0][prediction[0]] * 100))

if __name__ == "__main__":
    main()
