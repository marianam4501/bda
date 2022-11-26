import pandas as pd

table_name = input("Please enter the name of the table: ")

datasets = ["holidays_events.csv", "items.csv", "oil.csv","stores.csv","bloque1.csv","bloque2.csv","bloque3.csv","bloque4.csv","bloque5.csv","transactions.csv"]

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
    
    for csv in datasets:
        if csv == "items.csv":
            print("Reading items.csv...")
            items_columns = pd.read_csv(csv, usecols=["item_nbr","family","perishable"])
        if csv == "bloque1.csv":
            print("Reading train.csv → 1st block...")
            train_columns1 = pd.read_csv(csv, usecols=["id","date","store_nbr","item_nbr","unit_sales","onpromotion"])
        if csv == "bloque2.csv":
            print("Reading train.csv → 2nd block...")
            train_columns2 = pd.read_csv(csv, usecols=["id","date","store_nbr","item_nbr","unit_sales","onpromotion"])
        if csv == "bloque3.csv":
            print("Reading train.csv → 2nd block...")
            train_columns3 = pd.read_csv(csv, usecols=["id","date","store_nbr","item_nbr","unit_sales","onpromotion"])
        if csv == "bloque4.csv":
            print("Reading train.csv → 2nd block...")
            train_columns4 = pd.read_csv(csv, usecols=["id","date","store_nbr","item_nbr","unit_sales","onpromotion"])    
        if csv == "bloque5.csv":
            print("Reading train.csv → 2nd block...")
            train_columns5 = pd.read_csv(csv, usecols=["id","date","store_nbr","item_nbr","unit_sales","onpromotion"])  
    print("Finish reading train.csv")
    # Block 1
    block_number = "1"
    file_name = table_name + block_number + ".csv"
    print("Generating " + file_name + "...")
    SalesRecord_ItemsTable1 = items_columns.merge(train_columns1, how='right',on='item_nbr')
    names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    SalesRecord_ItemsTable1.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
    # Block 2
    block_number = "2"
    file_name = table_name + block_number + ".csv"
    print("Generating " + file_name + "...")
    SalesRecord_ItemsTable2 = items_columns.merge(train_columns2, how='right',on='item_nbr')
    names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    SalesRecord_ItemsTable2.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
    # Block 3
    block_number = "3"
    file_name = table_name + block_number + ".csv"
    print("Generating " + file_name + "...")
    SalesRecord_ItemsTable3 = items_columns.merge(train_columns3, how='right',on='item_nbr')
    names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    SalesRecord_ItemsTable3.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
    # Block 4
    block_number = "4"
    file_name = table_name + block_number + ".csv"
    print("Generating " + file_name + "...")
    SalesRecord_ItemsTable4 = items_columns.merge(train_columns4, how='right',on='item_nbr')
    names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    SalesRecord_ItemsTable4.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
    # Block 5
    block_number = "5"
    file_name = table_name + block_number + ".csv"
    print("Generating " + file_name + "...")
    SalesRecord_ItemsTable5 = items_columns.merge(train_columns5, how='right',on='item_nbr')
    names = {'id': 'record_id', 'date':'record_date','perishable':'item_perishable','family':'item_family','onpromotion':'record_on_promotion','unit_sales':'record_unit_sales','store_nbr':'store_number'}
    SalesRecord_ItemsTable5.rename(columns=names).to_csv('NoAm/'+file_name,columns=["item_nbr","record_id","record_date","item_perishable","item_family","record_on_promotion","record_unit_sales","store_number"], index=False)
    
    print("Finish reading train.csv")
#NoSe model
else:
    print("Invalid table name. ")
