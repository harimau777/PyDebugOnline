import random

print 'Hello, world!'

def main():
    print 'In main'
    for i in range(5):
        print i, random.randrange(0, 10)
    print 'Done.'

main()
