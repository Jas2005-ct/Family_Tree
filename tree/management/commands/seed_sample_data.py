"""
Run: python manage.py seed_sample_data
Creates a 3-generation sample family.
"""
from django.core.management.base import BaseCommand
from tree.models import Person, Relationship


class Command(BaseCommand):
    help = "Seed sample family data"

    def handle(self, *args, **kwargs):
        Person.objects.all().delete()

        gf  = Person.objects.create(first_name="Rajan",  last_name="Kumar",  gender="M", birth_date="1940-06-01")
        gm  = Person.objects.create(first_name="Kamala", last_name="Kumar",  gender="F", birth_date="1943-03-15")
        fa  = Person.objects.create(first_name="Suresh", last_name="Kumar",  gender="M", birth_date="1965-09-10")
        mo  = Person.objects.create(first_name="Priya",  last_name="Kumar",  gender="F", birth_date="1968-01-22")
        s1  = Person.objects.create(first_name="Ramesh", last_name="Kumar",  gender="M", birth_date="1963-04-05")
        s1w = Person.objects.create(first_name="Meena",  last_name="Kumar",  gender="F", birth_date="1965-07-19")
        s2  = Person.objects.create(first_name="Anitha", last_name="Sharma", gender="F", birth_date="1970-11-30")
        me  = Person.objects.create(first_name="Arjun",  last_name="Kumar",  gender="M", birth_date="1995-05-14")

        rels = [
            (gf, gm, "spouse"),  (fa, mo,  "spouse"),  (s1, s1w, "spouse"),
            (gf, fa, "parent"),  (gf, s1,  "parent"),  (gf, s2,  "parent"),
            (gm, fa, "parent"),  (gm, s1,  "parent"),  (gm, s2,  "parent"),
            (fa, me, "parent"),  (mo, me,  "parent"),
            (fa, s1, "sibling"), (fa, s2,  "sibling"),
        ]
        for fp, tp, rt in rels:
            Relationship.objects.get_or_create(from_person=fp, to_person=tp, rel_type=rt)

        self.stdout.write(self.style.SUCCESS("Sample family data seeded."))
