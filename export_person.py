from csv import writer
from json import dumps
import body
import global_variables
import interface


def export_csv():
    """ Экспортирует данные из файла csv """
    if body.person_list_not_empty(True, global_variables.global_person_list):
        with open('database.csv', 'w', encoding='utf-8') as fout:
            csv_writer = writer(fout)
            for employee in global_variables.global_person_list:
                csv_writer.writerow(employee.values())
            interface.print_import_export('Экспорт')

