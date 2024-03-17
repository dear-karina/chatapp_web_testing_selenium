#!/bin/bash

case "$1" in
    "run")
        # run the tests
        echo "TestMachine2 is starting the tests...."
        cd /home/ubuntu/repo/ChatApp_Web_Testing
        source .venv/bin/activate
        python3 main.py
        python3 reports/flask_run.py
        ;;
    "update")
        # update the automation code
        echo "TestMachine2 is updating the tests...."
        cd /home/ubuntu/repo/ChatApp_Web_Testing
        git pull
        source .venv/bin/activate
        .venv/bin/pip3 install -r requirements.txt
        deactivate
        echo "TestMachine2 finished updating"
        ;;
    "connect")
        # test ssh connection
        echo "TestMachine2 connecting..."
        ;;
    *)
        echo "Unknown command: $1"
        ;;
esac
