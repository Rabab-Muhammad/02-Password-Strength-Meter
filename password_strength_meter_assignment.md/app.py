# import streamlit as st

# def check_password(password):
#     score = 0
#     tips = []

#     if len(password) >= 8:  # Check Lenght
#         score += 1
#     else:
#         tips.append("Use atleast 8 characters.")

#     if any(c.isupper() for c in password): # Check Upper case
#         score += 1
#     else:
#         tips.append("Include upper letter.")

#     if any(c.islower() for c in password): # Check Lower case
#         score += 1
#     else:
#         tips.append("Include lower letter.")

#     if any(c.isdigit() for c in password): # Check Digit
#         score += 1
#     else:
#         tips.append("Add a number (0-9).")

#     if any(c in "!@#$%^&*" for c in password): # Check Special Character
#         score += 1 
#     else:
#         tips.append("Use a special character (!@#$%^&*)")
#     return score, tips


# def main():
#     st.title("Password Strength Meter")
#     password = st.text_input("Enter password", type="password")

#     if password:
#         score,tips = check_password(password)
#         if score == 5:
#             st.success("Strong Password! secure and Safe.")
#         elif score == 3 or score == 4:
#             st.warning("Moderate password! Improve It.")
#         else:
#             st.error("Weak Password! Follow These Steps:")
#         for tip in tips:
#             st.write(tip)

# main()

import streamlit as st

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:  # Check Length
        score += 1
    else:
        tips.append("🔢 Use at least 8 characters.")

    if any(c.isupper() for c in password):  # Check Upper case
        score += 1
    else:
        tips.append("🔠 Include upper letter.")

    if any(c.islower() for c in password):  # Check Lower case
        score += 1
    else:
        tips.append("🔡 Include lower letter.")

    if any(c.isdigit() for c in password):  # Check Digit
        score += 1
    else:
        tips.append("🔢 Add a number (0-9).")

    if any(c in "!@#$%^&*" for c in password):  # Check Special Character
        score += 1 
    else:
        tips.append("🔒 Use a special character (!@#$%^&*)")

    return score, tips


def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("🔑 Enter password", type="password")

    if password:
        score, tips = check_password(password)
        if score == 5:
            st.success("✅ Strong Password! Secure and Safe. 🔒")
        elif score == 3 or score == 4:
            st.warning("⚠️ Moderate password! Improve It. 🛠")
        else:
            st.error("❌ Weak Password! Follow These Steps: 📌")

        for tip in tips:
            st.write("•", tip)

main()
