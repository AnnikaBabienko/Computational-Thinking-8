import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial","apple", "brand", "clamp",
              "drain", "eagle", "flame", "grape", "haste", "ideal", "jolly", "knack",
                "liver", "mirth", "night", "opal", "pearl", "quilt", "rose",
                  "salt", "tiger", "vivid", "wager", "xenon", "yacht", "zebra",
                    "abide", "bison", "candy", "dance", "echo", "fire", "goose",
                      "harm", "idle", "join", "kite", "lime", "move", "neon", "open",
                        "pure", "quest", "rush", "swoop", "tree", "urge", "vent", "warp",
                          "year", "zoom", "adore", "blaze", "charm", "done", "ember", "flex",
                            "grip", "hype", "iron", "joke", "knee", "loud", "mine", "nude", "pave",
                              "quiet", "rest", "sore", "turn", "undo", "vibe", "weave", "xray", "yarn", "about",
                                "brace", "cliff", "doubt", "echoes", "fable", "gloom", "hinty", "imply", "jumpy",
                                  "kindy", "latch", "messy", "nesty", "only", "purely", "quick", "riot", "silly", "thump",
                                    "usher", "vowel", "wrist", "yanks", "zesty", "acids", "billy", "cages", "darts", "edge",
                                      "faint", "gleam", "hairy", "kicks", "leash", "messy", "noble", "open", "peppy", "qatar", 
                                      "rainy", "seats", "tango", "upset", "vigor", "wait", "yearn", "zone", "area", "beast", "copse",
                                        "flick", "glare", "holt", "iris", "jacks", "lovely", "menge", "queen", "rave", "snowy", "tune", 
                                        "unity", "waves", "zonal", "acts", "brims", "caged", "dopes", "elfed",]
hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    if len(guess_word) > 5:
        print("Pick a five letter word")

    if len(guess_word) < 5:
        print("Pick a five letter word")

# First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
# Second letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
# Third letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

# Fifth letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
     

# Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break
print(f"The word was {hidden_word}")
print(f"You used {i+1} guesses")