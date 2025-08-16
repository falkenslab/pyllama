import inspect
from typing import get_type_hints
from docstring_parser import parse

def func_to_tool_schema(func):
    """Convierte una función a un schema de herramienta usando docstring_parser.
    
    Args:
        func: Función a convertir en schema de herramienta.
        
    Returns:
        Diccionario con el schema compatible con Ollama function calling.
    """
    sig = inspect.signature(func)
    hints = get_type_hints(func)
    
    # Obtener información del docstring usando docstring_parser si está disponible
    description = ""
    param_descriptions = {}
    
    if func.__doc__:
        try:
            parsed_doc = parse(func.__doc__)
            description = parsed_doc.short_description or ""
            if parsed_doc.long_description:
                description += f"\n\n{parsed_doc.long_description}"
            
            # Extraer descripciones de parámetros
            for param in parsed_doc.params:
                param_descriptions[param.arg_name] = param.description or ""
                
        except Exception as e:
            print(f"⚠️  Error parseando docstring: {e}")
            description = inspect.getdoc(func) or ""
    else:
        # Fallback a inspect.getdoc si docstring_parser no está disponible
        description = inspect.getdoc(func) or ""
    
    # Construir parámetros del schema
    params = {
        "type": "object",
        "properties": {},
        "required": []
    }
    
    for name, param in sig.parameters.items():
        # Obtener tipo del parámetro
        typ = hints.get(name, str)
        typ_name = getattr(typ, "__name__", str(typ))
        
        # Mapear tipos de Python a tipos JSON Schema
        type_mapping = {
            "str": "string",
            "int": "integer", 
            "float": "number",
            "bool": "boolean",
            "list": "array",
            "dict": "object"
        }
        
        json_type = type_mapping.get(typ_name.lower(), "string")
        
        # Construir propiedad del parámetro
        param_schema = {
            "type": json_type
        }
        
        # Agregar descripción si está disponible
        if name in param_descriptions:
            param_schema["description"] = param_descriptions[name]
        
        params["properties"][name] = param_schema
        
        # Agregar a requeridos si no tiene valor por defecto
        if param.default is inspect.Parameter.empty:
            params["required"].append(name)
    
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": description.strip(),
            "parameters": params
        }
    }