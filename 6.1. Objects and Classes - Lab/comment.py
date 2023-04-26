class Comment:
    def __init__(self, username, content, likes=0):    # likes is optional, 0 by default
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)