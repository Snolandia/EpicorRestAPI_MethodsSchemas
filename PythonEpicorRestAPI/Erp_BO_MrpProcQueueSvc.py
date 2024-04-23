import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MrpProcQueueSvc
# Description: Bussiness Object for MrpProcQueue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MrpProcQueues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MrpProcQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MrpProcQueues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MrpProcQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/MrpProcQueues",headers=creds) as resp:
           return await resp.json()

async def post_MrpProcQueues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MrpProcQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MrpProcQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MrpProcQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/MrpProcQueues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MrpProcQueues_Company_ProcessType_GroupID_ProcessName_Queue(Company, ProcessType, GroupID, ProcessName, Queue, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MrpProcQueue item
   Description: Calls GetByID to retrieve the MrpProcQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MrpProcQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param ProcessName: Desc: ProcessName   Required: True   Allow empty value : True
      :param Queue: Desc: Queue   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MrpProcQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/MrpProcQueues(" + Company + "," + ProcessType + "," + GroupID + "," + ProcessName + "," + Queue + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MrpProcQueues_Company_ProcessType_GroupID_ProcessName_Queue(Company, ProcessType, GroupID, ProcessName, Queue, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MrpProcQueue for the service
   Description: Calls UpdateExt to update MrpProcQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MrpProcQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param ProcessName: Desc: ProcessName   Required: True   Allow empty value : True
      :param Queue: Desc: Queue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MrpProcQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/MrpProcQueues(" + Company + "," + ProcessType + "," + GroupID + "," + ProcessName + "," + Queue + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MrpProcQueues_Company_ProcessType_GroupID_ProcessName_Queue(Company, ProcessType, GroupID, ProcessName, Queue, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MrpProcQueue item
   Description: Call UpdateExt to delete MrpProcQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MrpProcQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param ProcessName: Desc: ProcessName   Required: True   Allow empty value : True
      :param Queue: Desc: Queue   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/MrpProcQueues(" + Company + "," + ProcessType + "," + GroupID + "," + ProcessName + "," + Queue + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MrpProcQueueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMrpProcQueue, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMrpProcQueue=" + whereClauseMrpProcQueue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(processType, groupID, processName, queue, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processType=" + processType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processName=" + processName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "queue=" + queue

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGroupID
   Description: UPdate MRPPRocQueue when a different GroupID is selected.
   OperationID: ChangeGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMrpProcQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMrpProcQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMrpProcQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMrpProcQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMrpProcQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpProcQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MrpProcQueueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MrpProcQueueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MrpProcQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MrpProcQueueRow] = obj["value"]
      pass

class Erp_Tablesets_MrpProcQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.ProcessName:str = obj["ProcessName"]
      """  This is the name used to check the status in SysTaskParam  """  
      self.Queue:str = obj["Queue"]
      """  Queue Name (In/out)  """  
      self.QueueText:str = obj["QueueText"]
      """  Text to place in Queue Status to compare against other queues  """  
      self.Order:int = obj["Order"]
      """  Order of Queue within group and processor name  """  
      self.QType:str = obj["QType"]
      """  Indicates if Queue is Job, Part, TO, or default queue type  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.GroupStartMsg:str = obj["GroupStartMsg"]
      """  Message to put in log when group starts  """  
      self.GroupEndMsg:str = obj["GroupEndMsg"]
      """  Message to put in log at Group end  """  
      self.PartLevel:bool = obj["PartLevel"]
      """  Indicates if Part Levels are tracked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled 
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpProcQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.ProcessName:str = obj["ProcessName"]
      """  This is the name used to check the status in SysTaskParam  """  
      self.Queue:str = obj["Queue"]
      """  Queue Name (In/out)  """  
      self.QueueText:str = obj["QueueText"]
      """  Text to place in Queue Status to compare against other queues  """  
      self.Order:int = obj["Order"]
      """  Order of Queue within group and processor name  """  
      self.QType:str = obj["QType"]
      """  Indicates if Queue is Job, Part, TO, or default queue type  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.GroupStartMsg:str = obj["GroupStartMsg"]
      """  Message to put in log when group starts  """  
      self.GroupEndMsg:str = obj["GroupEndMsg"]
      """  Message to put in log at Group end  """  
      self.PartLevel:bool = obj["PartLevel"]
      """  Indicates if Part Levels are tracked  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled 
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeGroupID_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The MRPProcQueue data set  """  
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      pass

class ChangeGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   processType
   groupID
   processName
   queue
   """  
   def __init__(self, obj):
      self.processType:str = obj["processType"]
      self.groupID:str = obj["groupID"]
      self.processName:str = obj["processName"]
      self.queue:str = obj["queue"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MrpProcQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.ProcessName:str = obj["ProcessName"]
      """  This is the name used to check the status in SysTaskParam  """  
      self.Queue:str = obj["Queue"]
      """  Queue Name (In/out)  """  
      self.QueueText:str = obj["QueueText"]
      """  Text to place in Queue Status to compare against other queues  """  
      self.Order:int = obj["Order"]
      """  Order of Queue within group and processor name  """  
      self.QType:str = obj["QType"]
      """  Indicates if Queue is Job, Part, TO, or default queue type  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.GroupStartMsg:str = obj["GroupStartMsg"]
      """  Message to put in log when group starts  """  
      self.GroupEndMsg:str = obj["GroupEndMsg"]
      """  Message to put in log at Group end  """  
      self.PartLevel:bool = obj["PartLevel"]
      """  Indicates if Part Levels are tracked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled 
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpProcQueueListTableset:
   def __init__(self, obj):
      self.MrpProcQueueList:list[Erp_Tablesets_MrpProcQueueListRow] = obj["MrpProcQueueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MrpProcQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.ProcessName:str = obj["ProcessName"]
      """  This is the name used to check the status in SysTaskParam  """  
      self.Queue:str = obj["Queue"]
      """  Queue Name (In/out)  """  
      self.QueueText:str = obj["QueueText"]
      """  Text to place in Queue Status to compare against other queues  """  
      self.Order:int = obj["Order"]
      """  Order of Queue within group and processor name  """  
      self.QType:str = obj["QType"]
      """  Indicates if Queue is Job, Part, TO, or default queue type  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.GroupStartMsg:str = obj["GroupStartMsg"]
      """  Message to put in log when group starts  """  
      self.GroupEndMsg:str = obj["GroupEndMsg"]
      """  Message to put in log at Group end  """  
      self.PartLevel:bool = obj["PartLevel"]
      """  Indicates if Part Levels are tracked  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled 
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpProcQueueTableset:
   def __init__(self, obj):
      self.MrpProcQueue:list[Erp_Tablesets_MrpProcQueueRow] = obj["MrpProcQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMrpProcQueueTableset:
   def __init__(self, obj):
      self.MrpProcQueue:list[Erp_Tablesets_MrpProcQueueRow] = obj["MrpProcQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   processType
   groupID
   processName
   queue
   """  
   def __init__(self, obj):
      self.processType:str = obj["processType"]
      self.groupID:str = obj["groupID"]
      self.processName:str = obj["processName"]
      self.queue:str = obj["queue"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpProcQueueTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpProcQueueTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpProcQueueTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpProcQueueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMrpProcQueue_input:
   """ Required : 
   ds
   processType
   groupID
   processName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      self.processType:str = obj["processType"]
      self.groupID:str = obj["groupID"]
      self.processName:str = obj["processName"]
      pass

class GetNewMrpProcQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMrpProcQueue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMrpProcQueue:str = obj["whereClauseMrpProcQueue"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpProcQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMrpProcQueueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMrpProcQueueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MrpProcQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

