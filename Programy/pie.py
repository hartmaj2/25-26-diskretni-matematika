"""
Test principu inkluze a exkluze
Jaky je pocet retezcu delky 5 anglicke abecedy, ktere splnuji alespon jednu nasledujici podminku:
1. zacina a konci na stejnou samohlasku
2. prostredni podretezec je "ada" (tedy od indexu 1 do indexu 4 nevcetne)
3. obsahuje pismeno z

Podle vypoctu by to melo byt: 20*26^3 + 26^2 + sum([(-1)^{n-1} * 26^(5-n) * nCr(5,n) for n in range(1,6)]) - 20 - (2*26-1) + 1 = 2_637_006

Celkem slov je 26^5 = 11_881_376

First_last_conson je 20 * 26^3 = 351_520

Middle_ada je 26^2 = 676

Contains_z je: 26^4 + 26^3 * 25 + 26^2 * 25^2 + 26 * 25^3 + 25^4 = 2_115_751
(to lze odvodit buď tak, že počítáme postupně počet posl. kde z je na prvním, druhém, třetím místě atd. ale musíme u i-tého místa počítat jen takové posl. kde na všech předchozích už z není)
(druhý způsob je zase použít princip inkluze a exkluze)

"""

words = []

def first_last_conson(word : str) -> bool:
    return word[0] not in "aeiyou" and word[0] == word[-1]

def middle_ada(word : str) -> bool:
    return word[1:4] == "ada"

def contains_z(word : str) -> bool:
    return "z" in word

def generate_next(word : str):
    global words
    if len(word) == 5:
        if contains_z(word):
            words.append(word)
        return
    for i in range(ord("a"),ord("z")+1):
        generate_next(word + chr(i))

generate_next("")

print(f"{len(words):_}")