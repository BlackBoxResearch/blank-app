import requests
import streamlit as st

# API URL and Key
VPS_API_URL = "http://62.216.80.231:5000/authorize"
API_KEY = "c6decf43acaf30136719524db59d2a46a036ab1fe3e4bff73e4f9f63d9e2d920"  # Same key as defined on the Flask server

# Streamlit UI
st.title("MT5 Account Authorization")

# Inputs for login details
login = st.text_input("Login ID", value="", placeholder="Enter your Login ID")
password = st.text_input("Password", value="", placeholder="Enter your Password", type="password")
server = st.text_input("Server", value="", placeholder="Enter the Server Name")

# Button to connect
if st.button("Connect"):
    if not login or not password or not server:
        st.error("Please fill in all fields.")
    else:
        # Prepare the data payload
        payload = {
            "login": login,
            "password": password,
            "server": server
        }

        # Add the API key to the headers
        headers = {"x-api-key": API_KEY}

        try:
            # Send a POST request to the VPS Flask server
            response = requests.post(VPS_API_URL, json=payload, headers=headers)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("success"):
                st.success(f"Successfully authorized account {login} on server {server}.")
                st.write("Account Information:")
                st.json(response_data.get("account_info"))
            else:
                st.error(f"Error: {response_data.get('error')}")
        except Exception as e:
            st.error(f"Failed to connect to the VPS: {str(e)}")
