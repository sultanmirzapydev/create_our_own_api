import csv
from django.http import HttpResponse
from ...models import DataModel
from django.core.management.base import BaseCommand, CommandError
from openpyxl import Workbook

class Command(BaseCommand):

    def handle(self, *args, **options):
        transform_to_csv()
        csv_to_xlsx()





def transform_to_csv():
    data = DataModel.objects.all()
    col_titles = [item.name for item in DataModel._meta.fields][:4]
    print('here')
    try:
        with open('co.csv', 'w', newline='') as file:
            print("create file")
            writer = csv.writer(file)
            writer.writerow(col_titles)
            for obj in data:
                writer.writerow([getattr(obj, titles) for titles in col_titles])
            print('file has been created successfully')
    except Exception:
        print('read the error logs')
    

def csv_to_xlsx():
    workbook = Workbook()
    worksheet = workbook.active
    
    with open('co.csv','r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            for col_index, col in enumerate(row):
                cell = worksheet.cell(row=row_index+1,  column=col_index+1)
                cell.value = col
    workbook.save('data.xlsx') 




