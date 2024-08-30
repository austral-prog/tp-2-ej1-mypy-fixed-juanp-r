def is_leap_year() -> bool:
    """Solicita al usuario ingresar un año, imprime si es bisiesto o no, y retorna True o False."""
    year: int = int(input("Ingrese un año: "))
    
    is_leap: bool = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
    
    return is_leap
