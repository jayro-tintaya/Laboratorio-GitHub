def saludar(nombre_completo):
    if not nombre_completo:
        return "Error: el nombre no puede estar vacío"
    return f"Hola {nombre_completo}, bienvenido al Sistema de Gestión de Restaurante"

print(saludar("El Puerto de la Costa"))
