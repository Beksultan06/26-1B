from django.core.management.base import BaseCommand
import asyncio
from telegram.bot import main

class Command(BaseCommand):
    help = 'Start Bot'

    def handle(self, *args, **kwargs):
        asyncio.run(main())