from _datetime import datetime
import time
import currencies_operation as curr_op
from classes import Bot
import numpy
import json

INDENT_LEVEL = 4


def Main():
    my_bot = Bot()

    # [ITA] Creo il dizionario che verrà scritto su file
    # [ENG] I create the dictionary that will be written on file
    currencies_data = {}

    # [ITA] Richiesta 1) La criptovaluta con il volume maggiore ($) nelle ultime 24 ore
    # [ENG] Request 1) The cryptocurrency with the highest volume ($) over the last 24 hours

    # [ITA] Recupero la criptovaluta in questione 24 e aggiungo le informazioni al dizionario
    # [ENG] I retrieve the aforementioned cryptocurrency and add the information to the dictionary
    largest_24h_volume_currency = my_bot.fetch_currencies_data(sort="volume_24h", limit=1)[0]

    currencies_data["largest_24h_volume_currency"] = curr_op.get_main_info(largest_24h_volume_currency)

    # [ITA] Richiesta 2) Le migliori e peggiori 10 criptovalute per incremento in percentuale nelle ultime 24
    # [ITA] Request 2) The best and worst 10 cryptocurrencies by percentage increase in the last 24 hours

    # [ITA] Recupero le criptovalute con maggiore incremento percentuale nelle ultime 24h
    # [ENG] I retrieve the cryptocurrencies with the highest percentage increase in the last 24h

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the informations to the dictionary
    best_currencies_by_24h_percent_change = my_bot.fetch_currencies_data(sort="percent_change_24h",
                                                                         limit=10, sort_dir="desc")

    # [ITA] Creo un dizionario temporaneo per gestire con comodità la lista di criptovalute ottenuta
    # [ENG] I create a temporary dictionary to easily manage the list of cryptocurrencies obtained
    best_currencies_data = []

    for currency in best_currencies_by_24h_percent_change:
        best_currencies_data.append(curr_op.get_main_info(currency))

    currencies_data["best_currencies_by_24h_percent_change"] = best_currencies_data

    # [ITA] Recupero le criptovalute con maggiore decremento percentuale nelle ultime 24h
    # [ENG] I retrieve the cryptocurrencies with the greatest percentage decrease in the last 24h

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the informations to the dictionary
    worst_currencies_by_24h_percent_change = my_bot.fetch_currencies_data(sort="percent_change_24h",
                                                                          limit=10, sort_dir="asc")

    # [ITA] Creo un dizionario temporaneo per gestire con comodità la lista di criptovalute ottenuta
    # [ENG] I create a temporary dictionary to easily manage the list of cryptocurrencies obtained
    worst_currencies_data = []

    for currency in worst_currencies_by_24h_percent_change:
        worst_currencies_data.append(curr_op.get_main_info(currency))

    currencies_data["worst_currencies_by_24h_percent_change"] = worst_currencies_data

    # [ITA] Richiesta 4) La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute
    #                    il cui volume delle ultime 24 ore sia superiore a 76.000.000$
    # [ENG] Request 4) The amount of money required to purchase one unit of all cryptocurrencies
    #                  whose volume of the last 24 hours exceeds $ 76,000,000

    currencies_by_min_volume = my_bot.fetch_currencies_data(volume_24h_min="76000000")

    # [ITA] Trasformo la lista ottenuta in un array numpy composto dai prezzi di ciascuna criptovaluta
    # [ITA] In questo modo, le operazioni sono estramemente più veloci

    # [ENG] I transform the resulting list into a numpy array made up of the prices of each cryptocurrency
    # [ENG] In this way, the operations are extremely faster
    currencies_by_min_volume_np = numpy.array([curr_op.get_price(currency) for currency in currencies_by_min_volume])

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the informations to the dictionary
    currencies_data["76mln+_volume_currencies_total_price"] = numpy.sum(currencies_by_min_volume_np)

    # [ITA] Richiesta 3) La quantità di denaro necessaria per acquistare un'unità
    #                    di ciascuna delle prime 20 criptovalute
    # [ENG] Request 3) The amount of money needed to purchase one unit of each of the top 20 cryptocurrencies

    top_20_currencies = my_bot.fetch_currencies_data(limit=20)

    # [ITA] Trasformo la lista ottenuta in un array numpy composto dai prezzi di ciascuna criptovaluta
    # [ITA] In questo modo, le operazioni sono estramemente più veloci

    # [ENG] I transform the resulting list into a numpy array made up of the prices of each cryptocurrency
    # [ENG] In this way, the operations are extremely faster
    top_20_prices = numpy.array([curr_op.get_price(currency) for currency in top_20_currencies])

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the informations to the dictionary
    currencies_data["top_20_total_price_now"] = numpy.sum(top_20_prices)

    # [ITA] Richiesta 5) La percentuale di guadagno o perdita che avreste realizzato
    #                    se aveste comprato una unità di ciascuna
    #                    delle prime 20 criptovalute il giorno prima (ipotizzando che la classifca non sia cambiata)
    # [ENG] Request 5) The percentage of gain or loss you would have made if you had bought one unit of each
    #                  of the top 20 cryptocurrencies the day before (assuming the ranking hasn't changed)

    # [ITA] Recupero il prezzo delle criptovalute in top 20 nella giornata di ieri
    # [ITA] L'operazione viene svolta basandosi sull'incremento percentuale nelle ultime 24 ore
    # [ITA] Viene usata la formula (prezzo_oggi * (100 + incremento_percentuale)) / 100

    # [ENG] I retrieve the price of cryptocurrencies in the top 20 yesterday
    # [ENG] The operation is carried out based on the percentage increase in the last 24 hours
    # [ENG] The formula (price_ today * (100 + percentage_increase)) / 100 is used
    top_20_yesterday_prices = numpy.array([curr_op.get_price(currency) *
                                           ((100 + (curr_op.get_24h_percent_change(currency))) / 100)
                                           for currency in top_20_currencies])

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the informations to the dictionary
    currencies_data["top_20_total_price_yesterday"] = numpy.sum(top_20_yesterday_prices)

    # [ITA] Uso la proporzione top_20_total_price_yesterday : 100 = top_20_total_price_now : x
    # [ENG] I use the proportion top_20_total_price_yesterday: 100 = top_20_total_price_now: x
    gain_from_yesterday_to_now = (100.0 * numpy.sum(top_20_yesterday_prices)) / (numpy.sum(top_20_prices)) - 100

    # [ITA] Aggiungo le informazioni al dizionario
    # [ENG] I add the information to the dictionary
    currencies_data["gain_from_yesterday_to_now"] = gain_from_yesterday_to_now

    # [ITA] Creo il del nome file in base alla data attuale
    # [ENG] I create the file name based on the current date
    now = str(datetime.now().date()) + ".json"

    # [ITA] Scrivo le informazioni sul file
    # [ENG] I write the informations on the file
    with open(now, "w") as outfile:
        json.dump(currencies_data, outfile, indent=INDENT_LEVEL)

    print("Report just created: {}".format(datetime.now()))
    print("Another report will be created in 24 hours")

    seconds = 24 * 60 * 60
    time.sleep(seconds)


if __name__ == '__main__':
    Main()
