cd /home/websson/ && wget https://xxxxxx.fineupp.com/extraport/hello_world_flask.zip
cd /home/websson/ && unzip hello_world_flask.zip
cd /home/websson/ && rm hello_world_flask.zip
cd /home/websson/hello_world_flask && . /home/websson/default_py_env/bin/activate && pip install -r requirements.py
cd /home/websson/hello_world_flask && . /home/websson/default_py_env/bin/activate &&  python hello_flask.py &
