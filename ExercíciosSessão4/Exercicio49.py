"""
Faça um programa para ler o horário ( hora, minuto e segundo )
de inicio e a duração em segundos de uma experiencia biologica.
O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""
start_hour = int(input('Digite a hora que começou: '))
start_minute = int(input('Digite os minutos: '))
start_second = int(input('Digite os segundos: '))
duration = int(input('Digite a duração: '))

start_time_in_seconds = start_hour * 3600 + start_minute * 60 + start_second
end_time_in_seconds = start_time_in_seconds + duration

end_hour = (end_time_in_seconds // 3600) % 24
end_time_in_seconds %= 3600
end_minute = end_time_in_seconds // 60
end_time_in_seconds %= 60
end_second = end_time_in_seconds

print(f'Sua experiência teve a duração de: {end_hour} horas, {end_minute} minutos , e {end_second} segundos')