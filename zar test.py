import random

def zar():
    input("Apasa Enter Pentru A Arunca Zarul")
    ZARUL1 = random.randint(1, 6)
    ZARUL2 = random.randint(1, 6)
    print("Zarul1 Arata " + str(ZARUL1))
    print("Zarul2 Arata " + str(ZARUL2))
    if ZARUL1 == ZARUL2:
        print("AI DAT DUBLA")
    else:
        print("NU AI DUBLA. MAI INCEARCA")

def main():
    zar()

if __name__ == "__main__":
    main()