from django.core.management import BaseCommand
from django.db.models import Sum, F

from market.models import Order, Client


class Command(BaseCommand):
    help = 'Get total sales for each seller'

    def handle(self, *args, **options):
        sellers = Client.objects.filter(is_seller=True)
        result = []

        for seller in sellers:
            buyers_and_sum = Order.objects.filter(lot__seller=seller).values('buyer') \
                .annotate(total=Sum(F('lot__price_per_item') * F('quantity'))).order_by('buyer')

            buyers_list = [{'buyer': item['buyer'], 'total': item['total']} for item in buyers_and_sum]

            total_sales = Order.objects.filter(lot__seller=seller).aggregate(total=Sum(F('lot__price_per_item') * F('quantity')))['total']

            result.append({
                'seller': seller.username,
                'buyers_and_sum': buyers_list,
                'total_sales': total_sales
            })

        for s in result:
            self.stdout.write(f"Seller: {s['seller']}")
            self.stdout.write(f"Seller: {s['buyers_and_sum']}")
            self.stdout.write(f"Total Sales: {s['total_sales']}")
            self.stdout.write('---------------------------')
