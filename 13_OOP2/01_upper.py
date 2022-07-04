def uppercase(func_txt):
    def upper_letter():
        result = func_txt()
        return result.upper()

    return upper_letter

@uppercase
def txt_fun():
    return 'abc'

def main():
    print(txt_fun())

if __name__ == '__main__':
    main()