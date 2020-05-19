from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, widgets, TextAreaField
from wtforms import SelectMultipleField, SelectField, IntegerField, SubmitField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import EqualTo, Length, DataRequired, NumberRange
from app.countries_dict import countries
from app.gender import gender_select


class RequiredRadioField(RadioField):

    def __iter__(self):

        opts = dict(
            widget=self.option_widget,
            _name=self.name,
            validators=self.validators,
            _form=None,
            _meta=self.meta
        )

        for i, (value, label, checked) in enumerate(self.iter_choices()):
            opt = self._Option(label=label, id="%s-%d" % (self.id, i), **opts)
            opt.process(None, value)
            opt.checked = checked
            yield opt


class MultipleCheckboxField(SelectMultipleField):

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class SignupForm(FlaskForm):

    username = StringField('Username',
                       validators=[DataRequired()])

    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Ripeti Password',
                            validators=[DataRequired(),
                                        EqualTo('password', message='Passwords must match.')])

    country = SelectField("Paese", choices=[("None", "Seleziona il tuo Paese")]+countries, validators=[DataRequired()])


class InformativeForm(FlaskForm):

    accept = SubmitField("Accetta")
    reject = SubmitField("Rifiuta")


class ProfileForm(FlaskForm):

    gender = SelectField("Genere", choices=[("None", "Seleziona il tuo genere")]+gender_select,
                         validators=[DataRequired()])
    institution = StringField("Nome ente di appartenenza",
                              validators=[DataRequired()])
    type = StringField("Tipo di ente",
                       validators=[DataRequired()])
    size = IntegerField("Dimensione dell'ente",
                        validators=[DataRequired()])
    role = StringField("Ruolo all'interno dell'ente", validators=[DataRequired()])


class HardIndicatorsWBForm(FlaskForm):

    d6 = RequiredRadioField("d6", choices=[
        ("d6.a", "legge dedicata alla protezione dei whistleblower (la protezione del whistleblower è l’unico scopo della legge)"),
        ("d6.b",
         "protezione completa dei whistleblower attraverso leggi più ampie o disposizioni in leggi settoriali (es. anticorruzione, media, protezione dei testimoni…)"),
        ("d6.c",
         "protezione dei whistleblower sparsa in più leggi o disposizioni in leggi settoriali (es. anticorruzione, media, protezione degli informatori…)"),
        ("d6.d", "Nessuna delle precedenti")],
                            validators=[DataRequired()])

    d7 = RadioField("d7", choices=[("d7.a", "Si"), ("d7.b", "No")])

    d8 = RequiredRadioField("d8", choices=[("d8.a", "solo nel settore pubblico"),
                                           ("d8.b", "in entrambi i settori, pubblico e privato")],
                            validators=[DataRequired()])

    d9 = MultipleCheckboxField("d9", choices=[
        ("d9.a", "solo lavoratori dipendenti"),
        ("d9.b", "appaltatori, subappaltatori, fornitori"),
        ("d9.c", "consulenti o altri lavoratori autonomi"),
        ("d9.d", "volontari, tirocinanti")])

    d10 = RadioField("d10", choices=[("d10.a", "qualunque tipo di violazione e abuso che può causare un pregiudizio all’interesse pubblico"),
                                     ("d10.b",
                                      "solo alcuni tipi di violazioni o solo in alcuni settori (ad esempio frode finanziaria, evasione fiscale…)")])

    d11 = RequiredRadioField("d11", choices=[("d11.a", "Si"), ("d11.b", "No")], validators=[DataRequired()])

    d12 = MultipleCheckboxField("d12", choices=[("d12.a", "canali di segnalazione interna"),
                                                ("d12.b", "canali di segnalazione esterna ad una autorità competente designata"),
                                                ("d12.c", "canali di divulgazione pubblica")])

    d13 = RequiredRadioField("d13", choices=[("d13.a", "la procedura di segnalazione è costituita da un sistema a tre livelli"),
                                             ("d13.b",
                                              "il whistleblower è libero di scegliere il canale per effettuare la segnalazione")],
                             validators=[DataRequired()])

    d14 = RequiredRadioField("d14", choices=[("d14.a", "Si"),
                                             ("d14.b",
                                              "Si, ma la rivelazione dell’identità è permessa in alcune specifiche circostanze e solo con il consenso del whistleblower"),
                                             ("d14.c", "No")],
                             validators=[DataRequired()])

    d15 = RequiredRadioField("d15", choices=[("d15.a", "Si"), ("d15.b", "No")], validators=[DataRequired()])

    d16 = RequiredRadioField("d16", choices=[("d16.a", "Si"), ("d16.b", "No")], validators=[DataRequired()])

    d17 = RequiredRadioField("d17", choices=[("d17.a", "Si e sono obbligatorie"),
                                             ("d17.b",
                                              "Si, ma sono solo raccomandate e la loro implementazione non è obbligatoriay"),
                                             ("d17.c", "No")],
                             validators=[DataRequired()])

    d18 = RequiredRadioField("d18", choices=[("d18.a", "Si"), ("d18.b", "No")], validators=[DataRequired()])

    d19 = RequiredRadioField("d19", choices=[("d19.a", "Si"), ("d19.b", "No")], validators=[DataRequired()])

    d20 = RequiredRadioField("d20", choices=[("d20.a", "Si"), ("d20.b", "No")], validators=[DataRequired()])

    d21 = RequiredRadioField("d21", choices=[("d21.a", "Si"), ("d21.b", "No")], validators=[DataRequired()])

    d22 = RequiredRadioField("d22", choices=[("d22.a", "Si"), ("d22.b", "No")], validators=[DataRequired()])

    d23 = RequiredRadioField("d23", choices=[("d23.a", "Si"), ("d23.b", "No")], validators=[DataRequired()])


