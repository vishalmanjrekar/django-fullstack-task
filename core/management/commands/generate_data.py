from django.core.management.base import BaseCommand
from core.models import Employee, Department, Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        departments = [Department.objects.create(name=fake.job(), location=fake.city()) for _ in range(3)]

        for _ in range(5):
            dept = random.choice(departments)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                department=dept,
                join_date=fake.date_between(start_date='-3y', end_date='today'),
                designation=fake.job(),
                salary=random.randint(40000, 120000)
            )

            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent'])
                )

            for _ in range(3):
                Performance.objects.create(
                    employee=emp,
                    review_date=fake.date_this_year(),
                    rating=round(random.uniform(2.0, 5.0), 2),
                    comments=fake.sentence()
                )
