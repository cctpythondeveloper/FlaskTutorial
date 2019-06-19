#!/bin/bash

cd frontend
npm run build
cd ..
FLASK_APP=run.py FLASK_DEBUG=1 flask run
