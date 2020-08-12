# CryptocurrencyDailyReport
A simple python project that deals with creating a daily mini-report on the trend of cryptocurrencies.

[ENG VERSION]

The project was created at the suggestion of Start2Impact(https://www.start2impact.it/) and for this reason it answers these 5 simple questions:
 
1. The cryptocurrency with the largest volume (in $) of the last 24 hours
2. The best and worst 10 cryptocurrencies (by percentage increase in the last 24 hours)
3. The amount of money required to purchase one unit of each of the top 20 cryptocurrencies *
4. The amount of money required to purchase one unit of all cryptocurrencies whose last 24-hour volume exceeds $ 76,000,000
5. The percentage of gain or loss you would have made if you had bought one unit of each of the top 20 cryptocurrencies the day before (assuming that the ranking has not changed)
 
The information is processed and saved on json files daily.
 
Everything is done with the help of the CoinMarketCap API.
 
Improvements in progress ...

As a matter of privacy I have removed my API key provided by coin market cap.
For the program to work it is necessary to insert a valid one in the file classes. In particular, it must be inserted in the __init__ method of the Bot () class

---------------------------------------------------------------------------------------------------------------------------------------------------------------- 

[ITA VERSION]

Il progetto è stato creato su suggerimento di Start2Impact e per questo motivo risponde a questi 5 semplici quesiti:
 
1. La criptovaluta con il volume maggiore (in $) delle ultime 24 ore
2. Le migliori e peggiori 10 criptovalute (per incremento in percentuale delle ultime 24 ore)
3. La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute*
4. La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$
5. La percentuale di guadagno o perdita che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute il giorno prima (ipotizzando che la classifca non sia cambiata)
 
Le informazioni vengono eleborate e salvate su file json giornalmente.
 
Il tutto è realizzato tramite l'ausilio delle API di CoinMarketCap.
 
Miglioramenti in corso...

Per una questione di privacy ho rimosso la mia chiave API fornita da coin market cap.
Affichè il programma funzioni è necessario inserirne una valida nella nel file classes. In particolare essa va inserita nel metodo __init__ della classe Bot() 
