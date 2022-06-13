from os import listdir, remove
from os.path import isfile, join
from logs import save_log
from configuration import get_conf
from datetime import datetime

import shutil
import requests


def import_chart():
    sourcePath = get_conf("CONFIGURATION", "sourcePath")
    destinationPath = get_conf("CONFIGURATION", "destinationPath")

    date = datetime.now()
    formateDate = date.strftime("%d-%m-%Y_%H-%M-%S")

    save_log("@@Start import files@@")

    try:
        files = [f for f in listdir(sourcePath) if isfile(join(sourcePath, f))]
        for file in files:
            excelPath = sourcePath + "\\" + file
            data = open(excelPath, 'rb')
            url = get_conf("CONFIGURATION", "url")
            files = {'file': (excelPath, data, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
            r = requests.post(
                url,
                auth=(
                    get_conf("CONFIGURATION", "user"), 
                    get_conf("CONFIGURATION", "key")),
                files=files,
                verify=False
            )
            data.close()
            save_log("[INFO] File was imported: " + excelPath)
    except Exception as e:
        save_log("[ERROR] Something wrong with import excel to api: " + str(e)  + excelPath)

    try:
        files = [f for f in listdir(sourcePath) if isfile(join(sourcePath, f))]
        for file in files:
            excelPath = sourcePath + "\\" + file

            try:
                shutil.copyfile(
                    excelPath,
                    destinationPath + "\\" +
                    formateDate + "_" +
                    file
                )
                remove(excelPath)
                save_log("[INFO] File has been transfered: " + excelPath)
            except shutil.SameFileError as e:
                save_log(
                    "[ERROR] Source and destination represents the same file." + str(e)  + excelPath)
            except IsADirectoryError as e:
                save_log("[ERROR] Destination is a directory." + str(e)  + excelPath)
            except PermissionError as e:
                save_log("[ERROR] Permission denied." + str(e)  + excelPath)
            except Exception as e:
                save_log(
                    "[ERROR] Error occurred while copying file." + str(e)  + excelPath)
    except Exception as e:
        save_log(
            "[ERROR] Something wrong with source or destination path: " + str(e)  + excelPath)

    save_log("@@End import files@@")
