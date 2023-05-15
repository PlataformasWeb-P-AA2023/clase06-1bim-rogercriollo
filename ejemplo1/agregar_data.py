from sqlalchemy.orm import sessionmaker

from crear_base import MisSaludos
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

miSaludo = MisSaludos()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = MisSaludos()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
