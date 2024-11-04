cd /home/websson/ && git clone https://github.com/KellerKev/flask-htmx-todolist-snowflake.git
echo "snowflake-sqlalchemy" >> /home/websson/flask-htmx-todolist-snowflake/requirements.txt
echo "flask" >> /home/websson/flask-htmx-todolist-snowflake/requirements.txt
cd /home/websson/flask-htmx-todolist-snowflake && . /home/websson/default_py_env/bin/activate && pip install -r requirements.txt
#cd /home/websson/flask-htmx-todolist-snowflake && sed -i 's|sqlite:///app_data.db|snowflake://'"${SNOWUSER}"':'"${SNOWPASS}"'@'"${SNOWACCOUNT}"'/'"${SNOWDB}"'/'"${SNOWSCHEMA}"'?warehouse='"${SNOWWH}"'\&role='"${SNOWROLE}"'|g' todo_app/__init__.py
#cd /home/websson/flask-htmx-todolist-snowflake && sed -i 's|sqlite:///app_data.db||g' todo_app/__init__.py
cd /home/websson/flask-htmx-todolist-snowflake && sed -i "s|app.run()|app.run(host='0.0.0.0', port=5000)|g" run.py
cd /home/websson/flask-htmx-todolist-snowflake && . /home/websson/default_py_env/bin/activate &&  python run.py
