import pandas as pd

datasets = ["holidays_events.csv", "items.csv", "oil.csv","stores.csv","test.csv","train.csv","transactions.csv"]

## NoAm Model
# Store_OilPriceTable 
for csv in datasets:
    if csv == "oil.csv":
        oil_columns = pd.read_csv(csv, usecols=["date","dcoilwtico"])
    if csv == "transactions.csv":
        transactions_columns = pd.read_csv(csv, usecols=["date","store_nbr","transactions"])
Store_OilPriceTable = transactions_columns.merge(oil_columns, how='right', on='date')

# Create csv    
names = {'date':'oil_measure_date','dcoilwtico': 'oil_price', 'transactions':'store_transaction_count'}
Store_OilPriceTable.rename(columns=names).to_csv('NoAm/Store_OilPrice.csv',columns=["store_nbr","oil_measure_date","oil_price", "store_transaction_count"], index=False)

# Store_Holidays_SalesRecordTable 
for csv in datasets:
    if csv == "holidays_events.csv":
        holiday_events_columns = pd.read_csv(csv, usecols=["date","description","type","locale","locale_name"])
    if csv == "transactions.csv":
        transactions_columns = pd.read_csv(csv, usecols=["date","store_nbr","transactions"])

Store_Holidays_SalesRecordTable = holiday_events_columns.merge(transactions_columns, how='right', on='date')
print("Store_Holidays_SalesRecordTable\n")
print(Store_Holidays_SalesRecordTable)

# Create csv    
names = {'date':'record_date','transactions':'store_transaction_count', 'description':'celebration_description'}
Store_Holidays_SalesRecordTable.rename(columns=names).to_csv('NoAm/Store_Holidays_SalesRecord.csv',columns=["store_nbr","record_date","store_transaction_count", "celebration_description", "type","locale","locale_name"], index=False)
