import streamlit as st
import random
import string
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for uppercase
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., @, $, !).")

    return strength, feedback

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("Password Strength Meter")

# Password input
password_input = st.text_input("Enter your password:", type="password")

# Check password strength if input is given
if password_input:
    strength, feedback = check_password_strength(password_input)
    
    # Display strength bar
    st.progress(strength / 5)

    # Display feedback
    if strength == 5:
        st.success("Your password is strong!")
    else:
        st.warning("Your password could be improved.")
        for line in feedback:
            st.write(f"- {line}")

# Random password generator
st.title("Password Generator")

if st.button("Generate Password"):
    st.subheader("Generated Password:")
    random_password = generate_random_password()
    st.text(random_password)
