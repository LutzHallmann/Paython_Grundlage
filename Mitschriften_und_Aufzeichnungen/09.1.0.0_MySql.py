'''
     Arbeiten mit mysql bzw. MariaDB
'''
# Es gibt verschiedene Connectoren zu MySQL bzw. MariaDB
# http://dev.mysql.com/downloads/connector/python bietet Python Connectoren an, diese werden
# über den Microsoft Installer installiert
# PYthon selbst bietet pymysql an. Dieses muss über den pip installiert werden:
# pip install mysql

# Voraussetzung für das Funktionerien ist natürlich eine vorhandenes DBMS, das separat installiert
# werden muss (MySQL oder MariaDB bieten hier entsprechende Downloads an)
# Alternativ über das Projekt XAMPP ... auch auf dieses DBMS kann dann zugegriffen werden
#
#
# Als Vorarbeit müssen die Zugriffsreche auf das DMBS erteilt werden. Dies wird in der DBMS-Instanz vorgenommen:
'''
     mysql> create database pytest
     mysql> grant all on pytest.* to pyuser@localhost identified by 'passwort'
'''
# so .. jetzt können wir uns anmelden als pyuser mit dem Passwort 'passwort'
#
import pymysql.cursors
import sys

try:
     connector = pymysql.connect(host='localhost',
                                 user='pyuser',
                                 password='passwort',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
except BaseException as err:
     print('Fehler im Verbindungsaufbau', err)
     sys.exit()
except:
     sys.exit()

# Wenn wir mit with arbeiten, wird der Cursor automatisch am Ende geschlossen
with connector.cursor() as cur:
     sql = 'Select * from mytable'
     cur.execute(sql)

'''
     Die hier verwendete Technik:
     1. Schritt: Auslesten eines Datensatzes
     2. Schritt: In die while-Schleife gehen
     3. Schritt: Ausgeben des ersten Datensatzes
     4. Schritt: holen des nächsten Datensatzes
     nennt man: Read-Ahead Technik
'''
     result = cur.fetchone() # hier gilt das Gleiche wie by der Übung sqllite -> ein Datensatz oder alle fetchall()
                              # oder mit einer for schleife
                              
     while result:
          print('Feld=%d txt=%s  number=%d' % (result['id'], result['txt'], result['number']))
          result = cur.fetchone()
# Da mit Beendigung der with-Bedinung gleichzeitig der Cursor geschlossen wurde,
# müssen wir jetzt nur noch den Connector schließen (was einem schließen der Datenbank gleichzusetzen ist)
connector.close()


'''
     Auch bei MySQL/MariaDB müssen wir Änderungen in der DB mit einem Commit bestätigen:
     connector.commit()
'''
