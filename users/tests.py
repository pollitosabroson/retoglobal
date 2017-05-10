from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from hobbies.models import Hobbie


class RandomUserTest(TestCase):
    def test_command_output(self):
        hobbies = [
            'Natacion', 'Voleibol', 'Futbol', 'Correr', 'Estudiar', 'Comer',
            'Caminar', 'Musica', 'Programar'
        ]

        for hobbie in hobbies:
            hob = Hobbie(name=hobbie)
            hob.save()
        out = StringIO()
        call_command('random_user', 4, stdout=out)
        self.assertIn('Successfully created users', out.getvalue())
