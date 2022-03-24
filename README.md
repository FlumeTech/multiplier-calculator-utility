# multiplier-calculator-utility
A python command line utility to calculate suggested multipliers form accuracy test results

# Dependencies
`Python3`

# Usage
Example usage in Ubuntu WSL 20.04:
```
python3 ./calculator -h
```
will print the help menu like so:
```meter-mult-calculator.py USAGE:
--read1=<meter read 1>
--read2=<meter read 2>
--meter_read=<meter delta (bypass reads)>
--flume_read=<flume delta>
--current_mult=<current multiplier>
```

You can either provide raw meter readings via `--read1 && --read2` arguments, or you can just provide the meter delta through the `--meter_read` arguments.
`--flume_read` and `--current_mult` are mandtory arguments.

Full example:
```
python3 ./calculator.py --meter_read=411.429 --flume_read=739.00052 --current_mult=0.02526079
```
output:
```Accuracy test results:
meter delta: 411.429
flume delta: 739.00052
current mult: 0.02526079
projected mult: 0.014063618749429296
```
