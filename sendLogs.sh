#!/bin/bash
search_dir=/root/adminbyrequest/Logs/
for entry in "$search_dir"*
do
  echo "$entry";
  /opt/qradar/bin/logrun.pl -u adminbyrequest -f $entry  10; rm -rf $entry
done
