temperature_c = input('輸入攝氏溫度')
temperature_c = float(temperature_c) #Casting : str cast to float

temperature_f = (temperature_c * 9) / 5 + 32

print('華氏溫度: ',temperature_f)