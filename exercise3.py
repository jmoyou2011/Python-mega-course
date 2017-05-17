from CeltoFah import C_F, F_C

temperatures = [10, -20, -289, 100]

for i in temperatures:
    if i < -273.15:
        print("This is not physically possible and you have destroyed the universe. Goodbye")
    else:
        print(C_F(i))
