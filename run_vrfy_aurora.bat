@echo off
set env=%1
set vrfyNo=%2
if "%env%" == "" (
    echo ====================================================
    echo = USAGE : %0 dev vrfyNo # 개발환경수행  
    echo = USAGE : %0 tst vrfyNo # 테스트환경수행 
    echo = USAGE : %0 prd vrfyNo # 운영환경수행 
    echo ====================================================

) else (
@echo on
    curl "http://10.131.81.103:8001/dq/vrfy/tasks/?pk=%vrfyNo%&env=%env%"
)
