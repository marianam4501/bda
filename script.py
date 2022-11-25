import pandas as pd
import csv

table_name = input("Please enter the name of the table: ")
#number_of_rows = int(input("Please enter the number of rows: "))
#print("Generating " + str(table_name) + ".csv with " + str(number_of_rows)+" rows...")

datasets = ["holidays_events.csv", "items.csv", "oil.csv","stores.csv","test.csv","train.csv","transactions.csv"]

## NoAm Model
if table_name == "Store_Holidays_SalesRecord":
    file_name = table_name + ".csv"
    print("Generating " + file_name + "...")
    for csv in datasets:
        if csv == "holidays_events.csv":
            holiday_events_columns = pd.read_csv(csv, usecols=["date","description","type","locale","locale_name"])
        if csv == "transactions.csv":
            transactions_columns = pd.read_csv(csv, usecols=["date","store_nbr","transactions"])
    Store_Holidays_SalesRecordTable = holiday_events_columns.merge(transactions_columns, how='right', on='date')
    names = {'date':'record_date','transactions':'store_transaction_count', 'description':'celebration_description'}
    Store_Holidays_SalesRecordTable.rename(columns=names).to_csv('NoAm/'+file_name,columns=["store_nbr","record_date","store_transaction_count", "celebration_description", "type","locale","locale_name"], index=False)

elif table_name == "Store_OilPrice":
    file_name = table_name + ".csv"
    print("Generating " + file_name + "...")
    for csv in datasets:
        if csv == "oil.csv":
            oil_columns = pd.read_csv(csv, usecols=["date","dcoilwtico"])
        if csv == "transactions.csv":
            transactions_columns = pd.read_csv(csv, usecols=["date","store_nbr","transactions"])
    Store_OilPriceTable = transactions_columns.merge(oil_columns, how='right', on='date')
    names = {'date':'oil_measure_date','dcoilwtico': 'oil_price', 'transactions':'store_transaction_count'}
    Store_OilPriceTable.rename(columns=names).to_csv('NoAm/'+file_name,columns=["store_nbr","oil_measure_date","oil_price", "store_transaction_count"], index=False, float_format='%.0f')

elif table_name == "SalesRecord_Items":
    file_name = table_name + ".csv"
    print("Generating " + file_name + "...")
    for csv2 in datasets:
        if csv2 == "items.csv":
            print("Reading items.csv...")
            items_columns = pd.read_csv(csv2, usecols=["item_nbr","family","perishable"])
        if csv2 == "train.csv":
            print("Reading train.csv...")
            
        with open('train.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if(line_count < 100000):
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        print(f'\t{row[0]} , {row[1]} , {row[2]}, {row[3]}, {row[4]}, {row[5]}')
                        line_count += 1
                else:
                    print('primer bloque')
                    exit()
            print(f'Processed {line_count} lines.')
            
    print("Finish reading train.csv")
    # SalesRecord_ItemsTable = items_columns.merge(train_columns, how='right',on='item_nbr')
    # names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    # SalesRecord_ItemsTable.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
else:
    print("Invalid table name. ")
