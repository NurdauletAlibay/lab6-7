#Резюме
print("                      Резюме            ")

# info - Кортеж
info = (
    ("Әлібай", "Нурдаулет", "Нурланұлы"),
)
for item in info:
    lastname, firstname, fname = item
    print("\nФ.И.О : " + lastname, firstname, fname)

# experience  - set
company = {"Astana hub"}
vacancy = {"Python разработчик"}
experience = company.union(vacancy)
print("Опыт работы : " + str(experience))

# obrazovanie = dict
study = {
    'ВУЗ': 'Satbayev University',
    'Специальность ': 'Computer Science',
    'Год окончания ': '2023'
}
for x, y in study.items():
    print(x + ' : ' + y)

# skills - кортеж
skills = ('Языки программирования C++, Python', 'OS Linux, HTML,CSS')
skills = ''.join(skills)
print("Основные навыки : " + skills)

info = []
info.append("Номер телефона : ")
info.append("Эл.почта : ")
print(info[0] + '87475639912')
print(info[1] + 'alibay.n01@gmail.com')
