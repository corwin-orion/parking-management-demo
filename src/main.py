import sha256_hash
import json
import Interface
import User
import atexit

users = []

# On program exit, save data to a file
def exit_handler():
    if len(users) != 0:
        json_data = json.dumps(users)
        with open('data_list.json', 'w') as file:
            file.write(json_data)

if __name__ == "__main__":
    # On startup, retrieve list of users
    with open('users.json', 'r') as file:
        json_data = file.read()
    users = json.loads(json_data)

    # If no users, initialize an admin with password 1234 to enable setup
    if len(users) == 0:
        users = [User("Admin", sha256_hash(password="1234"), "Admin")]

    json_data = json.dumps(users.__dict__)

    # Register exit_handler() to save  on program exit
    atexit.register(exit_handler)

    # Save to a file or transmit over a network
    with open('person_data.json', 'w') as file:
        file.write(json_data)

    interface = Interface()
