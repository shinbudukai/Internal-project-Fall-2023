# from settings import *
# from azure import *
import os


#Access system's environment
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('WEBSITE_HOSTNAME'))


