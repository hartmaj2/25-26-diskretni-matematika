# Řešení cvičení 1

## Devatero mincí (GPT-hard 0)

Každé vážení vyústí ve 3 možnosti:
- levá strana těžší
- pravá strana těžší
- obě strany stejně těžké

Kdyby vyústilo ve:
- 2 možnosti - 1 bit informace.
- 4 možnosti - 2 bity informace

Tím pádem musíme dostat # bitů někde mezi 1 a 2. Formálně počet bitů odpovídá tomu, kolika půleními bychom mohli rozeznat jednotlivé možnosti. Tedy je to $\log_2{3}$

Pokud vážíme $k$ krát, tak počet získaných bitů informace je $k \cdot \log_2{3} = \log_2{3^k}$, kde $3^k$ je počet stavů, které dokážeme rozlišit. To tedy odpovídá maximálnímu počtu mincí, ve kterém na $k$ vážení dokážeme identifikovat falešnou minci.


## Topinka (GPT-hard 0)

Úloha by se měla formulovat takto:
> Jsme chudý student a nemáme peníze na topinkovač. Proto opékáme topinky na pánvi a na tu se vejdou nejvýše dvě topinky naráz. Každá strana topinky se musí smažit 2 minuty, aby byla hotová. Jak rychle dokážeme usmažit 3 topinky?

Máme $n$ topinek a chceme opéct celkem $2n$ stran. Pravidlo říká, můžeme opéct vždy 2 strany topinek naráz, ale nesmí to být 2 strany jedné a té samé topinky.

Pokud bychom použili hladový způsob, tak bychom opekli nejprve dva z jedné strany a pak z druhé. Potom už bychom však nemohli využít oba sloty naší pánve.

## Popletené truhly (GPT-hard 0)

Dobře demonstruje různé způsoby znázornění problému:

### Grafové znázornění
Řešením je bipartitní graf, jehož vrcholy jedné partity jsou předměty a vrcholy druhé partity jsou truhly. Hrana vyznačuje, že předmět se může nacházet v dané truhle. Postupně mažeme ty hrany, kde víme, že se předmět nacházet nemůže. Víme, že výsledný graf má být grafem perfektního párování.

### Tabulkové znázornění
Řádky odpovídají truhlám a sloupce předmětům. Na diagonále jsou křížky, jelikož truhla s označením D nemůže obsahovat diamanty atp. Volná políčka pak znamenají možnosti toho, co by mohlo nastat. Kolečko pak napíšeme tam, kde jsme si jistí. Důležité pozorování je, že v každém řádku a sloupci smí být pouze jedno kolečko. Jeden předmět totiž nemůže být ve více truhlách a zároveň jedna truhla nemůže obsahovat více předmětů.

## Mravenci na tyči

Ta mi není hned jasná...

## Lámání čokolády (GPT-hard 1)

### Mé řešení indukcí

Nejprve si problém zjednodušíme. Nezáleží totiž na tom, jak máme čokoládu zrotovanou a můžeme tedy beztrestně předpokládat, že $n \geq m$ (tedy, že šířka čokolády je aspoň taková, jako je její výška).

Nejprve si uděláme odhad na to, kolik si myslíme, že lámání celé tabulky zabere kroků. Kdybychom to dělali systematicky a nejprve provedli všechny svislé zlomy a pak postupně dolámali každý ze vzniklých sloupců, tak máme celkem $n-1 + n \cdot (m-1) = m \cdot n - 1$ kroků.

Dokazujeme sporem. Víme, že pokud nějaká tabulka $m \times n$ lze rozlomit s jiným počtem kroků, tak určitě nejde o tabulku typu $1 \times n$, jelikož takovou můžeme rozlomit pouze $n-1$ kroky, což je v souladu s naším tvrzením. Jakákoliv špatná čokoláda, kterou by šlo rozlomit jiným počtem kroků má tedy nutně $n,m > 1$.

Těch špatných čokolád může být mnoho. Nám ale nic nebrání, vzít si ze všech špatných tu, která má nejmenší dimenzi $n$ (tedy tu delší). Takových čokolád ale může být více s různou velikostí dimenze $m$. Z těch s nejmenším $n$, tedy následně vybereme tu s nejmenším $m$. To je náš unikátní nejmenší špatný exemplář čokolády, jejíž dimenze pojmenuji $m_0 \times n_0$.

