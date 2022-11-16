from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://cryptoslate.com/coins/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

table_rows = soup.findAll('tr')
print(title.text)
print('Top 5 Cryptocurrencies')
print()
print()

table_rows = soup.findAll('tr')

for row in table_rows[1:6]:
    td = row.findAll('td')
    name = (td[1].text)
    newname = (td[1].text.replace(' ',''))
    print('Name of Coin:',name)
    print()


    #No symbol given in table 
    price = td[2].text
    print(f"Current Price: {price}")
    price = float(td[2].text.replace('$','').replace(' ','').replace(',',''))
    print()
    
    day_change = float(td[3].text.replace('%',''))
    variable = 1 + (day_change/100)
    previous_price = price/variable
    calculation = float(price - previous_price)

  

    print(f"% Percent Change in last 24 hours: {day_change}%")
    print()
    
    previous_price = price/variable
    calculation = float(price - previous_price)

    value = '+'
    if calculation > 0:
        value = '+'
    else:
        value = '-'

    
    print("Price 24 hours ago :","${:,.4f}". format(previous_price))
    print()
    
    
    import keys2
    from twilio.rest import Client
    

    client = Client(keys2.accountSID, keys2.authToken)

    TwilioNumber = '+18303767583'
    myCellPhone = '+18325250652'

    if str(newname) == 'BitcoinBTC':
        if price < 40000:
            textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body='The price of Bitcoin is below $40,000')

    if str(newname) == 'EthereumETH':
        if price < 3000: 
            textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="The price of Ethereum is below $3,000")
