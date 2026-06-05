#!/bin/bash
CURRENT_DATE=$(date "+%Y-$m-%d-%H:%M:%S")
BACKUP_DIR="backup_${CURRENT_DATE}"
# создание бэкапа
pg_basebackup -h 127.0.0.1 -p 9200 -U postgres -D $HOME/first/backups/$BACKUP_DIR -Xf -w -T $HOME/first/mto69=$HOME/first/backups/$BACKUP_DIR/mto69
# копирование бекапа с основного узла на резервный
cp -a $HOME/first/backups/$BACKUP_DIR $HOME/second/backups/$BACKUP_DIR
# удаление старых бэкапов на основном узле
bash $HOME/first/remove_first.sh 7
# удаление старых бэкапов на резервном узле
bash $HOME/second/remove_second.sh 28
echo "$(date): Backup $BACKUP_DIR was successfully created"

