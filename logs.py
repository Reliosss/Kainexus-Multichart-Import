from datetime import datetime, timedelta

import os
import configuration
import shutil


def save_log(description):
    path = 'C:\\Service\\KainexusImport\\Logs\\'
    
    try:
        ## Get current datetime
        date = datetime.now()

        ## Retrieve year, month, day
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        ## Create subfolders for logs
        logs_path = path + year + '\\' + month
        check_path = os.path.exists(logs_path)

        if not check_path:
            os.makedirs(logs_path)

        ## Save record logs to the file and print to terminal
        file_path = logs_path + '\\logs_' + day + '.txt'
        file = open(file_path, 'a')
        
        date_string = date.strftime("%d/%m/%Y %H:%M:%S")
        logs_string = "[" + date_string + "] " + description + "\n"

        file.write(logs_string)
        print(logs_string)

        ## Create remove date
        remove_date = date - timedelta(int(configuration.get_conf("CONFIGURATION", "logsTime")))

        ## Delete old days from logs
        days_path = logs_path
        days = os.listdir(logs_path)

        for day in days:
            remove_path = days_path + '\\' + day
            modified_date = datetime.fromtimestamp(os.path.getmtime(remove_path))
            modified_date.strftime("%d/%m/%Y %H:%M:%S")

            if modified_date < remove_date:
                os.remove(remove_path)
        
        ## Delete old months from logs
        months_path = path + year
        months = os.listdir(months_path)

        for month in months:
            remove_path = months_path + '\\' + month
            modified_date = datetime.fromtimestamp(os.path.getmtime(remove_path))
            modified_date.strftime("%d/%m/%Y %H:%M:%S")

            if modified_date < remove_date:
                shutil.rmtree(remove_path)

        ## Delte old years from logs
        years_path = path
        years = os.listdir(years_path)

        for year in years:
            remove_path = years_path + '\\' + year
            modified_date = datetime.fromtimestamp(os.path.getmtime(remove_path))
            modified_date.strftime("%d/%m/%Y %H:%M:%S")

            if modified_date < remove_date:
                shutil.rmtree(remove_path)

    except Exception as e:
        print("[ERROR] Something wrong with logs funcionality: " + str(e))