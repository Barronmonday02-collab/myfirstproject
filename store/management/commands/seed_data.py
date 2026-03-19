from django.core.management.base import BaseCommand
from store.models import Category, Product, Testimonial


class Command(BaseCommand):
    help = 'Seed the database with initial product data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding categories...')
        categories_data = [
            {'name': 'Fish & Seafood', 'slug': 'fish-seafood', 'icon': '🐟', 'description': 'Fresh fish and seafood from trusted fisheries', 'order': 1},
            {'name': 'Poultry', 'slug': 'poultry', 'icon': '🍗', 'description': 'Premium quality chicken and poultry', 'order': 2},
            {'name': 'Vegetables', 'slug': 'vegetables', 'icon': '🥬', 'description': 'Fresh vegetables sourced from local farms', 'order': 3},
            {'name': 'Tomatoes', 'slug': 'tomatoes', 'icon': '🍅', 'description': 'Fresh and tinned tomatoes', 'order': 4},
            {'name': 'Oils & Spices', 'slug': 'oils-spices', 'icon': '🫒', 'description': 'Quality cooking oils and aromatic spices', 'order': 5},
            {'name': 'Seafood Delicacies', 'slug': 'seafood-delicacies', 'icon': '🦐', 'description': 'Premium prawns, clams and more', 'order': 6},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data,
            )
            categories[cat.slug] = cat
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'  {status}: {cat.name}')

        self.stdout.write('Seeding products...')
        products_data = [
            # Fish & Seafood
            {'name': 'Fresh Tilapia', 'slug': 'fresh-tilapia', 'category': 'fish-seafood', 'price': 3500, 'unit': 'per kg', 'is_featured': True,
             'description': 'Freshly caught tilapia fish, cleaned and ready for cooking. Perfect for grilling, frying, or making delicious fish stew.'},
            {'name': 'Catfish (Fresh)', 'slug': 'catfish-fresh', 'category': 'fish-seafood', 'price': 4000, 'unit': 'per kg', 'is_featured': True,
             'description': 'Premium catfish sourced from trusted fish farms. Ideal for pepper soup, grilled fish, or stews.'},
            {'name': 'Mackerel (Titus)', 'slug': 'mackerel-titus', 'category': 'fish-seafood', 'price': 2800, 'unit': 'per kg',
             'description': 'High-quality frozen mackerel fish. Great source of omega-3 fatty acids.'},
            {'name': 'Stockfish', 'slug': 'stockfish', 'category': 'fish-seafood', 'price': 5000, 'unit': 'per piece',
             'description': 'Premium dried stockfish, perfect for traditional Nigerian soups and stews.'},

            # Poultry
            {'name': 'Whole Chicken', 'slug': 'whole-chicken', 'category': 'poultry', 'price': 5000, 'unit': 'per piece', 'is_featured': True,
             'description': 'Farm-fresh whole chicken, properly cleaned and ready to cook. Free-range quality.'},
            {'name': 'Chicken Breast', 'slug': 'chicken-breast', 'category': 'poultry', 'price': 3500, 'unit': 'per kg',
             'description': 'Lean chicken breast cuts, perfect for grilling, salads, and healthy meals.'},
            {'name': 'Chicken Wings', 'slug': 'chicken-wings', 'category': 'poultry', 'price': 3000, 'unit': 'per kg',
             'description': 'Juicy chicken wings, great for frying, baking, or making delicious sauces.'},

            # Vegetables
            {'name': 'Fresh Onions', 'slug': 'fresh-onions', 'category': 'vegetables', 'price': 1500, 'unit': 'per kg', 'is_featured': True,
             'description': 'Crisp, fresh onions essential for every Nigerian kitchen. Available in red and white varieties.'},
            {'name': 'Red Bell Pepper', 'slug': 'red-bell-pepper', 'category': 'vegetables', 'price': 2000, 'unit': 'per kg', 'is_featured': True,
             'description': 'Vibrant red bell peppers, fresh and crunchy. Perfect for stews, salads, and garnishing.'},
            {'name': 'Green Pepper', 'slug': 'green-pepper', 'category': 'vegetables', 'price': 1800, 'unit': 'per kg',
             'description': 'Fresh green peppers with a mild, crisp flavor. Great for stir-fries and sauces.'},
            {'name': 'Fresh Cabbage', 'slug': 'fresh-cabbage', 'category': 'vegetables', 'price': 800, 'unit': 'per head',
             'description': 'Crisp, green cabbage perfect for coleslaw, salads, and vegetable stir-fries.'},
            {'name': 'Fresh Carrots', 'slug': 'fresh-carrots', 'category': 'vegetables', 'price': 1200, 'unit': 'per kg', 'is_featured': True,
             'description': 'Crunchy, sweet carrots rich in vitamins. Great raw, steamed, or in stews.'},

            # Tomatoes
            {'name': 'Fresh Tomatoes', 'slug': 'fresh-tomatoes', 'category': 'tomatoes', 'price': 1500, 'unit': 'per kg',
             'description': 'Ripe, juicy tomatoes freshly harvested. Essential for Nigerian tomato stew and sauces.'},
            {'name': 'Tin Tomatoes (Paste)', 'slug': 'tin-tomatoes', 'category': 'tomatoes', 'price': 800, 'unit': 'per tin',
             'description': 'Quality tinned tomato paste for rich, flavorful stews and jollof rice.'},
            {'name': 'Plum Tomatoes', 'slug': 'plum-tomatoes', 'category': 'tomatoes', 'price': 2000, 'unit': 'per kg',
             'description': 'Premium plum tomatoes with thick flesh, ideal for sauces and cooking.'},

            # Oils & Spices
            {'name': 'Groundnut Oil', 'slug': 'groundnut-oil', 'category': 'oils-spices', 'price': 4500, 'unit': 'per 4L', 'is_featured': True,
             'description': 'Pure, natural groundnut oil perfect for frying and cooking. Rich flavor and high smoke point.'},
            {'name': 'Curry Powder', 'slug': 'curry-powder', 'category': 'oils-spices', 'price': 500, 'unit': 'per pack',
             'description': 'Premium curry powder blend for flavoring rice, stews, and meat dishes.'},
            {'name': 'Thyme', 'slug': 'thyme', 'category': 'oils-spices', 'price': 400, 'unit': 'per pack',
             'description': 'Aromatic dried thyme, a staple spice in Nigerian cooking.'},
            {'name': 'Mixed Spices', 'slug': 'mixed-spices', 'category': 'oils-spices', 'price': 600, 'unit': 'per pack',
             'description': 'Our signature spice blend with cumin, coriander, and more. Perfect for marinades.'},

            # Seafood Delicacies
            {'name': 'King Prawns', 'slug': 'king-prawns', 'category': 'seafood-delicacies', 'price': 8000, 'unit': 'per kg', 'is_featured': True,
             'description': 'Jumbo king prawns, cleaned and deveined. Perfect for stir-fries, grilling, or seafood platters.'},
            {'name': 'Fresh Clams', 'slug': 'fresh-clams', 'category': 'seafood-delicacies', 'price': 3000, 'unit': 'per kg',
             'description': 'Fresh clams harvested from clean waters. Excellent for soups, stews, and pasta dishes.'},
            {'name': 'Crayfish (Ground)', 'slug': 'crayfish-ground', 'category': 'seafood-delicacies', 'price': 2500, 'unit': 'per cup',
             'description': 'Finely ground crayfish, essential seasoning for Nigerian soups and stews.'},
        ]

        for prod_data in products_data:
            cat_slug = prod_data.pop('category')
            prod_data['category'] = categories[cat_slug]
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults=prod_data,
            )
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'  {status}: {product.name}')

        self.stdout.write('Seeding testimonials...')
        testimonials_data = [
            {'name': 'Adebayo Johnson', 'role': 'Regular Customer', 'rating': 5,
             'content': "The freshest fish I've ever had delivered! FRESVORA has completely changed how I shop for groceries. The quality is consistent every single time."},
            {'name': 'Funmi Oladele', 'role': 'Restaurant Owner', 'rating': 5,
             'content': "As a restaurant owner, I need reliable suppliers. FRESVORA delivers quality vegetables and spices every time. Their delivery is always on time!"},
            {'name': 'Chinedu Eze', 'role': 'Chef', 'rating': 5,
             'content': "Best groundnut oil and spices in Lagos! The prices are fair and the quality is unmatched. My go-to supplier for everything I need in the kitchen."},
        ]

        for test_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=test_data['name'],
                defaults=test_data,
            )
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'  {status}: {testimonial.name}')

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
