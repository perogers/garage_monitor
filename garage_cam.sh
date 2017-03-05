#!/bin/bash

APP_NAME="garage3.py"
APP=~pi/flask/$APP_NAME
LOG="/var/log/webapps/web.log"

active=`ps -ef |grep ${APP_NAME} |grep -v grep`

#echo "active: \"${active}\""

if [[ -z "${active// }" ]] 
	then
	START=`date`	
	#sudo su echo "${START} - Not active starting\n" >>$LOG
	sudo su -c "nohup python ${APP}  1>${LOG} 2>&1 &" -s /bin/sh webuser
fi
