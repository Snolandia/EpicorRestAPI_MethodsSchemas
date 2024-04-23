import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysTaskSvc
# Description: The SysTask service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysTasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysTasks
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks",headers=creds) as resp:
           return await resp.json()

async def post_SysTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysTasks
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysTasks_SysTaskNum(SysTaskNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysTask item
   Description: Calls GetByID to retrieve the SysTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTask
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysTasks_SysTaskNum(SysTaskNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysTask for the service
   Description: Calls UpdateExt to update SysTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysTask
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
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysTasks_SysTaskNum(SysTaskNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysTask item
   Description: Call UpdateExt to delete SysTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysTask
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysTasks_SysTaskNum_SysTaskParams(SysTaskNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysTaskParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysTaskParams1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")/SysTaskParams",headers=creds) as resp:
           return await resp.json()

async def get_SysTasks_SysTaskNum_SysTaskParams_SysTaskNum_ParamName(SysTaskNum, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysTaskParam item
   Description: Calls GetByID to retrieve the SysTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskParam1
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTasks(" + SysTaskNum + ")/SysTaskParams(" + SysTaskNum + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysTaskParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysTaskParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysTaskParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams",headers=creds) as resp:
           return await resp.json()

async def post_SysTaskParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysTaskParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysTaskParams_SysTaskNum_ParamName(SysTaskNum, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysTaskParam item
   Description: Calls GetByID to retrieve the SysTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysTaskParam
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysTaskParams_SysTaskNum_ParamName(SysTaskNum, ParamName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysTaskParam for the service
   Description: Calls UpdateExt to update SysTaskParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysTaskParam
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysTaskParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysTaskParams_SysTaskNum_ParamName(SysTaskNum, ParamName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysTaskParam item
   Description: Call UpdateExt to delete SysTaskParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysTaskParam
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/SysTaskParams(" + SysTaskNum + "," + ParamName + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysTask, whereClauseSysTaskParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSysTaskParam=" + whereClauseSysTaskParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_SysTaskExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SysTaskExists
   Description: Determines if a SysTask record exists with the given AgentID and agentSchedNum with the History flag set to the indicated value.
   OperationID: SysTaskExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SysTaskExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SysTaskExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSysTaskKillRecords(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSysTaskKillRecords
   Description: Clears SysTaskKill records.
   OperationID: DeleteSysTaskKillRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSysTaskKillRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CleanUpActiveTasks(epicorHeaders = None):
   """  
   Summary: Invoke method CleanUpActiveTasks
   Description: This functionality is no longer available.
   OperationID: CleanUpActiveTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CleanUpActiveTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_KillActiveTasks(epicorHeaders = None):
   """  
   Summary: Invoke method KillActiveTasks
   Description: Kills the active tasks by writing out SysTaskKill records for them.
   OperationID: KillActiveTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KillActiveTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckForDups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDups
   Description: Checks for a duplicate running task using the supplied parameters.
   OperationID: CheckForDups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSysTaskStatusForPendingTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSysTaskStatusForPendingTask
   Description: Sets the system task status for task that is currently pending.
   OperationID: SetSysTaskStatusForPendingTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysTaskStatusForPendingTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysTaskStatusForPendingTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteToTaskLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteToTaskLog
   Description: Writes a message to the SysTaskLog file.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysTaskParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysTaskParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysTaskParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysTaskParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysTaskParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysTaskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysTaskParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysTaskParamRow] = obj["value"]
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

class Ice_Tablesets_SysTaskParamRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.ParamName:str = obj["ParamName"]
      """  Parameter Name  """  
      self.ParamLabel:str = obj["ParamLabel"]
      """  Parameter Label  """  
      self.ParamType:str = obj["ParamType"]
      """  Variable/Pre-Processor/TempTable/Parameter  """  
      self.ParamDataType:str = obj["ParamDataType"]
      """  Date/Logical/Character/Integer/Decimal  """  
      self.ParamCharacter:str = obj["ParamCharacter"]
      """  Parameter Character Value  """  
      self.ParamDate:str = obj["ParamDate"]
      """  Parameter Date Value  """  
      self.ParamLogical:bool = obj["ParamLogical"]
      """  Parameter Logical Value  """  
      self.ParamInteger:int = obj["ParamInteger"]
      """  Parameter Integer Value  """  
      self.ParamDecimal:int = obj["ParamDecimal"]
      """  Parameter Decimal Value  """  
      self.ParamToken:str = obj["ParamToken"]
      """   Tokens are predefined values used to dynamically determine a value of a corresponding parameter. This setting of a parameter field based on a token is performed in the systaskparam write trigger.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParamLong:int = obj["ParamLong"]
      """  ParamLong  """  
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
class CheckForDups_input:
   """ Required : 
   SysTaskNum
   RunProcedure
   ProcessID
   """  
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      self.RunProcedure:str = obj["RunProcedure"]
      self.ProcessID:str = obj["ProcessID"]
      pass

class CheckForDups_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if another task is found for the same RunProcedure/ProcessID, otherwise `false`.  """  
      pass

class CleanUpActiveTasks_output:
   def __init__(self, obj):
      pass

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

class DeleteSysTaskKillRecords_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   sysTaskNum
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysTaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysTaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysTaskTableset] = obj["returnObj"]
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

class GetNewSysTaskParam_input:
   """ Required : 
   ds
   sysTaskNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class GetNewSysTaskParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysTask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      pass

class GetNewSysTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysTask
   whereClauseSysTaskParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysTask:str = obj["whereClauseSysTask"]
      self.whereClauseSysTaskParam:str = obj["whereClauseSysTaskParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysTaskTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysTaskParamRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.ParamName:str = obj["ParamName"]
      """  Parameter Name  """  
      self.ParamLabel:str = obj["ParamLabel"]
      """  Parameter Label  """  
      self.ParamType:str = obj["ParamType"]
      """  Variable/Pre-Processor/TempTable/Parameter  """  
      self.ParamDataType:str = obj["ParamDataType"]
      """  Date/Logical/Character/Integer/Decimal  """  
      self.ParamCharacter:str = obj["ParamCharacter"]
      """  Parameter Character Value  """  
      self.ParamDate:str = obj["ParamDate"]
      """  Parameter Date Value  """  
      self.ParamLogical:bool = obj["ParamLogical"]
      """  Parameter Logical Value  """  
      self.ParamInteger:int = obj["ParamInteger"]
      """  Parameter Integer Value  """  
      self.ParamDecimal:int = obj["ParamDecimal"]
      """  Parameter Decimal Value  """  
      self.ParamToken:str = obj["ParamToken"]
      """   Tokens are predefined values used to dynamically determine a value of a corresponding parameter. This setting of a parameter field based on a token is performed in the systaskparam write trigger.
Examples of valid tokens are; &FirstOfMonth, &EndOfMonth  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParamLong:int = obj["ParamLong"]
      """  ParamLong  """  
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

class Ice_Tablesets_SysTaskTableset:
   def __init__(self, obj):
      self.SysTask:list[Ice_Tablesets_SysTaskRow] = obj["SysTask"]
      self.SysTaskParam:list[Ice_Tablesets_SysTaskParamRow] = obj["SysTaskParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtSysTaskTableset:
   def __init__(self, obj):
      self.SysTask:list[Ice_Tablesets_SysTaskRow] = obj["SysTask"]
      self.SysTaskParam:list[Ice_Tablesets_SysTaskParamRow] = obj["SysTaskParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class KillActiveTasks_output:
   def __init__(self, obj):
      pass

class SetSysTaskStatusForPendingTask_input:
   """ Required : 
   sysTaskNum
   runProcedure
   taskStatus
   messageToLog
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      """  The system task number.  """  
      self.runProcedure:str = obj["runProcedure"]
      """  The run procedure for the task.  """  
      self.taskStatus:str = obj["taskStatus"]
      """  The task status.  """  
      self.messageToLog:str = obj["messageToLog"]
      """  The message to log.  """  
      pass

class SetSysTaskStatusForPendingTask_output:
   def __init__(self, obj):
      pass

class SysTaskExists_input:
   """ Required : 
   history
   agentID
   agentSchedNum
   """  
   def __init__(self, obj):
      self.history:bool = obj["history"]
      self.agentID:str = obj["agentID"]
      self.agentSchedNum:int = obj["agentSchedNum"]
      pass

class SysTaskExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if the Ice.Services.BO.SysTaskSvc.SysTask exits.  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysTaskTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysTaskTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class WriteToTaskLog_input:
   """ Required : 
   NewMessage
   TaskNum
   """  
   def __init__(self, obj):
      self.NewMessage:str = obj["NewMessage"]
      self.TaskNum:int = obj["TaskNum"]
      pass

class WriteToTaskLog_output:
   def __init__(self, obj):
      pass

