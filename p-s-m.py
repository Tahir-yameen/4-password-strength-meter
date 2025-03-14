import streamlit as st
import zxcvbn

st.title("Password Strength Meter")
st.write("""
    This app evaluates the strength of your password and gives suggestions for improvement.
    Use a mix of uppercase, lowercase, numbers, and special characters to make your password stronger!
""")

password = st.text_input("Enter your password", type="password")

if password:
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']

    st.write(f"Password Strength: {score}/4")

    # Visual feedback based on score
    if score == 0:
        st.markdown('<div style="color: red; font-weight: bold;">Weak password. Try to use a mix of characters, numbers, and symbols.</div>', unsafe_allow_html=True)
    elif score == 1:
        st.markdown('<div style="color: orange; font-weight: bold;">Very weak password. Consider adding more characters.</div>', unsafe_allow_html=True)
    elif score == 2:
        st.markdown('<div style="color: yellow; font-weight: bold;">Fair password. Add some complexity.</div>', unsafe_allow_html=True)
    elif score == 3:
        st.markdown('<div style="color: green; font-weight: bold;">Strong password. Well done!</div>', unsafe_allow_html=True)
    elif score == 4:
        st.markdown('<div style="color: green; font-weight: bold;">Very strong password! Great job!</div>', unsafe_allow_html=True)
    
    # Suggestions for improvement (if any)
    if feedback:
        st.write("Suggestions:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

    if password:
        result = zxcvbn.zxcvbn(password)
        score = result['score']


    # Progress bar for password strength
    st.progress(score / 4)  # Normalize score to a value between 0 and 1

