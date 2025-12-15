# 15.12.205

## Intro Eulerovské grafy

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

## Intro rovinné grafy

### Definice rovinného grafu

- rovinný graf - graf, který lze nakreslit na plochu bez křížení hran
  - nakreslitelný na sféru <=> nakreslitelný do roviny

- jak o grafu dokázat, že je rovinný - stačí poskytnout nakreslení
- dosvědčit, že rovinný NENÍ je těžší

### Eulerova formule

- můžeme využít vztahů, které musí každý rovinný graf splňovat
- Eulerova formule: $v + f = e + 2$
  - co napsat na jakou stranu? přidání hrany buď zvedne počet vrcholů nebo stěn
  - proč 2? mnemotechnika samostatný vrchol - $1 + 1 = 0 + 2$

- můžeme také použít vztah mezi počtem stěn a hran v rovinném grafu
  - každá stěna obklopena nejméně 3 hranami
  - $2e \geq 3f$

- z toho můžeme přepsat $3v + 3f - 6 = 3e$ na $3v - 6 \geq e$

- můžeme z toho říci něco o průměrném stupni?

- average degree $\overline{d} < 6$

- sometimes, we know that we know that our graph is $\bigtriangleup$-free $\rightarrow$ better bound can be achieved

- $e \geq 2f$ takže máme $2v - 4 \geq e$
  - avgdeg $\overline{d} \leq 4 - \frac{8}{v}$

### Kuratowského věta

- silný nástroj, jak testovat rovinnost
- stačí ukázat, že náš graf obsahuje $K_{3,3}$ nebo $K_5$ jako dělení a nutně je pak rovinný
- ale věta říká něco silnějšího, tedy že $K_{3,3}$ a $K_5$ jsou nutnými svědky k usvědčení z nerovinnosti (pokud tam není jejich dělení, tak už je graf nutně rovinný)