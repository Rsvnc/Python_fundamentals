# mail = "mailto: Clarusway admission@clarusway.com, 6 Haz 2021 Paz, 21:08 tarihinde şunu yazdı:"

# Write python code that outputs "clarusway.com" from the string in the "mail" variable.

# Expected Output: clarusway.com

mail = "mailto: Clarusway admission@clarusway.com, 6 Haz 2021 Paz, 21:08 tarihinde şunu yazdı:"
print(mail[mail.index("@")+1:mail.index(",")])




