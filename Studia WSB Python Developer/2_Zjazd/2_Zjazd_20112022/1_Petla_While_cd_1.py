while True:
    x = input('Wprowadz liczbe ')
    try:
        x = int(x)
        print('bedzie int')
        break
    except ValueError:
        try:
            x = float(x)
            print('bedzie float')
            break
        except ValueError:
            print('zostaje string')
            break
print(type(x))