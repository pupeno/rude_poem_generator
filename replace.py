import random

import requests

swear = {
    "anal": {
        "Adjective"
    },
    "anus": {
        "Noun"
    },
    "arse": {
        "Verb",
        "Noun"
    },
    "ass": {
        "Noun"
    },
    "balls": {
        "Verb",
        "Noun"
    },
    "bastard": {
        "Noun",
        "Adjective"
    },
    "bitch": {
        "Verb",
        "Noun"
    },
    "biatch": {
        "Noun"
    },
    "bloody": {
        "Verb",
        "Adjective"
    },
    "bollock": {
        "Verb"
    },
    "boner": {
        "Noun"
    },
    "boob": {
        "Verb",
        "Noun"
    },
    "bum": {
        "Verb",
        "Noun",
        "Adjective"
    },
    "butt": {
        "Verb",
        "Noun"
    },
    "clitoris": {
        "Noun"
    },
    "cock": {
        "Verb",
        "Noun"
    },
    "crap": {
        "Verb",
        "Noun",
        "Adjective"
    },
    "cunt": {
        "Noun"
    },
    "damn": {
        "Verb",
        "Adjective"
    },
    "dick": {
        "Verb",
        "Noun"
    },
    "dildo": {
        "Noun"
    },
    "feck": {
        "Interjection"
    },
    "fellate": {
        "Verb"
    },
    "fellatio": {
        "Noun"
    },
    "fuck": {
        "Verb",
        "Noun"
    },
    "flange": {
        "Noun"
    },
    "hell": {
        "Noun"
    },
    "jerk": {
        "Verb",
        "Noun"
    },
    "jizz": {
        "Verb",
        "Noun"
    },
    "labia": {
        "Noun"
    },
    "muff": {
        "Verb",
        "Noun"
    },
    "penis": {
        "Noun"
    },
    "piss": {
        "Verb",
        "Noun"
    },
    "poop": {
        "Verb",
        "Noun"
    },
    "prick": {
        "Verb",
        "Noun"
    },
    "pube": {
        "Noun"
    },
    "pussy": {
        "Noun"
    },
    "scrotum": {
        "Noun"
    },
    "sex": {
        "Verb",
        "Noun"
    },
    "shit": {
        "Verb",
        "Noun"
    },
    "slut": {
        "Noun"
    },
    "smegma": {
        "Noun"
    },
    "spunk": {
        "Noun"
    },
    "tit": {
        "Noun"
    },
    "tosser": {
        "Noun"
    },
    "turd": {
        "Noun"
    },
    "twat": {
        "Verb",
        "Noun"
    },
    "vagina": {
        "Noun"
    },
    "wank": {
        "Verb",
        "Noun"
    }
}


def get_le(word):
    app_id = 'db9114f7'
    app_key = '1b9da04c2b43c0477d58030dba5a8ed6'
    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    json = r.json()
    s = set()
    for item in json["results"]:
        for le in item["lexicalEntries"]:
            s.add(le["lexicalCategory"])
    return s


def replacement(word):
    s = get_le(word)

    while True:
        sw = random.choice(list(swear.keys()))
        if s.intersection(swear[sw]):
            return sw
