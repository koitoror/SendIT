""""Application Product Point."""

import os
import unittest


# third-party imports
from flask_script import Manager # controller class for handling commands

# local imports
from instance import create_app
from app.api.v1 import api_v1 as v1
from app.api.v2 import api_v2 as v2

# application development instance
# app = create_app(config_name=os.getenv("FLASK_CONFIG"))
app = create_app(config_name=os.getenv("FLASK_CONFIG"))


# registering the blueprint
app.register_blueprint(v1)
app.register_blueprint(v2)

# initializing the manager object
manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)

@manager.command
def test():
    test = unittest.TestLoader().discover("./app/tests", pattern="test*.py")
    unittest.TextTestRunner(verbosity=2).run(test)


if __name__ == "__main__":
    manager.run()
