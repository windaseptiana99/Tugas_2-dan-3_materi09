kata_spam = {"promo", "diskon", "hadiah", "gratis"}

email = input("Masukkan isi email: ")

kata_email = set(email.lower().split())

if kata_spam.intersection(kata_email):
    print("Email terdeteksi sebagai SPAM")
else:
    print("Email aman")