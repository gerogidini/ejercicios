#un mail le cambia la parte despues del @ por libi.ut
mail = input("Mail: ")
print(mail[:mail.find('@')] + "@libi.ut")