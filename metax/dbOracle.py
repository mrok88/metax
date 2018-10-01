"""
====================================
 :mod: Oracle 관련  모듈 
====================================
.. moduleauthor:: 유원석 <wsyou@wizbase.co.kr>

설명
=====

Oracle 접속하고 수행할 수 있도록함.

참고
====

관련 링크:
 * 

관련 작업자
===========

 * 유원석 (Wonseok You)

작업일지
--------

 * 2018-09-06 wsyou : 초기함수 정의
 """
import os
import sys
import cx_Oracle
from . import conn_info
##############################
class Conn():
    """
    Oracle Connection관리 
    pymysql 모듈을 사용하여 mysql 커넥션을 관리함.
    예제 :

        conn = Conn(p_db_nm)
        conn.DbConn()
        conn.param_replace = False  # SQL STRING % 관련해서 무시함. 
        conn.curType = 'list'       # 'list', 'dict' 중에 sql resultset을 list형태로 return함 
        ...   
        sql2 = "SELECT ..." 
        rows2 = conn.execute(sql2,{'tbl_nm' : tbl_nm , 'cpy_nm' : cpy_nm })
        ...
        conn.close()
    """    
    def __init__(self,db='da05'):
        self.db = db
        self.server_info = conn_info.server_infos[db]
        server_info = self.server_info
        self.dsn = cx_Oracle.makedsn(server_info['source_endpoint'], server_info['source_endpoint_port'], server_info['source_endpoint_sid'])
        os.putenv('NLS_LANG', '.UTF8')       
        self.conn = None
        self.curType = 'dict'
        self.param_replace = True
        self.cols = None


    def dbConn(self):
        """ssh 터널링 없이 일반적인 db접속을 수행함.
        :returns: 정상 수행시 True
        """        
        server_info = self.server_info
        try:
            self.conn = cx_Oracle.connect(server_info['source_db_user'], server_info['source_db_pwd'], self.dsn)
            return True
        except Exception as e:
            return None

    def execute(self,sql,sql_params ={}):
        """sql을 수행하고 resultset을 list or dict형태로 return함 
        :returns: 정상수행시 resultset, 오류시 None
        """
        curs = None
        try:
            curs = self.conn.cursor()
            curs.execute(sql,sql_params)
            if (self.curType == 'dict'):
                recs = curs.fetchall()
                rows = []
                for rec in recs:
                    row = dict(zip([d[0] for d in curs.description], rec))
                    rows.append(row)                          
            else:
                rows = curs.fetchall()
            #컬럼목록 설정 
            self.cols = None
            try: 
                self.cols = [i[0] for i in curs.description]
            except Exception as e :
                pass
            return rows
        except Exception as e:
            print(e)         
        # finally:
        #     curs.close()
        return None

    def select_db(self,schema):
        """Oracle에서 database를 선택함.
        """
        return self.conn.execute("alter session set current_schema = '%s' " % schema )

    def commit(self):
        """commit명령을 수행함.
        """
        self.conn.commit()

    def close(self):
        """DB Connection을 끊고 해당 자원을 해제함.
        """
        if self.conn is not None:
            self.conn.close()

##############################
# GET_QRY
# 쿼리와 파라미터를 받아서 Dict 형태로 return한다 
# 없을 경우 None을 return한다 
##############################
def get_qry(sql,sql_params = {} ):
    server_info = conn_info.server_infos['da05']  
    dsn = cx_Oracle.makedsn(server_info['source_endpoint'], server_info['source_endpoint_port'], server_info['source_endpoint_sid'])
    os.putenv('NLS_LANG', '.UTF8')
    conn = None    
    try:
        conn = cx_Oracle.connect(server_info['source_db_user'], server_info['source_db_pwd'], dsn)
        try:
            curs = conn.cursor()
            curs.execute(sql,sql_params)
            recs = curs.fetchall()
            rows = []
            for rec in recs:
                row = dict(zip([d[0] for d in curs.description], rec))
                rows.append(row)            
            return rows
        finally:
            curs.close()
    finally:
        if conn is not None:
            conn.close()
    return None