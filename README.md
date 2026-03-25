# VotaWeb · Demo universitario Django + Svelte

Aplicación de votación en tiempo real que demuestra la integración de un backend **Django REST Framework** con un frontend **Svelte 4**, todo orquestado con **Docker Compose**.

## Cómo ejecutar

```bash
docker compose up --build
```

Eso es todo. Docker descargará las imágenes, instalará dependencias y levantará ambos servicios.

## URLs

| Servicio        | URL                              |
|-----------------|----------------------------------|
| Frontend Svelte | http://localhost:5173            |
| API REST        | http://localhost:8000/api/polls/ |
| Django Admin    | http://localhost:8000/admin/     |

## Credenciales del admin

| Campo    | Valor    |
|----------|----------|
| Usuario  | admin    |
| Contraseña | admin123 |

## Estructura del proyecto

```
voting-app/
├── docker-compose.yml          # Orquestación de servicios
├── backend/                    # Django + DRF
│   ├── config/                 # Configuración del proyecto
│   └── polls/                  # App de encuestas
│       ├── models.py           # Poll y Option (ORM)
│       ├── serializers.py      # JSON ↔ modelos (DRF)
│       ├── views.py            # Endpoints de la API
│       └── management/         # Comando seed personalizado
└── frontend/                   # Svelte 4 + Vite
    └── src/
        ├── App.svelte          # Componente raíz + CSS variables
        └── lib/
            ├── PollCard.svelte # Lógica principal + store + polling
            ├── VoteBar.svelte  # Barras de progreso animadas
            └── api.js          # Comunicación con el backend
```

## Características de Svelte demostradas

- **Reactive declarations (`$:`)** — cálculo automático de porcentajes
- **Svelte store (`writable`)** — estado compartido y reactivo
- **Transitions (`fade`, `fly`)** — animaciones declarativas
- **`onMount`** — ciclo de vida para carga inicial y polling
- **`localStorage`** — persistencia del voto entre recargas

## Características de Django demostradas

- **Django ORM** — modelos `Poll` y `Option` con relaciones FK
- **Django REST Framework** — serializers, APIView, Response
- **django-cors-headers** — habilitación de CORS para el frontend
- **Django Admin** — interfaz CRUD automática con inlines
- **Management commands** — comando `seed` personalizado
