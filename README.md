# Django Stripe Shop

## Features

* 3 fixed products (Laptop, Phone, Headphones)
* User selects quantity and buys
* Stripe Checkout integration (test mode)
* Webhook confirms payment
* Paid orders shown on same page

---

## Flow

1. User selects products
2. Clicks Buy
3. Redirected to Stripe Checkout
4. Completes payment
5. Webhook marks order as paid
6. Order appears in "My Orders"

---

## Setup

```bash
pip install django stripe python-dotenv
python manage.py migrate
python manage.py runserver
```

---

## Run Webhook

```bash
stripe listen --forward-to localhost:8000/webhook/
```

---

## Test Card

```
4242 4242 4242 4242
```
---

