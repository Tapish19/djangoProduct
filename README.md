# Django Stripe Shop

## Features

* 3 fixed products (Laptop, Phone, Headphones)
* User selects quantity and buys
* Stripe Checkout integration (test mode)
* Webhook confirms payment
* Paid orders shown on same page

---
## Flow chosen
Stripe Checkout was chosen because It handles UI, validation, and payment flow automatically with Built-in support for error handling and retries
## avoiding double charge / inconsistent state
The system relies on Stripe webhooks to confirm successful payments 
The frontend redirect is NOT trusted. 
Order is marked as paid only after Stripe confirms via webhook
Each order stores a unique stripe_session_id, which  Prevents duplicate updates for the same payment  

## Flow

1. User selects products
2. Clicks Buy
3. Redirected to Stripe Checkout
4. Completes payment
5. Webhook marks order as paid
6. Order appears in "My Orders"

---

## Local setup (without Docker)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Docker setup

```bash
docker compose up --build
```

The app will be available at `http://localhost:8000`.

Optional env vars:

* `STRIPE_SECRET_KEY`
* `STRIPE_WEBHOOK_SECRET`
* `ALLOWED_HOSTS` (comma-separated, defaults to `*`)

---

## Run Webhook (local Stripe CLI)

```bash
stripe listen --forward-to localhost:8000/webhook/
```

---

## Test Card

`4242 4242 4242 4242`

## AI-assist
Fixed syntax, imported libraries and docker file through help of Codex

## Time Spent
11 hours 
