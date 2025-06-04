def trancos( ):
    print('—' * 50)

nomes = ["Joaquim", "Maria","Ana"]

trancos( )
print(nomes [0] )  
print(nomes [1] )
print(nomes [2] )
trancos( )

nomes[0] = "João" 

trancos( )
print(nomes [0] )             
print(nomes [1] )             
print(nomes [2] )            
trancos( )

nomes.append("Marcos")
nomes.append("Joana")


trancos( )
print(nomes [0] )  
print(nomes [1] )
print(nomes [2] )  
print(nomes [3] )
print(nomes [4] )
trancos( )


trancos( )

print("lista inicial:",nomes)
trancos( )

nomes.append("Carlos")
print("Após append:", nomes)
trancos( )

nomes.insert(1, "Fernanda")
print("Após insert:",nomes)
trancos( )

nomes[2] = "Ana"
print("Após modificação:", nomes)
trancos( )


del nomes[3]
print("Após del:", nomes)
trancos( )

nomes.remove("Ana")
print("Após remove :",nomes)
trancos( )

removido = nomes.pop(2)
print(f"Após  pop (removido ' {removido}'):", nomes)
trancos( )

nomes.clear()
print("Após clear :", nomes)
trancos( )
