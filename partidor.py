import csv

#open and read the file after the appending:
first_row = True
max = 100000
block_num = 1
file_name = "bloque" + str(block_num) + ".csv"
f = open(file_name, "w")
with open('train.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if first_row:
                    columns = f'{",".join(row)}\n'
                    print("Column names are " +columns)
                    f.write(columns)
                    first_row = False

            else:
                number = row[4]
                  
                try:
                    number = int(float(number))

                except:
                    number = -1

                f.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+','+str(number)+'\n')
                
                print(line_count)
                line_count += 1
            
            if line_count == max:
                f.close()
                print("Done with " + str(block_num) + "...")

                if max == 500000:
                    break

                else:
                    max += 100000
                    block_num += 1
                    file_name = "bloque" + str(block_num) + ".csv"
                    f = open(file_name, "w")
                    f.write(columns)
           

   