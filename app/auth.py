from flask import render_template, flash, redirect, url_for, Blueprint, request
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, SignupForm, ProfileForm, HardIndicatorsWBForm, InformativeForm
from app.business_logic import compute_scores_wb
from app.models import db, User, HardIndicatorsWB
from app import login_manager
from datetime import datetime
import sys


auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():

    if current_user.is_authenticated:

        existing_user = User.query.filter_by(id=current_user.get_id()).first()

        if not existing_user.is_inf_accepted():
            return redirect(url_for("auth_bp.informativa"))
        if not existing_user.is_userinfo_compiled():
            return redirect(url_for("auth_bp.userinfo"))
        if not existing_user.is_hard_indicators_compiled():
            return redirect(url_for("auth_bp.hard_indicators"))

        return redirect(url_for('main_bp.home'))

    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            country = request.form.get('country')
            if country == "None":
                flash("Error in selecting the counrty")
                return render_template("sign_up.html", title='signup', form=signup_form)
            existing_user = User.query.filter_by(username=username).first()
            if existing_user is None:
                user = User(username=username, country=country, created_on=datetime.today())
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('moving to main page')
                return redirect(url_for('auth_bp.informativa'))
            flash("A user already exists with that username")
            return redirect(url_for('auth_bp.login'))

    return render_template("sign_up.html", title='signup', form=signup_form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:

        existing_user = User.query.filter_by(id=current_user.get_id()).first()

        if not existing_user.is_inf_accepted():
            return redirect(url_for("auth_bp.informativa"))
        if not existing_user.is_userinfo_compiled():
            return redirect(url_for("auth_bp.userinfo"))
        if not existing_user.is_hard_indicators_compiled():
            return redirect(url_for("auth_bp.hard_indicators"))

        return redirect(url_for('main_bp.home'))

    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            existing_user = User.query.filter_by(username=username).first()
            if existing_user and existing_user.check_password(password):

                login_user(existing_user)

                if not existing_user.is_inf_accepted():
                    return redirect(url_for("auth_bp.informativa"))
                if not existing_user.is_userinfo_compiled():
                    return redirect(url_for("auth_bp.userinfo"))
                if not existing_user.is_hard_indicators_compiled():
                    return redirect(url_for("auth_bp.hard_indicators"))

                return redirect(url_for('main_bp.home'))

            flash('Invalid username/password combination')
            return redirect(url_for('auth_bp.login'))

    return render_template("login.html", title='main', form=login_form)


@login_required
@auth_bp.route('/info', methods=["GET", "POST"])
def informativa():

    inf_form = InformativeForm()
    if request.method == "POST":
        if inf_form.validate_on_submit():
            clickedButton = request.form.get('accept')
            if clickedButton == "Accetta":
                user = User.query.filter_by(id=current_user.get_id()).first()
                user.set_inf_accepted()
                db.session.commit()
                return redirect(url_for("auth_bp.userinfo"))
            else:
                return redirect(url_for("auth_bp.logout"))

    return render_template("informativa.html", title='informativa', form=inf_form)


@login_required
@auth_bp.route('/userinfo', methods=['GET', 'POST'])
def userinfo():

    profile_form = ProfileForm()

    if request.method == "POST":
        if profile_form.validate_on_submit():
            gender = request.form.get("gender")
            institution = request.form.get("institution")
            type = request.form.get("type")
            size = request.form.get("size")
            role = request.form.get("role")
            existing_user = User.query.filter_by(id=current_user.get_id()).first()
            existing_user.set_personal_info(gender, institution, type, size,role)
            db.session.commit()
            return redirect(url_for('auth_bp.hard_indicators'))

    return render_template("user_info.html", form=profile_form)


@auth_bp.route('/compile/hard/WB', methods=['GET', 'POST'])
@login_required
def hard_indicators():

    indicator_form = HardIndicatorsWBForm()

    if request.method == 'POST':
        if indicator_form.validate_on_submit():
            d = compute_scores_wb(current_user.get_id(), datetime.today(), request.form)
            wb = HardIndicatorsWB(**d)
            db.session.add(wb)
            user = User.query.filter_by(id=current_user.get_id()).first()
            user.set_hard_indicators_compiled()
            db.session.commit()
            return redirect(url_for("main_bp.recap"))
        else:
            flash(indicator_form.errors)

    return render_template("wb_hard.html", title='indicators', current_user=current_user, form=indicator_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
