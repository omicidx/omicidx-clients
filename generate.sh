#!/bin/bash
for LANG in python go 
do
rm -rf $LANG-client
docker run --rm -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i https://api.omicidx.cancerdatasci.org/openapi.json \
  --remove-operation-id-prefix \
  --package-name omicidx_client \
  -g $LANG -o /local/$LANG-client
done

find . -name git_push.sh -exec rm {} \;

