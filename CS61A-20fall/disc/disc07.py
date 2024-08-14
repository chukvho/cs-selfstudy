# 1.2
class MinList:
    """ A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0
        
    def append(self, item):
        """ Appends an item to the Minlist
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1
        return
        
    def pop(self):
        """ Removes and return the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        smallest = min(self.items)
        self.items.remove(smallest)
        self.size -= 1
        return smallest

# 1.3
class Email:
    """Every email object has 3 instance attributes: the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        
class Server:
    """Each Server has an instance attribute clients, which is a dictionary that associates client names with client objects.
    """
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to.
        """
        recipient_name = email.recipient_name
        if recipient_name in self.clients:
            self.clients[recipient_name].receive(email)
        else:
            print(f"Error: Recipient {recipient_name} not found.")
        
    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to the clients instance attribute.
        """
        self.clients[client_name] = client
        
class Client:
    """Every Client has instance attributes name (which is used for addressing emails to the client), server (which is used to send emails out to other clients), and inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self, name) # Claude的建议：自动注册客户端
        
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)
        
    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)
        
# 2.1
class Pet():
	def __init__(self, name, owner):
		self.is_alive = True
		self.name = name
		self.owner = owner
	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")
	def talk(self):
		print(self.name)

class Dog(Pet):
	def talk(self):
		print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner) # 记住这个写法
        self.lives = lives
    # 不需要特别指明is_alive，已经通过Pet的初始化方法设置了
        
    def talk(self):
        """Print out a cat's greeting.
        
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')
    
    def lose_life(self):
        """Decrement a cat's life by 1. When lives reaches zero, 'is_alive' becomes False. If this is called after lives has reached zero, print out that the cat has no more lives to lose.
        """
        if not self.lives:
            print("The cat has no more lives to lose.")
        else:
            self.lives -= 1
            if not self.lives:
                self.is_alive = False
        # if self.lives:
        #     self.lives -= 1
        #     self.is_alive = self.lives > 0
        # else:
        #     print("The cat has no more lives to lose.")
        
# 2.2
class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        super().__init__(name, owner, lives)
        # Not necessary, this method is as same as the Cat.
        
    def talk(self):
        """Talks twice as much as a regular cat.
        
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print(self.name + ' says meow!')
        print(self.name + ' says meow!')
        
    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat
        
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)
      # return f"NoisyCat('{self.name}', '{self.owner}')"