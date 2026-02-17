# Harsh Marvel Shop - POC

This is a Proof of Concept (POC) for a microservices eCommerce project.

The app is split into small services:
- `user-service`
- `product-service`
- `cart-service`
- `order-service`
- `frontend` (Nginx + static UI)
- `victoria` and `vmagent` (monitoring)

## Goal of this POC

Show how multiple backend services can run together and be accessed from one URL using Nginx.

## Tech Stack

- FastAPI (Python)
- Docker + Docker Compose
- Nginx (reverse proxy)
- VictoriaMetrics + vmagent (basic monitoring)

## Architecture (Simple)

- Browser calls `http://localhost:8090`
- Nginx receives request and routes by path:
  - `/` -> frontend page
  - `/users` -> user-service
  - `/products` -> product-service
  - `/cart` -> cart-service
  - `/orders` -> order-service

## How to Run

### 1. Build and start all services

```bash
docker compose up --build -d
```

### 2. Check running containers

```bash
docker compose ps
```

### 3. Open in browser

- Frontend: `http://localhost:8090`
- Products API: `http://localhost:8090/products`
- Users API: `http://localhost:8090/users`
- Cart API: `http://localhost:8090/cart/1`
- Orders API: `http://localhost:8090/orders`

## Sample API Test (Terminal)

```bash
curl http://localhost:8090/products
```

## Monitoring URLs

- VictoriaMetrics: `http://localhost:8428`
- vmagent: `http://localhost:8429`

## Project Structure

```text
.
├── user_service/
├── product_service/
├── cart_service/
├── order_service/
├── frontend/
├── docker-compose.yml
├── requirements.txt
└── scrape.yml
```

## POC Scope

This POC focuses on:
- Service communication
- Single entry point (API gateway style)
- Basic containerized deployment

Not included (for now):
- Authentication
- Database persistence
- Payment integration
- Production security hardening

## Author

Harsh

<img width="1847" height="1018" alt="Screenshot from 2026-02-16 14-11-38" src="https://github.com/user-attachments/assets/fafbf6f8-7d7b-42be-9995-6438dd008d85" />


<img width="1847" height="1018" alt="Screenshot from 2026-02-17 16-06-49" src="https://github.com/user-attachments/assets/82b9ec94-acb7-4859-8d66-8e10b9d45284" />


<img width="1443" height="448" alt="Screenshot from 2026-02-17 17-18-02" src="https://github.com/user-attachments/assets/5d462dee-6e3f-4d94-b347-fd1a0d061db5" />


<img width="1855" height="1011" alt="Screenshot from 2026-02-17 18-33-30" src="https://github.com/user-attachments/assets/40865865-4129-4e10-ad01-17afbda67e79" />


<img width="1855" height="1011" alt="Screenshot from 2026-02-17 18-34-59" src="https://github.com/user-attachments/assets/04f485c5-ae38-433a-a49b-eb82c1e4844d" />



