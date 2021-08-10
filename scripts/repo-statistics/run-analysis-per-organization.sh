#!/bin/bash

# 
# Script to run analysis per organization
# @author Bryant Son
# @since 08/10/2021
#

while read org;
  do
    ./repo-statistics.sh -u https://$GHES_HOST -t $GHES_TOKEN $org
  fi;
done < ./organizations.txt
