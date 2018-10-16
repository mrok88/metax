export env=$1
if [ $# -ne 1  ]; then
    echo ====================================================
    echo = USAGE : $0 dev # DEV ENV
    echo = USAGE : $0 tst # TST ENV 
    echo = USAGE : $0 prd # PRD ENV 
    echo ====================================================
else
   curl -d env=$env http://127.0.0.1:80/dq/vrfy/tasks_aurora/ 
fi
