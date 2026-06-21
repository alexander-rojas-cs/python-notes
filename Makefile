.PHONY: up down entrar restart

# Levanta el entorno de Python 3.14 en segundo plano
up:
	docker compose up -d

# Apaga y remueve el contenedor para liberar memoria
down:
	docker compose down

# Te mete directo a la terminal de Python 3.14 sin vueltas
entrar:
	docker compose exec entorno_curso bash

# Reinicia el contenedor (útil si algo se tilda)
restart:
	docker compose down && docker compose up -d