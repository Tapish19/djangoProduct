from django.shortcuts import render

# Create your views here.

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    products = Product.objects.all()
    orders = Order.objects.filter(is_paid=True).prefetch_related('orderitem_set')

    return render(request, "home.html", {
        "products": products,
        "orders": orders
    })


def checkout(request):
    if request.method == "POST":
        order = Order.objects.create()
        line_items = []

        for product in Product.objects.all():
            qty = int(request.POST.get(f"qty_{product.id}", 0))
            if qty > 0:
                OrderItem.objects.create(order=order, product=product, quantity=qty)

                line_items.append({
                    "price_data": {
                        "currency": "inr",
                        "product_data": {"name": product.name},
                        "unit_amount": product.price * 100,
                    },
                    "quantity": qty,
                })

        if not line_items:
            return redirect("/")

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/",
            cancel_url="http://localhost:8000/",
        )

        order.stripe_session_id = session.id
        order.save()

        return redirect(session.url)


@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception as e:
        print("Webhook error:", e)
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        print("SESSION ID:", session["id"])

        try:
            order = Order.objects.get(stripe_session_id=session["id"])
            order.is_paid = True
            order.save()
            print("ORDER MARKED PAID")
        except Order.DoesNotExist:
            print("ORDER NOT FOUND ❌")

    return HttpResponse(status=200)