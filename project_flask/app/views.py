from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from . import app

from .models import *
from .forms import *



@app.route('/')
def index():
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        return render_template('index.html', user=user)
    flash("Пожалуйста, войдите в систему.", "warning")
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("Пользователь с таким именем уже существует. Выберите другое имя.", "danger")
            return render_template('register.html', form=form)

        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        flash("Регистрация прошла успешно! Вы вошли в систему.", "success")
        return redirect(url_for('index'))

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash("Вы успешно вошли!", "success")
            return redirect(url_for('index'))
        flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html', form=form)


@app.route('/entries')
def entries():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    entries = Entry.query.all()
    return render_template('entries.html', entries=entries)



@app.route('/add_entry', methods=['POST'])
def add_entry():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_input = request.form.get('user_input')
    user_id = session['user_id']

    if not user_input.strip():
        flash("Пожалуйста, введите текст для записи", "danger")
        return redirect(url_for('index'))

    new_entry = Entry(user_input=user_input.strip(), user_id=user_id)
    db.session.add(new_entry)
    db.session.commit()
    flash("Запись успешно добавлена!", "success")
    return redirect(url_for('index'))



@app.route('/delete_entry/<int:id>')
def delete_entry(id):
    entry = Entry.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
    return redirect(url_for('entries'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Вы вышли из системы.", "info")
    return redirect(url_for('login'))