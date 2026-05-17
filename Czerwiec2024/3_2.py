slownik = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
    "n": "a",
    "o": "b",
    "p": "c",
    "q": "d",
    "r": "e",
    "s": "f",
    "t": "g",
    "u": "h",
    "v": "i",
    "w": "j",
    "x": "k",
    "y": "l",
    "z": "m",
}

#abcdefghijklmnopqrstuvwxyz

with open("d:\\programowanie\\inf_matura\\Czerwiec2024\\materialy\\slowa.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0
    najdluzszy_wyraz = ""

    for index, value in enumerate(lines):
        slowo = list(value)
        slowo_rot = []
        for j in range(len(value)):
            slowo_rot.append(slownik[value[j]])
        slowo_rot = "".join(slowo_rot)
        slowo = "".join(slowo)
        slowo_palindrom = slowo[::-1]
        if slowo_rot == slowo_palindrom:
            ilosc+=1
            if len(slowo) > len(najdluzszy_wyraz):
                najdluzszy_wyraz = slowo
    print(ilosc)
    print(najdluzszy_wyraz)