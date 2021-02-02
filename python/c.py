from os import system, name
import sys
from time import sleep
import platform
import colorama
from colorama import Fore, Back, Style
import sys
import termcolor
from termcolor import colored, cprint
from datetime import date, datetime
import keyboard
from webbrowser import open
lb = ('\033[94m')

def clear():
    if name == 'nt': 
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

opcao = 0
while opcao != 5:
    clear()

    banner = colored('''8888888b.          d8b                                 888                        \n888   Y88b         Y8P                                 888                        \n888    888                                             888                        \n888   d88P 888d888 888 .d8888b  88888b.d88b.   8888b.  88888b.   .d88b.  888  888 \n8888888P"  888P"   888 88K      888 "888 "88b     "88b 888 "88b d88""88b `Y8bd8P' \n888        888     888 "Y8888b. 888  888  888 .d888888 888  888 888  888   X88K   \n888        888     888      X88 888  888  888 888  888 888 d88P Y88..88P .d8""8b. \n888        888     888  88888P' 888  888  888 "Y888888 88888P"   "Y88P"  888  888 \n\n''')
    cprint(banner,'blue', attrs=['bold'])
    header = colored('Bem-vindo à calculadora de Juros/Multa Prismabox!','blue', attrs=['bold'])
    print(header)
    print('''\n\nEscolha uma das opções para continuar:\n
    [ 1 ] Calcular
    [ 2 ] Tutorial
    [ 3 ] Ajuda
    [ 4 ] Info
    [ 5 ] Sair''')
    opcao = int(input('Qual é a sua opção? '))
#---------------------------------------------------------------------------------------------------
    if opcao == 1:
        class Percent(float):
            def __str__(self):
                return '{:.3%}'.format(self)
        clear()
        o = None
        jm = None
        m = None
        while o is None:
            try:
                 o = float(input('\nValor Original:    R$'))
            except ValueError:
                print("Opa! Utilize . para separar unidades,e apenas números")

        while jm is None:
            try:
                jm = float(input('\n\nPercentual Juros a.m. (SOMENTE NÚMEROS):   '))
            except:
                print("Opa! Utilize . para separar unidades, e apenas números")
        jd = (jm/30)
        jd_percent = Percent(jd/100)
        print('% Juros por dia: ',jd_percent)

        while m is None:
            try:
                m = float(input('\n\nPercentual Multa (SOMENTE NÚMEROS):    '))
            except:
                print("Opa! Utilize . para separar unidades, e apenas números")
        m_percent = Percent(m/100)
        print('% Multa por mês: ',m_percent)
        
        while True:
            venc_str = str(input('\nData de Vencimento:  '))
            b_str = str(input('Data Baixa:   '))
            try:
                data_venc = datetime.strptime(venc_str, '%d/%m/%Y')
                data_b = datetime.strptime(b_str, '%d/%m/%Y')
                break
            except ValueError as ve:
                print('Formato de Data inválido, tente novamente.\n Exemplo: 22/10/2021 (DD/MM/AAAA)')

        print('\n\nData de Vencimento: ',venc_str)
        print('Data Baixa: ',b_str)
        atraso = data_b.date() - data_venc.date()
        cprint('Dias de atraso: {}'.format(atraso.days),'magenta',attrs=['bold'])

        m_total = o * m_percent
        cprint('Multa Total = R${}'.format(m_total),'red',attrs=['bold'])

        j_total = atraso.days * jd_percent * o
        cprint('Juros total = R${:.2}'.format(j_total),'cyan',attrs=['bold'])

        jem = j_total + m_total
        cprint('Juros e Multa total = R${:.2}'.format(jem),'cyan','on_red', attrs=['bold'])

        om = float(o + jem)
        cprint('Valor da cobrança com Juros/Multa = R${:.2f}'.format(om), 'green',attrs=['bold'])

        print('\n\nPressione Enter para continuar...')
        input(keyboard.wait("enter"))

