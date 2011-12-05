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
    msg['Subject'] = "Nieuwe openingsuren, eindejaarsregeling"
    msg['From'] = me
    msg['To'] = you
    # Create the body of the message (a plain-text and an HTML version).
    text = """Beste klant,\n\n
Frituur Den Baron veranderde de openingsuren vanaf deze week. Wat verandert er?\n\n
Tot nu toe waren we gesloten op zondagavond maar op vraag van meerdere klanten, hebben we besloten op zondag alsook op feestdagen 's avonds open te zijn.\n\n
Ter compensatie zijn we gesloten op maandag en woensdag onder de middag (maar 's avonds wel open)\n\n\n
Voor de feestdagen hebben we volgende regeling uitgewerkt:\n\n
Wij zijn gesloten op 24, 25 en 26 december en eveneens op 31 dec, 1 en 2 jan gesloten.\n\n\n
Wij hopen u hiermee van dienst te zijn.\n\n
Hieronder een overzicht van de nieuwe openingsuren.\n\n
Vriendelijke groet,\n\n
Team Den Baron\n\n
Maandag: 18.00u tot 22.30u\n
Dinsdag: 11.30u tot 22.30u\n
Woensdag: 18.00u tot 22.30u\n
Donderdag: 11.30u tot 22.30u\n
Vrijdag: 11.30u tot 22.30u\n
Zaterdag: 11.30u tot 22.30u\n
Zondag/feestdag: 18.00u tot 22.30u"""
    html = """<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>newsletter</title>
<style>.tblGenFixed td {padding:0 3px;overflow:hidden;white-space:normal;letter-spacing:0;word-spacing:0;background-color:#fff;z-index:1;} .dn {display:none} .tblGenFixed td.s0 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-top:1px solid #CCC;border-right:1px solid black;border-bottom:1px solid black;border-left:1px solid #CCC;} .tblGenFixed td.s2 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:center;vertical-align:bottom;white-space:normal;overflow:hidden;border-top:1px solid black;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s1 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:center;vertical-align:bottom;white-space:normal;overflow:hidden;border-top:1px solid black;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s16 {background-color:#6aa84f;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s17 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:left;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:1px solid black;border-left:1px solid black;} .tblGenFixed td.s18 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s19 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s12 {background-color:#38761d;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s9 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:;} .tblGenFixed td.s13 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:;} .tblGenFixed td.s7 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s14 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#ffffff;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s15 {background-color:#6aa84f;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#ffffff;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s8 {background-color:#6aa84f;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s5 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s21 {background-color:#6aa84f;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s22 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:1px solid black;} .tblGenFixed td.s6 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s3 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:center;vertical-align:bottom;white-space:normal;overflow:hidden;border-top:1px solid black;border-right:1px solid black;border-bottom:1px solid black;} .tblGenFixed td.s10 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:left;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:;border-left:1px solid black;} .tblGenFixed td.s20 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:1px solid black;} .tblGenFixed td.s11 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;text-decoration:none;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:;border-bottom:;} .tblGenFixed td.s4 {background-color:white;font-family:arial,sans,sans-serif;font-size:100.0%;font-weight:normal;font-style:normal;color:#000000;text-decoration:none;text-align:left;vertical-align:bottom;white-space:normal;overflow:hidden;border-right:1px solid black;border-bottom:;border-left:1px solid black;}</style>
</head>
<body>
<br>
<span style="font-family: Helvetica,Arial,sans-serif;"></span>
<table style="text-align: left; width: 1100px; height: 619px;"
border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td style="vertical-align: top; width: 107px;"><img
style="width: 102px; height: 144px;" alt="Logo"
src="https://lh3.googleusercontent.com/-FHc3mprd764/TcvKTq9hT7I/AAAAAAAAAGo/3KZlRN7QT5c/s144/Logo-Den-Baron3.png"><br>
</td>
<td style="vertical-align: top; width: 920px;"><span
style="font-family: Helvetica,Arial,sans-serif;">Beste klant,</span><br
style="font-family: Helvetica,Arial,sans-serif;">
<br style="font-family: Helvetica,Arial,sans-serif;">
<span style="font-family: Helvetica,Arial,sans-serif;">Frituur
Den Baron veranderde de openingsuren vanaf deze week. Wat verandert er?<br>
<br>
Tot nu toe waren we gesloten op zondagavond maar op
vraag van meerdere klanten, hebben we besloten op <span
style="font-weight: bold;">zondag</span> alsook op <span
style="font-weight: bold;">feestdagen 's avonds open</span> te zijn.<br>
<br>
Ter compensatie zijn we <span style="font-weight: bold;">gesloten</span>
op <span style="font-weight: bold;">maandag</span> en <span
style="font-weight: bold;">woensdag</span> onder de <span
style="font-weight: bold;">middag</span> (maar 's avonds wel open)<br>
<br>
</span><span style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><br>
<span style="font-family: Helvetica,Arial,sans-serif;">Voor de <span
style="font-weight: bold;">feestdagen</span> hebben we volgende
regeling uitgewerkt:<br>
<br>
Wij zijn <span style="font-weight: bold;">gesloten</span> op <span
style="font-weight: bold;">24, 25 en 26</span> december en eveneens op
<span style="font-weight: bold;">31 dec, 1 en 2 jan</span>
gesloten.<br>
</span> <span style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><span
style="font-family: Helvetica,Arial,sans-serif;"><img
style="width: 144px; height: 8px;" alt="slinger"
src="https://lh5.googleusercontent.com/-cY9ST8yIvps/TtYdkoHcvoI/AAAAAAAAAI0/LeguUjBixhs/s144/kerstslinger.png"></span><br>
<br>
<span style="font-family: Helvetica,Arial,sans-serif;">Wij hopen
u hiermee van dienst te zijn.<br>
<br>
</span><span style="font-family: Helvetica,Arial,sans-serif;">Hieronder
een
overzicht van de nieuwe openingsuren.</span><br>
<span style="font-family: Helvetica,Arial,sans-serif;"> <br>
Vriendelijke groet,<br>
<br>
<span style="font-style: italic;">Team Den Baron</span><br>
<br>
TIP:
Vind en volg ons op <a href="http://www.facebook.com/FrituurDenBaron">http://www.facebook.com/FrituurDenBaron</a><br>
</span></td>
<td style="vertical-align: top;"><br>
</td>
</tr>
<tr>
<td colspan="3" rowspan="1" style="vertical-align: top;">
<div id="content"> <br>
<big style="font-weight: bold;"><big><span
style="font-family: Helvetica,Arial,sans-serif;">Openingsuren:</span></big></big><br>
<hr style="width: 100%; height: 2px;"></div>
<div style="text-align: center;"><a
href="https://picasaweb.google.com/lh/photo/KCRSrBMLQcJdLLm8t8brIfuikVftCuzvx3hFWb3-RAc?feat=embedwebsite"><img
src="https://lh4.googleusercontent.com/-ic38UbDijk8/Tte8ERrDLoI/AAAAAAAAAI4/Oh2sAAMia7I/s800/detail_openingsuren.png"
border="0" height="132" width="800"></a></div>
</td>
</tr>
<tr>
<td><br>
</td>
<td colspan="2"><span
style="font-family: Helvetica,Arial,sans-serif;">Maandag:
18.00u tot 22.30u<br>
Dinsdag: 11.30u tot 22.30u<br>
Woensdag: 18.00u tot 22.30u<br>
Donderdag: 11.30u tot 22.30u<br>
Vrijdag: 11.30u tot 22.30u<br>
Zaterdag: 11.30u tot 22.30u<br>
Zondag/feestdag: 18.00u tot 22.30u</span><br>
</td>
</tr>
</tbody>
</table>
<span style="font-family: Helvetica,Arial,sans-serif;"></span><small><small>Deze
email werd u gestuurd omdat u opgenomen bent in het klantenbestand van
Frituur Den Baron (Belgian Food Group bvba). Indien u geen emails wenst
te ontvangen, reply dan eenvoudig op deze email met als onderwerp
"unsubscribe".</small></small><br
style="font-family: Helvetica,Arial,sans-serif;">
<br>
</body>
</html>"""
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
    s.sendmail(me, you, msg.as_string())
    s.quit()



conn = sqlite3.connect(ini.DB_NAME_SQLITE3, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
conn.text_factory = str
cur = conn.cursor()
cur.execute("select emailAddress, no from customer where emailAddress <> '' and no>=166")
customers = cur.fetchall()

for customer in customers:
    print "Sending %s, No: %s" % (customer[0],customer[1])
    DoSend(customer[0])
