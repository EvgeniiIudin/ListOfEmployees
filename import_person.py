from csv import reader
import global_variables
import interface


def import_csv():
    """ Импортирует данные в файл csv """
    global_variables.global_person_list = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = reader(fin)
        for row in csv_reader:
            if row != []:
                global_variables.global_person_list.append(
                    dict(zip(global_variables.person_list_ids, row)))
        interface.print_import_export('Импорт')
