import codecs

from django.contrib.localflavor.pl import pl_voivodeships
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.utils.translation import activate

from stores.models import Locality, Store
from unicode_csv import *


class Command(BaseCommand):

    args = '<csv_filename>'
    help = 'Load stores from CSV file'

    def handle(self, *args, **options):
        activate('pl')
        try:
            VOIVODESHIP_PREPARED = dict((unicode(vsh[1]).upper(), vsh[0])
                for vsh in pl_voivodeships.VOIVODESHIP_CHOICES)

            with codecs.open(args[0], 'r', 'utf-8') as csv_file:
                Store.objects.all().delete() # not InnoDB :-(

                try:
                    r = 0
                    for row in unicode_csv_reader(csv_file, delimiter=';'):
                        r += 1
                        if r == 1:
                            continue
                        try:
                            locality = Locality.objects.get(
                                name=row[6].strip(),
                                voivodeship=VOIVODESHIP_PREPARED[row[7].upper()]
                            )
                        except Locality.DoesNotExist:
                            locality = Locality(
                                name=row[6].strip(),
                                slug=slugify(row[6].strip()),
                                voivodeship=VOIVODESHIP_PREPARED[row[7].upper()],
                            )
                            locality.save()
                        Store(
                            name=row[2].strip()[:50],
                            address=row[3].strip()[:100],
                            phone=row[4].strip(),
                            postal_code=row[5].strip(),
                            locality=locality,
                        ).save()
                    self.stdout.write("Successfully loaded from %s\n" % args[0])

                except KeyError, key:
                    raise CommandError("Voivodeship %s not found" % key)

        except IndexError:
            raise CommandError("Usage: storeload %s" % self.args)
  