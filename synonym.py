
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


if __name__ == "__main__":
    import json
    import os
    DATA = {}

    save="synonyms.json"
    print(f"Will write data to {save} once terminated")
    if os.path.exists(save):
        f = open(save,mode="r")
        DATA.update(json.loads(f.read()))
    else:
        f = open("synonyms.json",mode="w+")
    
    print("Type 'q' to save the data and close the program.")

    while True:
        print("Synonyms for: ",end="")
        word = input().strip()
        if word == "q":
            print("Saving and quitting...")
            print(json.dumps(DATA))
            f.write(json.dumps(DATA))
            f.close()
            quit()

        print("are: ",end="")
        synonyms = input().replace(" ","").split(",")

        syns(word,synonyms,DATA)
    