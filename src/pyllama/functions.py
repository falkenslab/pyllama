import os
import datetime

# Definir las funciones que el modelo puede llamar
def get_current_time():
    """
    Obtiene la fecha y hora actual del sistema.
    Returns:
        La fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS".
    Examples:
        >>> get_current_time()
        '2025-08-14 15:30:45'

        >>> current_time = get_current_time()
        >>> print(f"Hora actual: {current_time}")
        Hora actual: 2025-08-14 15:30:45
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_weather(city: str):
    """
    Obtiene información meteorológica para una ciudad específica.
    Args:
        city: Nombre de la ciudad para la cual obtener el clima.
            Puede ser cualquier nombre válido de ciudad.
    Returns:
        Un diccionario con la siguiente estructura:
            city: Nombre de la ciudad consultada.
            temperature: Temperatura en grados Celsius (rango: 8-30°C).
            condition: Condición climática ("soleado", "nublado", "lluvioso", "ventoso").
            humidity: Porcentaje de humedad relativa (rango: 30-90%).
    Examples:
        >>> get_weather("Madrid")
        {'city': 'Madrid', 'temperature': 22, 'condition': 'soleado', 'humidity': 65}
        >>> weather_info = get_weather("Barcelona")
        >>> print(f"En {weather_info['city']} hace {weather_info['temperature']}°C")
        En Barcelona hace 25°C
    """
    # Esta es una función simulada, en la realidad harías una llamada a una API
    import random
    temps = [15, 18, 22, 25, 28, 30, 12, 8]
    conditions = ["soleado", "nublado", "lluvioso", "ventoso"]    
    return {
        "city": city,
        "temperature": random.choice(temps),
        "condition": random.choice(conditions),
        "humidity": random.randint(30, 90)
    }


def calculate_math(expression: str):
    """
    Calcula una expresión matemática simple de forma segura. Esta función evalúa expresiones 
    matemáticas básicas utilizando solo caracteres permitidos para evitar ejecución de código 
    malicioso.
    Args:
        expression: Expresión matemática a evaluar. Solo se permiten números,
            operadores básicos (+, -, *, /), paréntesis y espacios.
    Returns:
        Un diccionario con el resultado o error:
            expression: La expresión original evaluada.
            result: El resultado numérico de la expresión.
            error: Mensaje de error si la expresión es inválida.
    Examples:
        >>> calculate_math("25 * 30 + 100")
        {'expression': '25 * 30 + 100', 'result': 850}
        >>> calculate_math("(10 + 5) * 2")
        {'expression': '(10 + 5) * 2', 'result': 30}
        >>> calculate_math("print('hack')")
        {'error': 'Expresión no válida'}
    """
    try:
        # Solo permite operaciones básicas por seguridad
        allowed_chars = "0123456789+-*/(). "
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return {"expression": expression, "result": result}
        else:
            return {"error": "Expresión no válida"}
    except Exception as e:
        return {"error": str(e)}


def list_files(directory: str = "."):
    """
    Lista los archivos en un directorio específico. Esta función obtiene una lista de archivos 
    y directorios en la ruta especificada, limitando el resultado a los primeros 10 elementos
    para evitar respuestas muy largas.
    Args:
        directory: Ruta del directorio a listar. Por defecto es el
            directorio actual (".").
    Returns:
        Un diccionario con la información del directorio:
            directory: Ruta del directorio listado.
            files: Lista de nombres de archivos y directorios (máximo 10).
            error: Mensaje de error si no se puede acceder al directorio.
    Examples:
        >>> list_files()
        {'directory': '.', 'files': ['file1.txt', 'folder1', 'script.py']}
        >>> list_files("/home/user/documents")
        {'directory': '/home/user/documents', 'files': ['doc1.pdf', 'image.png']}
        >>> list_files("/nonexistent")
        {'error': '[Errno 2] No such file or directory: \'/nonexistent\''}
    """
    try:
        files = os.listdir(directory)
        return {"directory": directory, "files": files[:10]}  # Limitar a 10 archivos
    except Exception as e:
        return {"error": str(e)}
