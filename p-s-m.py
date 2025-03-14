import streamlit as st
from zxcvbn import zxcvbn  # Ensure correct import

st.title("Password Strength Meter")
st.write("""
    This app evaluates the strength of your password and gives suggestions for improvement.
    Use a mix of uppercase, lowercase, numbers, and special characters to make your password stronger!
""")

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    result = zxcvbn(password)  # Corrected function call
    score = result['score']
    feedback = result['feedback'].get('suggestions', [])  # Avoid KeyError if suggestions are missing

    st.write(f"Password Strength: {score}/4")

    # Visual feedback based on score
    color_map = {0: "red", 1: "orange", 2: "yellow", 3: "green", 4: "green"}
    messages = {
        0: "Weak password. Try to use a mix of characters, numbers, and symbols.",
        1: "Very weak password. Consider adding more characters.",
        2: "Fair password. Add some complexity.",
        3: "Strong password. Well done!",
        4: "Very strong password! Great job!",
    }

    st.markdown(
        f'<div style="color: {color_map[score]}; font-weight: bold;">{messages[score]}</div>',
        unsafe_allow_html=True
    )

    # Suggestions for improvement
    if feedback:
        st.write("Suggestions:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

    # Progress bar for password strength (normalized to 0-1 range)
    st.progress(score / 4)
