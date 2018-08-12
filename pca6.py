__author__ = 'Vishal'
import click
import sys
import MySQLdb as sqlDB
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



@click.command()
@click.argument("college_name", nargs=1)
def college_report(college_name):
    """Sends out a class report to specified email."""

    dbname = 'pizza'
    fromEmail = "email_address"
    toEmail = "email_address"
    password = "pass_sender_email"
    
    try:
        db = sqlDB.connect(host="localhost", user="root", passwd="shanu", db=dbname)
        
    except sqlDB.Error:
        print("Error while connecting to db")
        return
    except MySQLdb.Error:
        print("Error occured while creating schema")
        return
    except MySQLdb.linebaseError:
        print("line base Error occured while creating schema")
        return
    except MySQLdb.IntegrityError:
        print("Integrity Error occured while creating schema")
        return
    except MySQLdb.NotSupportedError:
        print("not supported Error occured while creating schema")
        return 
    else:
        print("Connected to database %s\n" %dbname)     
    
    
    query = db.cursor()

    sql_cmd1 = f""" SELECT m.* FROM marks m INNER JOIN students s
                    ON m.name = s.dbname
                    WHERE s.college = '{college_name}'
               """
    
    sql_cmd2 = f""" SELECT count(*), MIN(total), MAX(total), AVG(total)
                    FROM marks m INNER JOIN students s
                    ON m.name = s.dbname
                    WHERE s.college = '{college_name}'
               """
               
    sql_cmd3 = f""" SELECT count(*), MIN(total), MAX(total), AVG(total) FROM
                    marks m INNER JOIN students s
                    ON m.name = s.dbname
               """

   
       
    
    
    text="<html><head></head><body><p>The list of college students and their scores</p>"
    text+= "<table><tr><th>Name</th><th>Test 1</th><th>Test 2</th><th>Test 3</th><th>Test 4</th><th>Total</th></tr>"
    
    query.execute(sql_cmd1)
    res = query.fetchall()
    
    for row in res:
        text += "<tr><td>"+str(row[0])+"</td><td>" + str(row[2]) + "</td><td> " + str(row[3]) + "</td><td> " + str(row[4]) + "</td><td>"+str(row[5])+"</td></tr>"
    text+="</table>"
    
    query.execute(sql_cmd2)
    res = query.fetchall()
    text+="<p><b>CollegeStats for "+college_name+" college</b></p>"
    text+="<table><tr><th>count of students</th><th> min</th><th> max </th><th>avg</th></tr>"
    
    for row in res:
        text += "<tr><td>"+str(row[0])+"</td><td>" + str(row[1]) + "</td><td> " + str(row[2]) + "</td><td> " + str(row[3]) + "</td></tr>"
    text+="</table>"
    
    query.execute(sql_cmd3)
    res = query.fetchall()
    text+="<p><b>The global summary for the whole class</b></p>"
    text+="<table><tr><th>count of students</th><th> min</th><th> max </th><th>avg</th></tr>"
    
    for row in res:
        text += "<tr><td>"+str(row[0])+"</td><td>" + str(row[1]) + "</td><td> " + str(row[2]) + "</td><td> " + str(row[3])+"</td></tr>"
    text+="</table></body></html>"
    
    print(text)
      
    
    
    msg=MIMEMultipart('alternative')
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = f'college report of colllege {college_name}'
    part1=MIMEText(text,'html')
    msg.attach(part1)
    #msg=msg.as_string()
   # print(msg.as_string)
    try:
        print("Establishing connection to Gmail")
        smtp_client = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_client.ehlo()
        smtp_client.starttls()
        
        smtp_client.login(fromEmail, password)
        temp=msg.as_string()
        smtp_client.sendmail(fromEmail,toEmail,temp)
    
    except smtplib.SMTPAuthenticationError:
        click.echo("Check password or email mismatch")
        
    except socket.error:
        click.echo("Error in establishing a connection with gmail server")
    
    except smtplib.SMTPException:
        click.echo("Unknown Error", sys.exc_info()[0])
    
    except smtplib.SMTPNotSupportedError:
        click.echo("SMTP AUTH extension not supported by ur email service provider.")
    
    else:
        print("Mail Succefully Dispatched")
    finally:
        smtp_client.quit()
        db.close()


if __name__ == '__main__':
    college_report()
