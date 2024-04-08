비밀코드, 접선장소, 시간 = map(str, input().split())

class secret_007:
    def __init__(self, 비밀코드, 접선장소, 시간):
         self.비밀코드 = 비밀코드
         self.접선장소 = 접선장소
         self.시간 = 시간

first_007 = secret_007(비밀코드, 접선장소, 시간)

print('secret code :', first_007.비밀코드)
print('meeting point :', first_007.접선장소)
print('time :', first_007.시간)