#!/bin/bash

curl "http://localhost:8000/worlds/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
