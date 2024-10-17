#ДЗ 7.2. Модифікувати рядок
#На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так,
#щоб вони завжди починалися з великої літери та закінчувалися крапкою.
#Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
#додавати ще одну не потрібно, це буде помилкою
#Вхідні аргументи: string.
#Вихідні аргументи: string.
#Замість pass необхідно написати Ваше рішення.
#def correct_sentence(text):
#     pass
#assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
#assert correct_sentence("hello") == "Hello.", 'Test2'
#assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
#assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
#assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
#print('ОК')
def correct_sentence(text):
   if text[-1]==".":
       str1=text[0].upper()
       str2=text[1:].lower()
       text=str1+str2
       kki=text.count(".")
       if kki>1:
           for i in range(kki-1):
               ind=text.find('.')
               text = text[:ind].title() + '.' + text[ind+1:].title()
   elif text[-1]!=".":
       str1=text[0].upper()
       str2=text[1:].lower()
       text=str1+str2+"."
       kki=text.count(".")
       if kki>1:
           for i in range(kki-1):
               ind=text.find('.')
               text = text[:ind].title() + '.' + text[ind+1:].title()
   return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print("OK")