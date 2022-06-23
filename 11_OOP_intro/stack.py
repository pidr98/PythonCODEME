class Stack:
    def __init__(self, lifo = []):
        self.lifo = lifo

    def show(self):
        print('Queue: ', self.lifo)

    def push(self, item):
        self.lifo.append(item)

    def get(self):
        return self.lifo.pop(-1)

def main():
    q = Stack([3, 2, 7, 9, 'txt'])
    q.show()
    q.push('rita')
    q.show()
    x = q.get()
    print('wyjeto --->', x)
    q.show()

if __name__ == '__main__':
    main()