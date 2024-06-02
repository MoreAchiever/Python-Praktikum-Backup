# Zusammenarbeit mit folgenden Teilnehmern:

from datetime import datetime
import time
import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()


sql_Email = """create table email (
        id int,
        mailbox int,
        sender int,
        subject text,
        body text,
        timestamp int
        );"""

sql_Mailbox = """create table mailbox (
        id int primary key,
        name text
        );
        """

sql_Contact = """create table contact (
        id int primary key,
        address text,
        name text
        );
        """

connection.execute(sql_Contact)
connection.execute(sql_Mailbox)
connection.execute(sql_Email)

class Email:
	def __init__(self, mailbox, sender, subject, content, timestamp):
		self.mailbox = mailbox
		self.sender = sender
		self.subject = subject
		self.content = content
		self.timestamp = timestamp

freeID = 1000
def createID():
	global freeID
	id = freeID
	freeID += 1
	return id

def listEmails(mailboxName): # diese Funktion wurde mithilfe chatGPT in der vorherigen Aufgabe erstellt und hier von mir geändert
    global cursor, connection
    cursor.execute("""select id from mailbox where name = ?;""", (mailboxName,))
    temp_mailbox = cursor.fetchone()[0] # id hier gespeichert an index 0
    cursor.fetchall()

    sql_select = "select * from email where mailbox = ? order by timestamp desc;"
    cursor.execute(sql_select, (temp_mailbox,))
    emails_data = cursor.fetchall()

    emails = {}
    for email_data in emails_data:
        cursor.execute("""select name from contact where id = ?;""", (email_data[2],))
        temp = cursor.fetchone()[0]
        email = Email(mailboxName, temp, email_data[3], email_data[4], TimeAsStr(email_data[5]))
        emails[email_data[0]] = email

    return emails



def createEmail(email):
    global connection, dictionary_mail, dictionary_contact
    temp = createID()
    cursor.execute("""select id from mailbox where name = ?;""", (str(email.mailbox),))
    temp_mailbox = cursor.fetchone()[0]

    cursor.fetchall()
    cursor.execute("""select id from contact where name = ?;""", (str(email.sender),))
    temp_contact = cursor.fetchone()[0]

    connection.execute("""insert into email (
		id, mailbox,sender ,subject, body, timestamp)
		values (?, ?, ? ,?, ?, ?);
		""", (temp, temp_mailbox, temp_contact ,email.subject, email.content, TimeAsNum(email.timestamp)))
    return temp


def TimeAsNum(zeit):
    timestamp = int(time.mktime(time.strptime(zeit, "%d.%m.%Y %H:%M:%S")))
    return timestamp

def TimeAsStr(zeit):
	localtime = datetime.fromtimestamp(zeit)
	return localtime.strftime('%d.%m.%Y - %H:%M:%S')



# Ab hier test Code
connection.execute("""insert into mailbox (id, name) values (15, "Inbox");""")
connection.execute("""insert into contact (id,address ,name) values (5,"Flurstr 153" ,"Bob");""")
mail = Email(
 		"Inbox",                 # mailbox
 		"Bob",                   # sender
 		"meeting",               # subject
 		"See you then!",         # content
 		"24.12.2025 20:00:00")   # timestamp

id = createEmail(mail)

print(listEmails("Inbox"))

# #Hier ausgabe der Tabelle email
# select_sql = """SELECT * FROM email""" #Test Code
# cursor.execute(select_sql)
#
# # Fetch all rows from the result set
# rows = cursor.fetchall()
#
# # Print the table content
# for row in rows:
#     print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")
#
#
#
#


connection.execute("""insert into mailbox (id, name) values (7, "Inbox");""")
connection.execute("""insert into mailbox (id, name) values (8, "Studium");""")
connection.execute("""insert into contact (id, address, name) values (11, "a@example.com", "Alice");""")
connection.execute("""insert into contact (id, address, name) values (13, "c@example.com", "Charlie");""")
connection.execute("""insert into contact (id, address, name) values (12, "b@example.com", "Bob");""")
connection.execute("""insert into email (id, mailbox, sender, subject, body, timestamp) values (50, 7, 12, "Hallo!", "Hi, wie geht es Dir?", 1766602800);""")
connection.execute("""insert into email (id, mailbox, sender, subject, body, timestamp) values (51, 7, 12, "Re: Re: Hallo!", "Bei mir auch alles gut.", 1766602860);""")
connection.execute("""insert into email (id, mailbox, sender, subject, body, timestamp) values (52, 8, 11, "Mensa", "Hunger???", 1766599200);""")
connection.execute("""insert into email (id, mailbox, sender, subject, body, timestamp) values (53, 8, 13, "Projekt", "Können wir am Mittwoch über das Projekt sprechen?", 1766602980);""")
connection.commit()

id = createEmail(Email("Inbox", "Alice", "Phishing", "Click this link immediately to avoid bankruptcy!", "24.12.2025 20:00:50"))
print("ID der neu erstellten EMail:", id)
print("Inbox content:")
for id, email in listEmails("Inbox").items():
	print(id, email.mailbox, email.sender, email.subject, email.content, email.timestamp)




#connection.commit()