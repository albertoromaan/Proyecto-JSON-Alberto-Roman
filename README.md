[README_json_futbol.md](https://github.com/user-attachments/files/27973214/README_json_futbol.md)# JSON Futbol — Consulta de equipos y jugadores

Script de Python que carga un fichero JSON con datos de equipos de fútbol y permite consultarlos de forma interactiva desde la terminal mediante un menú de opciones.

---

## Estructura del proyecto

```
json_futbol/
├── main.py          # Script principal con el menú y las funciones
└── futbol.json      # Datos de equipos y jugadores
```

---

## Uso

```bash
python main.py
```

El script carga automáticamente `futbol.json` desde el mismo directorio. Si no lo encuentra, muestra un error y termina.

---

## Opciones del menú

| Opción | Descripción |
|--------|-------------|
| 1 | Listar todos los equipos con su país y liga |
| 2 | Mostrar el número de jugadores y goles totales por equipo |
| 3 | Pedir un equipo y mostrar sus jugadores con posición y goles |
| 4 | Pedir un nombre de jugador y mostrar su equipo y liga |
| 5 | Pedir un mínimo de goles y listar los jugadores que lo superan |
| 6 | Salir |

---

## Formato del JSON

```json
{
  "equipos": [
    {
      "nombre": "Real Madrid",
      "pais": "España",
      "liga": "La Liga",
      "jugadores": [
        {
          "nombre": "Vinicius Jr",
          "posicion": "Delantero",
          "goles": 23
        }
      ]
    }
  ]
}
```

Cada equipo debe tener los campos `nombre`, `pais`, `liga` y una lista `jugadores`. Cada jugador requiere `nombre`, `posicion` y `goles`.

---

## Requisitos

- Python 3
- No requiere dependencias externas

