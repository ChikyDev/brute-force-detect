# SSH Failed Password Log Analyzer

Script en Python para analizar intentos fallidos de autenticación SSH a partir del archivo `/var/log/auth.log`.

El programa recorre el log del sistema, detecta eventos de **"Failed password"**, extrae información relevante como la **dirección IP**, el **puerto** y el **usuario**, y muestra un análisis básico para identificar posibles intentos de **fuerza bruta**.

## Características

- Lectura automática del archivo `/var/log/auth.log`
- Detección de intentos fallidos de contraseña en SSH
- Conteo de intentos por:
  - Dirección IP
  - Puerto
  - Usuario
- Identificación básica de posibles ataques de fuerza bruta
- Sugerencia de comando para bloquear una IP con `ufw`

## Tecnologías usadas

- Python 3
- Diccionarios
- Lectura de archivos
- Análisis básico de logs

## Requisitos

- Python 3 instalado
- Sistema Linux con archivo de log en:

```bash
/var/log/auth.log
```

- Permisos suficientes para leer el archivo de log

## Ejecución

Guarda el script en un archivo, por ejemplo:

```bash
brute-force-dt.py
```

Y ejecútalo con:

```bash
python3 brute-force-dt.py
```

## ¿Qué analiza?

El script busca líneas que contengan:

```text
Failed password
```

A partir de esas líneas, extrae:

- **IP atacante**
- **Puerto usado**
- **Usuario objetivo**

Después cuenta los intentos y, si una IP supera los **10 intentos**, la marca como posible ataque de fuerza bruta.

## Ejemplo de salida

```text
203.0.113.45 --> 14 Intentos
Puertos afectados: 22

=== ANALISIS TOTAL ===
Brute force detected
IP: 203.0.113.45
Puertos afectados: 22
Usuario afectado: root
Comando requerido: sudo ufw deny from 203.0.113.45
```

## Objetivo del proyecto

Este proyecto está orientado a practicar:

- manejo de archivos en Python
- uso de diccionarios
- análisis de logs
- automatización básica en ciberseguridad
- detección inicial de actividad sospechosa en sistemas Linux

## Autor

Desarrollado por **ChikyDev**

## Licencia

Este proyecto puede usarse con fines educativos y de práctica personal.
