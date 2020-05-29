#!/bin/bash



if [ "${ENABLE_HTTPS}" == "True" ]; then
  if test -e /certs/cert.pem && test -f /certs/key.pem ; then
    exec gunicorn --bind 0.0.0.0:5001 -w "$WORKERS" --certfile /certs/cert.pem --keyfile /certs/key.pem --timeout "$TIMEOUT"  cookiecutterform:app
  else
    echo "[ERROR] File /certs/cert.pem or /certs/key.pem NOT FOUND!"
    exit 1
  fi
else
  exec gunicorn --bind 0.0.0.0:5001 -w "$WORKERS" --timeout "$TIMEOUT"  cookiecutterform:app
fi
