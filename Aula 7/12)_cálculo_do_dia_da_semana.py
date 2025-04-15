from datetime import datetime
data_hoje = datetime.today()
print ("Data de hoje:", data_hoje)
data_time = data_hoje.strftime("%A")
print ("Dia da semana de hj é", data_time)
