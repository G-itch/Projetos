from iqoptionapi.stable_api import IQ_Option
import time, json

from datetime import datetime
from dateutil import tz

API= IQ_Option("enfurtini@hotmail.com","mythka0sz")
#   API.change_balance("Real")
while True:
    API.connect()
    if API.check_connect() == False:
        print("Erro ao conectar")
        API.connect()
    else:
        print("Conectado com sucesso!")
        break
        
    time.sleep(1)
def perfil():
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))

    return perfil
def timestamp_converter(x):
    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo = tz.gettz('GMT'))
    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]
x = perfil()


par = "EURUSD"

"""vela= API.get_candles(par,60, 1, time.time())

print(vela)
print(timestamp_converter(vela[0]['from']))

API.start_candles_stream(par,60,1)
time.sleep(1)
vela = API.get_realtime_candles(par,60)
while True:
    for velas in vela:
        print(vela[velas]["close"])
        time.sleep(0.5)

API.stop_candles_stream(par,60)"""

API.start_mood_stream(par)

while True:
    x = API.get_traders_mood(par)
    print(int(100*round(x,2)))
    time.sleep(1)

API.stop_mood_stream(par)

API.