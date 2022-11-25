import csv

#open and read the file after the appending:
f = open("bloque4.csv", "w")
min = 300000
max = 400000
with open('train.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = min
        for row in csv_reader:
            if(line_count < max):
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    number = row[4]
                  
                    try:
                        number = int(float(number))
                        print(number)
                    except:
                        number = -1

                    f.write(row[0]+','+ row[1] +','+ row[2]+','+row[3]+','+','+str(number)+'\n')
                    
                    line_count += 1
            else:
                print('primer bloque')
                break
           
f.close()
   