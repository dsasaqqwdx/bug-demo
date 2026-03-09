def login(username, password):

    # BUG: password can be None
    if password == "":
        return "Password cannot be empty"

    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid credentials"


# test
print(login("admin", None))
