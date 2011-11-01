import smtplib

import sqlite3
import ini

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address

def DoSend(you):
    me = '"Frituur Den Baron" <info@frituurdenbaron.be>'
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Feestdagen november."
    msg['From'] = me
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    text = """Beste klant,\n
    Frituur Den Baron zal op dinsdag en woensdag 1 en 2 november.\n
    Op vrijdag 11 november zijn wij open!"""
    html = """\
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>newsletter</title>
</head>
<body>
<span style="font-family: Helvetica,Arial,sans-serif;"></span>
<table style="text-align: left; width: 100%;" border="0" cellpadding="2"
cellspacing="2">
<tbody>
<tr>
<td style="vertical-align: top;"><img
style="width: 102px; height: 144px;" alt="Logo"
src="https://lh3.googleusercontent.com/-FHc3mprd764/TcvKTq9hT7I/AAAAAAAAAGo/3KZlRN7QT5c/s144/Logo-Den-Baron3.png"><br>
</td>
<td style="vertical-align: top;"><span
style="font-family: Helvetica,Arial,sans-serif;">Beste klant,</span><br
style="font-family: Helvetica,Arial,sans-serif;">
<br style="font-family: Helvetica,Arial,sans-serif;">
<span style="font-family: Helvetica,Arial,sans-serif;">Frituur
Den Baron is <span style="font-weight: bold;">gesloten</span> op <span
style="font-weight: bold;">dinsdag en woensdag 1 en 2 november</span>.</span><br
style="font-family: Helvetica,Arial,sans-serif;">
<br style="font-family: Helvetica,Arial,sans-serif;">
<span style="font-family: Helvetica,Arial,sans-serif;">Wij zijn
<span style="font-weight: bold;">open</span> op <span
style="font-weight: bold;">vrijdag 11 november</span>.</span><br
style="font-family: Helvetica,Arial,sans-serif;">
<br style="font-family: Helvetica,Arial,sans-serif;">
<span style="font-family: Helvetica,Arial,sans-serif;">PS:
Vergeet komende zaterdagnacht 29 oktober uw horloge niet aan te passen
naar </span><a style="font-family: Helvetica,Arial,sans-serif;"
href="http://www.belgium.be/nl/nieuws/2011/news_overgang_winteruur_2011.jsp"
target="_blank">winteruur</a><span
style="font-family: Helvetica,Arial,sans-serif;">, 3u wordt 2u.<br>
<br>
Vriendelijke groet,<br>
<br>
Team Den Baron<br>
</span></td>
</tr>
</tbody>
</table>
<span style="font-family: Helvetica,Arial,sans-serif;"></span><small><small>Deze
email werd u gestuurd omdat u opgenomen bent in het klantenbestand van
frituur den baron (Belgian Food Group bvba). Indien u geen emails wenst
te ontvangen, reply dan eenvoudig op deze email met als onderwerp
"unsubscribe".</small></small><br
style="font-family: Helvetica,Arial,sans-serif;">
<br>
</body>
</html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("dennis.decoene@gmail.com", "CramIt002")
    ########s.sendmail(me, you, msg.as_string())
    print you
    s.quit()



conn = sqlite3.connect(ini.DB_NAME, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
conn.text_factory = str
cur = conn.cursor()
cur.execute("select emailAddress from customer where emailAddress <> '' and no>157")
customers = cur.fetchall()

for customer in customers:
    DoSend(customer[0])