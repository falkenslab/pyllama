import argparse
import time
from pyllama.agent import ask_model, list_models

def main():

    parser = argparse.ArgumentParser(description="Interactúa con modelos de lenguaje")
    parser.add_argument("--list", action="store_true", help="Lista de modelos disponibles")  
    parser.add_argument("--model", default="llama3.2:latest", help="Modelo a utilizar para la consulta")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperatura para la respuesta del modelo")
    parser.add_argument("--verbose", action="store_true", help="Habilitar salida detallada")
    parser.add_argument("query", nargs="?", help="Consulta para enviar al modelo")
    args = parser.parse_args()

    if args.list:
        list_models()
    elif args.query:
        start_time = time.time()
        ask_model(args.query, args.model, args.verbose, args.temperature)
        elapsed_time = time.time() - start_time
        print(f"\n⏱️ Tiempo transcurrido: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
