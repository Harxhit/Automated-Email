import smtplib
import datetime as dt 
import random 

now = dt.datetime.now()
weekday = now.weekday()

email = "pariharharshit760@gmail.com"
password = "gvja rnuz zvxe payx"

if weekday == 3 :
  with open("C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\Birthday-Wisher\\quotes.txt") as data :
    quotes = data.readlines()
    quote = random.choice(quotes)

  with smtplib.SMTP ("smtp.gmail.com")  as conncetion :
    conncetion.starttls()
    conncetion.login(email , password)
    conncetion.sendmail(
      from_addr="pariharharshit760@gmail.com" ,
      to_addrs= "harshit.parihar@yahoo.com" , 
      msg=f"Subject:Monday Motivation\n\n{quote}"
      )
  
 
  



