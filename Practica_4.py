import datetime
from time import ctime
import ntplib
import os

#Hora de peticion
t1 = datetime.datetime.now()
print("Hora de la solicitud: "+str(t1))
#Hora del servidor
servidor_de_tiempo = "time-b-wwv.nist.gov"
print("\nObteniendo la hora del servidor NTP...")
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
Hora_Servidor = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("Hora del servidor: "+str(Hora_Servidor))
#Hora de recepcion
t2 = datetime.datetime.now()
print("Hora de llegada: "+str(t2))
#Ajuste de tiempo
Ajuste = (t2-t1)/2
print("El ajuste fue: "+str(Ajuste))
Reloj = Hora_Servidor+Ajuste
print("Hora ajustada: "+str(Reloj))
os.system(f"date --set '{Reloj}'")