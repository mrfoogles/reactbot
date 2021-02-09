
TREE = {
    "biden": {
        "is": {
            "bad": -1,
            "good": 1
        },
        "won": 1,
        "lost": -1
    },
    "trump": {
        "won": -1,
        "lost": 1,
        "is": {
            "bad": 1,
            "good": -1,
            "poopy": 2,
            "invisible": 0,
            "banana": 43,
            "joshua": 43,
            "hacked": 43,

            "trump": 42
        }
    }
}

def syn(word,synonym,DATA):
    if word in DATA:
        DATA[word].append(synonym)
    else:
        DATA[word] = [word,synonym]
    if synonym in DATA:
        DATA[synonym].append(word)
    else:
        DATA[synonym] = [synonym,word]

def syns(word,synonyms,DATA):
    for synonym in synonyms:
        syn(word,synonym,DATA)

import json
print("loading synonyms.json...")
with open("synonyms.json") as f:
    SYNONYMS = json.loads(f.read())
print("loaded")
SYNONYMS.update({
    "trump": ["trump","Trump"],
    "biden": ["biden","Biden"],
    "good": ["good"]
})

RAGES = {
    "-1": ["Thank you!","Yourrr welcome"],
    "0": ["What.","Huh?","I don't get it.","Are you talking to me?"],
    "1": ["Shut up kid, I won the election.","SHUT UP","No, you are, retard","Hey!","Ugh."],
    "2": ["RAAAUUUUUGHGGGHGHGH"],
    "43": ["..NEXT PASSCODE REQUIRED..","ACCESS GRANTED.","WEELCOME TO APPERTURE LABSSSSS","HELLO, PROFESSOR","No I'm not"],
    
    "42": ["WELCOME TO THE MATRIX, PADAWAN."]
}

def overlap(l,l2):
    result = []
    for x in l:
        for y in l2:
            if x == y:
                result.append(x)
    return result

import random
from copy import deepcopy

def process(content):
    w = content.split(" ")
    response = ""
    i = 0

    go = True
    branch = TREE
    while go:
        if type(branch) == int:
            response = random.choice(RAGES[str(branch)])
            go = False

        elif type(branch) == str:
            response = branch
            go = False

        elif type(branch) == dict:

            if w[i] not in SYNONYMS:
                SYNONYMS[w[i]] = [w[i]]

            found = False
            for s in SYNONYMS[w[i]]:
                if s in branch:
                    branch = branch[s]
                    found = True
                    break
            i += 1

            def debug(w,at):
                debugW = deepcopy(w)
                debugW[i-1] = f"\033[1m>{debugW[i-1]}<\033[0m"
                return f"""'{" ".join(debugW)}'"""

            if type(branch) == dict and i >= len(w):
                print("Ran out of words")
                print(debug(w,i-1))
                go = False
            if not found:
                print("No path found")
                print(debug(w,i-1))
                go = False

    return response
            
if __name__ == "__main__":
    print("input a message to get a response!")
    while True:
        print(process(input("? ")))