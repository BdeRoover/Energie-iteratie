import streamlit as st
import numpy as np
import os

st.set_page_config(
    page_title="Energieiteratie",
    layout="wide"
    )

col1, col2, col3 = st.columns([1,1,4])

with col1:    
    st.header('Input')
    Eben = round(st.number_input("Benodigde energie [kNm]", min_value=1.00, step=0.05),2)
    F = round(st.number_input("Stootkracht [kN]", min_value=10.00, step=0.05),2)
    U = round(st.number_input("Vervorming [mm]", min_value=10.00, step=0.05),2)
    Eopt = round(0.5*F*(U/1000),2)

with col2:
    st.empty()
    
with col3:
    st.header('Output')
    K = round(F/(U/1000),2)
    f = round(Eopt / Eben,3)

    if Eopt < Eben:
        st.write(f"De optredende energie bedraagt 0.5 x {F}[kN] x {round(U/1000,4)}[m] = :red[{Eopt}] [kNm]")
    else:
         st.write(f"De optredende energie bedraagt 0.5 x {F}[kN] x {round(U/1000,4)}[m] = :green[{Eopt}] [kNm]")   
    
    Fs = round(np.sqrt(Eben/Eopt)*F,2)
    
    if 1 <= f <= 1.02:
        st.empty()
        st.write(f"De afwijking bedraagt {Eopt}[kNm]/{Eben}[kNm] = :green[{f}] [-]")
        st.write('De gekozen stootkracht is juist')        
    else:
        st.write(f"De afwijking bedraagt {Eopt}[kNm]/{Eben}[kNm] = :red[{f}] [-]")
        st.write(f"De nieuwe stootkracht bedraagt \u221A({Eben}[kNm]/{Eopt}[kNm]) x {F}[kN] = {Fs} [kN]")

    def addToClipBoard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

    copy = addToClipBoard(str(Fs))
    
    st.button('Kopieer stootkracht', on_click=copy)