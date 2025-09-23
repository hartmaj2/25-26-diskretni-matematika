# Řešení příkladů z prvního cvičení

## Výroky

### Příklad 1

#### (a) 
$V(\text{Slovensko},\text{Francie})$

#### (b) 
Existuje stát, do kterého Německo vyváží víno.

### Příklad 2

#### (a) NEPLATÍ
Pro každý stát $x$, existuje nějaký stát $y$ z M, do kterého stát $x$ vyváží víno. 

Co to znamená na obrázku? Že z každé tečky musí vést nějaká šipka.

Proč neplatí: Neexistuje stát, do kterého by Slovensko vyváželo víno.

#### (b) PLATÍ

Pro každý stát $x$ existuje stát $y$, který do $x$ vyváží víno.

Do každé tečky musí existovat šipka.

#### (c) PLATÍ

Existuje stát, který vyváží víno do všech států.

Proč platí: Splňuje to Francie

#### (d) NEPLATÍ

Existuje stát, do kterého vyváží víno všechny státy.

Proč neplatí: Každý stát má někoho, kdo do něj nevyváží.

### Příklad 3

#### (a)

1 

Pro všechny dvojice států platí, že když vyváží jeden do druhého, tak nutně už nevyváží ten druhý do prvního. (Například pokud Francie vyváží do Německa, tak už nutně Německo nevyváží do Francie)

Na šipkách to znamená, že nemáme mezi dvěmi tečkami šipku v obou směrech.

Náš model nesplňuje tuto podmínku jelikož Německo vyváží do Francie. Co kdyby tedy Německo přestalo odebírat víno od Francie, platilo by to pak?

2

Pro každou trojici států $x,y,z$ platí, že když ten první vyváží do druhého a zároveň ten druhý vyváží do třetího, tak už nutně vyváží ten první do třetího.

Na šipkách to znamená, že když mezi třemi tečkami nastane situace, kdy se dá z první tečky dostat po dvou šipkách s mezikrokem ve druhé tečce do té třetí, tak nutně musí existovat i šipka rovnou z první tečky do té třetí.

#### (b)

Toto jednoduše dokážeme sporem. Stačí si vzít libovolný stát $s$ a předpokládat, že platí $V(s,s)$. Uvažme poté podmínku 1. Podle ní máme, $V(s,s) \Rightarrow \neg V(s,s)$, což se vyhodnotí na $1 \Rightarrow 0$, což nemůže nastat.

#### (c)

Na diagramu se snažíme dokázat, že šipky nemohou tvořit cyklus. Budeme postupovat znovu sporem a budeme předpokládat, že nějaký cyklus jsme našli. 

Dále ukážeme, že to vede k tomu, že platí $V(x_0,x_i)$  pro libovolné $i \leq n$. Jakou podmínku z 1 a 2 použijeme?

Vidíme, že jelikož máme $V(x_0,x_1)$ a $V(x_1,x_2)$, tak máme $V(x_0,x_2)$. Podobně pak můžeme vzít $V(x_0,x_2)$ a $V(x_2,x_3)$ k odvození $V(x_0,x_3)$. Tímto postupem se dostaneme až k $V(x_0,x_n) = V(x_0,x_0)$. Jak nám dokázat toto pomohlo?

Výrok $V(x_0,x_0)$ je totiž v rozporu s podmínkou 1.

## Množiny

### Příklad 4

$A \bigtriangleup B = (A \cup B) \setminus (A \cap B)$

$A \bigtriangleup B = (A \setminus B) \cup (B \setminus A)$

BONUS: Kolik existuje způsobů, jak vyjádřit $A \bigtriangleup B$ kombinací libovolného počtu těchto operací? (nekonečně mnoho)

### Příklad 5

Jaké množiny určitě vytvořit umíme?

Co prázdná množina? Umíme pokud $|K| > 1$ a tedy máme k dispozici nějakou dvouprvkovou podmnožinu $K$.

Co množiny velikosti 1? Zvládnu to použitím dvou různých dvouprvkových množin? Co když se překrývají? Vypadá to, že to spíš nelze.

Umím vytvořit tříprvkovou množinu? To je také divné.

Čtyřprvková množina jde vyrobit lehce. No a vlastně i šesti, osmi atd. když na to máme dostatečně velkou množinu $K$.

Jaké množiny nám tedy nejdou vytvořit? Ty liché!

Proč nám nejdou vytvořit liché množiny? 

Je užitečné si seřadit a očíslovat prvky množiny $K$ do vektoru $(x_1, \ldots x_n)$. Každou podmnožinu $A \subseteq K$, pak můžeme vyjádřit jako vektor nul a jedniček kde na $i$-té pozici se nachází $1$ právě tehdy když $x_i \in K$.

Například pro $K = M$ by množina $\{ \text{Francie}, \text{Česko}\}$ odpovídala vektoru $(1,0,1,0)$ nebo zkráceně $1010$.

Dokážeme si představit, co dělá operace $\bigtriangleup$ na vektorech odpovídajících podmnožinám? 

Co ta operace dělá jest, operaci XOR po bitech na odpovídajících si pozicích ve vektorech. S tím že tabulka pro XOR je:

| a   | b   | $\oplus$ |
| --- | --- | -------- |
| 0   | 0   | 0        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 0        |

Co nás zajímá je, jaký počet jedniček bude obsažen ve výsledném vektoru?

Počítejme je následovně, nejprve spočítáme kolik jich může být potenciálně, kdyby se žádné nevykrátily. Vezmeme tedy součet počtu jedniček obou vektorů. To je nutně sudé číslo, jelikož začínáme pouze s množinou sudé velikosti. To jsme se ale přepočítali a musíme z výsledné sumy odečíst ty vykrácené jedničky. Ty se však pro každý index zkrátí obě (tedy jeden pár pro každý index). Tím pádem celkem odečteme sudé číslo od sudého a tím vznikne nutně zase sudé číslo.

### Příklad 6

TODO:

## Hádanky

### Příklad 7

TODO:

### Příklad 8

TODO:

### Příklad 9

TODO: