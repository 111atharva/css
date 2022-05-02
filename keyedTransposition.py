import math


def keyTransEncrypt(msg, key):
    cText = ''
    msgsize = len(msg)
    colsize = len(key)
    rowsize = math.ceil(msgsize/colsize)
    keyList = []
    for num in key:
        keyList.append(int(num))
    print(keyList)
    table = []
    index = 0
    for x in range(rowsize):
        col = []
        for y in range(colsize):
            if index < msgsize:
                col.append(msg[index])
            else:
                col.append(" ")
            index += 1
        table.append(col)
    print(table)
    for row in table:
        for k in keyList:
            cText += row[k]
    print([cText])
    return cText
    #     k=0
    #     jumbledarr=template
    #     for element in msgarr:
    #         jumbledarr[keyarr[k%arrsize]]=element
    #         k+=1
    #     jumbedmsg+=jumbledarr
    # print(jumbledarr)


def keyTransDecrypt(cText, key):
    dText = ''
    cTextLen = len(cText)
    colsize = len(key)
    rowsize = math.ceil(cTextLen/colsize)
    keyList = []
    for num in key:
        keyList.append(int(num))
    index = 0
    table = []
    for i in range(rowsize):
        col = []
        for j in range(colsize):
            col.append(cText[index])
            index += 1
        table.append(col)
    print(table)

    for row in table:
        dList = [" "]*colsize
        k = 0
        for ele in row:
            dList[keyList[k % colsize]] = ele
            k += 1
        for cha in dList:
            dText += cha
    print(dText)
    return dText


key = '30421'
msg = 'Hello world'
input('Enter Your Message:')
cText = keyTransEncrypt(msg, key)
keyTransDecrypt(cText, key)
