##import smtplib
##import time
##import imaplib
##import email
##
##ORG_EMAIL   = "@mathobotix.com","
##FROM_EMAIL  = "fdepaz" + ORG_EMAIL
##FROM_PWD    = "fernando123"
##SMTP_SERVER = "imap.gmail.com","
##SMTP_PORT   = 993
##
##mail = imaplib.IMAP4_SSL(SMTP_SERVER)
##mail.login(FROM_EMAIL,FROM_PWD)
##
##mail.select('inbox')
##
##type, data = mail.search(None, 'ALL')
##mail_ids = data[0]
##id_list = mail_ids.split()
##
##first_email_id = int(id_list[0])
##latest_email_id = int(id_list[-1])
##
##typ, data = mail.fetch(latest_email_id, '(RFC822)' )
##print data

x = """
Dear Parents of {},

As you may know, our Summer camps are just 2 weeks away. If your child is currently enrolled under our 3:00-4:40 or 10:00-11:40 class please consult with our Mathobotix Administrator or Mentors to properly transition to one of our new week days classes during our Summer schedule. You may also reply this email or call @ 949-857-1419, and there we can help you reschedule your child's class. 

Our Summer scheduled will be in affect from June 12th through August 28th. Below will be the new schedule:
Monday - Friday
o 4:40-6:20 and 6:20-8:00
o 3:00-4:40 or 10:00-11:40 not available 
Saturday
o 9:00-10:40, 11:00-12:40, 1:00-2:40

If you have any questions or concerns please reply to this email and our team will be there to help. 

We apologize for any inconvenience and appreciate your understanding,

Mathobotix Team
 
Creating Problem Solvers and Solution Providers...for a better tomorrow
1000 Roosevelt. Suite 200 IRVINE CA 92620
10900 Los Alamitos Blvd. Unit 146 Los Alamitos CA 90720

"""

names = [
"Kyrus Huang",
"Jarde Davis",
"Ido Bahalul",
"Devon Chang",
"Sean Yu",
"Mason Mcintyre",
"Greg Minasian",
"Eliza Karabian", 
"Rohan Hablani",
"Murad Malik",
"Kuan Fu",
"Roshan Patel",
"Kyrus Huang",
"Bryant Shi",
"Benjamin Chen",
"John Kim",
"Hannah Karabian", 
"Denis Senbay",
"Branden Tang",
"Taewon Kim",
"Alvin Kim",
"Ashlyn Burrus",
"Kahlen Burrus",
"Cadence Burrus",
"Alexis Jude", 
"Adam Mahook",
"Lawrence Xiong",
"Keijay Huang",
"Lucy Xu",
"Yuyand (Sunny) Zhang",
"Jeremy Ahn",
"Carmen Yang",
"Jiwon Jeong",
"Kyrus Huang",
"Andy(Yuanxin) Jia",
"Aaron Esmaeili-tehrani",
"Christian Ahn",
"Jason Anthony",
"Euan Tandiono",
"Aran Pattarachanyahul",
"Tom Li",
"Leonard Yu",
"Anthony Liang",
"Andre Ramos"

]
emails=[
"sunshenginv@yahoo.com",
"jandmd@gmail.com",
"ocpolymerclay@gmail.com",
"leannelu11@yahoo.com",
"sunyelle@outlook.com",
"marjoquinonez@hotmail.com",
"kirsten.minasian@sbcglobal.net",
"bita13@gmail.com",
"drshablani@yahoo.com",
"tanhuss@hotmail.com",
"huazeng@hotmail.com",
"rekhap@sbcglobal.net",
"sunshenginv@yahoo.com",
"shirleywang996@yahoo.com",
"chenbwj@gmail.com",
"taekim31@cox.net",
"bita13@gmail.com",
"senbay1@hotmail.com",
"sherrilynne_tang@yahoo.com",
"jiwoong1kim@gmail.com",
"jiwoong1kim@gmail.com",
"dhermosi@gmail.com",
"dhermosi@gmail.com",
"dhermosi@gmail.com",
"felssy_antoni@yahoo.com",
"Candiharos@yahoo.com",
"mariafabruada@yahoo.com",
"mantsignw@gmail.com",
"jececasun@gmail.com",
"bzhang.usa@gmail.com",
"angelahong@hotmail.com",
"kenyang1@gmail.com",
"hejin1005@gmail.com",
"sunshenginv@yahoo.com",
"haobang592@gmail.com",
"robintehrani@hotmail.com",
"alinaahn@gmail.com",
"fati_jas@yahoo.com",
"tandionoeuan@gmail.com",
"janpan89@hotmail.com",
"yadongli1975@gmail.com",
"minzhang_mail@yahoo.com",
"joanne_geng@yahoo.com",
"laurapeck007@gmail.com",
    ]
names = ["Fernando de Paz"]
emails = ["fdepaz@mathobotix.com"]
import smtplib
from email.Message import Message


gmail_user = 'mxfrontdesk@gmail.com'
gmail_pwd = 'Frontdesk11'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
print(len(names))
print(len(emails))
for i in range(len(names)):
    print(names[i])
    x = ("""
Dear Parents of {},

As you may know, our Summer camps are just 2 weeks away. If your child is currently enrolled under our 3:00-4:40 or 10:00-11:40 class please consult with our Mathobotix Administrator or Mentors to properly transition to one of our new week days classes during our Summer schedule. You may also reply this email or call @ 949-857-1419, and there we can help you reschedule your child's class. 

Our Summer scheduled will be in affect from June 12th through August 28th. Below will be the new schedule:
Monday - Friday
o 4:40-6:20 and 6:20-8:00
o 3:00-4:40 or 10:00-11:40 not available 
Saturday
o 9:00-10:40, 11:00-12:40, 1:00-2:40

If you have any questions or concerns please reply to this email and our team will be there to help. 

We apologize for any inconvenience and appreciate your understanding,

Mathobotix Team
 
Creating Problem Solvers and Solution Providers...for a better tomorrow
1000 Roosevelt. Suite 200 IRVINE CA 92620
10900 Los Alamitos Blvd. Unit 146 Los Alamitos CA 90720

""").format(names[i])
    m = Message()
    m['From'] = 'mxfrontdesk@gmail.com'
    m['To'] = emails[i]
    m['X-Priority'] = '2'
    m['Subject'] = "Mathobotix Summer Schedule Notice, Class Change Inside"
    
    m.set_payload(x)
    smtpserver.sendmail(gmail_user, emails[i], m.as_string())
print 'done!'
smtpserver.close()
