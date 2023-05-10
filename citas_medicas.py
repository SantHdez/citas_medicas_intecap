#inicio

def agregar_citas(file, dpi, fecha,hora,especialidad):
    

    try: 
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(dpi + ',' + fecha + ','+ hora + ','+ especialidad+'\n')
        f.close()
        return('La cita se ha añadido.\n')
    
    

    
def buscar_cita(file, dpi):
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        for line in directory:
            cita = line.strip().split(',')
            if cita[0] == dpi:
                return ', '.join(cita[1:])
        return('¡El cliente ' + dpi + ' no tiene citas programadas!\n')



      
def eliminar_citas(file, eliminar):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        citas_borradas = 0
        updated_directory = []
        for line in directory:
            cita = line.strip().split(',')
            if cita[1] != eliminar:
                updated_directory.append(line)
            else:
                citas_borradas += 1
        if citas_borradas > 0:
            f = open(file, 'w')
            for line in updated_directory:
                f.write(line)
            f.close()
            return('¡Se han borrado ' + str(citas_borradas) + ' citas para el día ' + eliminar + '!\n')
        else:
            return('¡No hay citas programadas para el día ' + eliminar + '!\n')






    
def menu():

    print('Citas Médicas ')
    print('============================')
    print('1 - Crear una cita')
    print('2 - Consultar citas')
    print('3 - Eliminar citas')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option




def opciones():
    file = 'citas.txt' 
    while True:
        option = menu()
        if option == '1':
            dpi = input('Introduzca su número de DPI: ')
            fecha = input('Introduzca dia y mes (dd/mm): ')
            hora= input('Ingrese la hora a reservar la cita:  ')
            especialidad= input('Ingrese la especialidad :  ')
            print(agregar_citas(file, dpi, fecha, hora, especialidad))
        elif option == '2':
            buscador= input('Introduzca el numero de DPI del ciente: ')
            print(buscar_cita(file, buscador))
        elif option == '3':
         eliminar = input('Introduce la fecha en formato dia y mes (dd/mm) de citas a eliminar: ')
         print(eliminar_citas(file, eliminar))
        else :
            break
    return

opciones()