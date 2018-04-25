import sys
for line in sys.stdin:
        flag=0;
        for el in line:
            for s in ['.','?','!']:
                if s in el and el != line[len(line)-1]: flag+=1
        if flag== 0:  
           writer.writerow(line) 
