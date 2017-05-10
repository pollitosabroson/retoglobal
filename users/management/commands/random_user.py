import random
from datetime import datetime

import requests
from django.core.management.base import BaseCommand

from genres.models import Genre
from hobbies.models import Hobbie
from users.models import User
from users.utils import calculate_age


class Command(BaseCommand):
    help = 'Add number for user create'

    def add_arguments(self, parser):
        parser.add_argument('total', nargs='+', type=int)

    def handle(self, *args, **options):
        print(options['total'])
        print(options)
        for number in options['total']:
            payload = {
                'inc': 'gender,name,dob',
                'nat': 'us,dk,fr,gb',
                'results': number,
            }
            results = requests.get(
                'https://randomuser.me/api/',
                params=payload
            )
            results_json = results.json()
            for user in results_json['results']:
                # Calculate Age
                born = datetime.strptime(user['dob'], '%Y-%m-%d %H:%M:%S')
                age = calculate_age(born)
                # Validation Genre
                genre, status = Genre.objects.get_or_create(
                    name=user['gender']
                )
                # Create User instance
                user = User(
                    name=user['name']['first'],
                    last_name=user['name']['last'],
                    age=age,
                    genre=genre,

                )
                user.save()
                # Add hobbies
                hobbies = Hobbie.objects.all().values_list('id', flat=True)
                hobbies = list(hobbies)
                hobbies = random.sample(hobbies, 2)
                hobbies = Hobbie.objects.filter(id__in=hobbies)
                for hobbie in hobbies:
                    user.hobbies.add(hobbie)

        self.stdout.write(self.style.SUCCESS('Successfully created users'))
