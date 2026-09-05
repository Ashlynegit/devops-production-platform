 '''
 To run your frontend:

cd C:\Users\dell\Documents\Ashlyne\Portifolio\Project\devops-production-platform\frontend\app
python -m http.server 3000


docker compose up --build

'''

# 🍔 Flavor Blitz

**AI-native ordering infrastructure for African food businesses.**

Flavor Blitz is a full-stack restaurant ordering platform — built as a hands-on DevOps and software engineering project, now evolving into a real product aimed at a real problem: small African food businesses need simple, affordable digital ordering infrastructure.

**Status:** Early-stage prototype, actively in development. Not a demo shell — real services, real database, real containers.

---

## 🚀 Project Links

**Source Code:**
https://github.com/Ashlynegit/devops-production-platform

**Live Deployment:**
https://flavor-blitz-devaidev.ashlynechiweshe1.workers.dev/

**Pitch Deck:**
https://docs.google.com/presentation/d/1FJKdRGUe4OrBHZ6hqk4ybBB4ohi2qwtX/edit?usp=sharing

The live deployment is currently being developed and validated. The GitHub repository contains the complete project architecture and instructions for running the system locally.

---

## What's Built

| Layer            | Technology                                                              |
| ---------------- | ----------------------------------------------------------------------- |
| Frontend         | HTML / CSS / JavaScript — menu, cart, simulated checkout                |
| Menu Service     | Python (Flask) + PostgreSQL — `/api/menu`, `/health`                    |
| Order Service    | Node.js (Express) + PostgreSQL — `/api/orders`, server-side pricing     |
| Database         | PostgreSQL (raw SQL, no ORM)                                            |
| Containerization | Docker + Docker Compose                                                 |
| Architecture     | Two independent backend microservices                                   |
| Payments         | Simulated checkout (Luhn-validated), designed to swap in a real gateway |

The backend is intentionally separated into microservices.

The order service does not directly access menu data. Instead, it communicates with the menu service over HTTP to obtain authoritative menu information and then recalculates order totals server-side.

This provides a foundation for independently deploying, scaling, monitoring, and eventually expanding each service.

---

## 🐳 Containerized Architecture

The project uses Docker Compose to run the complete application stack as multiple containers:

```text
                    ┌─────────────────────┐
                    │      Frontend       │
                    │   HTML/CSS/JS       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Order Service    │
                    │ Node.js / Express   │
                    │      Port 4000      │
                    └──────────┬──────────┘
                               │
                               │ HTTP
                               ▼
                    ┌─────────────────────┐
                    │    Menu Service     │
                    │ Python / Flask      │
                    │      Port 5000      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │      Port 5432      │
                    └─────────────────────┘
```

Docker Compose provides the internal service networking required for the microservices to communicate using service names rather than hard-coded IP addresses.

---

## 📡 API Endpoints

### Menu Service

**Health check:**

```http
GET /health
```

**Menu:**

```http
GET /api/menu
```

Example:

```text
http://localhost:5000/api/menu
```

### Order Service

**Health check:**

```http
GET /health
```

**Orders:**

```http
POST /api/orders
```

Example:

```text
http://localhost:4000/api/orders
```

---

## 🗄️ Database

Flavor Blitz uses PostgreSQL as its persistent data layer.

The current database contains the restaurant menu and supports the backend services through database connections supplied via environment variables.

The project deliberately uses raw SQL rather than an ORM at this stage so that the database interaction remains explicit and easy to reason about.

---

## 🧠 Where It's Going

Flavor Blitz started as a DevOps portfolio project.

Building the system raised a bigger question:

**How can small food businesses across Africa accept digital orders without needing expensive restaurant technology?**

The long-term goal is to turn the ordering infrastructure into an AI-native platform that can work across different African food businesses and eventually support conversational, voice, and local-language ordering.

### Roadmap

* ✅ Working ordering prototype
* ✅ Frontend + two backend microservices
* ✅ PostgreSQL database
* ✅ Dockerized services
* ✅ Docker Compose orchestration
* 🔜 Production-ready public deployment
* 🔜 CI/CD pipeline
* 🔜 Observability and monitoring
* 🔜 Gemini-powered conversational ordering
* 🔜 Voice-based ordering
* 🔜 WhatsApp ordering integration
* 🔜 Local-language ordering — Shona and Ndebele
* 🔜 AI-driven demand forecasting
* 🔜 AI-assisted stock insights
* 🔜 Kubernetes + Helm for multi-restaurant scale

---

## 🤖 AI-Native Direction

The objective is not simply to "add AI to an existing restaurant application."

The longer-term vision is to make AI part of the actual ordering workflow.

A customer could eventually interact with a restaurant using natural language or voice:

```text
Customer:

"I want a burger, chips and a cold drink.
Make the burger spicy."

              ↓

        AI ordering layer

              ↓

    Understands intent
    Selects menu items
    Handles modifications
    Confirms order

              ↓

        Order Service

              ↓

          Database
```

The next AI development phase will explore Google's Gemini models for conversational ordering, voice interaction, menu understanding, and operational intelligence.

---

## 🌍 African Market Focus

Flavor Blitz is being developed with African small and medium-sized food businesses in mind.

Potential use cases include:

* Takeaway restaurants
* Fast-food businesses
* Food kiosks
* Small independent restaurants
* Home-based food businesses
* Local delivery businesses

The platform is designed around the idea that digital ordering should be simple, affordable, mobile-friendly, and adaptable to local markets.

Future development will explore:

* Local payment gateways
* WhatsApp-based ordering
* Local languages
* Delivery-distance calculations
* Tips and add-ons
* Multi-restaurant support
* AI-assisted business insights

---

## 🛠️ DevOps Engineering

Flavor Blitz is also being used as a practical environment for developing real DevOps engineering skills.

The project currently covers:

* Linux / WSL
* Git and GitHub
* Docker
* Docker Compose
* Container networking
* PostgreSQL
* Python
* Node.js
* REST APIs
* Environment-based configuration
* Microservice architecture

Planned infrastructure work includes:

* CI/CD
* Cloud deployment
* Observability
* Infrastructure as Code
* Kubernetes
* Helm
* Production deployment practices

---

## 💻 Running Locally

### Clone the repository

```bash
git clone https://github.com/Ash
```
