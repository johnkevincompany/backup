from datetime import date, datetime

input_data_venc = input('DATA VENCIMENTO: ')
input_data_pag = input('DATA PAGAMENTO: ')

data_venc = datetime.strptime(input_data_venc, '%d/%m/%Y')
data_pag = datetime.strptime(input_data_pag, '%d/%m/%Y')

diferenca = data_venc.date() - data_pag.date()
print(diferenca.days) # diferença em dias






