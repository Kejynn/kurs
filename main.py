import requests
import xml.etree.ElementTree as ET

vib = int(input("1. Вывести курс на сегодняшний день \n"
      "2. Вывести курс за определенный день\n"))

if vib == 1:
    usd = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp').text).find("./Valute[CharCode='USD']/Value").text.replace(",", "."))
    eur = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp').text).find("./Valute[CharCode='EUR']/Value").text.replace(",", "."))
    gbp = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp').text).find("./Valute[CharCode='GBP']/Value").text.replace(",", "."))
    print("Курс доллара: ", usd, " рублей")
    print("Курс евро: ", eur, " рублей")
    print("Курс фунта: ", gbp, " рублей")

if vib == 2:
    date = str(input("Введите дату(формат dd/mm/yyyy)\n"))
    usd = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp?date_req=%s' %date).text).find("./Valute[CharCode='USD']/Value").text.replace(",", "."))
    eur = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp?date_req=%s' %date).text).find("./Valute[CharCode='EUR']/Value").text.replace(",", "."))
    gbp = float(ET.fromstring(requests.get('https://cbr.ru/scripts/XML_daily.asp?date_req=%s' %date).text).find("./Valute[CharCode='GBP']/Value").text.replace(",", "."))
    print("Курс доллара: ", usd, " рублей")
    print("Курс евро: ", eur, " рублей")
    print("Курс фунта: ", gbp, " рублей")