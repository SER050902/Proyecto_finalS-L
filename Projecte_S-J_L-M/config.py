import os


ggm_init = os.listdir('../Projecte_S-J_L-M')
ggm_classificat = os.chdir('../Projecte_S-J_L-M/S-L_dst')
mida_mitjana = 17
mida_petita = 10



extension = ['pdf','txt','bin']

configuracion = {
    "DIR_INIT": f'{ggm_init}',
    "DIR_DST": f'{ggm_classificat}',
    "MIDA_PETITA": f'{mida_mitjana}' + 'MB',
    "MIDA_MITJANA": f'{mida_mitjana}' + 'MB',
    "EXTENSIO_FILTRADA": f'{extension}'
}



def Carregar_config():
    global configuracion,extension
    archivo = input('Introduce el nombre del archivo: ')
    try:
        with (open(archivo, 'r') as file):
            contenido = file.read()
            if archivo != extension:
                print('el pdf es extension filtrado')
                if archivo.endswith('.txt'):
                    print('Contenido del archivo', archivo, ':')
            else:
                print('No se puede abrir el archivo',archivo)
            print(contenido)
    except FileNotFoundError:
        print('El archivo', archivo, 'no existe.')




def veure_config():
    global configuracion
    print(configuracion,'\n')
    with open('config.cfg') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())

def guardar_config():
    global configuracion
    with open('config.cfg', 'w') as f:
        f.write(str(configuracion))


def cambiar_parametros():
    print('LA INFORMACION DE', ggm_init)
    veure_config()
    clave = input("Quin paràmetre vols canviar? (Escriu el nom del paràmetre): ")
    if clave not in configuracion:
        print("La clau", clave, "no existeix a la configuració.")
        return
    print("El valor actual de", clave, "és:", configuracion[clave])
    nou_valor = input("Introdueix el nou valor per a " + clave + ": ")

    if nou_valor:
        if clave == 'MIDA_PETITA' and int(nou_valor) > 10:
            print('El valor debe ser igual o menor que 10.')
        else:
            if clave == 'MIDA_MITJANA' and (int(nou_valor) < 10 or int(nou_valor) > 17):
                print('El valor debe estar entre 10 y 17.')
            else:
                configuracion[clave] = nou_valor
                print("El valor de", clave, "s'ha canviat a:", configuracion[clave])
                guardar_config()
                veure_config()
                print("Cambiado correctamente")


def mostrar_configuraciones():
    global configuracion
    print("Valors actuals de la configuració:")
    for clave, valor in configuracion.items():
        print(clave, "=", valor)

print(configuracion)
