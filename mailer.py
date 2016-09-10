import smtplib
 
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('smallfootprojekt@gmail.com','q1w2e3r4t5z6u7i8o9p0')
 
def sendVerify(mail, code):
    str = str(code)
    msg = """Subject: SmallFoot verification \n\n
   Hello environmentalist!
 
   Your verification code is: """+ str + """
 
   Your SmallFoot-Team
   """
    smtpObj.sendmail("smallfootprojekt@gmail.com", mail, msg)
    print ("Mail Sent at " + mail + ", with code " + code)
