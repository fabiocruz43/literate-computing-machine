

bind = '127.0.0.1:5000'  # Endereço e porta que o Gunicorn irá utilizar
workers = 2               # Número de workers para lidar com solicitações
threads = 4               # Número de threads por worker
timeout = 120             # Tempo limite em segundos para requisições
