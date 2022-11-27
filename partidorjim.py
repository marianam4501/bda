import csv

#open and read the file after the appending:
first_row = True
max = 85000
block_num = 1
block_num2 = 2
block_num3 = 3
file_name = "bloque" + str(block_num) + ".csv"
file_name2 = "bloque" + str(block_num2) + ".csv"
file_name3 = "bloque" + str(block_num3) + ".csv"
f = open(file_name, "w")
f2 = open(file_name2, "w")
f3 = open(file_name3, "w")
with open('NoAm/Store_OilPrice.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if first_row:
                    columns = f'{",".join(row)}\n'
                    print("Column names are " +columns)
                    f.write(columns)
                    f2.write(columns)
                    f3.write(columns)
                    first_row = False

            else:
                if line_count <= 24999:
                    f.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')
                    f2.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')
                    f3.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')

                elif line_count <= 44999:
                    f2.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')
                    f3.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')

                elif line_count <= 84999:
                    f3.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+'\n')
                  
                line_count += 1
            
            if line_count == max:
                f.close()
                f2.close()
                f3.close()
           

   