import datetime
import random

# List of thoughts (you can expand this significantly!)
thoughts = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    # ... (rest of the thoughts list) ...
]

def get_random_thought():
    return random.choice(thoughts)

def update_readme():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    thought_of_the_day = get_random_thought()

    new_content = f"# Daily Thought and Green Graph!\n\n"
    new_content += f"**Date:** {current_date}\n\n"
    new_content += f"**Thought of the Day:**\n> {thought_of_the_day}\n\n"
    new_content += f"This repository is updated daily to keep my GitHub contributions graph green!"

    with open("README.md", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
    print("README.md updated with new thought!")

