# Django Stripe Shop

## Features

* 3 fixed products (Laptop, Phone, Headphones)
* User selects quantity and buys
* Stripe Checkout integration (test mode)
* Webhook confirms payment
* Paid orders shown on same page

---

## Flow Chosen

Stripe Checkout was chosen because it handles UI, validation, and the entire payment flow automatically, with built-in support for error handling and retries. This reduces frontend complexity and speeds up development.

---

## Avoiding Double Charge / Inconsistent State

* The system relies on Stripe webhooks to confirm successful payments
* The frontend redirect is **NOT trusted**
* Order is marked as paid only after Stripe confirms via webhook
* Each order stores a unique `stripe_session_id`, preventing duplicate updates

---

## Flow

1. User selects products
2. Clicks Buy
3. Redirected to Stripe Checkout
4. Completes payment
5. Webhook marks order as paid
6. Order appears in "My Orders"

---

## Setup / Run Steps (Local)

### 1. Clone repo

```bash
git clone https://github.com/Tapish19/djangoProduct.git
cd djangoProduct
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
STRIPE_SECRET_KEY=sk_test_your_key_here
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
```

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Seed products (one-time)

```bash
python manage.py shell
```

```python
from app.models import Product
Product.objects.create(name="Laptop", price=50000)
Product.objects.create(name="Phone", price=20000)
Product.objects.create(name="Headphones", price=5000)
```

---

### 7. Run server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

### 8. Start Stripe webhook listener

```bash
stripe listen --forward-to localhost:8000/webhook/
```

👉 Copy the generated `whsec_...` into your `.env`

---

## Docker Setup (Optional)

```bash
docker compose up --build
```

The app will be available at:

```
http://localhost:8000
```

---

## .env.example

```env
STRIPE_SECRET_KEY=your_key_here
STRIPE_WEBHOOK_SECRET=your_webhook_secret
```

---

## Test Card

```
4242 4242 4242 4242
Any future date
Any CVC
```

---

## AI Assistance

Used AI tools (ChatGPT/Codex) for:

* Debugging Stripe webhook issues
* Fixing syntax and imports
* Creating Docker setup

All code was reviewed and understood before use.

---

## Time Spent

~11 hours
