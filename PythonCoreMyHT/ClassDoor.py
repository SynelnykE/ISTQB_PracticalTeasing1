class Door:
    colour='brawn'
    def __init__(self, number, status):
        self.number=number
        self.status=status
    @classmethod
    def knock(cls):
        print("Knock!")
    def open(self):
        self.status='opened'
    def close(self):
        self.status='closed'

door1=Door(1, 'closed')
print(door1.status, door1.colour)
door1.knock()
door1.open()
Door.colour='white'
print(door1.status, door1.colour)
