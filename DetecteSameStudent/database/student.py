class Student:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nUsername: {self.username}\nEmail: {self.email}"
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.name, self.username, self.email) == (other.name, other.username, other.email)
        return False

    def __hash__(self):
        return hash((self.name, self.username, self.email))
