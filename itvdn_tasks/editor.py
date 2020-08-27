class Editor():
    def view_document(self):
        print('Смотрим документ ...')
    
    def edit_document(self):
        print('Редактирование недоступно для бесплатной версии!')
        
class ProEditor(Editor):
    def edit_document(self):
        print('Редактируем документ ...')
def main():
    key = input('введите лицензионный ключ :')
    if key == 'AAA':
        print('Продукт активирован!')
        edit = ProEditor()
    else:
        print('Некорректный ключ!')
        edit = Editor()
    edit.edit_document()
    edit.view_document()
if __name__ == '__main__':
    main()