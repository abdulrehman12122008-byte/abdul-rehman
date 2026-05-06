import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Thermodynamics P-V Visualizer")

st.title("📊 P-V Diagram Generator")
st.write("Visualize thermodynamic processes for an Ideal Gas.")

# Sidebar Inputs
st.sidebar.header("Initial State Parameters")
P1 = st.sidebar.number_input("Initial Pressure (P1) [kPa]", value=100.0)
V1 = st.sidebar.number_input("Initial Volume (V1) [m³]", value=1.0)
process_type = st.sidebar.selectbox("Select Process", ["Isobaric (Const P)", "Isochoric (Const V)", "Isothermal (Const T)"])
V2 = st.sidebar.slider("Final Volume (V2)", min_value=0.1, max_value=5.0, value=2.0)

# Calculations
V_range = np.linspace(V1, V2, 100)
P_range = []

if process_type == "Isobaric (Const P)":
    P_range = [P1] * 100
    work_done = P1 * (V2 - V1)

elif process_type == "Isochoric (Const V)":
    # For plotting a vertical line, we handle V differently
    V_range = [V1] * 100
    P_range = np.linspace(P1, P1 * (V2/V1), 100) # Assuming P changes
    work_done = 0

elif process_type == "Isothermal (Const T)":
    # P*V = constant -> P = C/V
    constant = P1 * V1
    P_range = constant / V_range
    work_done = constant * np.log(V2 / V1)

# Plotting
fig, ax = plt.subplots()
ax.plot(V_range, P_range, 'r-', linewidth=2, label=process_type)
ax.set_xlabel("Volume (V) [m³]")
ax.set_ylabel("Pressure (P) [kPa]")
ax.set_title(f"P-V Diagram: {process_type}")
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display results
st.pyplot(fig)
st.metric("Work Done (W)", f"{work_done:.2f} kJ")
