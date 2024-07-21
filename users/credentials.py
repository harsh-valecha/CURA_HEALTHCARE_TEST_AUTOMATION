from dotenv import load_dotenv
import os

# Load .env file with override set to True
load_dotenv(override=True)

class UserCredentials:
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

