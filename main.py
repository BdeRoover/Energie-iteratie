import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Energieiteratie",
    layout="centered"
    )

col1, col2, col3 = st.columns([1,1,2])

with col1:    
    st.header('Input')
    Eben = st.number_input("Benodigde energie [kNm]", min_value=1.00)    
    F = st.number_input("Stootkracht [kN]", min_value=10.00)
    U = st.number_input("Vervorming [mm]", min_value=10.00)
    Eopt = round(0.5*F*(U/1000),2)

with col2:
    st.empty()
    
with col3:
    st.header('Output')
    K = round(F/(U/1000),2)
    f = round(Eopt / Eben,3)

    if Eopt < Eben:
        st.write(f"De optredende energie bedraagt 0.5 x {F} x {U/1000} = :red[{Eopt}] [kNm]")
    else:
         st.write(f"De optredende energie bedraagt 0.5 x {F} x {U/1000} = :green[{Eopt}] [kNm]")   
            
    # st.write("De veerwaarde bedraagt: ", K, '[kN/m]')
    
    if 1 < f < 1.02:
        st.write(f"De afwijking bedraagt {Eopt}/{Eben} = :green[{f}] [-]")
    else:
        st.write(f"De afwijking bedraagt {Eopt}/{Eben} = :red[{f}] [-]")
    
    Fs = round(np.sqrt(Eben/Eopt)*F,2)
    st.write(f"De nieuwe stootkracht bedraagt \u221A({Eben}/{Eopt}) x {F} =  :black[{Fs}] [kN]")