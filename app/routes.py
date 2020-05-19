from flask import render_template, flash, redirect, url_for, Blueprint, request
from flask_login import current_user, login_required
from datetime import datetime
from app.models import db, HardIndicatorsWB
from app.forms import SoftIndicatorsWBForm
from app.bokeh_plot import plot_scores

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/home')
@login_required
def home():

    data = HardIndicatorsWB.query.filter_by(user_id=current_user.get_id()).order_by(HardIndicatorsWB.created_at.desc())
    aggregated_data = []
    for d in data:
        aggregated_data.append(d.get_aggregated_data())
    script, div, js_resources, css_resources = plot_scores(aggregated_data)
    return render_template("table.html", title='home',
                           current_user=current_user,
                           values=aggregated_data,
                           plot_script=script,
                           plot_div=div,
                           js_resources=js_resources,
                           css_resources=css_resources)


@main_bp.route('/recap/hard')
@login_required
def recap():

    data = HardIndicatorsWB.query.filter_by(user_id=current_user.get_id()).order_by(HardIndicatorsWB.created_at.desc()).first()

    values = data.get_values()

    return render_template("recap_wb.html", current_user=current_user, values=values)


@login_required
@main_bp.route('/compile/soft/WB', methods=['GET', 'POST'])
def compile_soft():

    soft_wb_form = SoftIndicatorsWBForm()

    if request.method == 'POST':
        if soft_wb_form.validate_on_submit():

            # salvataggio dati
            # nel db

            pass

        else:
            flash(soft_wb_form.errors)

    return render_template("wb_soft.html", current_user=current_user, form=soft_wb_form)


@main_bp.route('/show/<id>', methods=['GET'])
@login_required
def show(id):

    data = HardIndicatorsWB.query.filter_by(id=id).first()

    values = data.get_values()

    return render_template("recap_wb.html", current_user=current_user, values=values)
