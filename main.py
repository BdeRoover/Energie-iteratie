import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Energieiteratie", layout="centered")

  
col1, col2, col3 = st.columns([2,1,5])

with col1:
    st.header('Input')
    Eben = st.number_input("Benodigde energie [kNm]")

    F = st.number_input("Stootkracht [kN]")
    U = st.number_input("Vervorming [mm]")
    Eopt = round( 0.5*F*(U/1000),2)

with col2:
    st.empty()
    
with col3:
    st.header('Output')
    K = round(F/(U/1000),2)
    f = round(Eopt / Eben,3)

    if Eopt < Eben:
        st.write(f"De optredende energie bedraagt :red[{Eopt}] [kNm]")
    else:
         st.write(f"De optredende energie bedraagt :green[{Eopt}] [kNm]")   
            
    # st.write("De veerwaarde bedraagt: ", K, '[kN/m]')
    
    if 1 < f < 1.02:
        st.write(f"De afwijking bedraagt :green[{f}] [-]")
    else:
        st.write(f"De afwijking bedraagt :red[{f}] [-]")
    
    Fs = round(np.sqrt(Eben/Eopt)*F,2)
    st.write(f"De nieuwe stootkracht bedraagt :black[{Fs}] [kN]")