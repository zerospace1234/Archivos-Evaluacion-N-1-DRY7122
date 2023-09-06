ACL = int(input("Colocar el numero de IPV4 ACL:"))
if ACL >= 1 and ACL <= 99:
    print ("Esto es una ACL estandar.")
elif ACL >= 100 and ACL <= 199:
    print ("Esto es una ACL extendida.")
else:
    print ("Esto no es una ACL ni extendida o estandar.")