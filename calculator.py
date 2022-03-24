
#!/usr/bin/python3
from pickle import FALSE, TRUE
import sys
import getopt

def printArgHelp():
    print('meter-mult-calculator.py -r1 <reading 1> -r2 <reading 2> -mr <meter read> -fr <flume read> -cm <current mult> -h <help>')

def main(argv):
    ## Check the args
    if len(argv) < 3:
        printArgHelp()
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv, "r1:r2:mr:fr:cm:h",["read1=","read2=","meter_read=","flume_read=","current_mult="])
    except getopt.GetoptError:
        printArgHelp()
        sys.exit(2)

    ## Parse the args
    must_calc_delta = FALSE
    meter_read1 = 0
    meter_read2 = 0
    meter_delta = 0
    flume_read = 0
    current_mult = 0
    for opt, arg in opts:
        if opt == '-h':
            printArgHelp()
            sys.exit()
        elif opt in ("-r1", "--read1"):
            meter_read1 = float(arg)
            must_calc_delta = TRUE
        elif opt in ("-r2", "--read2"):
            meter_read2 = float(arg)
        elif opt in ("-mr", "--meter_read"):
            meter_delta = float(arg)
        elif opt in ("-fr", "--flume_read"):
            flume_read = float(arg)
        elif opt in ("-cm", "--current_mult"):
            current_mult = float(arg)

    if must_calc_delta == TRUE:
        meter_delta = meter_read2 - meter_read1
    
    pct_diff = (flume_read - meter_delta) / flume_read
    projected_mult = (1 - pct_diff) * current_mult
    print("Accuracy test results:\nmeter delta: " + str(meter_delta))
    print("flume delta: " + str(flume_read))
    print("current mult: " + str(current_mult))
    print("projected mult: " + str(projected_mult))

if __name__ == "__main__":
    main(sys.argv[1:])