# 15.12.205

## Intro

- sled - navazující posloupnost vrcholů a hran (walk)
- tah - sled, který navíc nesmí opakovat hrany (vrcholy může) (tour?)
- cesta - sled, který nesmí opakovat žádný z objektů (path)

- orientované grafy
  - silná vs. slabá souvislost

- Eulerovský graf
  - graf, který obsahuje Eulerovský tah - tah, který použije všechny hrany
    - A SKONČÍ TAM, KDE ZAČAL
  - souvislý a má všechny stupně sudé

## Důkaz charakteristiky Eulerovských grafů

Graf $G$ je eulerovský právě tehdy, když je souvislý a každý vrchol $G$ má sudý stupeň. 

### Implikace zleva doprava

- když graf obsahuje elerovský tah, který končí tam kde začal a použije všechny hrany
  - musí být souvislý (kdyby nebyl, tak se nemůžeme dostat do nějakého vrcholu a tah ho nemůže obsahovat)
  - předpokládejme, že máme vrchol s lichým stupněm
    - pokud se nejedná o počáteční vrchol tahu - vždy když přijdeme, tak musíme i odejít
    - pokud se jedná o počáteční vrchol - musíme v něm i skončit

### Implikace zprava doleva

- nechť máme graf $G$ jehož každý stupeň je sudý a který je souvislý
- chceme ukázat, že existuje eulerovský tah (ukážeme to konstrukcí)
- začneme v libovolném vrcholu a hladově volíme doposud nepoužité hrany
- pozorování:
  - 1. proces musí určitě skončit tam, kde začal (sudé stupně)
  - 2. NEMUSÍME SKONČIT TAM, KDE JSME ZAČALI!!!
  - 3. náš tah buď obsahuje všechny hrany, nebo z nějakého jeho vrcholu vede hrana, kterou jsme ještě nepoužili (souvislost grafu)

## Příklady