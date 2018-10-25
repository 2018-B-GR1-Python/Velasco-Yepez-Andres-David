from proyecto_personal.conexionBD import *
from proyecto_personal.controllers import *


us=Usuario('juan','correo1','14457645')
Data_Base.usuarios.append(us)
Data_Base.usuarios.append(Factura('08/08/2018',us))