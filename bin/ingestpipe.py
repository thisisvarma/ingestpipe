import threading
import argparse
import configparser
import os
import pymssql
import logging

logFile = '../logs/ingestpipeline.log'
datDumpDir = '../dumpOld/'
dataLakeDir = '../dataNew/'

logging.basicConfig(filename=logFile,level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# parser = argparse.ArgumentParser(description="call help function here")
# parser.add_argument('-a', '--avalue', type=int, help='Enter a value', required= True)
# parser.add_argument('-b', '--bvalue', type=int, help='Enter b value', required= True)
# args = parser.parse_args()
# print(args.avalue)

query = "select @@version"


def db_connection(query):

    try:
        #logging.DEBUG("connecting to DataBase server")
        connection = pymssql.connect(host='localhost',
                                     user='sa',
                                     password='HelloWorld1@3'
                                     )
        logging.debug("connection is established with database")
        cursor = connection.cursor()
        cursor.execute(qudfdfery)
        logging.debug("returning fetch data")
        return cursor.fetchall()
    # except NameError as f:
    #     logging.error ("name error is raised : {} ".format(f))
    # except TypeError as e:
    #     logging.error("there is some problem with database connection, error is : {} ".format(e))
    except Exception as e:
        logging.error("there is some problem with database connection, error is : {} ".format(str(e)))


    # finally:
    #     connection.close()
    #     logging.debug("closing database connection")

logging.info("this is ingest application")

if __name__ == '__main__':

    try:

        logging.debug("trying to connect to DB server")
        data = db_connection(query)
        logging.debug("returned output value is {} ".format(data))

    except Exception as e:
        logging.error("Error is : {} ".format(e))











#files = os.listdir(datDumpDir)
# for i in files:
#     print("current file is : ", i)
