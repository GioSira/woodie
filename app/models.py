from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(100),
                         index=False,
                         unique=True,
                         nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    created_on = db.Column(db.DateTime,
                           default=date.today,
                           index=False,
                           unique=False,
                           nullable=False)
    country = db.Column(db.String(200),
                        index=False,
                        unique=False,
                        nullable=False)
    gender = db.Column(db.String(200),
                       index=False,
                       unique=False,
                       nullable=True)
    institution = db.Column(db.String(200),
                            index=False,
                            unique=False,
                            nullable=True)
    type = db.Column(db.String(200),
                     index=False,
                     unique=False,
                     nullable=True)
    size = db.Column(db.Integer,
                     index=False,
                     unique=False,
                     nullable=True)
    role = db.Column(db.String(200),
                     index=False,
                     unique=False,
                     nullable=True)
    inf_accepted = db.Column(db.Boolean,
                           index=False,
                           unique=False,
                           nullable=True)
    data_compiled = db.Column(db.Boolean,
                           index=False,
                           unique=False,
                           nullable=True)
    hard_indicators_compiled = db.Column(db.Boolean,
                           index=False,
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def set_inf_accepted(self):
        self.inf_accepted = True

    def set_personal_info(self, gender, institution, type, size, role):
        self.data_compiled = True
        self.gender = gender
        self.institution = institution
        self.type = type
        self.size = size
        self.role = role

    def set_hard_indicators_compiled(self):
        self.hard_indicators_compiled = True

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_inf_accepted(self):
        return self.inf_accepted or False

    def is_userinfo_compiled(self):
        return self.data_compiled or False

    def is_hard_indicators_compiled(self):
        return self.hard_indicators_compiled or False

    def __repr__(self):
        return '<User {}>'.format(self.username)


class HardIndicatorsOD(db.Model):

    __tablename__ = 'hard_od'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=date.today, index=False, unique=False, nullable=False)

    d1_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d1_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d1_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d1_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d2_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4_5 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_5 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_6 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_7 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d3_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d3_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d4 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d5 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def get_values(self):

        data = {"d1_1": self.d1_1,
                "d1_2": self.d1_2,
                "d1_3": self.d1_3,
                "d1_4": self.d1_4,
                "d2_1": self.d2_1,
                "d2_2": self.d2_2,
                "d2_3": self.d2_3,
                "d2_4_1": self.d2_4_1,
                "d2_4_2": self.d2_4_2,
                "d2_4_3": self.d2_4_3,
                "d2_4_4": self.d2_4_4,
                "d2_4_5": self.d2_4_5,
                "d2_5": self.d2_5,
                "d2_6": self.d2_6,
                "d2_7": self.d2_7,
                "d3_1": self.d3_1,
                "d3_2": self.d3_2,
                "d4": self.d4,
                "d5": self.d5}

        return data

    def get_aggregated_data(self):

        data = {"id": self.id,
                "created_at": self.created_at.strftime("%d/%m/%y"),
                "open": self.d1_1 + self.d1_2 + self.d1_3 +self.d1_4 +\
                        self.d2_1 + self.d2_2 + self.d2_3 + self.d2_4_1 + self.d2_4_2 + \
                        self.d2_4_3 + self.d2_4_4 + self.d2_4_5 + self.d2_5 + self.d2_6 +self.d2_7 +\
                        self.d3_1 +self.d3_2 + self.d4 + self.d5}

        return data

    def __repr__(self):
        return "<HOD: {}".format(self.id)


class HardIndicatorsWB(db.Model):

    __tablename__ = 'hard_wb'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=date.today, index=False, unique=False, nullable=False)

    d6_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d7 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d8_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d9 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d10_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d10_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d10_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d11 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d12 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d13 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d14 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d15 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d16 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d17 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d18 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d19 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d20 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d21 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def get_values(self):

        data = {"d6_1": self.d6_1,
                "d6_2": self.d6_2,
                "d6_3": self.d6_3,
                "d6_4": self.d6_4,
                "d7": self.d7,
                "d8_1": self.d8_1,
                "d8_2": self.d8_2,
                "d8_3": self.d8_3,
                "d8_4": self.d8_4,
                "d9": self.d9,
                "d10_1": self.d10_1,
                "d10_2": self.d10_2,
                "d10_3": self.d10_3,
                "d11": self.d11,
                "d12": self.d12,
                "d13": self.d13,
                "d14": self.d14,
                "d15": self.d15,
                "d16": self.d16,
                "d17": self.d17,
                "d18": self.d18,
                "d19": self.d19,
                "d20": self.d20,
                "d21": self.d21}

        return data

    def get_aggregated_data(self):

        data = {"id": self.id,
                "created_at": self.created_at.strftime("%d/%m/%y"),
                "wb": self.d6_1 +self.d6_2 + self.d6_3 + self.d6_4 + self.d7 +self.d8_1 + self.d8_2 +\
                      self.d8_3 + self.d8_4 + self.d9 + self.d10_1 + self.d10_2 + self.d10_3 +self.d11 +\
                      self.d12 + self.d13 + self.d14 + self.d15 + self.d16 + self.d17 + self.d18 +self.d19 +\
                      self.d20 + self.d21}

        return data

    def __repr__(self):
        return "<HWB: {}".format(self.id)



class SoftIndicatorsWB(db.Model):

    __tablename__ = 'soft_wb'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=date.today, index=False, unique=False, nullable=False)

    d1 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d2_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_5 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d2_5_text = db.Column(db.String(400), index=False, unique=False, nullable=False)

    d3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d3_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d4_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d4_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d4_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d4_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d5 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d5_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d6 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_1_text = db.Column(db.String(400), index=False, unique=False, nullable=False)
    d6_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_3_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_3_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_3_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_3_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_4_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_4_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_4_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d6_4_text = db.Column(db.String(400), index=False, unique=False, nullable=False)
    d6_5 = db.Column(db.String(400), index=False, unique=False, nullable=False)

    d7 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d8_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_1_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_1_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d8_1_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d9 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d10 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d10_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d10_2 = db.Column(db.String(400), index=False, unique=False, nullable=False)

    d11 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d12 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d13 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d14 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d15 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d16_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d16_2 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d16_3 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d16_4 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d16_text = db.Column(db.String(400), index=False, unique=False, nullable=False)

    d17 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d18 = db.Column(db.Integer, index=False, unique=False, nullable=False)
    d18_1 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d19 = db.Column(db.Integer, index=False, unique=False, nullable=False)

    d20 = db.Column(db.String(400), index=False, unique=False, nullable=False)
    
    def get_values(self):

        data = {}

        return data

    def __repr__(self):
        return "<SWB: {}".format(self.id)
