import time

print('Hello from github!')

time.sleep(1)
print('Let\'s do something useless, like spinning a spinner:')
time.sleep(1)

for i in range(100):
    print(' ' + r'/-\|'[i % 4], end='\r')
    time.sleep(0.02)

print('Thank you for your attention!')