#----------------------------------------------------------------------------------------------

    elif opcao == 2:
        clear()
        ex = colored('Exemplo:','red')

        cprint('\nBem vindo ao tutorial Prismabox de Juros/Multa!\n\n','blue', attrs=['bold'])

        cprint('- Juros e Multa são porcentagens mensais,na qual, são enviados para o sistema de cobrança \n  e aplicados automaticamente de acordo com a data de pagamento.\n')
        cprint('- Ambos os valores são definidos pelo usuário ao gerar o contrato, na seção Parametrização Financeira,\n  no sistema Prismabox.\n')
       
        cprint('Exemplo:\n','green')
        cprint('Valor Original:','blue',attrs=['bold'],end=' ') 
        cprint('R$Valor original (acordada no contrato ou anterior ao Juros/Multa) da cobrança em questão\n')

        cprint('Percentual Juros a.m.:','blue',attrs=['bold'],end=' ')
        cprint('Percentual de Juros, acordado em contrato. Insira este valor somente em números.\n(valor referido na seção Parametrização Financeira, na aba principal do contrato).\n{} 1 para 1% Juros a.m.;\n'.format(ex))

        cprint('Percentual Multa:','blue',attrs=['bold'],end=' ')
        cprint('Percentual de Multa, acordado em contrato. Insira este valor somente em números.\n(valor referido na seção Parametrização Financeira, na aba principal do contrato).\n{} 2 para 2% Multa a.m.;\n'.format(ex))

        cprint('Data de Vencimento:','blue',attrs=['bold'],end=' ')
        cprint('Data de vencimento da cobrança. (data de pagamento acordado em contrato, podendo ser alterado pelo usuário\n ou pela existência de feriados, postergando assim, a data original.\n{} Data de Pagamento (acordado): 02/10/2021.\n         Data de vencimento(sem ser postergado): 02/10/2021.\n'.format(ex))

        cprint('Data Baixa:','blue',attrs=['bold'],end=' ')
        cprint('Data da baixa da cobrança. (data de pagamento realizado pelo cliente, sendo automática (ASAAS) e manual.\n{} Data de Pagamento (realizado pelo cliente): 02/10/2021.\n         Data Baixa: 02/10/2021.\n'.format(ex))

        cprint('Valor da cobrança com Multa/Juros:','blue',attrs=['bold'],end=' ')
        cprint('R$Valor original + Valor Juros/Multa (Juros/Multa é calculado a partir dos dias de atraso) da cobrança em questão\n{} Juros/Multa: R$2.48.\n         Valor da cobrança com Juros/Multa: Valor Original + R$2.48.\n'.format(ex))


        print('\n\nPressione Enter para continuar...')
        input(keyboard.wait("enter"))

    elif opcao == 3:
        clear()
        ex = colored('Exemplo:','red')

        cprint('\nBem vindo à Ajuda Prismabox de Juros/Multa!\n\n','blue', attrs=['bold'])

        cprint('Valor Original:','blue',attrs=['bold'],end=' ') 
        cprint('R$Valor original (acordada no contrato ou anterior ao Juros/Multa) da cobrança em questão\n')

        cprint('Percentual Juros a.m.:','blue',attrs=['bold'],end=' ')
        cprint('Percentual de Juros ao mês, em caso de atraso. Insira este valor somente em números.\n{} 1 para 1% Juros a.m.;\n'.format(ex))

        cprint('Percentual Juros ao dia:','blue',attrs=['bold'],end=' ')
        cprint('Percentual de Juros ao dia, em caso de atraso. Sendo o valor mensal dividido por 30\n{} 1 para 1%/30 = 0,033% ao dia.\n'.format(ex))

        cprint('Percentual Multa:','blue',attrs=['bold'],end=' ')
        cprint('Percentual de Multa, acordado em contrato. Insira este valor somente em números.\n{} 2 para 2% Multa a.m.;\n'.format(ex))

        cprint('Data de Vencimento:','blue',attrs=['bold'],end=' ')
        cprint('Data de vencimento da cobrança.\n')

        cprint('Data Baixa:','blue',attrs=['bold'],end=' ')
        cprint('Data da baixa da cobrança.\n')

        cprint('Valor da cobrança com Multa/Juros:','blue',attrs=['bold'],end=' ')
        cprint('R$Valor original + Valor Juros/Multa da cobrança em questão\n')

        print('\n\nPressione Enter para continuar...')
        input(keyboard.wait("enter"))

    elif opcao == 4:
        clear()

        cprint('\nCalculadora desenvolvida para a optimização de cálculos relacionados à Juros/Multa de cobranças.\n','white')

        cprint('Desenvolvido por:','blue', attrs=['bold'])
        cprint('     ___  _______  __   __  __    _    ___   _  _______  __   __  ___   __    _ \n    |   ||       ||  | |  ||  |  | |  |   | | ||       ||  | |  ||   | |  |  | |\n    |   ||   _   ||  |_|  ||   |_| |  |   |_| ||    ___||  |_|  ||   | |   |_| |\n    |   ||  | |  ||       ||       |  |      _||   |___ |       ||   | |       |\n ___|   ||  |_|  ||       ||  _    |  |     |_ |    ___||       ||   | |  _    |\n|       ||       ||   _   || | |   |  |    _  ||   |___  |     | |   | | | |   |\n|_______||_______||__| |__||_|  |__|  |___| |_||_______|  |___|  |___| |_|  |__|\n','blue',attrs=['bold'])

        site = 'https://prismabox.com.br/'
        cprint('\n\nPara mais informações, acesse: {}\n\n'.format(site),'magenta')

        print('Todos os direitos reservados.')
        cprint('2021 © Prisma Box','cyan')

        print('\n\nPressione Enter para continuar...')
        input(keyboard.wait("enter"))


    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
        
print('Fim do programa, volte sempre!')