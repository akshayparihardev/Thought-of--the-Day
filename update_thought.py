import requests
from bs4 import BeautifulSoup

url = "https://example.com/daily-thought"  # Replace with actual URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract the thought from a specific HTML element
thought = soup.find('div', class_='thought').get_text(strip=True)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# Thought of the Day\n\n{thought}\n")

