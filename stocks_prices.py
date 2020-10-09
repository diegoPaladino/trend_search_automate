#stocks_prices

# libraries
import investpy as inv
# declarations
# execution
preco = inv.get_stock_company_profile('IBFF11','brazil')
print(preco)