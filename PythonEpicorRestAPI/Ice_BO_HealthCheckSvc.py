import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.HealthCheckSvc
# Description: Health Check implementation testing status of ERP application, database, task and reporting services
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ErpAlive(epicorHeaders = None):
   """  
   Summary: Invoke method ErpAlive
   Description: Check if application server is running
   OperationID: ErpAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ErpAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DatabaseAlive(epicorHeaders = None):
   """  
   Summary: Invoke method DatabaseAlive
   Description: Checks if the database is responding.
   OperationID: DatabaseAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DatabaseAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ReportServerAlive(epicorHeaders = None):
   """  
   Summary: Invoke method ReportServerAlive
   Description: Checks whether the Report Server is accessible.
   OperationID: ReportServerAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportServerAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ListCompanies(epicorHeaders = None):
   """  
   Summary: Invoke method ListCompanies
   Description: Return company identifiers that the current user has access to.
   OperationID: ListCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_StartProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartProcess
   Description: Submit the test process to the task agent.
   OperationID: StartProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartProcessOnAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartProcessOnAgent
   Description: Submit the test process to the task agent
   OperationID: StartProcessOnAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartProcessOnAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartProcessOnAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessStatus
   Description: Checks the status of the process that was started earlier in M:Ice.Services.BO.HealthCheckSvc.StartProcess(System.String).
   OperationID: ProcessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartPrint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartPrint
   Description: Submit the test print to the task agent.
   OperationID: StartPrint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartPrintOnAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartPrintOnAgent
   Description: Submit the test print to the task agent
   OperationID: StartPrintOnAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPrintOnAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPrintOnAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintStatus
   Description: Get the current status of the print
   OperationID: PrintStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountImmediateSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountImmediateSched
   OperationID: CountImmediateSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountImmediateSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountImmediateSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskDetails(epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskDetails
   Description: Get details of tasks.
   OperationID: GetTaskDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CountImmediateSched_input:
   """ Required : 
   cutOffMinutes
   """  
   def __init__(self, obj):
      self.cutOffMinutes:int = obj["cutOffMinutes"]
      pass

class CountImmediateSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.count:int = obj["parameters"]
      self.earliest:str = obj["parameters"]
      pass

      """  output parameters  """  

class DatabaseAlive_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  The execution time in milliseconds.  """  
      pass

class ErpAlive_output:
   def __init__(self, obj):
      pass

class GetTaskDetails_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ListCompanies_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The companies that the user has access to.  """  
      pass

class PrintStatus_input:
   """ Required : 
   id
   submitTime
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      """  The process identifier.  """  
      self.submitTime:str = obj["submitTime"]
      """  The submit time.  """  
      pass

class PrintStatus_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  The !:Ice.BO.HealthCheck.TaskStatus for the process.  """  
      pass

class ProcessStatus_input:
   """ Required : 
   id
   submitTime
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      """  The process identifier.  """  
      self.submitTime:str = obj["submitTime"]
      """  The submit time.  """  
      pass

class ProcessStatus_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  The !:Ice.BO.HealthCheck.TaskStatus for the process.  """  
      pass

class ReportServerAlive_output:
   def __init__(self, obj):
      pass

class StartPrintOnAgent_input:
   """ Required : 
   companyID
   agentID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  If not specified will execute against current company  """  
      self.agentID:str = obj["agentID"]
      """  Agent ID to run against  """  
      pass

class StartPrintOnAgent_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A JSON serialized object that holds the identifier and submit time.  """  
      pass

class StartPrint_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  If not specified will execute against current company.  """  
      pass

class StartPrint_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A JSON serialized object that holds the identifier and submit time.  """  
      pass

class StartProcessOnAgent_input:
   """ Required : 
   companyID
   agentID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  If not specified will execute against current company  """  
      self.agentID:str = obj["agentID"]
      """  Agent ID to run against  """  
      pass

class StartProcessOnAgent_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A JSON serialized object that holds the identifier and submit time.  """  
      pass

class StartProcess_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  If not specified will execute against current company  """  
      pass

class StartProcess_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A JSON serialized object that holds the identifier and submit time.  """  
      pass

