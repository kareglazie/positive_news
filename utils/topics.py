import random 

RANDOM_TOPICS = [
    "technology innovation", "scientific discovery", "medical breakthrough",
    "environmental success", "education progress", "space exploration",
    "community heroes", "animal rescue", "renewable energy",
    "cultural celebration", "economic growth", "peace agreement"
]

def generate_random_topic():
    return random.choice(RANDOM_TOPICS)
