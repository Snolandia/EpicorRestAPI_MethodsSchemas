import asyncio
import aiohttp
# from . import configEpicorSchemas
import PythonEpicorRestAPI.Erp_BO_JobEntrySvc


import json
import os
import base64
import asyncio
import aiohttp
import pprint
import urllib.parse
import datetime




async def main():
      obj = await PythonEpicorRestAPI.Erp_BO_JobEntrySvc.get_JobEntries()
      for key,value in obj.items():
            print(key)
            print(type(value))
      
      pprint.pprint(obj["value"][0])
      for each in obj["value"]:
            # print(type(each))
            a = PythonEpicorRestAPI.Erp_BO_JobEntrySvc.Erp_Tablesets_JobHeadRow(each)
                  
      

    
start = datetime.datetime.now()
print("StartTime : ", start)

asyncio.run(main())

end = datetime.datetime.now()
timediff = end-start

print("timetake = ",(timediff))