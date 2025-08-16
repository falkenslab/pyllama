import sys
import textwrap
import ollama
from pyllama.tools import func_to_tool_schema
from pyllama.functions import calculate_math, get_current_time, get_weather, list_files

# Mapeo de funciones disponibles
AVAILABLE_FUNCTIONS = {
    "get_current_time": get_current_time,
    "get_weather": get_weather,
    "calculate_math": calculate_math,
    "list_files": list_files,
}

def list_models():
    models = ollama.list()
    print("Modelos disponibles:")
    for model in models["models"]:
        print(f"- {model['model']}")


def ask_model(message, model, verbose=True, temperature=0.7):
    print(f"🤖 Modelo utilizado: {model}")
    print(f"🗣️ Pregunta: {message}")

    # Definir las herramientas disponibles para el modelo
    tools = [func_to_tool_schema(func) for func in AVAILABLE_FUNCTIONS.values()]

    # Inicializa los mensajes
    messages = [
        {
            "role": "system",
            "content": """
                Eres un asistente que prioriza respuestas sin herramientas.
                Reglas:
                - Responde sin herramientas si es suficiente.
                - Nunca inventes resultados de herramientas.
                - Usa las herramientas sólo si es estrictamente necesario.
                - Analiza bien para qué sirve cada herramienta antes de usarla.
            """,
        },
        {
            "role": "user", 
            "content": message
        },
    ]

    if verbose:
        print("\n🛠️ Herramientas disponibles:")
        for tool in tools:
            function = tool['function']
            name = function['name']
            description = function['description'].replace('\n', ' ')
            description = textwrap.shorten(description, width=80, placeholder="...")
            print(f"\t* {name}: {description}")
        print()

    try:
        # Primera llamada para verificar si el modelo quiere usar herramientas
        response = ollama.chat(
            model=model,
            messages=messages,
            tools=tools,
            options={"temperature": temperature},
        )
        messages.append(response["message"])


        while response["message"].get("tool_calls"):
            # Procesar cada llamada a función
            for tool_call in response["message"]["tool_calls"]:
                function_name = tool_call["function"]["name"]
                function_args = tool_call["function"]["arguments"]

                if verbose:
                    print(f"⚙️ Llamando función: {function_name}({function_args})")

                # Ejecutar la función
                if function_name in AVAILABLE_FUNCTIONS:
                    function_to_call = AVAILABLE_FUNCTIONS[function_name]

                    # Llamar la función con los argumentos
                    if function_args:
                        function_result = function_to_call(**function_args)
                    else:
                        function_result = function_to_call()

                    if verbose:
                        print(f"✅ Resultado: {function_result}")

                    # Agregar el resultado a los mensajes para que el modelo pueda usarlo
                    messages.append({"role": "tool", "content": str(function_result)})
                else:
                    print(f"❌ Función no encontrada: {function_name}", file=sys.stderr)

            # Obtener respuesta final del modelo con streaming
            response = ollama.chat(
                model=model, 
                messages=messages,
                tools=tools,
                options={"temperature": temperature},
            )
            messages.append(response["message"])

        print(f"\n💬 Respuesta del modelo:")
        print(f"{response['message']['content']}\n")

    except Exception as e:
        print(f"❌ Error: {e}")
