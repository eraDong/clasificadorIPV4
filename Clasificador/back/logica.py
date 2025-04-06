import re ## modulo de expresiones regulares para validar la ip
import sys ## modulo para recibir argumentos desde la terminal
def ipValidation(ip):

    estructura = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if not re.match(estructura, ip):
        return False
    
    octetos = ip.split('.')
    
    for octeto in octetos:
        # verificar que sean digitos y este dentro del rango 0-255
        if not (0 <= int(octeto) <= 255):
            return False
    
    return True

def buscarClase(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    # Convertir la cadena de IP en una lista de octetos
    octetos = ip.split('.')
    primerOcteto = int(octetos[0])
    
    # Determine the class based on the first octet
    if primerOcteto <= 127:
        return "Clase A"
    elif 128 <= primerOcteto <= 191:
        return "Clase B"
    elif 192 <= primerOcteto <= 223:
        return "Clase C"
    elif 224 <= primerOcteto <= 239:
        return "Clase D"
    elif 240 <= primerOcteto <= 255:
        return "Clase E"
    
def buscarTipo(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    # Convertir la cadena de IP en una lista de octetos
    octetos = ip.split('.')
    primerOcteto = int(octetos[0])
    segundoOcteto = int(octetos[1])
    tercerOcteto = int(octetos[2])
    cuartoOcteto = int(octetos[3])

    ## if anidados para verificar dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        if primerOcteto == 10:
            return "Privada"
        elif primerOcteto == 127:
            return "Reservada para loopback"
        elif primerOcteto == 0:
            return "Reservada para ips no asignadas"
        elif segundoOcteto == 0 and tercerOcteto == 0 and cuartoOcteto == 0:
            return "Reservada (Dirección de red)"
        elif segundoOcteto == 255 and tercerOcteto == 255 and cuartoOcteto == 255:
            return "Reservada (Dirección de broadcast)"
        else:
            return "Publica"
    elif buscarClase(ip) == "Clase B":
        if primerOcteto == 172 and 16 <= segundoOcteto <= 31:
            return "Privada"
        elif tercerOcteto == 0 and cuartoOcteto == 0:
            return "Reservada (Dirección de red)"
        elif tercerOcteto == 255 and cuartoOcteto == 255:
            return "Reservada (Dirección de broadcast)"
        else:
            return "Publica"
    elif buscarClase(ip) == "Clase C":
        if primerOcteto == 192 and segundoOcteto == 168:
            return "Privada"
        elif cuartoOcteto == 0:
            return "Reservada (Dirección de red)"
        elif cuartoOcteto == 255:
            return "Reservada (Dirección de broadcast)"
        else:
            return "Publica"
    elif buscarClase(ip) == "Clase D":
        return "Reservada Multicast"
    elif buscarClase(ip) == "Clase E":
        return "Reservada Experimental"
    
def devolverEstructura(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    ## if para devolver la estructura de la ip dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        return "R.H.H.H"
    elif buscarClase(ip) == "Clase B":
        return "R.R.H.H"
    elif buscarClase(ip) == "Clase C":
        return "R.R.R.H"
    elif buscarClase(ip) == "Clase D":
        return "N/A"
    elif buscarClase(ip) == "Clase E":
        return "N/A"
    
def devolverDirRed(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    ## if para devolver la dirección de red dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        return ip.split('.')[0] + ".0.0.0"
    elif buscarClase(ip) == "Clase B":
        return ip.split('.')[0] + "." + ip.split('.')[1] + ".0.0"
    elif buscarClase(ip) == "Clase C":
        return ip.split('.')[0] + "." + ip.split('.')[1] + "." + ip.split('.')[2] + ".0"
    elif buscarClase(ip) == "Clase D":
        return "N/A"
    elif buscarClase(ip) == "Clase E":
        return "N/A"
    
def devolverDirBroadcast(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    ## if para devolver la dirección de broadcast dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        return ip.split('.')[0] + ".255.255.255"
    elif buscarClase(ip) == "Clase B":
        return ip.split('.')[0] + "." + ip.split('.')[1] + ".255.255"
    elif buscarClase(ip) == "Clase C":
        return ip.split('.')[0] + "." + ip.split('.')[1] + "." + ip.split('.')[2] + ".255"
    elif buscarClase(ip) == "Clase D":
        return "N/A"
    elif buscarClase(ip) == "Clase E":
        return "N/A"
    
def devolverMascara(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    ## if para devolver la mascara dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        return "255.0.0.0"
    elif buscarClase(ip) == "Clase B":
        return "255.255.0.0"
    elif buscarClase(ip) == "Clase C":
        return "255.255.255.0"
    elif buscarClase(ip) == "Clase D":
        return "N/A"
    elif buscarClase(ip) == "Clase E":
        return "N/A"
    
def devolverDirHosts(ip):
    # Verificar si la IP es válida
    if not ipValidation(ip):
        return "Dirección no válida"
    
    segundoOcteto = int(ip.split('.')[1])
    tercerOcteto = int(ip.split('.')[2])
    cuartoOcteto = int(ip.split('.')[3])

    ## if para devolver la direccion de hosts dependiendo de la clase
    if buscarClase(ip) == "Clase A":
        return "0."+str(segundoOcteto) + "." + str(tercerOcteto) + "." + str(cuartoOcteto)
    elif buscarClase(ip) == "Clase B":
        return "0.0." + str(tercerOcteto) + "." + str(cuartoOcteto)
    elif buscarClase(ip) == "Clase C":
        return "0.0.0." + str(cuartoOcteto)
    elif buscarClase(ip) == "Clase D":
        return "N/A"
    elif buscarClase(ip) == "Clase E":
        return "N/A"

def analizarIP(ip):
    if not ipValidation(ip):
        resultado = {"⚠️ Error⚠️": "Dirección no válida", "¡Recomedación!": "Verifica la IP ingresada."}
        return resultado
    # Crear un diccionario para almacenar los resultados
    resultado = {
        "Clase": buscarClase(ip),
        "Tipo": buscarTipo(ip),
        "Estructura": devolverEstructura(ip),
        "Dirección de Red": devolverDirRed(ip),
        "Dirección de Broadcast": devolverDirBroadcast(ip),
        "Máscara de Subred": devolverMascara(ip),
        "Dirección de Hosts": devolverDirHosts(ip)
    }
    
    return resultado

