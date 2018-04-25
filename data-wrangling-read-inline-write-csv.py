import csv
import sys

reader=csv.reader(sys.stdin,delimiter = "\t")
writer=csv.writer(sys.stdout,delimiter="\t")

def writeCsv():
    for line in reader:
        writer.writerow()
        
test_text = """abcxyz
abjhsfbdkhjbvfbbjbjbb
"""

def main():   
    import stringIO
    sys.stdin = stringIO.StringTO(test_text)
    writeCsv()
    sys.stdin = sys.__stdin__
    
if '__name__' == '__main__':
    main()

