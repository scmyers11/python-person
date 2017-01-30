class Person():

    def __init__(self, name, emails=[], phone=""):
        self.name = name
        self.emails = emails
        self.phone = phone

    def primaryEmail(self):
        if len(self.emails) > 0:
            return self.emails[0]
        else:
            return "No Emails Set"

    def addEmail(self, email):
        self.emails.append(email)

    def changePhoneNumber(self, phone):
        self.phone = phone

    def __str__(self):
        return "Hi! My name is %(name)s. You can reach me at %(phone)s or %(email)s." % { "name" : self.name, "phone" : self.phone, "email" : self.primaryEmail() }
