import os.path
import sys


iniciales = sys.argv[1]
users = []
for i in range(1,4):
    user = iniciales + str(i)
    users.append(user)
print(users)

for user in users:
    cmd = f'useradd {user}'
    os.system(cmd)
    print('excuted:',cmd)

dir = iniciales + '_init'
if os.path.exists(dir):
    print('dir',dir,'ja existeix')
else:
    os.mkdir(dir)
    print('created:',dir)