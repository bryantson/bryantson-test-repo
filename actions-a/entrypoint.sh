#!/bin/bash

###############################################
# Simple bash script             
###############################################

#######
# VARS #
########
GITHUB_EVENT_PATH="${GITHUB_EVENT_PATH}"
GITHUB_REPOSITORY="${GITHUB_REPOSITORY}"
GITHUB_RUN_ID="${GITHUB_RUN_ID}"
GITHUB_SHA="${GITHUB_SHA}"
GITHUB_TOKEN="${GITHUB_TOKEN}"
GITHUB_WORKSPACE="${GITHUB_WORKSPACE}"
VAR="${VAR:-nothing}"

##########
# Run the script
#############
echo "-----------------------------------"
echo "Welcome to this container action!"
echo "-----------------------------------"
echo ""

echo "---------------------------------"
echo "Here is what is in the env"
printenv
echo "----------------------------------"

echo "You passed the Var:[${VAR}]"
