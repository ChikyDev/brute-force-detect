"""
Analizador de intentos de acceso fallidos en el archivo de log de autenticación.

Este script lee el archivo /var/log/auth.log (o el especificado en 'host') y analiza
las líneas que contienen "Failed password" para contar los intentos de acceso fallidos
por IP, puerto y usuario. Si una IP tiene más de 10 intentos, se considera un ataque
de fuerza bruta y se sugiere bloquearla con ufw.

Nota: Este script está diseñado para sistemas Linux. Para Windows, ajustar la ruta del log.
"""

# Diccionarios para almacenar los conteos
ips = {}  # Contador de intentos por dirección IP
ports = {}  # Contador de intentos por puerto
user = {}  # Contador de intentos por usuario

# Ruta al archivo de log (ajustar según el sistema operativo)
host = "/var/log/auth.log"

# Abre el archivo de log y procesa cada línea
with open(host) as file:
    for line in file:
        # Verifica si la línea contiene un intento de contraseña fallido
        if "Failed password" in line:
            print(line)  # Imprime la línea completa para depuración
            # Extrae la IP (posición 10 en la línea dividida)
            ip = line.split()[10]
            # Extrae el puerto (posición 12)
            p = line.split()[12]
            # Extrae el usuario (posición 8)
            u = line.split()[8]

            # Si la IP ya está en el diccionario, incrementa los contadores
            if ip in ips:
                ips[ip] += 1
                ports[p] += 1
                user[u] += 1
            else:
                # Si es la primera vez que aparece la IP, inicializa los contadores
                ips[ip] = 1
                ports[p] = 1
                user[u] = 1

# Imprime los resultados para cada IP
for ip, intentos in ips.items():
    print(ip, "-->", intentos, "Intentos")
    print("Puertos afectados:", p)  # Nota: 'p' es del último procesamiento, no específico por IP
    # Si los intentos superan 10, analiza como posible ataque de fuerza bruta
    if intentos > 10:
        print("\n=== ANALISIS TOTAL ===")
        print("Brute force detected")
        print("IP:", ip)
        print("Puertos afectados:", p)
        print("Usuario afectado:", u)  # Nota: 'u' es del último procesamiento
        print(f"Comando requerido: sudo ufw deny from {ip}")