class HardIndicatorsFormEng(FlaskForm):

    d1 = MultipleCheckboxField("d1", choices=[("d1.a", "The policy framework includes the principle of \"open data by default\""),
                                              ("d1.b", "There is a specific law or regulation on OD"),
                                              ("d1.c", "There is the Freedom of information Act"),
                                              ("d1.d", "There are national or international commitments on OD setting goals and targets to achieve")])

    d2_1 = RequiredRadioField("d2_1", choices=[("d2_1.a", "Yes and they are mandatory"),
                                       ("d2_1.b", "Yes, but they are only advisory and their implementation is not mandatory"),
                                       ("d2_1.c", "No")],
                      validators=[DataRequired()])
    d2_2 = RequiredRadioField("d2_2", choices=[("d2_2.a", "Yes, there are only limitations only for public security reasons, national security (military/state security) and public order"),
                                       ("d2_2.b", "Yes, but with limitations that go beyond the above answer"),
                                       ("d2_2.c", "No")],
                      validators=[DataRequired()])
    d2_3 = RequiredRadioField("d2_3", choices=[("d2_3.a", "Yes"), ("d2_3.b", "No")], validators=[DataRequired()])
    d2_4 = RequiredRadioField("d2_4", choices=[("d2_4.a", "Yes"), ("d2_4.b", "No")], validators=[DataRequired()])
    d2_5 = MultipleCheckboxField("d2_5", choices=[("d2_5.a", "Tender announcement"),
                                                  ("d2_5.b", "Steps of the tender procedure"),
                                                  ("d2_5.c", "Evaluation award"),
                                                  ("d2_5.d", "Contract award"),
                                                  ("d2_5.e", "Amendments of the contract")])
    d2_6 = RequiredRadioField("d2_6", choices=[("d2_6.a", "Yes"), ("d2_6.b", "No")], validators=[DataRequired()])
    d2_7 = RequiredRadioField("d2_7", choices=[("d2_7.a", "Yes"), ("d2_7.b", "No")], validators=[DataRequired()])
    d2_8 = RequiredRadioField("d2_8", choices=[("d2_8.a", "Yes"), ("d2_8.b", "No")], validators=[DataRequired()])

    d3_1 = RequiredRadioField("d3_1", choices=[("d3_1.a", "Yes"), ("d3_1.b", "No")], validators=[DataRequired()])
    d3_2 = RequiredRadioField("d3_2", choices=[("d3_2.a", "Yes"), ("d3_2.b", "No")], validators=[DataRequired()])

    d4 = RequiredRadioField("d4",  choices=[("d4.a", "Yes"), ("d4.b", "No")], validators=[DataRequired()])

    d5 = RequiredRadioField("d5", choices=[("d5.a", "Yes"), ("d5.b", "No")], validators=[DataRequired()])

    d6 = RequiredRadioField("d6", choices=[("d6.a", "Dedicated law on WB protection (WB protection is the solely purpose of the legislation)"),
                                   ("d6.b", "Complete WB protection through comprehensive laws or provisions in sectoral laws (i.e. Anticorruption)"),
                                   ("d6.c", "WB protection is scattered across different laws or provisions in sectoral laws (i.e. Anticorruption)"),
                                   ("d6.d", "None of the previous ones")],
                    validators=[DataRequired()])

    d7 = RadioField("d7", choices=[("d7.a", "Yes"), ("d7.b", "No")])

    d8 = RequiredRadioField("d8", choices=[("d8.a", "Only to the public sector"),
                                   ("d8.b", "Both the public and private sectors")],
                      validators=[DataRequired()])

    d9 = MultipleCheckboxField("d9", choices=[
                                     ("d9.a", "Only employees"),
                                     ("d9.b", "Contractors, subcontractors, suppliers, business partners"),
                                     ("d9.c", "Consultants, other self-employed person providing services"),
                                     ("d9.d", "Volunteers, trainees")])

    d10 = RadioField("d10", choices=[("d10.a", "any kinds of violations, malpractises and wrogdroings"),
                                     ("d10.b", "only certain kinds of violations (i.e financial fraud, tax evasion, etc)")])

    d11 = RequiredRadioField("d11", choices=[("d11.a", "Yes"), ("d11.b", "No")], validators=[DataRequired()])

    d12 = MultipleCheckboxField("d12", choices=[("d12.a", "internal reporting systems"),
                                                ("d12.b", "external disclosure to designated body/competent body"),
                                                ("d12.c", "external disclosure to the public/to the media")])

    d13 = RequiredRadioField("d13", choices=[("d13.a", "The reporting procedure is based on a tiered process"),
                                     ("d13.b", "The WB is free to choose the channel to make the disclosure to")],
                      validators=[DataRequired()])

    d14 = RequiredRadioField("d14", choices=[("d14.a", "Yes"),
                                     ("d14.b", "Yes, but it is allowed in some specific circumstances and only with the WB consent"),
                                     ("d14.c", "No")],
                      validators=[DataRequired()])

    d15 = RequiredRadioField("d15", choices=[("d15.a", "Yes"), ("d15.b", "No")], validators=[DataRequired()])

    d16 = RequiredRadioField("d16", choices=[("d16.a", "Yes"), ("d16.b", "No")], validators=[DataRequired()])

    d17 = RequiredRadioField("d17", choices=[("d17.a", "Yes and they are mandatory"),
                                     ("d17.b", "Yes, but they are only advisory and their implementation is not mandatory"),
                                     ("d17.c", "No")],
                      validators=[DataRequired()])

    d18 = RequiredRadioField("d18", choices=[("d18.a", "Yes"), ("d18.b", "No")], validators=[DataRequired()])

    d19 = RequiredRadioField("d19", choices=[("d19.a", "Yes"), ("d19.b", "No")], validators=[DataRequired()])

    d20 = RequiredRadioField("d20", choices=[("d20.a", "Yes"), ("d20.b", "No")], validators=[DataRequired()])

    d21 = RequiredRadioField("d21", choices=[("d21.a", "Yes"), ("d21.b", "No")], validators=[DataRequired()])

    d22 = RequiredRadioField("d22", choices=[("d22.a", "Yes"), ("d22.b", "No")], validators=[DataRequired()])

    d23 = RequiredRadioField("d23", choices=[("d23.a", "Yes"), ("d23.b", "No")], validators=[DataRequired()])



