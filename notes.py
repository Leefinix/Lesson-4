a = int(input("How much rupiah do you want to withdraw: "))

note1= a//100
note2= (a%100)//50
note3= ((a%100)%50)//10

print("Notes of Rp100.000,00: ", note1)
print("Notes of Rp50.000,00: ", note2)
print("Notes of Rp10.000,00: ", note3)