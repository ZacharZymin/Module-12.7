
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму для расчета депозита: '))

bank1 = per_cent['ТКБ']/100*money
bank2 = per_cent['СКБ']/100*money
bank3 = per_cent['ВТБ']/100*money
bank4 = per_cent['СБЕР']/100*money

deposit = round(bank1), round(bank2), round(bank3), round(bank4)

deposit_max = max(deposit)


print( deposit )
print( deposit_max )
