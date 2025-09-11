# Řešení cvičení 1

## Devatero mincí

Každé vážení vyústí ve 3 možnosti:
- levá strana těžší
- pravá strana těžší
- obě strany stejně těžké

Kdyby vyústilo ve:
- 2 možnosti - 1 bit informace.
- 4 možnosti - 2 bity informace

Tím pádem musíme dostat # bitů někde mezi 1 a 2. Formálně počet bitů odpovídá tomu, kolika půleními bychom mohli rozeznat jednotlivé možnosti. Tedy je to $\log_2{3}$

Pokud vážíme $k$ krát, tak počet získaných bitů informace je $k \cdot \log_2{3} = \log_2{3^k}$, kde $3^k$ je počet stavů, které dokážeme rozlišit. To tedy odpovídá maximálnímu počtu mincí, ve kterém na $k$ vážení dokážeme identifikovat falešnou minci.


## Topinka

Máme $n$ topinek a chceme opéct celkem $2n$ stran. Pravidlo říká, můžeme opéct vždy 2 strany topinek naráz, ale nesmí to být 2 strany jedné a té samé topinky.

Pokud bychom použili hladový způsob, tak bychom opekli nejprve dva z jedné strany a pak z druhé. Potom už bychom však nemohli využít oba sloty topinkovače.

## Popletené truhly

