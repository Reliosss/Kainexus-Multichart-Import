from importFile import import_chart
from configuration import get_conf
import schedule
import time

schedule.every(int(get_conf("CONFIGURATION", "interval"))).minutes.do(import_chart)

import_chart()
while True:
    time.sleep(1)
    schedule.run_pending()
