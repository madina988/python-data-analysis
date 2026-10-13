with open('data.csv', 'r', encoding='utf-8') as d:
    data = d.readlines()
    data = data[1:]
    surnames, names, ages = [],[],[]
    for line in data:
        s = [x.strip() for x in line.split(',')]
        surnames.append(s[0])
        names.append(s[1])
        ages.append(int(s[2]))
    #средний возраст
    avg_age = sum(ages)/len(ages)
    #сколько имен в файле
    count_names = len(names)
    #частота имени Антон
    freq_Anton = (names.count('Anton'))/len(names)
with open('result.csv', 'w', encoding='utf-8') as r:
    r.write(f'Средний возраст: {avg_age}\n')
    r.write(f'Сколько имен в файле: {count_names}\n')
    r.write(f'Частота имени Антон: {freq_Anton}\n')