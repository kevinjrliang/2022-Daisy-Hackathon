import re

import pandas as pd


def cleanup():
    data = pd.read_json("reddit_jokes.json")
    nono = ["fuck", "shit", "dick", "cock", "bastard", "penis", "bitch", "vagina", "pussy", "piss", "arse", " ass ",
            "bollocks", "bugger", "crap", "cunt", "effing", "frigger", "prick", "slut", "nigg", "whore",
            "retard", " tit ", " titty ", "wanker", " asshole ", " asswipe ", " nazi ", " hitler ", "fcuk", " sex",
            "fuk"]

    data_lower = data.copy()
    data_lower['body'] = data['body'].str.lower()
    data_lower['title'] = data_lower['title'].str.lower()

    almost_clean = data_lower[~data_lower["body"].str.contains('|'.join(nono))]
    clean = almost_clean[~data_lower["title"].str.contains('|'.join(nono))]

    clean.to_json("clean_reddit_jokes.json")


def frequency():
    data = pd.read_json("clean_reddit_jokes.json")
    body = data["body"]
    words = {}

    for d in body:
        split = re.split(r',.?!', d)
        print(split)
        for word in split:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            # print(word)
    df = pd.DataFrame(words)
    df.to_json("word_dict.json")


# cleanup()
frequency()
