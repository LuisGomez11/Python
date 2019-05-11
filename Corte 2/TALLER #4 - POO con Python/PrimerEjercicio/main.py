from ClaseEmpleado import Empleado

emp1 = Empleado(123,'Luis','Programador',2000000,'luisgomez24g@gmail.com',3002149179)

emp1.setNombre('Luis Alberto')

print('Nombre:',emp1.getNombre())
print('Salario: $',emp1.getSalario())
print('Cargo:',emp1.getCargo())
print('Email:',emp1.getEmail())
print('Telefono:',emp1.getTelefono())