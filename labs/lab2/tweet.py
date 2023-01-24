"""Object-Oriented Programming: Twitter example

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains two sample classes Tweet and User that we developed
as way to introduce the major concepts of object-oriented programming.
"""
from __future__ import \
    annotations  # Allows forward references in type annotations.
from datetime import date  # Python library for working with dates (and times)
from typing import List  # Python library for expressing complex types


class Tweet:
    """A tweet, like in Twitter.

    === Attributes ===
    content: the contents of the tweet.
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    likes: the number of likes this tweet has received.

    === Sample Usage ===

    Creating a tweet:
    >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
    >>> t.userid
    'Rukhsana'
    >>> t.created_at
    datetime.date(2017, 9, 16)
    >>> t.content
    'Hey!'

    Tracking likes for a tweet:
    >>> t.likes
    0
    >>> t.like(1)
    >>> t.likes
    1
    >>> t.like(10)
    >>> t.likes
    11
    """
    # Attribute types
    content: str
    userid: str
    created_at: date
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.userid
        'Rukhsana'
        >>> t.created_at
        datetime.date(2017, 9, 16)
        >>> t.content
        'Hey!'
        >>> t.likes
        0
        """
        self.content = what
        self.userid = who
        self.created_at = when
        self.likes = 0

    def like(self, n: int) -> None:
        """Record the fact that this tweet received <n> likes.

        These likes are in addition to the ones <self> already has.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.like(3)
        >>> t.likes
        3
        """
        self.likes += n

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """
        self.content = new_content


class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    follows: a list of the other users who this Twitter user follows.
    tweets: a list of the tweets that this user has made.
    """
    # Attribute types
    userid: str
    bio: str
    follows: List[User]
    tweets: List[Tweet]

    def __init__(self, id_: str, bio: str) -> None:
        """Initialize this User.

        >>> u = User('Rukhsana', 'Roller coaster fanatic')
        >>> u.userid
        'Rukhsana'
        >>> u.bio
        'Roller coaster fanatic'
        >>> u.follows
        []
        >>> u.tweets
        []
        """
        self.userid = id_
        self.bio = bio
        self.follows = []
        self.tweets = []

    def tweet(self, message: str) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u1.tweet('Wheeeeee!')
        >>> u1.tweet('Again! Again!')
        >>> len(u1.tweets)
        2
        """
        new_tweet = Tweet(self.userid, date.today(), message)
        self.tweets.append(new_tweet)

    def follow(self, other: User) -> None:
        """Record that this User follows <other>.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u2 = User('POTUS', 'USA!!!')
        >>> u1.follow(u2)
        >>> len(u1.follows)
        1
        >>> len(u2.follows)
        0
        """
        self.follows.append(other)

    def verbosity(self, y: int) -> int:
        """Return the number of characters in this User's tweets in year <y>.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u1.tweet('The comet!!')
        >>> u1.tweet('Leviathan!!!!!')
        >>> u1.verbosity(date.today().year)
        25
        >>> u1.verbosity(2015)
        0
        """
        count = 0
        for twt in self.tweets:
            if twt.created_at.year == y:
                count += len(twt.content)
        return count

    def retweet(self, new_tweet: Tweet) -> None:
        """Return a copy of the given tweet with the new user and date.

        The new tweet has 0 likes, regardless of the number of likes of the
        original tweet.

        >>> t1 = User('David', 'David is so cool!')
        >>> t2 = Tweet('Diane', t1, date(2017, 8, 20))
        >>> t1.retweet(t2)
        >>> t1.tweets[0].content
        'David is so cool!'
        >>> t1.tweets[0].userid
        'Diane'
        >>> t1.tweets[0].created_at
        datetime.date(2017, 8, 20)
        """
        self.tweets.append(
            Tweet(new_tweet.userid, date.today(), new_tweet.content))

    def hack(self) -> None:
        """Make every tweet made by every user this user follows say
        'mwahahaha'.

        Use the <edit> method from the Tweet class.

        >>> u1 = User('Diane', 'amazing laugh')
        >>> u2 = User('David', 'okay laugh')
        >>> u1.follow(u2)
        >>> u2.tweet('David is so cool')
        >>> u2.tweets[0].content
        'David is so cool'
        >>> u1.hack()
        >>> u2.tweets[0].content
        'mwahahaha'
        """
        for twt in self.tweets:
            if twt.created_at.year == date.today().year:
                twt.edit('mwahahaha')


class Player:
    """
    A player has a name and a history of the last 100 scores they've achieved
    in the game. We need to be able to add new scores they get so we can
    determine their top score, and find their average score on their most
    recent n games (where n is some positive whole number).
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # Optionally, check your work with python_ta!
    # import python_ta
    # python_ta.check_all(config={'extra-imports': ['datetime']})