class SoftIndicatorsWBForm(FlaskForm):

    d1 = RequiredRadioField("d1", choices=[("d1.a", "Si"), ("d1.b", "No"), ("d1.c", "Non ancora")],
                            validators=[DataRequired()])

    d2 = MultipleCheckboxField("d2", choices=[("d2.a", "Mail dedicata"),
                                              ("d2.b", "Piattaforma IT"),
                                              ("d2.c", "Segnalazione scritta"),
                                              ("d2.d", "Segnalazione di persona"),
                                              ("d2.e", "Altro")],
                               validators=[DataRequired()])

    d2_1 = TextAreaField("d2_1")

    d3 = RadioField("d3", choices=[("d3.a", "Si"), ("d3.b", "No"), ("d3.c", "Non ancora")],
                    validators=[DataRequired()])

    d3_1 = RadioField("d3_1", choices=[("d3_1.a", "Si"), ("d3_1.b", "No")])

    d4 = MultipleCheckboxField("d4", choices=[("d4.a", "Si, una volta"),
                                              ("d4.b", "Si, periodicamente"),
                                              ("d4.c", "La comunicazione è fornita durante il processo di assunzione"),
                                              ("d4.d", "Le informazioni sono disponibili nell’intranet dell’amministrazione")],
                               validators=[DataRequired()])

    d5 = RadioField("d5", choices=[("d5.a", "Si"), ("d5.b", "No")], validators=[DataRequired()])

    d5_1 = RadioField("d5_1", choices=[("d5_1.a", "Si"), ("d5_1.b", "No")])

    d6 = RadioField("d6", choices=[("d6.a", "Si"), ("d6.b", "No")], validators=[DataRequired()])

    d6_1 = TextAreaField("d6_1")

    d6_2 = RadioField("d6_2", choices=[("d6_2.a", "Piu o meno lo stesso"),
                                       ("d6_2.b", "Aumentato"),
                                       ("d6_2.c", "Diminuito")])

    d6_3_1 = RadioField("d6_3_1", choices=[("d6_3_1.a", "Assente"),
                                           ("d6_3_1.b", "Scarsa"),
                                           ("d6_3_1.c", "Moderata"),
                                           ("d6_3_1.d", "Molta"),
                                           ("d6_3_1.e", "Moltissima")])

    d6_3_2 = RadioField("d6_3_2", choices=[("d6_3_2.a", "Assente"),
                                           ("d6_3_2.b", "Scarsa"),
                                           ("d6_3_2.c", "Moderata"),
                                           ("d6_3_2.d", "Molta"),
                                           ("d6_3_2.e", "Moltissima")])

    d6_3_3 = RadioField("d6_3_3", choices=[("d6_3_3.a", "Assente"),
                                           ("d6_3_3.b", "Scarsa"),
                                           ("d6_3_3.c", "Moderata"),
                                           ("d6_3_3.d", "Molta"),
                                           ("d6_3_3.e", "Moltissima")])

    d6_4_1 = RadioField("d6_4_1", choices=[("d6_4_1.a", "0%"),
                                           ("d6_4_1.b", "10%"),
                                           ("d6_4_1.c", "20%"),
                                           ("d6_4_1.d", "30%"),
                                           ("d6_4_1.e", "40%"),
                                           ("d6_4_1.f", "50%"),
                                           ("d6_4_1.g", "60%"),
                                           ("d6_4_1.h", "70%"),
                                           ("d6_4_1.i", "80%"),
                                           ("d6_4_1.l", "90%"),
                                           ("d6_4_1.m", "100%")])

    d6_4_2 = RadioField("d6_4_2", choices=[("d6_4_2.a", "0%"),
                                           ("d6_4_2.b", "10%"),
                                           ("d6_4_2.c", "20%"),
                                           ("d6_4_2.d", "30%"),
                                           ("d6_4_2.e", "40%"),
                                           ("d6_4_2.f", "50%"),
                                           ("d6_4_2.g", "60%"),
                                           ("d6_4_2.h", "70%"),
                                           ("d6_4_2.i", "80%"),
                                           ("d6_4_2.l", "90%"),
                                           ("d6_4_2.m", "100%")])

    d6_4_3 = RadioField("d6_4_3", choices=[("d6_4_3.a", "0%"),
                                           ("d6_4_3.b", "10%"),
                                           ("d6_4_3.c", "20%"),
                                           ("d6_4_3.d", "30%"),
                                           ("d6_4_3.e", "40%"),
                                           ("d6_4_3.f", "50%"),
                                           ("d6_4_3.g", "60%"),
                                           ("d6_4_3.h", "70%"),
                                           ("d6_4_3.i", "80%"),
                                           ("d6_4_3.l", "90%"),
                                           ("d6_4_3.m", "100%")])

    d6_4_4 = RadioField("d6_4_4", choices=[("d6_4_4.a", "0%"),
                                           ("d6_4_4.b", "10%"),
                                           ("d6_4_4.c", "20%"),
                                           ("d6_4_4.d", "30%"),
                                           ("d6_4_4.e", "40%"),
                                           ("d6_4_4.f", "50%"),
                                           ("d6_4_4.g", "60%"),
                                           ("d6_4_4.h", "70%"),
                                           ("d6_4_4.i", "80%"),
                                           ("d6_4_4.l", "90%"),
                                           ("d6_4_4.m", "100%")])

    d6_4_5 = TextAreaField("d6_4_5")

    d6_5 = TextAreaField("d6_5")

    d7 = RadioField("d7", choices=[("d7.a", "Si"), ("d7.b", "No")])

    d8 = MultipleCheckboxField("d8", choices=[("d8.a", "In un momento specifico del procedimento"),
                                              ("d8.b", "In ogni fase del procedimento"),
                                              ("d8.c", "Mai. Non è prevista alcuna comunicazione al whistleblower"),
                                              ("d8.d", "Mai perchè la segnalazione è anonima")])

    d8_1 = MultipleCheckboxField("d8_1", choices=[("d8_1.a", "Quando il responsabile o il referente della gestione delle segnalazioni riceve la segnalazione"),
                                                  ("d8_1.b", "Al termine della valutazione di ammissibilità del report (se non è ammissibile, la segnalazione è archiviata senza ulteriori azioni)"),
                                                  ("d8_1.c", "Al termine dell’istruttoria")])

    d9 = RadioField("d9", choices=[("d9.a", "Si, in ogni fase del procedimento"),
                                   ("d9.b", "Si, ma solo in alcune fasi"),
                                   ("d9.c", "Dipende dal canale di segnalazione adottato"),
                                   ("d9.d", "Dipende dal contenuto del report")])

    d10 = RadioField("d10", choices=[("d10.a", "Si"), ("d10.b", "No")])

    d10_1 = RadioField("d10_1", choices=[("d10_1.a", "Misure organizzative (ad esempio allocazione di nuove risorse, istituzione di nuove commissioni o sistemi di controllo)"),
                                         ("d10_1.b", "Misure o cambiamenti relativi alla comunicazione"),
                                         ("d10_1.c", "Procedure amministrative"),
                                         ("d10_1.d", "Altro")])

    d10_2 = TextAreaField("d10_2")

    d11 = RadioField("d11", choices=[("d11.a", "Si"), ("d11.b", "No")])

    d12 = RadioField("d12", choices=[("d12.a", "Si, su richiesta "),
                                     ("d12.b", "Si, periodicamente"),
                                     ("d12.c", "No")])

    d13 = RadioField("d13", choices=[("d13.a", "Dipendenti"),
                                     ("d13.b", "Altre categorie di lavoratori (ad esempio appaltatori, subappaltatori, fornitori, volontari, tirocinanti)")])

    d14 = RadioField("d14", choices=[("d14.a", "Si"), ("d14.b", "No")])

    d15 = RadioField("d15", choices=[("d15.a", "Si, sempre"),
                                     ("d15.b", "Su iniziativa della persona/ufficio responsabile del whistleblowing"),
                                     ("d15.c", "No")])

    d16 = MultipleCheckboxField("d16", choices=[("d16.a", "Assicurare e incoraggiare il contesto organizzativo per facilitare le segnalazioni"),
                                                ("d16.b", "Assicurare un atteggiamento positivo tra i collegi rispetto alla segnalazione (no stigmatizzazione) "),
                                                ("d16.c", "Aumentare la fiducia verso la persona o l’ufficio responsabile del whistleblowing (fiducia che la segnalazione sia presa in carico da qualcuno e che non sia inutile)"),
                                                ("d16.d", "Aumentare la consapevolezza dei benefici delle segnalazioni dei whistleblower (tutela dell’interesse pubblico, promozione della legalità)")])

    d16_1 = TextAreaField("d16_1")

    d17 = RadioField("d17", choices=[("d17.a", "Si"), ("d17.b", "No")])

    d18 = RadioField("d18", choices=[("d18.a", "Si"), ("d18.b", "No")])

    d18_1 = RadioField("d18", choices=[("d18_1.a", "Periodiche (su base regolare)"), ("d18_1.b", "Saltuarie")])

    d19 = RadioField("d19", choices=[("d19.a", "Estremamente insoddisfacente"),
                                     ("d19.b", "Moderatamente insoddisfacente"),
                                     ("d19.c", "Neutrale"),
                                     ("d19.d", "Moderatamente soddisfacente"),
                                     ("d19.d", "Estremamente soddisfacente")])

    d20 = TextAreaField("d20")
