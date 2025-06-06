import datetime
import random

# List of thoughts (you can expand this significantly!)
thoughts = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The mind is everything. What you think you become. - Buddha",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "It always seems impossible until it's done. - Nelson Mandela",
    "The journey of a thousand miles begins with a single step. - Lao Tzu",
    "What you give is what you get. - Iris Murdoch",
    "We can only learn to love by loving. - Karen Clark",
    "Life is change. Growth is optional. Choose wisely. - Wayne Dyer",
    "You'll see it when you believe it. - Wayne Dyer",
    "Today is the tomorrow we worried about yesterday. - Anonymous",
    "It's easier to see the mistakes on someone else's paper. - Anonymous",
    "Every man dies. Not every man really lives. - Lao Tzu",
    "To lead people walk behind them. - William Shakespeare",
    "Having nothing, nothing can he lose. - Henry J. Kaiser",
    "Trouble is only opportunity in work clothes. - Publilius Syrus",
    "A rolling stone gathers no moss. - Publilius Syrus",
    "The day is already blessed, find peace within it. - Sigmund Freud",
    "From error to error one discovers the entire truth. - Benjamin Franklin",
    "Well done is better than well said. - Benjamin Franklin",
    "Bite off more than you can chew, then chew it. - Buddha",
    "Work out your own salvation. Do not depend on others. - Buddha",
    "One today is worth two tomorrows. - Benjamin Franklin",
    "Once you choose hope, anything's possible. - Christopher Reeve",
    "God always takes the simplest way. - Albert Einstein",
    "One fails forward toward success. - Charles Kettering",
    "From small beginnings come great things. - Chinese Proverb",
    "Learning is a treasure that will follow its owner everywhere. - Chinese Proverb",
    "Who sows virtue reaps honour. - Dalai Lama",
    "Be kind whenever possible. It is always possible. - Dalai Lama",
    "Talk doesn't cook rice. - Chinese Proverb",
    "He is able who thinks he is able. - Larry Elder",
    "A goal without a plan is just a wish. - Antoine de Saint-Exupéry",
    "To succeed, we must first believe that we can. - Michael Korda",
    "Real magic in relationships means an absence of judgment of others. - Albert Einstein",
    "I never think of the future. It comes soon enough. - Ralph Waldo Emerson",
    "Skill to do comes of doing. - Sophocles",
    "Wisdom is the supreme part of happiness. - Sophocles",
    "I believe that every person is born with talent. - Maya Angelou",
    "Great talent finds happiness in execution. - Michelangelo",
    "Faith in oneself is the best and safest course. - Winston Churchill",
    "Courage is going from failure to failure without losing enthusiasm. - Winston Churchill",
    "The two most powerful warriors are patience and time. - Leo Tolstoy",
    "Anticipate the difficult by managing the easy. - Lao Tzu",
    "Those who are free of resentful thoughts surely find peace. - Buddha",
    "A short saying often contains much wisdom. - Sophocles",
    "It takes both sunshine and rain to make a rainbow. - Anonymous",
    "A beautiful thing is never perfect. - Princess Diana",
    "Only do what your heart tells you. - John Pierrakos",
    "Life is movement-we breathe, we eat, we walk, we move! - Anonymous",
    "Love all, trust a few, do wrong to none. - William Shakespeare",
    "In order to win, you must expect to win. - Richard Bach",
    "A goal is a dream with a deadline. - Napoleon Hill",
    "You can do it if you believe you can! - Bo Jackson",
    "Set your goals high, and don't stop till you get there. - Bo Jackson",
    "Every new day is another chance to change your life. - Thich Nhat Hanh",
    "Smile, breathe, and go slowly. - Liberace",
    "Nobody will believe in you unless you believe in yourself. - William Arthur Ward",
    "Do more than dream: work. - Seneca",
    "No man was ever wise by chance. - Seneca",
    "Some pursue happiness, others create it. - Anonymous",
    "He that is giddy thinks the world turns round. - William Shakespeare",
    "Who looks outside, dreams; who looks inside, awakes. - Carl Jung",
    "What we think, we become. - Buddha",
    "The shortest answer is doing. - Leonardo da Vinci",
    "All our knowledge has its origins in our perceptions. - Leonardo da Vinci",
    "The harder you fall, the higher you bounce. - Anne Wilson Schaef",
    "Trusting our intuition often saves us from disaster. - Sojourner Truth",
    "You can't stop the waves, but you can learn to surf. - Jon Kabat-Zinn",
    "Reality does not conform to the ideal, but confirms it. - Gustave Flaubert",
    "Speak low, if you speak love. - William Shakespeare",
    "A really great talent finds its happiness in execution. - Johann Wolfgang von Goethe",
    "Reality leaves a lot to the imagination. - John Lennon",
    "The greatest remedy for anger is delay. - Seneca",
    "Growth itself contains the germ of happiness. - Pearl Buck",
    "You can do what's reasonable or you can decide what's possible. - Leonardo da Vinci",
    "Nothing strengthens authority so much as silence. - Confucius",
    "Wherever you go, go with all your heart. - Confucius",
]

def get_random_thought():
    return random.choice(thoughts)

def update_readme():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    thought_of_the_day = get_random_thought()

    # --- START OF MODIFIED CONTENT ---
    new_content = f"# Daily Thought\n" # Changed header
    new_content += f"**Date:** {current_date}\n\n"
    new_content += f"**Thought of the Day:**\n> {thought_of_the_day}\n\n"
    new_content += f"# Thank You !\n" # Added Thank You
    new_content += f"# Have a Nice Day !\n" # Added Have a Nice Day
    # --- END OF MODIFIED CONTENT ---

    with open("README.md", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
    print("README.md updated with new thought!")

