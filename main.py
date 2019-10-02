from detect_ath import CountWeirdo, ReadData

read_data = ReadData('data')
x_fa, x_bu = read_data.read_data()
data = x_fa
test = CountWeirdo(data)
result = test.Get_Tendency()

print(result)