# pyllama

Pequeño cliente Python para interactuar con modelos de lenguaje mediante **ollama** (en modo local 😯).

## Instalación

Podemos instalar el paquete directamente desde el repositorio de GitHub con el siguiente comando:

```bash
pip install git+https://github.com/falkenslab/pyllama.git
```

Es necesario tener instalado [ollama](https://ollama.com/) 🦙 y descargar los [modelos](https://ollama.com/search) 🤖 que queremos utilizar:

```bash
ollama pull <modelo>
```

Por ejemplo: `ollama pull llama3.2:latest`

⚠️ No olvides iniciar el servicio:

```bash
ollama serve
```

## Uso

Para consultar como usar el script podemos consultar la ayuda de la siguiente forma:

```bash
$ $pyllama --help
usage: pyllama [-h] [--list] [--model MODEL] [--temperature TEMPERATURE] [--verbose] [query]

Interactúa con modelos de lenguaje

positional arguments:
  query                 Consulta para enviar al modelo

options:
  -h, --help            show this help message and exit
  --list                Lista de modelos disponibles
  --model MODEL         Modelo a utilizar para la consulta
  --temperature TEMPERATURE
                        Temperatura para la respuesta del modelo
  --verbose             Habilitar salida detallada
```

Para ver los modelos disponibles, podemos usar el siguiente comando:

```bash
$ pyllama --list
Modelos disponibles:
- qwen3:4b-instruct
- mistral:7b
- gemma3:latest
- llama3.2:latest
- qwen2.5-coder:latest
- deepseek-r1:8b
- gpt-oss:20b
```

Podemos hacer una consulta con el siguiente comando:

```bash
$ pyllama "¿Cuál es la capital de Francia?"
🤖 Modelo utilizado: llama3.2:latest
🗣️ Pregunta: cuál es la capital de Francia?

💬 Respuesta del modelo:
La capital de Francia es París.


⏱️ Tiempo transcurrido: 52.35 segundos
```

> Por defecto funciona en modo silencioso e intenta utilizar el modelo `llama3.2:latest`.

Si quieres utilizar otro modelo, puedes usar la opción `--model <modelo>`, indicando alguno de la lista anterior:

```bash
(venv) C:\Users\fvarrui\GitHub\pyllama>pyllama --model gpt-oss:20b "cómo se prepara una lasaña"
🤖 Modelo utilizado: gpt-oss:20b
🗣️ Pregunta: cómo se prepara una lasaña

💬 Respuesta del modelo:
### Lasaña clásica (de carne)

#### Ingredientes (para 6-8 personas)

| Ingrediente | Cantidad |
|-------------|----------|
| Láminas de lasaña (pre-cocidas o normales) | 12-15 |
| Carne molida (res o mezcla res/pollo) | 500 g |
| Cebolla | 1 grande, picada |
| Ajo | 2 dientes, picados |
| Zanahoria | 1, rallada (opcional) |
| Apio | 1 tallo, picado (opcional) |
| Tomate triturado | 400 g (o salsa de tomate) |
| Aceite de oliva | 2 cucharadas |
| Sal, pimienta | al gusto |
| Hierbas italianas (orégano, albahaca) | 1 cucharadita |
| Queso mozzarella | 200 g, rallado |
| Queso parmesano | 50 g, rallado |
| Bechamel (salsa blanca) | 400 ml |
| Mantequilla | 30 g |
| Harina | 30 g |
| Leche | 400 ml |
| Nuez moscada | una pizca |
| Aceitunas negras (opcional) | 10, troceadas |
| Hojas de albahaca fresca (para decorar) | al gusto |

#### Instrucciones

1. **Preparar la salsa boloñesa**
   - En una sartén grande, calienta el aceite de oliva a fuego medio.
   - Añade la cebolla y el ajo; sofríe 3–4 min hasta que estén transparentes.
   - Incorpora la carne molida y cocina hasta que pierda el color rosado.
   - Si usas zanahoria y apio, agrégalos ahora y cocina 2 min más.
   - Vierte el tomate triturado, añade sal, pimienta, orégano y albahaca.
   - Deja cocer a fuego lento 15–20 min, removiendo de vez en cuando.
   - Ajusta de sal y pimienta.

2. **Preparar la bechamel**
   - En una cacerola, derrite la mantequilla a fuego medio.
   - Añade la harina y cocina 1 min sin dejar que se dore.
   - Vierte la leche poco a poco, batiendo constantemente para evitar grumos.
   - Cocina hasta que la salsa espese (aprox. 5 min).
   - Añade una pizca de nuez moscada, sal y pimienta.
   - Reserva.

3. **Montar la lasaña**
   - Precalienta el horno a 180 °C (350 °F).
   - En una fuente rectangular (aprox. 30 × 20 cm), unta una capa fina de bechamel.
   - Coloca una capa de láminas de lasaña (pueden ser crudas si tu paquete indica que se cocinan en el horno).
   - Añade una capa de salsa boloñesa, una capa de bechamel y espolvorea queso mozzarella.
   - Repite las capas hasta terminar con una capa de bechamel y una generosa cantidad de mozzarella y parmesano.
   - Si deseas, añade aceitunas negras en la última capa para un toque extra de sabor.

4. **Hornear**
   - Cubre la fuente con papel de aluminio (para evitar que el queso se queme).
   - Hornea 30 min.
   - Retira el papel y hornea 10–15 min más, o hasta que la superficie esté dorada y burbujeante.

5. **Reposar y servir**
   - Deja reposar la lasaña 10 min antes de cortar.
   - Decora con hojas de albahaca fresca.
   - Sirve acompañada de una ensalada verde o pan de ajo.

#### Consejos

- **Láminas pre-cocidas**: Si usas láminas que ya están precocidas, solo necesitas una capa de salsa boloñesa y bechamel antes de hornear.
- **Versión vegetariana**: Sustituye la carne por champiñones salteados, berenjena, calabacín y espinacas.
- **Salsa de tomate casera**: Si prefieres usar tomate fresco, hierve y licúa los tomates, luego cocínalos con cebolla, ajo y hierbas.
- **Sabor extra**: Añade un chorrito de vino tinto a la boloñesa mientras se cocina.

¡Disfruta de tu lasaña casera!


⏱️ Tiempo transcurrido: 1001.82 segundos
```

Y si quieres que dé más información de lo que está haciendo (uso de funciones - tools), utiliza el modificador `--verbose`:

```bash
$ $pyllama --verbose "si tengo 3 establos, y en cada establo tengo 5 burros, y compro 2 burros más, cuántos burros tengo en total?"
🤖 Modelo utilizado: llama3.2:latest
🗣️ Pregunta: si tengo 3 establos, y en cada establo tengo 5 burros, y compro 2 burros más, cuántos burros tengo en total?

🛠️ Herramientas disponibles:
        * get_current_time: Obtiene la fecha y hora actual del sistema.
        * get_weather: Obtiene información meteorológica para una ciudad específica.
        * calculate_math: Calcula una expresión matemática simple de forma segura. Esta función evalúa...
        * list_files: Lista los archivos en un directorio específico. Esta función obtiene una...

⚙️ Llamando función: calculate_math({'expression': '(3*5)+2'})
✅ Resultado: {'expression': '(3*5)+2', 'result': 17}

💬 Respuesta del modelo:
Si tienes 3 establos y en cada establo hay 5 burros, eso significa que tienes un total de 3 x 5 = 15 burros.

Luego, compras 2 burros más, por lo que ahora tienes 15 + 2 = 17 burros.


⏱️ Tiempo transcurrido: 57.50 segundos
```

## Funciones disponibles para los modelos

Los modelos tienen acceso a las siguientes funciones (tools) que pueden utilizar automáticamente según sea necesario:

| Función            | Descripción                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `get_current_time` | Obtiene la fecha y hora actual del sistema en formato "YYYY-MM-DD HH:MM:SS"                                       |
| `get_weather`      | Obtiene información meteorológica simulada para una ciudad específica (temperatura, condición climática, humedad) |
| `calculate_math`   | Calcula expresiones matemáticas simples de forma segura (operaciones básicas: +, -, *, /, paréntesis)             |
| `list_files`       | Lista los archivos y directorios en una ruta específica (máximo 10 elementos)                                     |

Éstas se encuentran definidas en `src/pyllama/functions.py`.

### Ejemplos de uso con funciones

```bash
# El modelo usará automáticamente get_current_time
$ pyllama "¿Qué hora es?"

# El modelo usará get_weather
$ pyllama "¿Cómo está el clima en Madrid?"

# El modelo usará calculate_math
$ pyllama "Calcula 25 * 30 + 100"

# El modelo usará list_files
$ pyllama "¿Qué archivos hay en el directorio actual?"
```

## Para desarrolladores

Clonamos el repositorio y nos movemos al directorio del proyecto:

```bash
git clone https://github.com/falkenslab/pyllama.git
cd pyllama
```

Crearemos un entorno virtual:

```bash
python -m venv venv
```

Lo activamos:

```bash
venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux o macOS
```

Instalamos las dependencias necesarias en modo de edición:

```bash
pip install -e .
```

Y a programar:

```bash
code .
```

## Mejoras

Podemos incorporar más funciones para que el modelo pueda realizar más tareas o acciones, como hacer búsquedas web, consultar alguna API, conectarse a una base de datos, realizar tareas en el sistema (crear/eliminar archivos, instalar/desinstalar apps, comprobar que procesos se están comiendo tu RAM y tu CPU 😁...).

