import sqlite3
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

#Question #1. How many artists are represented in the database? 
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Jumlah artis yang disebutkan di dalam basis data', len(data))

#Question #2. How many women (Female) are in the database?
cursor.execute('SELECT *FROM artists WHERE gender == "female"')
data = cursor.fetchall()
print('Jumlah perempuan yang disebutkan di dalam basis data:', len(data))

#Question #3. How many people in the database were born before 1900?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print('Jumlah orang yang lahir sebelum tahun 1900:', len(data))

#Question #4*. What is the name of the oldest artist?

# # Python
# cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
# data = cursorfetchall()
# oldest = {'name': '', 'birthday': 1900}
# for person in data:
#     if person[4] < oldest['birthday']:
#         oldest['name'] = person[1]
#         oldest['birthday'] = person[4]
# print("Manusia tertua yang ada di basis data ini adalah", oldest)

# # SQL
# cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900 ORDER by "Birth Year"')
# data = cursor.fetchall()
# print("Manusia tertua yang ada di basis data ini adalah:", oldest[0][0])
# conn.commit()
