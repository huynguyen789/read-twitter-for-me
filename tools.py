import openai
from IPython.display import Markdown
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key  = os.getenv('OPENAI_API_KEY')


