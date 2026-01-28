FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

# ---------- Stage 2: Runtime ----------
FROM nginx:alpine

# Install node in nginx image
RUN apk add --no-cache nodejs npm

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy app from build stage
WORKDIR /app
COPY --from=build /app /app

EXPOSE 3000

# Start both Express and Nginx
CMD ["sh", "-c", "node server.js & nginx -g 'daemon off;'"]




# FROM node:18-alpine

# WORKDIR /app

# COPY package*.json ./

# RUN npm install

# COPY . .

# EXPOSE 3000

# CMD ["npm", "start"]
