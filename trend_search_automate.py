#trend_search_automate

#Stock_Trend_Identificator_Python
#title of tutorial: COMO IDENTIFICAR AÇÕES EM TENDÊNCIA DE ALTA AUTOMATICAMENTE | Análise Técnica e Python #3
#link of tutorial: https://www.youtube.com/watch?v=i6x8GaabMa0
#link of iHack page: https://ihack.com.br/at_003.php

#importing libraries
import investpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# from mpl_finance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
# comment

acao2 = 'IVVB11'

df_bolsa = investpy.get_stock_historical_data(stock=acao2,
                                          country='brazil',
                                          from_date='01/01/2020',
                                          to_date='08/08/2021')

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
    print(acao2 + ' está em tendência de alta!')
else:
    print(acao2 + ' não está em tendência de alta!')

##############
# Plot Chart #
##############


ohlc = df_[['Data', 'Abertura', 'Maximo', 'Minimo', 'Fechamento']]


f1, ax = plt.subplots(figsize=(10, 5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# plot the moving average lines
label_ = acao2.upper() + ' ma21'
ax.plot(df_.index, df_['ema21'], color='yellow', label=label_)
# ax.plot(df.index, df['ema100'], color = 'purple', label = 'ma100')

# other parameters
ax.grid(False)
ax.legend()

plt.title(acao2.upper() + ' : Gráfico Diário')

plt.show(block=True)

del (df_)