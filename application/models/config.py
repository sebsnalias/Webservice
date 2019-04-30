import web

db_host = 'mcldisu5ppkm29wf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'yvwwbqydnteaaje3'
db_user = 'x3r68ieoiirpqzgy'
db_pw = 'v2k7c1vohzn54rji'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )