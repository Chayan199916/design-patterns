class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.phone = None
        self.address = None

    def __str__(self):
        return f"UserProfile({self.username}, {self.email}, {self.phone}, {self.address})"


class UserProfileBuilder:
    def __init__(self, username, email):
        self.profile = UserProfile(username, email)

    def set_phone(self, phone):
        self.profile.phone = phone
        return self

    def set_address(self, address):
        self.profile.address = address
        return self

    def build(self):
        return self.profile


# Client code
if __name__ == "__main__":
    user_builder = UserProfileBuilder("john_doe", "john@example.com")
    user = user_builder.set_phone(
        "123-456-7890").set_address("123 Main St").build()

    print(user)
