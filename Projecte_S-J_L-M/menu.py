import config


def menu_configuración():
    while True:
        print('\n\tMENU configuración')
        print('1. veure_config')
        print('2. Carregar config')
        print('3. Canviar paràmetres')
        print('4. Desar config')
        print('5. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            config.veure_config()
        elif opcion == 2:
            config.Carregar_config()
        elif opcion == 3:
            config.cambiar_parametros()
        else:
            print('Opción no válida. Por favor, elige una opción válida.')

while True:
    print('\n\tMENU PRINCIPAL: \n')
    print('1. Configuración')
    print('2. creacio de directoris')
    print('3. classificacio arxius')
    print('4. filtratge')
    print('5. canvis de propietari i de permisos')
    print('6. comprovació')
    print('7. compressió')
    print('8. creació d’informe')
    print('0. Salir')
    opcion = -1
    while opcion not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        opcion = int(input('Opción: '))
    if opcion == 1:
        menu_configuración()
    else:
        break
