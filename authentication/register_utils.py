import mysql.connector as sql
import pandas as pd
from IPython.display import display, HTML
current_connection = None
current_cursor = None

def setup_current_connection(dbname=None):
    global current_connection
    if current_connection:
        current_connection.close()
        current_connection = None
    if dbname:
        current_connection = sql.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database = dbname
        )
    else:
        current_connection = sql.connect(
            host="localhost",
            user="root",
            passwd="mysql",
        )

def setup_cursor(dbname):
    global current_cursor
    if (not current_connection) or current_connection.database != dbname:
        setup_current_connection(dbname)
        current_cursor = current_connection.cursor()
    
def setup_db(dbname):
    setup_cursor(dbname)

def execute_and_print_dml(dml,dbname=None):
    if (not current_connection) or (not current_cursor) or current_connection.database != dbname:
        setup_db(dbname)
    current_cursor.execute(dml)
    for x in current_cursor:
        print(x)
    current_connection.commit()

def execute_and_print_dml_as_df (dml, dbname=None):
    if (not current_connection) or current_connection.database != dbname:
        setup_current_connection(dbname)
    df = pd.read_sql(dml, con = current_connection)
    display(df)
    current_connection.commit()
#user table
def register(uname, password1, password2,email,gender,location,phno,dob, fname, lname  ):
	#if password1 != password2:
	#	return error
	#q = "select * from user_table where user_name ='" + uname + "';"
	#df = pd.read_sql(dml, con = current_connection)
	#if len(df):
	#	return error
	query = "insert into user_table values('"+uname+"','"+password1+ "','"+email+"','"+gender+"','"
			+location+"','"+fname+"','"+lname+"','"+dob+"',"+phno+");"     
	execute_and_print_dml(query, "election_prediction")


def login(uname, password):
	query = "select * from user_table where uname = '"+uname+"';"
	df = pd.read_sql(dml, con = current_connection)
	#if !len(df):
	#	return error#no such uname
	if list(df['password'])[0] == password:
		#autheticated, log the user in

