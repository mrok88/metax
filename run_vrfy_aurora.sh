export env=$1
export vrfyNo=$2
if [ $# -ne 2  ]; then
    echo ====================================================
    echo = USAGE : $0 dev vrfyNo # DEV ENV
    echo = USAGE : $0 tst vrfyNo # TST ENV 
    echo = USAGE : $0 prd vrfyNo # PRD ENV 
    echo ====================================================
else
    curl "http://127.0.0.1:80/dq/vrfy/tasks/?pk=$vrfyNo&env=$env"
fi
