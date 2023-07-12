import requests

link1 = 'https://blaze.com/api/roulette_games/current'
link2 = 'https://blaze.com/api/roulette_games/recent'

req1=requests.get(link1)
req2=requests.get(link2)
d2=req2.json()

for i in range(len(d2)):
    c=d2[i]
    if c['color']==0:


    
        token ='6078935508:AAGfzFwISS11HHzF6HlJI5WwjdL_8ZiqYh4'
        chat_id = '-1001911037404'
        message='\U00002b1c'
        URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
        resposta = requests.get(URL)
