from dataclasses import dataclass

@dataclass
class Data():
    """
    Representa un registro de precipitación correspondiente a un mes y año
    para dos estaciones meteorológicas.

    Esta clase se usa como estructura base para almacenar los datos que se
    leen desde el archivo Excel y posteriormente se procesan para completar
    datos faltantes, calcular estadísticas y generar gráficos.

    Attributes
    ----------
    year : str
        Año al que pertenece el registro (por ejemplo: "2010").
    station_1 : str
        Valor de precipitación de la estación 1 para ese mes. Puede ser un número
        o None si el dato no está disponible.
    station_2 : str
        Valor de precipitación de la estación 2 para ese mes. Puede ser un número
        o None si el dato no está disponible.
    month : str
        Nombre del mes correspondiente al registro, en mayúsculas
        (por ejemplo: "ENERO").
    """
    year: str
    station_1: str
    station_2: str
    month: str