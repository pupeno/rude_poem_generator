from typing import List
import pyphen
import pronouncing
import re
import praw
import random
import requests


class PoemFetcher:
    poems = None

    def fetch_poems(self):
        reddit = praw.Reddit(
            user_agent="rude poem generator:1.0.0 (by /u/rude_poem_generator)")
        pfys = reddit.redditor("Poem_for_your_sprog")
        self.poems = [comment.body for comment in pfys.comments.new()]

    def random_poem(self):
        if not self.poems:
            self.fetch_poems()
        return random.choice(self.poems)


hyphen = "|"
dictionary = pyphen.Pyphen(lang="en")


def main():
    pf = PoemFetcher()
    pf.fetch_poems()
    while True:
        result = rude_dude(pf.random_poem())
        if result is not None:
            print(result)
            return
        # print(".", end="")

        #     print(rude_dude("""Do not leave your kids behind.
        # Should you do it, you shall find
        # Children left to wander by
        # Make a very tasty pie.
        #
        # Do not let them go alone.
        # If they're lost and on their own,
        # Children left all by themself
        # End up on a kitchen shelf.
        #
        # Do not let them disappear.
        # If you do not keep them near
        # Children left to drift and dream
        # Might be served with cakes and cream.
        #
        # Do not leave your kids behind.
        # Should you do it, you shall find
        # What precisely children get.
        #
        # Folks get hungry.
        #
        # Kids get et."""))


def syllables(words):
    return sum(len(dictionary.inserted(p, hyphen=hyphen).split(hyphen))
               for p in words.split(" "))


def rude_dude(poem):
    result = []
    prev_rhymes: List[str] = []
    num_replaced = 0
    for i, line in enumerate(poem.split("\n")):
        line = line.strip()
        if line == "":
            result.append(line)
            continue
        words = line.split(" ")
        extras: List[str] = []
        last = words[-1]
        while re.match(r".*[^a-zA-Z]$", last):
            extras.append(last[-1])
            last = last[:-1]
        rhymes = pronouncing.rhymes(last)
        if prev_rhymes:
            if last in prev_rhymes:
                num_replaced += 1
                # rpl = replace_it(words[-1])
                # if rpl is not None:
                #     words[-1] = rpl + "".join(reversed(extras))
                # else:
                words[-1] = "****" + "".join(reversed(extras))
                result.append(" ".join(words))
            prev_rhymes = []
        else:
            prev_rhymes = rhymes
            result.append(line)

    if num_replaced >= 4:
        return "\n".join(result)

    # TODO: more rhming patterns


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

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + \
        language + '/' + word.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    json = r.json()
    s = set()
    for item in json["results"]:
        for le in item["lexicalEntries"]:
            s.add(le["lexicalCategory"])
    return s


def replace_it(word):
    s = get_le(word)
    i = 0
    while i < 10:
        sw = random.choice(list(swear.keys()))
        if s.intersection(swear[sw]):
            return sw
        i += 1
    return


if __name__ == "__main__":
    main()
