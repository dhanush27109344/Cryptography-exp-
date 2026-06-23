import hashlib
import time
import secrets

# Simulated User Database
users = {
    "dhanush": "password123",
    "admin": "admin123"
}

# Ticket Granting Server Secret Key
TGS_SECRET = "TGS_SECRET_KEY"

# Service Server Secret Key
SERVICE_SECRET = "SERVICE_SECRET_KEY"


def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def authenticate_user(username, password):
    if username in users and users[username] == password:
        return True
    return False


def generate_ticket(username, service):
    timestamp = str(int(time.time()))
    session_key = secrets.token_hex(16)

    ticket_data = username + "|" + service + "|" + timestamp + "|" + session_key

    ticket_hash = generate_hash(ticket_data + SERVICE_SECRET)

    ticket = ticket_data + "|" + ticket_hash

    return ticket


def validate_ticket(ticket, service):
    parts = ticket.split("|")

    username = parts[0]
    ticket_service = parts[1]
    timestamp = int(parts[2])
    session_key = parts[3]
    received_hash = parts[4]

    ticket_data = username + "|" + ticket_service + "|" + str(timestamp) + "|" + session_key
    expected_hash = generate_hash(ticket_data + SERVICE_SECRET)

    current_time = int(time.time())

    # Ticket valid only for 60 seconds
    if current_time - timestamp > 60:
        return False, "Ticket expired"

    if ticket_service != service:
        return False, "Invalid service"

    if received_hash != expected_hash:
        return False, "Ticket modified"

    return True, "Ticket valid for user: " + username


# Main Program
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate_user(username, password):

    print("\nAuthentication Server: User verified.")

    service = input("Enter requested service name: ")

    ticket = generate_ticket(username, service)

    print("\nTicket Generated:")
    print(ticket)

    print("\nSending ticket to service server...")

    status, message = validate_ticket(ticket, service)

    print("\nService Server Result:")
    print(message)

else:
    print("\nAuthentication Failed: Invalid username or password.")