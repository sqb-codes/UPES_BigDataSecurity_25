from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("test_logs.log"),
                        logging.StreamHandler()
                    ])

logging.debug("Application Started...")

logging.debug("Roles initialized...")
roles = {
    "admin" : ["view_sensitive_data"],
    "guest" : []
}

user_roles = {
    "john" : "admin",
    "sam" : "guest"
}

credit_card = "9898-8882-8211"

def access_data(username):
    logging.warning(f"User : {username} tried to access data")
    role = user_roles.get(username)
    if role and 'view_sensitive_data' in roles[role]:
        print(f"User : {username} can access data")
        logging.info(f"Data accessed successfully by {username}")
    else:
        logging.error(f"Unauthorized user : {username} tried to access data")
        print("Unauthorized access")
        log_unauthorized_access(username)


def log_unauthorized_access(username):
    with open("access_logs.txt", "a") as file:
        file.write(f"\n{datetime.now()} : Unauthorized access attempt by {username}")

access_data("john")
access_data("sam")