import requests

# URL to interact with
url = "http://127.0.0.1:5000/"


#sendaGETrequestthURL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract cookies from the response
    cookies = response.cookies

    # Get the value of the specific cookie 'cookie_name'
    cookie_value = cookies.get('cookie_name')

    if cookie_value:
        print(f"Cookie value for 'cookie_name': {cookie_value}")

        # Assuming the password is obtained by sending the cookie in a request
        # Send a new request with the cookie to get the password
        cookies = {'cookie_name': cookie_value}
        password_response = requests.get(url, cookies=cookies)

        if password_response.status_code == 200:
            print("Password or Request ID:")
            print(password_response.text)  # or parse if it's in JSON format
        else:
            print("Failed to get password. Status code:", password_response.status_code)
    else:
        print("'cookie_name' not found in response cookies.")
else:
    print(f"Failed to connect to the server. Status code: {response.status_code}")
