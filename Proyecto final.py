# tabla de multiplicar
for i in range (1,13):
    for j in range(1,13):
        for k in range(1,13):
            print(i, "x", j, "x", k, "=", i*j*k)
        print("***********Fin for k****")
    print("***********Fin for j****")  
print("***********Fin for i****")             
