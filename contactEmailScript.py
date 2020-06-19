# smtplib module send mail
#https://gist.github.com/yzhong52/d703ec82aeee24164f0c


import smtplib

#print('starting app....\n')


def sendEmail(name,email,phone,msg)
    TO = email
    SUBJECT = 'Help is Needed!'
    TEXT = ("Hello %s", name) + msg + phone

    #print('message variable created...\n')

    # Gmail Sign In
    sender = "solarparadisevalley@gmail.com"
    print('sender created...\n')

    password = "SolarGoogle20"

    print('password created...\n')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()