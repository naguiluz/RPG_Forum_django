#!/bin/bash

curl "http://localhost:8000/worlds/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "world": {
      "name": "'"${NAME}"'",
      "setting": "'"${TYPE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
