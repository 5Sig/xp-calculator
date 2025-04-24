import streamlit as st

def calculate_total_xp(current_level, wanted_level, prestige):
    return sum(
        ((level ** 1.35) * (225000 + (56250 * prestige))) / (200 ** 1.35)
        for level in range(current_level, wanted_level)
    )

st.title("XP Calculator")

current_level = st.number_input("Current Level", min_value=0, max_value=200, step=1)
wanted_level = st.number_input("Wanted Level", min_value=current_level + 1, max_value=200, step=1)
prestige = st.number_input("Prestige", min_value=0, max_value=20, step=1)
xp_per_block = st.number_input("XP per Block (optional)", min_value=0.0, step=0.1, format="%.2f")

if st.button("Calculate XP"):
    total_xp = calculate_total_xp(current_level, wanted_level, prestige)
    st.success(f"You need {total_xp:,.2f} XP to reach level {wanted_level}.")
    if xp_per_block > 0:
        blocks = total_xp / xp_per_block
        st.info(f"That's approximately {blocks:,.2f} blocks.")
