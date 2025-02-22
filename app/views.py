# app/views.py

from flask import Blueprint, request, redirect, render_template
from .forms import URLForm
from .models import URL
from . import db, cache
import shortuuid


main_blueprint = Blueprint('main', __name__)

def generate_tiny_url():
    return shortuuid.ShortUUID().random(length=6)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            original_url = form.url.data
            tiny_url = generate_tiny_url()
        
            while URL.query.filter_by(tiny_url=tiny_url).first() is not None:
                tiny_url = generate_tiny_url()

            new_url = URL(original_url=original_url, tiny_url=tiny_url)
            db.session.add(new_url)
            db.session.commit()

            return render_template('index.html', form=form, tiny_url=tiny_url)
        else:
            return render_template('index.html', form=form)


    return render_template('index.html', form=form)

@main_blueprint.route('/<tiny_url>')
@cache.cached(timeout=300)
def redirect_to_original_url(tiny_url):
    url = URL.query.filter_by(tiny_url=tiny_url).first_or_404()
    return redirect(url.original_url)
