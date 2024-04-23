import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BatchOpsSvc
# Description: File        : bo/BatchOps/BatchOps.p
            
Purpose     : To  create a batch Job.
A Batch Job is created with the operations pulled from the primary job (first job selected) and
the necessary raw material requirements.
The operations are processed on all jobs begining at or ending at the specified operation. This
is only done per the single assembly of the operation.
All these operations will be marked as complete on the source job. Only the operations from the
primary job will transfered to the new Batch Job.
All related Raw materials from all jobs that are being batched are transfered to the Batch Job.
If bathcing the first operation of the assembly then the unrelated materials will be transfered also.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_DoBatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoBatching
   Description: Combines the given list of job operations from different jobs into a single "bathced" job.
   OperationID: DoBatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoBatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoBatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsFullSerial(epicorHeaders = None):
   """  
   Summary: Invoke method IsFullSerial
   Description: Dummy method IsFullSerial
   OperationID: IsFullSerial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsFullSerial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetFinalOprOnBatchedJob(epicorHeaders = None):
   """  
   Summary: Invoke method SetFinalOprOnBatchedJob
   Description: Purpose: SETS THE AUTO RECEIVE OPERATION ON THE BATCHED JOB.
            
Parameters:  none
Notes:
   OperationID: SetFinalOprOnBatchedJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFinalOprOnBatchedJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DoBatching_input:
   """ Required : 
   jobProcessMode
   pullDirection
   autoReceive
   finalOpr
   opRowIDList
   """  
   def __init__(self, obj):
      self.jobProcessMode:str = obj["jobProcessMode"]
      """  Process Mode for the new job. Values: S(Sequential) or C(Concurrent).  """  
      self.pullDirection:str = obj["pullDirection"]
      """  Direction to pull operations beginning at the specified operation.
           Can be Forward or Backward  """  
      self.autoReceive:bool = obj["autoReceive"]
      """  Auto Receive  """  
      self.finalOpr:bool = obj["finalOpr"]
      """  Final Operation  """  
      self.opRowIDList:str = obj["opRowIDList"]
      """  Comma separated list of Operations (JobOper.RowIdent) to begin pulling into batched job.  """  
      pass

class DoBatching_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newJobNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class IsFullSerial_output:
   def __init__(self, obj):
      pass

class SetFinalOprOnBatchedJob_output:
   def __init__(self, obj):
      pass

