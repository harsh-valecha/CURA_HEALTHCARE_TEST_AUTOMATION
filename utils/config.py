from dotenv import load_dotenv
import os

# Load .env file with override set to True
load_dotenv(override=True)


class Config:
    BASE_URL = 'https://katalon-demo-cura.herokuapp.com/'
    LOGIN_URL = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    BROWSER = 'chrome'

    # user credentials 
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
