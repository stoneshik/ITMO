#!/bin/bash
MAX_DAYS=$1
CURRENT_DATE=$(date "+%Y-$m-%d-%H:%M:%S")
find $HOME/first/backups -type d -mtime +$1 -delete
echo "$(date): backups older than $MAX_DAYS days were successfully deleted in main node"
find $HOME/first/wal -type d -mtime +$1 -delete
echo "$(date): wal files older than $MAX_DAYS days were successfully deleted in main node"

