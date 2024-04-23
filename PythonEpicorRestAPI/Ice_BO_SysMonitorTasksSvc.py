import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysMonitorTasksSvc
# Description: The System Monitor task service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysMonitorTasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysMonitorTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysMonitorTasks
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks",headers=creds) as resp:
           return await resp.json()

async def post_SysMonitorTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysMonitorTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysMonitorTasks_SysTaskNum(SysTaskNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysMonitorTask item
   Description: Calls GetByID to retrieve the SysMonitorTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysMonitorTask
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks(" + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysMonitorTasks_SysTaskNum(SysTaskNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysMonitorTask for the service
   Description: Calls UpdateExt to update SysMonitorTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysMonitorTask
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks(" + SysTaskNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysMonitorTasks_SysTaskNum(SysTaskNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysMonitorTask item
   Description: Call UpdateExt to delete SysMonitorTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysMonitorTask
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks(" + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysMonitorTasks_SysTaskNum_SysTaskLogs(SysTaskNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysTaskLogs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysTaskLogs1
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks(" + SysTaskNum + ")/SysTaskLogs",headers=creds) as resp:
           return await resp.json()

async def get_SysMonitorTasks_SysTaskNum_SysTaskLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysTaskLog item
   Description: Calls GetByID to retrieve the SysTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskLog1
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysMonitorTasks(" + SysTaskNum + ")/SysTaskLogs(" + SysTaskNum + "," + EntryNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysTaskLogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysTaskLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysTaskLogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysTaskLogs",headers=creds) as resp:
           return await resp.json()

async def post_SysTaskLogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysTaskLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysTaskLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysTaskLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysTaskLogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysTaskLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysTaskLog item
   Description: Calls GetByID to retrieve the SysTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysTaskLogs(" + SysTaskNum + "," + EntryNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysTaskLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysTaskLog for the service
   Description: Calls UpdateExt to update SysTaskLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysTaskLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysTaskLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysTaskLogs(" + SysTaskNum + "," + EntryNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysTaskLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysTaskLog item
   Description: Call UpdateExt to delete SysTaskLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysTaskLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/SysTaskLogs(" + SysTaskNum + "," + EntryNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysTask, whereClauseSysTaskLog, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseSysTask=" + whereClauseSysTask
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysTaskLog=" + whereClauseSysTaskLog
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysTaskNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "sysTaskNum=" + sysTaskNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetBallonRowsKeepIdleTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBallonRowsKeepIdleTime
   Description: Gets balloon data
   OperationID: GetBallonRowsKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBallonRowsKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBallonRowsKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteToTaskLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteToTaskLog
   Description: Add a message to the SysTask Log
   OperationID: WriteToTaskLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteToTaskLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteToTaskLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysTaskLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysTaskLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysTaskLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysTaskLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysTaskLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorTasksSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysTaskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskLogRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysTaskLogRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysTaskRow] = obj["value"]
      pass

class Ice_Tablesets_SysTaskListRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskLogRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.EntryNum:int = obj["EntryNum"]
      """  Entry Number  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  EnteredOn  """  
      self.IsError:bool = obj["IsError"]
      """  Error indicator  """  
      self.MsgText:str = obj["MsgText"]
      """  Message Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MsgType:str = obj["MsgType"]
      """  MsgType  """  
      self.MsgTypeDescription:str = obj["MsgTypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysTaskNum
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetBallonRowsKeepIdleTime_input:
   """ Required : 
   whereClauseSysTask
   whereClauseSysTaskLog
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysTask:str = obj["whereClauseSysTask"]
      """  where for SysTask table  """  
      self.whereClauseSysTaskLog:str = obj["whereClauseSysTaskLog"]
      """  where for SysTask log table  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetBallonRowsKeepIdleTime_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   sysTaskNum
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysTaskListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysTaskLog_input:
   """ Required : 
   ds
   sysTaskNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class GetNewSysTaskLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysTask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      pass

class GetNewSysTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysTask
   whereClauseSysTaskLog
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysTask:str = obj["whereClauseSysTask"]
      self.whereClauseSysTaskLog:str = obj["whereClauseSysTaskLog"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysMonitorTasksTableset:
   def __init__(self, obj):
      self.SysTask:list[Ice_Tablesets_SysTaskRow] = obj["SysTask"]
      self.SysTaskLog:list[Ice_Tablesets_SysTaskLogRow] = obj["SysTaskLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysTaskListRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskListTableset:
   def __init__(self, obj):
      self.SysTaskList:list[Ice_Tablesets_SysTaskListRow] = obj["SysTaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysTaskLogRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.EntryNum:int = obj["EntryNum"]
      """  Entry Number  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  EnteredOn  """  
      self.IsError:bool = obj["IsError"]
      """  Error indicator  """  
      self.MsgText:str = obj["MsgText"]
      """  Message Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MsgType:str = obj["MsgType"]
      """  MsgType  """  
      self.MsgTypeDescription:str = obj["MsgTypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtSysMonitorTasksTableset:
   def __init__(self, obj):
      self.SysTask:list[Ice_Tablesets_SysTaskRow] = obj["SysTask"]
      self.SysTaskLog:list[Ice_Tablesets_SysTaskLogRow] = obj["SysTaskLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysMonitorTasksTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysMonitorTasksTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTasksTableset] = obj["ds"]
      pass

      """  output parameters  """  

class WriteToTaskLog_input:
   """ Required : 
   newMessage
   taskNum
   messageType
   """  
   def __init__(self, obj):
      self.newMessage:str = obj["newMessage"]
      """  message  """  
      self.taskNum:int = obj["taskNum"]
      """  task number  """  
      self.messageType:int = obj["messageType"]
      """  Message type  """  
      pass

class WriteToTaskLog_output:
   def __init__(self, obj):
      pass

