@echo off
set env=%1
set vrfyNo=%2
if "%env%" == "" (
    echo ====================================================
    echo = USAGE : %0 dev vrfyNo # ����ȯ�����  
    echo = USAGE : %0 tst vrfyNo # �׽�Ʈȯ����� 
    echo = USAGE : %0 prd vrfyNo # �ȯ����� 
    echo ====================================================

) else (
@echo on
    curl "http://10.131.81.103:8001/dq/vrfy/tasks/?pk=%vrfyNo%&env=%env%"
)
