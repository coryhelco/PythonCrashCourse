class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize attributes to describe a car."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login attempts."""
        self.login_attempts += 1
        print(f"{self.username} has attempted to login {self.login_attempts} times.")
    
    def reset_login_attempts(self):
        """Reset the value of login attempts."""
        self.login_attempts = 0
        print(f"{self.username} has reset their login attempts.")
        print(f"{self.username} has attempted to login {self.login_attempts} times.")

class Privileges:
    """A simple attempt to model the privileges of an admin user."""
    
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """Initialize the privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the admin user."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A simple attempt to model an admin user."""
    
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, email, location, username)
        self.privileges = Privileges()

user_01 = User('john', 'doe', 'johndoe', 'jdoe@gmail.com', 'new york')

user_01.describe_user()
user_01.greet_user()

user_02 = User('jane', 'doe', 'janedoe', 'janedoe@gmail.com', 'los angeles')
user_03 = User('jane', 'smith', 'janesmith', 'janesmith@gmail.com', 'Salt Lake City')

user_02.describe_user()
user_02.greet_user()

user_03.describe_user()
user_03.greet_user()

for _ in range(10):
    user_01.increment_login_attempts()

user_01.reset_login_attempts()

admin01 = Admin('admin', 'admin', 'admin', 'admin@gmail.com', 'New York')
print(f"\n{admin01.username} has the following privileges:")
admin01.privileges.show_privileges()