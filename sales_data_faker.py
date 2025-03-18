import six
import sys
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

import random
from faker import Faker

fake = Faker()


TOPIC = "sales"

def generate_sales_data():
    return {
        "order_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
        "product_id": random.randint(1, 100),
        "product_name": fake.word(),
        "category": random.choice(["Electronics", "Clothing", "Books", "Home & Kitchen"]),
        "price": round(random.uniform(10.0, 500.0), 2),
        "quantity": random.randint(1, 5),
        "total_amount": round(random.uniform(10.0, 500.0), 2),
        "payment_method": random.choice(["Credit Card", "PayPal", "Gift Card"]),
        "customer_id": fake.uuid4(),
        "location_": fake.city(),
    }


if __name__ == '__main__':
    while True:
        data = generate_sales_data()
        print(f"Sent: {data}")

