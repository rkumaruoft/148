from datetime import date

class Tweet:
        """   === Attributes ===
        userid: the id of the user who wrote the tweet.
        created_at: the date the tweet was written.
        content: the contents of the tweet.
        likes: the number of likes this tweet has received.
        """
    # Attribute types
    userid: str
    created_at: date
    content: str
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.
        """
        self.userid = who
        self.created_at = when
        self.content = what
        self.likes = 0

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.
        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        Rukhsana is cool
        """
        old_user = self.userid
        old_date = self.created_at
        self = Tweet(old_user, old_date, new_content)
