from flask import Flask


app = Flask(__name__)
app.config.from_envvar('SETTING_FILE')
# print(app.config)
