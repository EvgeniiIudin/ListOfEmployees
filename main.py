import interface
import body
import global_variables

menu_id = '0'
while menu_id != '9':
    menu_id = interface.show_menu()
    match menu_id.split():
        case ['1']: body.print_person_list(global_variables.global_person_list)
        case ['2']: body.find_person(global_variables.person_list_ids[2])
        case ['3']: body.find_person(global_variables.person_list_ids[4])
        case ['4']: body.find_person(global_variables.person_list_ids[5])
        case ['5']: body.add_person()
        case ['6']: body.delete_person()
        case ['7']: body.change_person()
        case ['8']:
            export_import_menu_id = '0'
            while export_import_menu_id != '5':
                export_import_menu_id = interface.show_export_import_menu()
                body.do_menu_id(export_import_menu_id) 