My bychom chtěli ukázat, že ať už nepřítel bude lámat tuto čokoládu jakkoliv, tak se mu nepodaří ji zlomit na jiný počet, než tvrdíme. Jakkoliv bude čokoládu nepřítel lámat, tak musí udělat nejprve buď jeden svislý lom, nebo jeden vodorovný zlom.

Když nepřítel udělal první zlom vodorovný, tak rozdělí čokoládu na dvě čokolády se stejnou dimenzí $n_0$ ale jedna bude mít druhou dimenzi $k < m_0$ a druhá $m_0 - k < m_0$. Jelikož obě ty čokolády jsou menší, než ta špatná, tak už musí být dobré a nedají se rozlomit na jiný počet zlomení než ten ze vzorečku. Tím dostaneme počet zlomení $k \cdot n_0 -1$ za první čokoládu a $(m_0 - k) \cdot n_0 - 1$ za druhou. Nesmíme také zapomenout na jedno zlomení, které nám rozdělilo tu špatnou čokoládu na dva kousky. Celkem máme tedy $k \cdot n_0 - 1 + (m_0 - k) \cdot n_0 - 1 + 1 = m_0 \cdot n_0 - 1$, což jsme chtěli dokázat. 

Podobným argumentem můžeme dokázat i případ, kdy nepřítel první zlom provedl svislý.

### Řešení ChatGPT

Dokážeme, že potřebujeme přesně $mn - 1$ zlomení.

Nyní na to půjdeme jinou cestou. Zeptáme se sami sebe, kolik rozlámaná čokoláda bude obsahovat dílků. No přeci nehledě na to, jak ji budeme lámat, tak nakonec musíme disponovat $mn$ dílky. Na začátku vždy máme jeden dílek. Potřebujeme tedy zvýšit počet dílků přesně o $mn-1$.

Podívejme se, jak se změní po zlomení libovolného dílku v libovolném kroku počet dílků, kterými disponujeme. Řekněme, že na začátku máme $k$ dílků. Jeden z těchto dílků vezmeme a rozlomíme. Na konci tedy máme $k-1$ dílků na které jsme vůbec nešáhli a $2$ dílky držíme v ruce, takže celkem nám zbylo $k+1$ dílků. Uvědomme si, že tento počet je nezávislý na volbě dílku, který budeme lámat a na tom, kde konkrétně zlom provedeme.

Jelikož každé zlomení navýší počet dílků o jedna a chceme navýšit o $mn-1$, tak provedeme přesně $mn-1$ zlomení.

## Šachovnice

### Mé řešení

Nejprve uděláme úvahu o tom, kolik máme k dispozici dominových dílků. Šachovnice s ukousnutými rohy má celkem 62 políček a tedy dominových dílků je 31. Každý dílek je otočený buď vodorovně nebo svisle. Z tohoto plyne, že buď lichý počet jich je otočený svisle a sudý vodorovně nebo obráceně.

Tato podmínka sama o sobě k důkazu jistě nestačí, jelikož zatím nijak nezohledňujeme, že chybějící políčka šachovnice se nachází v opačných rozích. Kdyby například ležely ve stejném rohu ihned vedle sebe, tak by šachovnice dominovými dílky pokrýt šla.

Potřebujeme se tedy zaměřit na jednotlivé řádky a uvědomit si, jak mohou obecně být dílky v řádcích poskládány. Budeme postupovat od prvního řádku zdola směrem nahoru. 

Jelikož v prvním řádku chybí jedno políčko, tak máme k dispozici lichý počet políček, a tedy určitě nemůže vyčnívat z tohoto řádku sudý počet svislých dominových dílků. To by nám pak v tomto řádku zbyl lichý počet políček, který jistě nelze zaplit vodorovnými dominovými dílky. Tím nám na každém následujícím řádku nastane stejná situace až na ten předposlední. Tzn. celkem 7x máme lichý počet svislých dílků a v posledním řádku už žádný svislý dílek začínat nemůže. Máme tedy celkem lichý počet svislých dílků. 

Analogicky však můžeme tuto úvahu provést i pro dílky vodorovné, což je spor s naším prvním pozorováním.
