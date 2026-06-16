import random

# -------------------------------
# STEP 1: Training Text
# -------------------------------
text = """
Artificial Intelligence is transforming the world.
Machine learning helps computers learn from data.
Python is widely used in AI development.
AI systems can predict and analyze patterns.
Deep learning is a part of machine learning.
Neural networks power advanced AI systems.
"""

# -------------------------------
# STEP 2: Tokenize words
# -------------------------------
words = text.split()

# -------------------------------
# STEP 3: Build BIGRAM model (advanced Markov)
# -------------------------------
bigram_model = {}

for i in range(len(words) - 2):
    key = (words[i], words[i + 1])   # two-word state
    next_word = words[i + 2]

    if key not in bigram_model:
        bigram_model[key] = []

    bigram_model[key].append(next_word)

# -------------------------------
# STEP 4: Generate text
# -------------------------------
def generate_text(length=30):
    # start with random pair
    key = random.choice(list(bigram_model.keys()))
    result = [key[0], key[1]]

    for _ in range(length):
        if key in bigram_model:
            next_word = random.choice(bigram_model[key])
            result.append(next_word)
            key = (key[1], next_word)
        else:
            break

    return " ".join(result)

# -------------------------------
# STEP 5: Output
# -------------------------------
print("\n=== ADVANCED AI TEXT GENERATION (BIGRAM MODEL) ===\n")
print(generate_text(40))