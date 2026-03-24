FROM node:20-slim

WORKDIR /app

# Copiar package.json primero para aprovechar la caché de Docker
COPY package.json .

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

# npm install + dev server con --host para exponer fuera del contenedor
CMD ["sh", "-c", "npm install && npm run dev -- --host"]
