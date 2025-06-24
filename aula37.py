# Criando datas com módulo datetime
# Datetime(ano, mês, dia)
# datetime(ano, mes, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# datetime.fromtimestamp(Unix Timestamp)
# Para timezones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2025-06-24 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str_data, data_str_fmt)
print(data)