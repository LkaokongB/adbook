print ("****************************************************************************")
print ('                                    เสนอ\n                            อ.ดร.นฏกร  ประมายันต์\n')
print ("                                  จัดทำโดย")
print ("                       นางสาวธันยชนก ทรวงโพธิ์ 623050276-7")
print ("                       นางสาวอรพันธุ์  กั้ววัลย์   623050283-0")
print ("                       นางสาวมนสิชา หมู่สูงเนิน  623050413-3\n")
print("                        นักศึกษาชั้นปีที่ 1 สาขาคอมพิวเตอร์ศึกษา")
print("                        คณะศึกษาศาสตร์ มหาวิทยาลัยขอนแก่น\n")
print ("****************************************************************************\n")
from datetime import date
now=date.today().strftime('%d/%m/%Y')
import os
filename = ' '
a = []
line_no = 1
fdata=open('d:\\data_book.txt','a',encoding="UTF8")
fdata.writelines('\nวันที่ %s\n'%(now))
while True:
    
    print ('****************************** ระบบลงทะเบียนหนังสือ ***************************')
    print ('เพิ่มหนังสือ [a]  จบการลงทะเบียน [x]')
    #line_no=1
    fdata=open('d:\\data_book.txt','a',encoding="UTF8")
    manu = input('Plese select manu :')
    manu = manu.lower() 
    if manu == 'a' :
        print('\nชื่อหนังสือ/ผู้แต่ง/สำนักพิมพ์/ปีที่พิมพ์/ครั้งที่พิมพ์')
        book=input(' Enter Data :  ')
        a.append(book)
        print ('\n------------ข้อมูลหนังสือได้ถูกบันทึกเรียบร้อยแล้วค่ะ----------------\n')
        #print ('เพิ่มหนังสือ [a]  จบการลงทะเบียน [x]')
        #manu = input('Plese select manu :')
        manu = manu.lower() 
        fdata.writelines('%d,%s \n'%(line_no,book))
        line_no = line_no+1
    fdata = open('d:\\data_book.txt','r',encoding="UTF8")
    data = fdata.read()
    
    if manu =='x':
        print ('\n')
        print (now)
        print ('\n')
        print ('                                                  รายการหนังสือ')
        print ('{0:-<120}'.format(""))
        print ('{0:' '<30}{1:' '<30}{2:' '<30}{3:' '<30}{4:' '<30}'.format('ชื่อหนังสือ','ผู้แต่ง','สำนักพิมพ์','ปีที่พิมพ์','ครั้งที่พิมพ์'))
        print ('{0:-<120}'.format(""))
        for d in a :
            e = d.split('/')
            print('{0[0]:<27}{0[1]:<27}{0[2]:<27}{0[3]:<27}{0[4]:<27}'.format(e))
        print ('{0:-<120}'.format(""))
        break

filename = ("d:\\data_book.txt")
print('data_book.txt %s' %filename)
os.system(filename)
fdata.close()
#ญาณสื่อรัก/ณารา/พิมพ์คำ/2555/5
#กับดักรักลวง/ร่มแก้ว/พิมพ์คำ/2553/4
#เลห์บ่วงมนตรา/ซ่อนกลิ่น/พิมพ์คำ/2555/4
#มายาร้อยใจ/เก้าแต้ม/พิมพ์คำ/2554/5
#เปลวไฟในสายลม/แพรณัฐ/พิมพ์คำ/2554/4