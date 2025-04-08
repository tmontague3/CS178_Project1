import pymysql
import pymysql.cursors
import creds
import boto3

# ----------------
# Section 1: MySQL (RDS) Connection Helpers
# ----------------

def get_conn():
    """
    Established and return a connection to the MySQL RDS database
    using credentials from creds.py
    Uses DictCursor to return query results as dictionaries.
    """