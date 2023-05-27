# pip install speedtest-cli

import speedtest

teste = speedtest.Speedtest()

# Download
print('Testando o Download')
velocidade_download = teste.download()
print(f'Velocidade de download: {velocidade_download / 10**6:.2f}')

# Upload
print('Testando o Upload')
velocidade_upload = teste.upload()
print(f'Velocidade de upload: {velocidade_upload / 10 ** 6:.2f}')

# Ping
ping = teste.results.ping
print(f'Ping: {ping:.2f}') 