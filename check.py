from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the SBR_WEBDRIVER variable
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

if SBR_WEBDRIVER is None:
    raise ValueError("SBR_WEBDRIVER is not set. Please check your .env file.")
else:
    print(f"SBR_WEBDRIVER is set to: {SBR_WEBDRIVER}")
