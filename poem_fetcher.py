import praw
import random


class PoemFetcher:
    poems = None

    def fetch_poems(self):
        reddit = praw.Reddit(user_agent="rude poem generator:1.0.0 (by /u/rude_poem_generator)")
        pfys = reddit.redditor("Poem_for_your_sprog")
        self.poems = [comment.body for comment in pfys.comments.new()]

    def random_poem(self):
        if not self.poems:
            self.fetch_poems()
        return random.choice(self.poems)
