from SnmpFunctions import *
from TrapsDecoder import *
# 1.3.6.1.2.1.2.2.1.2  : Interfaces
# 1.3.6.1.2.1.2.1.0    : Number of interfaces
# 1.3.6.1.2.1.1.5.0    : Hostname
run = True

print("BIENVENIDO")
#rwCommunityString = input("Ingresa el nombre de la comunidad RW")
community = hlapi.CommunityData('escom')

while run:
    print("1.- Get")
    print("2.- Get Bulk")
    print("3.- Editar opción")
    print("4.- Ver traps")
    option = int(input())
    if option == 1:
        ip = input("Ingresa la ip del agente")
        oid = input("Ingresa el OID deseado")
        result = get(ip, [oid], hlapi.CommunityData(community))
        print(result)
    elif option == 2:
        ip = input("Ingresa la ip del agente")
        oid = input("Ingresa el OID deseado")
        countOid = input("Ingresa el OID para contar las entradas")
        its = get_bulk_auto(ip, [oid], community, countOid)
        for it in its:
            for k, v in it.items():
                print("{0}={1}".format(k, v))
            print('')
    elif option == 3:
        ip = input("Ingresa la ip del agente")
        oid = input("Ingresa los OID deseados")
        value = input("Ingresa el valor deseado")
        set(ip, {oid: value}, community)
        print("Valor editado")
    elif option == 4:
        translateTraps('/etc/var/log/traps.log')