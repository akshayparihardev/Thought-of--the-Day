import random
import re

# Read all thoughts from thoughts.txt
with open("thoughts.txt", "r", encoding="utf-8") as f:
    thoughts = [line.strip() for line in f if line.strip()]

# Pick a random thought
thought = random.choice(thoughts)

# Read current README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the thought section
pattern = r'<!-- thought starts -->(.*?)<!-- thought ends -->'
replacement = f'<!-- thought starts -->\n{thought}\n<!-- thought ends -->'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
