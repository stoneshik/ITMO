#!/bin/bash
MAX_DAYS=$1
CURRENT_DATE=$(date "+%Y-$m-%d-%H:%M:%S")
find $HOME/second/backups -type d -mtime +$1 -delete
echo "$(date): backups older than $MAX_DAYS days were successfully deleted in second node"
find $HOME/second/wal -type d -mtime +$1 -delete
echo "$(date): wal files older than $MAX_DAYS days were successfully deleted in second node"

