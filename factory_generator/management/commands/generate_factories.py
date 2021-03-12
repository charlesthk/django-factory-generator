from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

from factory_generator.generator import FactoryAppGenerator


class Command(BaseCommand):
    help = "Create model factories for all installed apps"

    def handle(self, *args, **options):
        created_files = []
        FACTORY_IGNORE_APPS = getattr(settings, "FACTORY_IGNORE_APPS", [])
        for app in apps.get_app_configs():
            if app.label not in FACTORY_IGNORE_APPS:
                factory_app_generator = FactoryAppGenerator(app)
                created_files += factory_app_generator.create_files()
        self.stdout.write(self.style.SUCCESS("Successfully created factories:"))
        for created_file in created_files:
            self.stdout.write(self.style.SUCCESS("- " + created_file))
