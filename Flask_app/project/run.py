from app import create_app
from flask_migrate import Migrate, MigrateCommand, upgrade
#from flask_script import Manager

app = create_app()
#manager = Manager(app)
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)


#@manager.command


if __name__ =='__main__':
    app.run(debug=True)