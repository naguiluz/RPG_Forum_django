#!/bin/bash

curl "http://localhost:8000/worlds/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "world": {
      "name": "'"${NAME}"'",
      "active": "'"${ACTIVE}"'",
      "setting_type": "'"${TYPE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
