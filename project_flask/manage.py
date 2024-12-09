import os
from app import app, db
from app.models import User, Entry
import click


@app.cli.command("create_tables")
def create_tables():
    db.create_all()
    click.echo("Все таблицы созданы.")


@app.cli.command("drop_tables")
def drop_tables():
    db.drop_all()
    click.echo("Все таблицы удалены.")


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Entry=Entry)


if __name__ == '__main__':
    app.run(debug=True)