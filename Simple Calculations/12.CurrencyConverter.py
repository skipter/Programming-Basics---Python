value = float(input())
inputCurrency = input()
outputCurrency = input()

bgnValue = 1
usdValue = 1.79549
euroValue = 1.95583
gbpValue = 2.53405

currentValue = 0

if inputCurrency=='USD':
    currentValue = value * usdValue
elif inputCurrency=='EUR':
    currentValue = value * euroValue
elif inputCurrency=='GBP':
    currentValue = value * gbpValue
elif inputCurrency=='BGN':
    currentValue = value * bgnValue

result = 0
strValue = None
if outputCurrency=='USD':
    result = currentValue / usdValue
    strValue = 'USD'
elif outputCurrency=='EUR':
    result = currentValue / euroValue
    strValue = 'EUR'
elif outputCurrency=='GBP':
    result = currentValue / gbpValue
    strValue = 'GBP'
elif outputCurrency=='BGN':
    result = currentValue * bgnValue
    strValue = 'BGN'
print()
print("{0:.02f} ".format(result),strValue)