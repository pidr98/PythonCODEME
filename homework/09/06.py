def main():
    '''
    try:
        f = open("file06.txt")
        f.close()
    except  IOError:
        print('File not found')
    '''
    '''
    try:
        f = open("exceprion_04.txt", "w")
        content = f.read()
        print(content)
        f.close()
    except  IOError:
        print('Could not read file')
    '''
    try:
        f = open("exceprion_04.txt", "x")
        f.close()
    except  IOError:
        print('File already exist')

if __name__ == '__main__':
    main()