def perkalian():
    input_a = int(input("Masukkan nilai a:"))
    input_b = int(input("Masukkan nilai b:"))
    
    for i in range (input_a):
        if i == 0: 
            print(f"{input_a} x {input_b} = {input_b} +", end=" ")
        elif i != input_a - 1:
            print(f"{input_b}", end=" + ")
        else:
            print(f"{input_b} =", input_a * input_b)
            
perkalian()



    
    