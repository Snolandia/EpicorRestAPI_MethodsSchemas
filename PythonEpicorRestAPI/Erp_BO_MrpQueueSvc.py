import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MrpQueueSvc
# Description: Bussiness Object for MrpQueue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MrpQueues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MrpQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MrpQueues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MrpQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/MrpQueues",headers=creds) as resp:
           return await resp.json()

async def post_MrpQueues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MrpQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MrpQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MrpQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/MrpQueues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MrpQueues_Company_ProcessType_Name(Company, ProcessType, Name, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MrpQueue item
   Description: Calls GetByID to retrieve the MrpQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MrpQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param Name: Desc: Name   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MrpQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/MrpQueues(" + Company + "," + ProcessType + "," + Name + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MrpQueues_Company_ProcessType_Name(Company, ProcessType, Name, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MrpQueue for the service
   Description: Calls UpdateExt to update MrpQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MrpQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param Name: Desc: Name   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MrpQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/MrpQueues(" + Company + "," + ProcessType + "," + Name + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MrpQueues_Company_ProcessType_Name(Company, ProcessType, Name, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MrpQueue item
   Description: Call UpdateExt to delete MrpQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MrpQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessType: Desc: ProcessType   Required: True   Allow empty value : True
      :param Name: Desc: Name   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/MrpQueues(" + Company + "," + ProcessType + "," + Name + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MrpQueueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMrpQueue, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMrpQueue=" + whereClauseMrpQueue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(processType, name, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "name=" + name

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMrpQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMrpQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMrpQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMrpQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMrpQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MrpQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MrpQueueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MrpQueueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MrpQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MrpQueueRow] = obj["value"]
      pass

class Erp_Tablesets_MrpQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.Order:int = obj["Order"]
      """  Order in which the steps should be processed  """  
      self.Name:str = obj["Name"]
      """  Step Name  """  
      self.QueueIn:str = obj["QueueIn"]
      """  Queue Name to search for processing  """  
      self.QueueOut:str = obj["QueueOut"]
      """  Name of outbound Queue to generate  """  
      self.CheckGrp:str = obj["CheckGrp"]
      """  Indicates that this step is waiting on the queues in the specified group to complete before moving on  """  
      self.QMessage:str = obj["QMessage"]
      """  Text to appear in MRP log  """  
      self.QStatus:str = obj["QStatus"]
      """  Queue name to check for when output status message to Session Monitor  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.Controller:bool = obj["Controller"]
      """  Indicates this is step is for the controller or listener(s)  """  
      self.Regen:bool = obj["Regen"]
      """  Indicates if step belongs only to regeneration mode  """  
      self.LevelRepeat:bool = obj["LevelRepeat"]
      """  Indicates that the step will be repeated for each Part Level  """  
      self.Finite:bool = obj["Finite"]
      """  Indicates if step is used for finite scheduling  """  
      self.QStatusMsg:str = obj["QStatusMsg"]
      """  Message to appear in the Session Monitor  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.ExtProcName:str = obj["ExtProcName"]
      """  Name of user defined external program to run when processing custom queues.  Not valid for system queues  """  
      self.AltQOut1:str = obj["AltQOut1"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut2:str = obj["AltQOut2"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut3:str = obj["AltQOut3"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut4:str = obj["AltQOut4"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut5:str = obj["AltQOut5"]
      """  Name of outbound Queue to generate  """  
      self.AltQIn1:str = obj["AltQIn1"]
      """  Queue Name to search for processing  """  
      self.AltQIn2:str = obj["AltQIn2"]
      """  Queue Name to search for processing  """  
      self.AltQIn3:str = obj["AltQIn3"]
      """  Queue Name to search for processing  """  
      self.AltQIn4:str = obj["AltQIn4"]
      """  Queue Name to search for processing  """  
      self.AltQIn5:str = obj["AltQIn5"]
      """  Queue Name to search for processing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled.
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.Order:int = obj["Order"]
      """  Order in which the steps should be processed  """  
      self.Name:str = obj["Name"]
      """  Step Name  """  
      self.QueueIn:str = obj["QueueIn"]
      """  Queue Name to search for processing  """  
      self.QueueOut:str = obj["QueueOut"]
      """  Name of outbound Queue to generate  """  
      self.CheckGrp:str = obj["CheckGrp"]
      """  Indicates that this step is waiting on the queues in the specified group to complete before moving on  """  
      self.QMessage:str = obj["QMessage"]
      """  Text to appear in MRP log  """  
      self.QStatus:str = obj["QStatus"]
      """  Queue name to check for when output status message to Session Monitor  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.Controller:bool = obj["Controller"]
      """  Indicates this is step is for the controller or listener(s)  """  
      self.Regen:bool = obj["Regen"]
      """  Indicates if step belongs only to regeneration mode  """  
      self.LevelRepeat:bool = obj["LevelRepeat"]
      """  Indicates that the step will be repeated for each Part Level  """  
      self.Finite:bool = obj["Finite"]
      """  Indicates if step is used for finite scheduling  """  
      self.QStatusMsg:str = obj["QStatusMsg"]
      """  Message to appear in the Session Monitor  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.ExtProcName:str = obj["ExtProcName"]
      """  Name of user defined external program to run when processing custom queues.  Not valid for system queues  """  
      self.AltQOut1:str = obj["AltQOut1"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut2:str = obj["AltQOut2"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut3:str = obj["AltQOut3"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut4:str = obj["AltQOut4"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut5:str = obj["AltQOut5"]
      """  Name of outbound Queue to generate  """  
      self.AltQIn1:str = obj["AltQIn1"]
      """  Queue Name to search for processing  """  
      self.AltQIn2:str = obj["AltQIn2"]
      """  Queue Name to search for processing  """  
      self.AltQIn3:str = obj["AltQIn3"]
      """  Queue Name to search for processing  """  
      self.AltQIn4:str = obj["AltQIn4"]
      """  Queue Name to search for processing  """  
      self.AltQIn5:str = obj["AltQIn5"]
      """  Queue Name to search for processing  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled.
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   processType
   name
   """  
   def __init__(self, obj):
      self.processType:str = obj["processType"]
      self.name:str = obj["name"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MrpQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.Order:int = obj["Order"]
      """  Order in which the steps should be processed  """  
      self.Name:str = obj["Name"]
      """  Step Name  """  
      self.QueueIn:str = obj["QueueIn"]
      """  Queue Name to search for processing  """  
      self.QueueOut:str = obj["QueueOut"]
      """  Name of outbound Queue to generate  """  
      self.CheckGrp:str = obj["CheckGrp"]
      """  Indicates that this step is waiting on the queues in the specified group to complete before moving on  """  
      self.QMessage:str = obj["QMessage"]
      """  Text to appear in MRP log  """  
      self.QStatus:str = obj["QStatus"]
      """  Queue name to check for when output status message to Session Monitor  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.Controller:bool = obj["Controller"]
      """  Indicates this is step is for the controller or listener(s)  """  
      self.Regen:bool = obj["Regen"]
      """  Indicates if step belongs only to regeneration mode  """  
      self.LevelRepeat:bool = obj["LevelRepeat"]
      """  Indicates that the step will be repeated for each Part Level  """  
      self.Finite:bool = obj["Finite"]
      """  Indicates if step is used for finite scheduling  """  
      self.QStatusMsg:str = obj["QStatusMsg"]
      """  Message to appear in the Session Monitor  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.ExtProcName:str = obj["ExtProcName"]
      """  Name of user defined external program to run when processing custom queues.  Not valid for system queues  """  
      self.AltQOut1:str = obj["AltQOut1"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut2:str = obj["AltQOut2"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut3:str = obj["AltQOut3"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut4:str = obj["AltQOut4"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut5:str = obj["AltQOut5"]
      """  Name of outbound Queue to generate  """  
      self.AltQIn1:str = obj["AltQIn1"]
      """  Queue Name to search for processing  """  
      self.AltQIn2:str = obj["AltQIn2"]
      """  Queue Name to search for processing  """  
      self.AltQIn3:str = obj["AltQIn3"]
      """  Queue Name to search for processing  """  
      self.AltQIn4:str = obj["AltQIn4"]
      """  Queue Name to search for processing  """  
      self.AltQIn5:str = obj["AltQIn5"]
      """  Queue Name to search for processing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled.
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpQueueListTableset:
   def __init__(self, obj):
      self.MrpQueueList:list[Erp_Tablesets_MrpQueueListRow] = obj["MrpQueueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MrpQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcessType:str = obj["ProcessType"]
      """  This is the type of process that has been started.  Valid values are "MRP","GenPO","Sched","SetOrder","SaveLoad"  """  
      self.Order:int = obj["Order"]
      """  Order in which the steps should be processed  """  
      self.Name:str = obj["Name"]
      """  Step Name  """  
      self.QueueIn:str = obj["QueueIn"]
      """  Queue Name to search for processing  """  
      self.QueueOut:str = obj["QueueOut"]
      """  Name of outbound Queue to generate  """  
      self.CheckGrp:str = obj["CheckGrp"]
      """  Indicates that this step is waiting on the queues in the specified group to complete before moving on  """  
      self.QMessage:str = obj["QMessage"]
      """  Text to appear in MRP log  """  
      self.QStatus:str = obj["QStatus"]
      """  Queue name to check for when output status message to Session Monitor  """  
      self.GroupID:str = obj["GroupID"]
      """  Group the step belongs to  """  
      self.Controller:bool = obj["Controller"]
      """  Indicates this is step is for the controller or listener(s)  """  
      self.Regen:bool = obj["Regen"]
      """  Indicates if step belongs only to regeneration mode  """  
      self.LevelRepeat:bool = obj["LevelRepeat"]
      """  Indicates that the step will be repeated for each Part Level  """  
      self.Finite:bool = obj["Finite"]
      """  Indicates if step is used for finite scheduling  """  
      self.QStatusMsg:str = obj["QStatusMsg"]
      """  Message to appear in the Session Monitor  """  
      self.SystemProc:bool = obj["SystemProc"]
      """  Indicates this is a system process  """  
      self.ExtProcName:str = obj["ExtProcName"]
      """  Name of user defined external program to run when processing custom queues.  Not valid for system queues  """  
      self.AltQOut1:str = obj["AltQOut1"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut2:str = obj["AltQOut2"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut3:str = obj["AltQOut3"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut4:str = obj["AltQOut4"]
      """  Name of outbound Queue to generate  """  
      self.AltQOut5:str = obj["AltQOut5"]
      """  Name of outbound Queue to generate  """  
      self.AltQIn1:str = obj["AltQIn1"]
      """  Queue Name to search for processing  """  
      self.AltQIn2:str = obj["AltQIn2"]
      """  Queue Name to search for processing  """  
      self.AltQIn3:str = obj["AltQIn3"]
      """  Queue Name to search for processing  """  
      self.AltQIn4:str = obj["AltQIn4"]
      """  Queue Name to search for processing  """  
      self.AltQIn5:str = obj["AltQIn5"]
      """  Queue Name to search for processing  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurDesignMode:bool = obj["CurDesignMode"]
      """   If this variable is true then the SystemProc field should default to true and be enabled.
If the Cur-DesignMode is false then the SystemProc field should be false and disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MrpQueueTableset:
   def __init__(self, obj):
      self.MrpQueue:list[Erp_Tablesets_MrpQueueRow] = obj["MrpQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMrpQueueTableset:
   def __init__(self, obj):
      self.MrpQueue:list[Erp_Tablesets_MrpQueueRow] = obj["MrpQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   processType
   name
   """  
   def __init__(self, obj):
      self.processType:str = obj["processType"]
      self.name:str = obj["name"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MrpQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MrpQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MrpQueueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMrpQueue_input:
   """ Required : 
   ds
   processType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MrpQueueTableset] = obj["ds"]
      self.processType:str = obj["processType"]
      pass

class GetNewMrpQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MrpQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMrpQueue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMrpQueue:str = obj["whereClauseMrpQueue"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MrpQueueTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtMrpQueueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMrpQueueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MrpQueueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MrpQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

