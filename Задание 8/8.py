import fitz

search_term = 'электрон'
pdf = fitz.open('tr.pdf')
total_found = int(0)

for current_page in range(len(pdf)):
    page = pdf.load_page(current_page)

    if page.search_for(search_term):
        total_found += 1
        print('%s найдено на %i странице' % (search_term, current_page))
print(f'Кол-во найденных слов {search_term}: {total_found}')
