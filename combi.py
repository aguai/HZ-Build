import sqlite3 as sql

temp = []
allCode = open('allcode.txt', 'r').readlines()
for i in allCode:
    temp.append(int(i.strip('\n'), 0))
allCode = []
allCode = temp
temp = []
allCombShort = open('allcombShort.txt', 'r').readlines()
for i in allCombShort:
    temp.append(i.strip('\n'))
allCombShort = []
allCombShort = temp
temp = []
allCombLong = open('allcombLong.txt', 'r').readlines()
for i in allCombLong:
    temp.append(i.strip('\n'))
allCombLong = []
allCombLong = temp
temp = []
LEN = len(allCode)
AllCodeList = []
AllHZ = open('allHZ.txt', 'w')
# con = sql.connect('HZCombi.db')
# cur = con.cursor()
# cur.execute(
#    "CREATE TABLE HZCombiTable(UnicodeId INTEGER, HanZiChar TEXT, ShortCombi TEXT, LongCombi TEXT );")
for i in range(LEN):
    # cur.execute(
    #    "INSERT INTO HZCombiTable VALUES(%s, \'%s\', \'%s\', \'%s\');"
    #    %
    #    (allCode[i], chr(allCode[i]), allCombShort[i], allCombLong[i]))
    #print("INSERT INTO HZCombiTable VALUES(%s, %s, %s, %s)" % (allCode[i], chr(allCode[i]), allCombShort[i], allCombLong[i]))
    #AllCodeList.append({chr(allCode[i]): (allCode[i], allCombShort[i], allCombLong[i])})
    #AllHZ.write(chr(allCode[i])+'\n')
AllHZ.close()
# con.commit()
# con.close()
