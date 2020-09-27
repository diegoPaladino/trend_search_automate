#stocks_prices

# libraries
import investpy as inv
# declarations
# execution
preco = inv.get_stock_information('AGRO3','brazil')
print(preco)