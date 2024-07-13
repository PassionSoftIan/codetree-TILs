code, place, time = map(str, input().split())

class Spy:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.place = time

spy1 = Spy(code, place, time)

print('secret code :', spy1.code)
print('meeting point :', spy1.place)
print('time :', spy1.time)