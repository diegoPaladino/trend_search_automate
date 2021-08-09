# test_execution
# após varios meses deu certo graças às orientações extraidas da documentação do investpy: https://pypi.org/project/investpy/

################################################################
#importing libraries
import investpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from numpy.core.fromnumeric import var
from numpy.lib.function_base import _extract_dispatcher
import pyautogui as p
import time as t
from datetime import datetime
import tkinter as tk
import pyperclip

################################################################
#declarations
x = 2
y = 0

#buca codigo na lista de acoes do excel:

def seleciona_excel():
    p.moveTo(316,-24)
    p.click()
    t.sleep(0.2)
    print(datetime.now(), ' - excel selecionado (primeira vez)')

#copiando codigo da acao na lista de acoes do excel
def copia_cod():
    p.moveTo(280,179)
    p.doubleClick()
    t.sleep(0.3)
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    root = tk.Tk()
    root.withdraw()
    a = root.clipboard_get()
    print(datetime.now(), ' - ACAO copiado')
    
    
    
    
    


def copia_parecer():
    p.moveTo(334,-92,duration=0.3)
    p.doubleClick()
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    root = tk.Tk()
    root.withdraw()
    b = root.clipboard_get()
    # pyperclip.copy(b)
    print(datetime.now(), ' - PARECER copiado')
    
    

def cola_parecer_excel():
    p.moveTo(316,-24,duration=0.3)
    p.click()
    t.sleep(0.2)
    p.hotkey('esc')
    t.sleep(0.2)
    p.press('left')
    t.sleep(0.2)
    p.keyDown('ctrl')
    p.hotkey('v')
    p.keyUp('ctrl')
    t.sleep(0.3)
    p.hotkey('down')
    p.press('right')
    t.sleep(1)
    print(datetime.now(), ' - PARECER colado')
    
def exception():
    # p.hotkey('esc')
    # t.sleep(0.2)
    p.moveTo(x=1337, y=-851,duration=0.2)
    p.click()

def pesquisa():

    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    print(datetime.now(), ' - ACAO2 copiado')
    print(c)


    acao2 = c
    print(acao2)

    df_bolsa = investpy.get_stock_historical_data(stock=acao2,
                                            country='brazil',
                                            from_date='02/07/2021',
                                            to_date='05/08/2021')

    df_bolsa.index.names = ['Data']
    df_bolsa.columns = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Volume', 'Moeda']

    df_ = df_bolsa.copy(deep=True)

    df_['Data'] = df_.index.map(mdates.date2num)

    # compute the simple moving average
    df_['ema21'] = df_['Fechamento'].ewm(span=21, adjust=False).mean()

    print(df_)

    tendencia_alta=1
    for i in range(6):
        if(df_.ema21[-i-1] < df_.ema21[-i-2]):
            tendencia_alta=0

    print()
    if(tendencia_alta==1):
        # print(acao2 + ' está em tendência de alta!')
        print('SIM')
    else:
        # print(acao2 + ' não está em tendência de alta!')
        print('NÃO')

    ##############
    # Plot Chart #
    ##############


    # ohlc = df_[['Data', 'Abertura', 'Maximo', 'Minimo', 'Fechamento']]


    # f1, ax = plt.subplots(figsize=(10, 5))

    # # plot the candlesticks
    # candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # # plot the moving average lines
    # label_ = acao2.upper() + ' ma21'
    # ax.plot(df_.index, df_['ema21'], color='yellow', label=label_)
    # # ax.plot(df.index, df['ema100'], color = 'purple', label = 'ma100')

    # # other parameters
    # ax.grid(False)
    # ax.legend()

    # plt.title(acao2.upper() + ' : Gráfico Diário')

    # plt.show(block=True)

    # del (df_)

################################################################
#execution

p.moveTo(316,-24)
p.click()
t.sleep(1)
print(datetime.now(), ' - excel selecionado (primeira vez)')

# p.alert(text='vamos começar!', title='COMEÇO', button='OK')

while True:
    try:
        copia_cod()
        pesquisa()
        t.sleep(2)
        copia_parecer()
        cola_parecer_excel()
        # print(acao)
    except:
        print('Exception ')
        p.hotkey('esc')
        t.sleep(0.2)
        p.hotkey('down')
    #     continue
    # else:
    #     if c != "":
    #         print('eureka!')
        
    # else:
    #     print('eureka!')

    #     copia_cod()
    #     # clipboard()
    #     pesquisa()
    #     t.sleep(3)
    #     copia_parecer()
    #     cola_parecer_excel()
        
    #     # x+=1
        
    #     # break
    
    # except:
    # #     pass
    #     print('except!')
    #     # x+=1
