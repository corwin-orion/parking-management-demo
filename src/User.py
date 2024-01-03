class User:
    def __init__(self, name, passwordHash, role):
        self.name = name
        self.passwordHash = passwordHash
        self.role = role # "Customer", "Steward", or "Admin"
        vehicles = []
        history = []