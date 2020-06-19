# smtplib module send mail
#https://gist.github.com/yzhong52/d703ec82aeee24164f0c


import smtplib, sys

#print('starting app....\n')


def sendEmail(name,email,phone,msg):
    TO = 'solarparadisevalley@gmail.com'
    SUBJECT = 'Help is Needed!'
    TEXT = 'Client\'s Name: ' + name
    TEXT = TEXT + ' \nClient Phone: ' + phone
    TEXT = TEXT + ' \nMessage: ' + msg
    TEXT = TEXT + '\n Client Email: ' + email

    #print('Text: ', TEXT)

    # Gmail Sign In
    sender = "solarparadisevalley@gmail.com"
    #print('sender created...\n')

    password = "SolarGoogle20"

    #print('password created...\n')

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
        print ('email sent', file=sys.stderr)
    except:
        print ('error sending mail', file=sys.stderr)

    server.quit()