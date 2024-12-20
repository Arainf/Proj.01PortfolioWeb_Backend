from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_fName = db.Column(db.String(100))
    account_lName = db.Column(db.String(100))
    account_email = db.Column(db.String(100), unique=True)
    account_password = db.Column(db.String(100))
    account_username = db.Column(db.String(100))
    account_phoneNumber = db.Column(db.String(100))
    account_DOB = db.Column(db.date)

    def __init__(self, account_fName, account_lName, account_email, account_password, account_username, account_phoneNumber, account_DOB ):
        self.account_fName = account_fName
        self.account_lName = account_lName
        self.account_email = account_email
        self.account_password = account_password
        self.account_username = account_username
        self.account_phoneNumber = account_phoneNumber
        self.account_DOB = account_DOB
                              