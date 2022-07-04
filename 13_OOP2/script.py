def wrapper():
    txt = 'closure'
    num = 6
    def nested():
        return '--> Jestem w środku', txt * num

    return nested




def main():
    returned_func = wrapper()

    print(returned_func())

if __name__ == '__main__':
    main()