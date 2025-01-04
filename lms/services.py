import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name_product):
    """Создает продукт в страйпе."""
    product = name_product.course
    name_course = stripe.Product.create(name=product)
    return name_course.get("id")


def create_stripe_price(amount, name_course):
    """Создает цену в страйпе."""
    return stripe.Price.create(
      currency="rub",
      unit_amount=amount * 100,
      product_data={"name": name_course},
    )


def create_stripe_session(price):
    """Создает сессию для оплаты в страйпе."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
