import logging

def main():

  try:
    digits = []
    while True:
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
          elements = int(input('Input numbers: '))
          digits.append(elements)
        avg = sum(digits) / len(digits)
        print(avg)
        break
  except ValueError as Exc04:
    f = open("exceprion_04.txt", "a")
    f.write(str(Exc04))
    f.close()

if __name__ == '__main__':
    main()