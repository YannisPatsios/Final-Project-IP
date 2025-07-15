from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.core.files.base import ContentFile
import random

class Command(BaseCommand):
    help = 'Load sample categories and products for SDR World'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create categories and subcategories
        sdr_cat = Category.objects.create(name='SDRs', slug='sdrs')
        acc_cat = Category.objects.create(name='Accessories', slug='accessories')
        usb_cat = Category.objects.create(name='USB SDRs', slug='usb-sdrs', parent=sdr_cat)
        pcie_cat = Category.objects.create(name='PCIe SDRs', slug='pcie-sdrs', parent=sdr_cat)
        ant_cat = Category.objects.create(name='Antennas', slug='antennas', parent=acc_cat)
        cable_cat = Category.objects.create(name='Cables', slug='cables', parent=acc_cat)

        # Sample products
        products = [
            {'name': 'RTL-SDR Blog V3', 'brand': 'RTL-SDR', 'price': 39.95, 'category': usb_cat},
            {'name': 'HackRF One', 'brand': 'Great Scott Gadgets', 'price': 299.00, 'category': usb_cat},
            {'name': 'USRP B200 Mini', 'brand': 'Ettus Research', 'price': 999.00, 'category': usb_cat},
            {'name': 'LimeSDR PCIe', 'brand': 'Lime Microsystems', 'price': 499.00, 'category': pcie_cat},
            {'name': 'Nooelec NESDR SMArt', 'brand': 'Nooelec', 'price': 29.95, 'category': usb_cat},
            {'name': 'Discone Antenna', 'brand': 'Diamond', 'price': 89.00, 'category': ant_cat},
            {'name': 'Magnetic Loop Antenna', 'brand': 'MLA', 'price': 120.00, 'category': ant_cat},
            {'name': 'Coaxial Cable 5m', 'brand': 'Generic', 'price': 12.50, 'category': cable_cat},
            {'name': 'PCIe SDR Adapter', 'brand': 'SDRplay', 'price': 59.00, 'category': pcie_cat},
        ]

        for prod in products:
            p = Product(
                name=prod['name'],
                brand=prod['brand'],
                price=prod['price'],
                description=f"Sample description for {prod['name']}.",
                category=prod['category']
            )
            # Add a placeholder image (1x1 px GIF)
            p.image.save('placeholder.gif', ContentFile(b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'), save=True)
            p.save()

        self.stdout.write(self.style.SUCCESS('Sample categories and products loaded.')) 