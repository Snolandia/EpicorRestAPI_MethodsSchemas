import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.RunTaskSvc
# Description: Runs a task or sub-task.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_RunSubTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunSubTask
   Description: Runs the sub-task.
   OperationID: RunSubTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunSubTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunSubTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunSystemTasks(epicorHeaders = None):
   """  
   Summary: Invoke method RunSystemTasks
   Description: Runs the system Tasks.
   OperationID: RunSystemTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunSystemTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_RunQueueTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunQueueTask
   Description: Runs the queue task.
   OperationID: RunQueueTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunQueueTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunQueueTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunTask
   Description: Runs the task, should be used by the Task Agent to run tasks..
   OperationID: RunTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunTaskDirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunTaskDirect
   Description: Use to run a task directly.
   OperationID: RunTaskDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunTaskDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunTaskDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.RunTaskSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Epicor_Hosting_TaskCaller_SubTaskParameter:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.DataType:int = obj["DataType"]
      self.StringValue:str = obj["StringValue"]
      self.BooleanValue:bool = obj["BooleanValue"]
      self.DateValue:str = obj["DateValue"]
      self.DecimalValue:int = obj["DecimalValue"]
      self.IntegerValue:int = obj["IntegerValue"]
      self.LongValue:int = obj["LongValue"]
      pass

class RunQueueTask_input:
   """ Required : 
   message
   """  
   def __init__(self, obj):
      self.message:str = obj["message"]
      """  The message.  """  
      pass

class RunQueueTask_output:
   def __init__(self, obj):
      pass

class RunSubTask_input:
   """ Required : 
   subTaskAssemblyName
   taskParameters
   """  
   def __init__(self, obj):
      self.subTaskAssemblyName:str = obj["subTaskAssemblyName"]
      """  Name of the sub-task assembly.  """  
      self.taskParameters:list[Epicor_Hosting_TaskCaller_SubTaskParameter] = obj["taskParameters"]
      """  The task parameters.  """  
      pass

class RunSubTask_output:
   def __init__(self, obj):
      pass

class RunSystemTasks_output:
   def __init__(self, obj):
      pass

class RunTaskDirect_input:
   """ Required : 
   ipTaskNum
   """  
   def __init__(self, obj):
      self.ipTaskNum:int = obj["ipTaskNum"]
      """  The SysTask number.  """  
      pass

class RunTaskDirect_output:
   def __init__(self, obj):
      pass

class RunTask_input:
   """ Required : 
   ipTaskNum
   """  
   def __init__(self, obj):
      self.ipTaskNum:int = obj["ipTaskNum"]
      """  The SysTask number.  """  
      pass

class RunTask_output:
   def __init__(self, obj):
      pass

