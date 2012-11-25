import codecs

from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import activate

from stores.models import Store


class Command(BaseCommand):

    args = '<csv_filename>'
    help = 'Dumps stores to CSV file'

    def handle(self, *args, **options):
        activate('pl')
        try:
            with codecs.open(args[0], 'w', 'utf-8') as csv_file:
                for store in Store.objects.all():
                    csv_file.write(';'.join([
                        store.name,
                        store.address,
                        store.phone,
                        store.postal_code,
                        store.locality.name,
                        unicode(store.locality.get_voivodeship_name()),
                    ]) + "\n")
                self.stdout.write("Dumped successfully to %s\n" % args[0])
        except IndexError:
            raise CommandError("Usage: storedump %s" % self.args)
