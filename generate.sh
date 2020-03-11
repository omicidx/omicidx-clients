#!/bin/bash
for LANG in python go 
do
docker run --rm -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i https://api.omicidx.cancerdatasci.org/openapi.json \
  -g $LANG -o /local/$LANG
done

find . -name git_push.sh -exec rm {} \;

