import sqlite3 as sql
import csv

def categorize_data(first_row):
    print("We need to understand what kind of data is in each column to cluster correctly.")
    print("(I)d - This column has an id in it, don't consider it when clustering")
    print("(S)pecimine - This column contains specimine data, do consider it when clustering.")
    print("(O)ther - This column contains other data, don't consider it when clustering, or reporting.")
    print("(R)est - Mark the rest as Specimine data.")
    types = []
    reply = None
    for col in first_row:
        if not reply == 'R':
            print(col)
            keep_asking = True
            while keep_asking:
                reply = input("What kind of data is this?> ").upper()
                acceptable_replies = ['I', 'S', 'O', 'R']
                if reply in acceptable_replies:
                    keep_asking = False
                else:
                    print('Please select a command from the categorize data command list.')
            types.append(reply)
        else:
            types.append("S")
    return types

def build_database(csv_file, project_name):
    connection = sql.connect(project_name+".db")
    c = connection.cursor()
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile)
        data = []
        column_headers = []
        types = []
        for i, row in enumerate(reader):
            if i == 0:
                types = categorize_data(row)
                column_headers = row
                for a, t in enumerate(types):
                    data.append([row[a], t])
                transaction = ", ".join(column_headers)
                c.execute('''CREATE TABLE data (%s)''' % transaction)
                c.execute('''CREATE TABLE data_description (column_name text, data_type text)''')
                for m, n in enumerate(types):
                    c.execute('''INSERT INTO data_description VALUES ('%s','%s')''' % (column_headers[m],n))
                connection.commit()
            else:
                questions = "'?', "*(len(row)-1)
                c.execute('''INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ''', tuple(row))
        connection.commit()
        connection.close()

def pull_columns(project_name):
    connection = sql.connect(project_name+".db")
    c = connection.cursor()
    types = c.execute("FROM data_description SELECT *")
    data = c.execute("FROM data SELECT *")
    return data
