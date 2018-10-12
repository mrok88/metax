###########################################################################
#     Meta-eXpress 2.1 
#     All right reserved by wonseokyou 
#     email : wonseokyou@gmail.com 
###########################################################################
import os
import sys
import pymysql
from functools import reduce
from metax import conn_info
from metax.dbMysql import Ssh,Conn,get_db_sch_nm
##############################
def get_qry( db , sql, sql_params = {} ):
    '''query와 파라미터를 전달해서 sql수행하는 함수'''
    conn = None   
    try:
        if ( db in ( 'ltcm','ltcmst','ltcmat', 'ltcmpr')):
            conn = Conn('ltcm')
        else :
            conn = Conn('elltdev')
        conn.ssh.start()
        conn.sshDbConn()            
        conn.param_replace = False
        conn.curType = 'dict'
        return conn.execute(sql,sql_params)
    finally:
        conn.close()
    return None

##############################
# GET_TBL
# 테이블 데이터타입, NULL여부, DEFAULT값 가져오기 
##############################
def get_tbl(p_tbl_nm = "GD"):
    sql = """select table_schema `SCHEMA`
, upper(table_name)  TBL_NM
, upper(column_name) COL_NM
, ordinal_position POS
, COLUMN_TYPE DT
, IS_NULLABLE NULLABLE
, COLUMN_DEFAULT DEFT
from information_schema.columns a
where table_schema in ( 'x' 
,'elltdpdev'
,'elltomdev','elltpydev','elltlodev'
,'elltgddev'
,'elltchdev'
,'elltetdev'
,'elltprdev'
,'ellttmsdev'
,'elltsedev'
,'elltcmdev'
,'ltcmatdev'
,'ltcmstdev'
,'elltscdev'
,'elltccdev'
,'elltmbdev'
,'ltcmprdev'
)
  and table_schema like concat(lower(%(tbl_nm)s),'%%')
#  AND table_name like concat(lower(%(tbl_nm)s),'%%')
  and table_schema not like '%%back'
"""
    rows = get_qry(p_tbl_nm,sql,{'tbl_nm' : p_tbl_nm })
    return rows

##############################
def get_tbl_src(p_tbl_nm = "GD"):
    '''원본테이블 데이터타입, NULL여부, DEFAULT값 가져오기'''
    sql = """select table_schema `SCHEMA`
, upper(table_name)  TBL_NM
, upper(column_name) COL_NM
, ordinal_position POS
, COLUMN_TYPE DT
, IS_NULLABLE NULLABLE
, COLUMN_DEFAULT DEFT
from information_schema.columns a
where table_schema in ( 'x' 
,'elltdpdev'
,'elltomdev','elltpydev','elltlodev'
,'elltgddev'
,'elltchdev'
,'elltetdev'
,'elltprdev'
,'ellttmsdev'
,'elltacdev'
,'elltcmdev'
,'ltcmatdev'
,'ltcmstdev'
,'elltscdev'
,'elltccdev'
,'elltmbdev'
,'ltcmprdev'
)
  and table_schema like concat(lower(%(tbl_nm)s),'%%')
  AND table_name not like '%%out'
  and table_schema not like '%%back'
"""
    rows = get_qry(p_tbl_nm,sql,{'tbl_nm' : p_tbl_nm })
    return rows
##############################
def get_tbl_out(p_tbl_nm = "GD"):
    '''복제본테이블(OUT) 데이터타입, NULL여부, DEFAULT값 가져오기''' 
    return get_qry(p_tbl_nm,"""select table_schema `SCHEMA`
, replace(upper(table_name),'_OUT','')  TBL_NM
, upper(column_name) COL_NM
, ordinal_position POS
, COLUMN_TYPE DT
, IS_NULLABLE NULLABLE
, COLUMN_DEFAULT DEFT
from information_schema.columns a
where table_schema in ( 'x' 
,'elltdpdev'
,'elltomdev','elltpydev','elltlodev'
,'elltgddev'
,'elltchdev'
,'elltetdev'
,'elltprdev'
,'ellttmsdev'
,'elltacdev'
,'elltcmdev'
,'ltcmatdev'
,'ltcmstdev'
,'elltscdev'
,'elltccdev'
,'elltmbdev'
,'ltcmprdev'
)
  and table_schema not like concat(lower(%(tbl_nm)s),'%%')
  AND table_name like '%%out'
  and table_schema not like '%%back'
""",{'tbl_nm' : p_tbl_nm})

##############################
# GET_CD_LIST
# 코드 목록
##############################
def get_cd_list(p_col_nm = "EVNT_TKPT_STAT_CD"):
    return get_qry('ltcm',"""select 
A.CD,A.CD_NM 
from ltcmstdev.st_csco_cd a
where group_cd like upper(%(col_nm)s) AND csco_id = 'ELLOTTE'
ORDER BY SORT_RNKG""",{'col_nm': p_col_nm})   

##############################
# TEST START 
##############################
if __name__ == "__main__":
    sa = "CC"
    for arg in sys.argv[1:]:
        sa = arg
    print(sa)
    out_list = get_cd_list()
    for out in out_list:
        print(out)
