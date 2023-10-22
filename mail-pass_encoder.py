import base64


mail = base64.b64encode(input("Mail: ").encode('utf-8')).decode()
password = base64.b64encode(input("Password: ").encode('utf-8')).decode()

print("\n\nEncoded mail:")
print(mail)

print("\nEncoded password:")
print(password)
input("")
