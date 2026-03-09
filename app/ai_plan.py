import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_study_plan(topics, ability):

    prompt = f"""
    A student finished an adaptive test.

    Weak topics: {topics}
    Ability score: {ability}

    Generate a simple 3-step study plan to improve the student's weaknesses.
    """

    response = model.generate_content(prompt)

    return response.text