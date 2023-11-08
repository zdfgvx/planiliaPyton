import openpyxl

#criar planilha
book = openpyxl.Workbook()

#como visualizar paginas existentes
print(book.sheetnames)

#como criar uma pagina 
book.create_sheet("frutas")
#como selecionar uma pagina
frutas_page = book['frutas']
frutas_page.append(['Fruta' , 'Quatidade', 'Preço'])
frutas_page.append(['Banana', '5',  'R$3,90'])
frutas_page.append(['Maçã', '12',  'R$6,50'])
frutas_page.append(['Uva', '25', 'R$12,90'])
# salvar planilha
book.save('Planilha de Conpras.xlsx')