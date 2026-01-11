import random
easy_words=[
    "happy", "run", "big", "eat", "fast", "good", "cold", "clean", "near", "play",
"sad", "sleep", "small", "hot", "slow", "bad", "old", "new", "far", "kind"
]
medium_words=[
        "analyze", "develop", "challenge", "remarkable", "imagine", "efficient", "achieve", "persuade", 
        "complex", "consider","creative", "observe", "inspire",
"strategy", "confident", "increase", "transform", "curious", "solution", "decision"
]
difficult_words=[
   "ambitious", "curious", "persistent", "creative", "strategic", "analytical", "innovative", "observant", 
   "persuasive", "confident", "adaptable", "insightful", "organized", "reflective", "dedicated", 
"thoughtful", "resourceful","pragmatic", "motivated", "decisive"
]
while True:
    user_input=input("Enter the difficulty level (easy/medium/difficult)").strip().lower()
    if user_input=="easy":
        secret=random.choice(easy_words)
        break
    elif user_input=="medium":
        secret=random.choice(medium_words)
        break
    elif user_input=="difficult":
        secret=random.choice(difficult_words)
        break
    else: 
        print("invalid choice!. Please enter (easy/medium/difficult)")
        continue
attempt=0
print(f"\nGuess the secret password! (It has {len(secret)} letters)")
while True:
    guess=input("enter your guess").lower()
    attempt+=1

    if guess==secret:
        print (f"congratulation you have guessed it right in {attempt} attempts")
        break
    hint="" 
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint",hint)
print("game over")

