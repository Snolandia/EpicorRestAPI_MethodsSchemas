import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ProcessSetSvc
# Description: ProcessSet service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ProcessSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProcessSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProcessSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets",headers=creds) as resp:
           return await resp.json()

async def post_ProcessSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProcessSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ProcessSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ProcessSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProcessSets_Company_SystemCode_ProcessID(Company, SystemCode, ProcessID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProcessSet item
   Description: Calls GetByID to retrieve the ProcessSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ProcessSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets(" + Company + "," + SystemCode + "," + ProcessID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProcessSets_Company_SystemCode_ProcessID(Company, SystemCode, ProcessID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProcessSet for the service
   Description: Calls UpdateExt to update ProcessSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProcessSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ProcessSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets(" + Company + "," + SystemCode + "," + ProcessID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProcessSets_Company_SystemCode_ProcessID(Company, SystemCode, ProcessID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProcessSet item
   Description: Call UpdateExt to delete ProcessSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProcessSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets(" + Company + "," + SystemCode + "," + ProcessID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProcessSets_Company_SystemCode_ProcessID_ProcessTasks(Company, SystemCode, ProcessID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProcessTasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProcessTasks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets(" + Company + "," + SystemCode + "," + ProcessID + ")/ProcessTasks",headers=creds) as resp:
           return await resp.json()

async def get_ProcessSets_Company_SystemCode_ProcessID_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company, SystemCode, ProcessID, SysTaskNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProcessTask item
   Description: Calls GetByID to retrieve the ProcessTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessTask1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param SysTaskNum: Desc: SysTaskNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessSets(" + Company + "," + SystemCode + "," + ProcessID + ")/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProcessTasks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProcessTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProcessTasks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessTasks",headers=creds) as resp:
           return await resp.json()

async def post_ProcessTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProcessTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company, SystemCode, ProcessID, SysTaskNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProcessTask item
   Description: Calls GetByID to retrieve the ProcessTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProcessTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param SysTaskNum: Desc: SysTaskNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company, SystemCode, ProcessID, SysTaskNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProcessTask for the service
   Description: Calls UpdateExt to update ProcessTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProcessTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param SysTaskNum: Desc: SysTaskNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ProcessTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProcessTasks_Company_SystemCode_ProcessID_SysTaskNum(Company, SystemCode, ProcessID, SysTaskNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProcessTask item
   Description: Call UpdateExt to delete ProcessTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProcessTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ProcessID: Desc: ProcessID   Required: True   Allow empty value : True
      :param SysTaskNum: Desc: SysTaskNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/ProcessTasks(" + Company + "," + SystemCode + "," + ProcessID + "," + SysTaskNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ProcessSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseProcessSet, whereClauseProcessTask, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseProcessSet=" + whereClauseProcessSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProcessTask=" + whereClauseProcessTask
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, systemCode, processID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "systemCode=" + systemCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processID=" + processID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateProcessSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateProcessSet
   Description: This method copies an existing process set to a new process set specified by the user.
   OperationID: DuplicateProcessSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateProcessSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateProcessSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveOnePosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveOnePosition
   Description: This method moves the Task Up/Down one position in the ProcessSet and returns the
whole updated dataset.
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveTaskToSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveTaskToSet
   Description: This method moves a process task from a source process set to the target
process set. The source process set cannot be a system process set.
   OperationID: MoveTaskToSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTaskToSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTaskToSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProcessSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProcessSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProcessSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProcessTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProcessTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProcessTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ProcessSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ProcessSetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ProcessSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ProcessTaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ProcessTaskRow] = obj["value"]
      pass

class Ice_Tablesets_ProcessSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.Description:str = obj["Description"]
      """  Process Description  """  
      self.SystemProcess:bool = obj["SystemProcess"]
      """  Indicates if the Process Set is a system process and not open to user updates  """  
      self.IsAsynchronous:bool = obj["IsAsynchronous"]
      """  IsAsynchronous  """  
      self.IsConversion:bool = obj["IsConversion"]
      """  IsConversion  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.RunPatchLevel:str = obj["RunPatchLevel"]
      """  RunPatchLevel  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.RunOn:str = obj["RunOn"]
      """  RunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ProcessSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.Description:str = obj["Description"]
      """  Process Description  """  
      self.SystemProcess:bool = obj["SystemProcess"]
      """  Indicates if the Process Set is a system process and not open to user updates  """  
      self.IsAsynchronous:bool = obj["IsAsynchronous"]
      """  IsAsynchronous  """  
      self.IsConversion:bool = obj["IsConversion"]
      """  IsConversion  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.RunPatchLevel:str = obj["RunPatchLevel"]
      """  RunPatchLevel  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.RunOn:str = obj["RunOn"]
      """  RunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ProcessTaskRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  System Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  StartedOn  """  
      self.EndedOn:str = obj["EndedOn"]
      """  EndedOn  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  Task submitted by user  """  
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
      """  Task Run Procedure  """  
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
      self.SourceDLL:str = obj["SourceDLL"]
      """  Application that defined the task.  Only this application can update the task.  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   company
   systemCode
   processID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.systemCode:str = obj["systemCode"]
      self.processID:str = obj["processID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateProcessSet_input:
   """ Required : 
   systemCode
   targetProcessID
   sourceProcessID
   companyID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The SystemCode  """  
      self.targetProcessID:str = obj["targetProcessID"]
      """  New Process Set identifier.  """  
      self.sourceProcessID:str = obj["sourceProcessID"]
      """  Process Set ID to copy from.  """  
      self.companyID:str = obj["companyID"]
      """  The company identifier.  """  
      pass

class DuplicateProcessSet_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   systemCode
   processID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.systemCode:str = obj["systemCode"]
      self.processID:str = obj["processID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ProcessSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewProcessSet_input:
   """ Required : 
   ds
   company
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewProcessSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewProcessTask_input:
   """ Required : 
   ds
   company
   systemCode
   processID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.systemCode:str = obj["systemCode"]
      self.processID:str = obj["processID"]
      pass

class GetNewProcessTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseProcessSet
   whereClauseProcessTask
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseProcessSet:str = obj["whereClauseProcessSet"]
      self.whereClauseProcessTask:str = obj["whereClauseProcessTask"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
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

class Ice_Tablesets_ProcessSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.Description:str = obj["Description"]
      """  Process Description  """  
      self.SystemProcess:bool = obj["SystemProcess"]
      """  Indicates if the Process Set is a system process and not open to user updates  """  
      self.IsAsynchronous:bool = obj["IsAsynchronous"]
      """  IsAsynchronous  """  
      self.IsConversion:bool = obj["IsConversion"]
      """  IsConversion  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.RunPatchLevel:str = obj["RunPatchLevel"]
      """  RunPatchLevel  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.RunOn:str = obj["RunOn"]
      """  RunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ProcessSetListTableset:
   def __init__(self, obj):
      self.ProcessSetList:list[Ice_Tablesets_ProcessSetListRow] = obj["ProcessSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ProcessSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.Description:str = obj["Description"]
      """  Process Description  """  
      self.SystemProcess:bool = obj["SystemProcess"]
      """  Indicates if the Process Set is a system process and not open to user updates  """  
      self.IsAsynchronous:bool = obj["IsAsynchronous"]
      """  IsAsynchronous  """  
      self.IsConversion:bool = obj["IsConversion"]
      """  IsConversion  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.RunPatchLevel:str = obj["RunPatchLevel"]
      """  RunPatchLevel  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.RunOn:str = obj["RunOn"]
      """  RunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ProcessSetTableset:
   def __init__(self, obj):
      self.ProcessSet:list[Ice_Tablesets_ProcessSetRow] = obj["ProcessSet"]
      self.ProcessTask:list[Ice_Tablesets_ProcessTaskRow] = obj["ProcessTask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ProcessTaskRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  System Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  StartedOn  """  
      self.EndedOn:str = obj["EndedOn"]
      """  EndedOn  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  Task submitted by user  """  
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
      """  Task Run Procedure  """  
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
      self.SourceDLL:str = obj["SourceDLL"]
      """  Application that defined the task.  Only this application can update the task.  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtProcessSetTableset:
   def __init__(self, obj):
      self.ProcessSet:list[Ice_Tablesets_ProcessSetRow] = obj["ProcessSet"]
      self.ProcessTask:list[Ice_Tablesets_ProcessTaskRow] = obj["ProcessTask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class MoveOnePosition_input:
   """ Required : 
   systemCode
   processID
   taskNum
   moveDir
   company
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The database system code.  """  
      self.processID:str = obj["processID"]
      """  The process set identifier.  """  
      self.taskNum:int = obj["taskNum"]
      """  Task Number to move up one position.  """  
      self.moveDir:str = obj["moveDir"]
      """  Direction to move task, "Up" or "Down".  """  
      self.company:str = obj["company"]
      """  The company identifier.  """  
      pass

class MoveOnePosition_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ProcessSetTableset] = obj["returnObj"]
      pass

class MoveTaskToSet_input:
   """ Required : 
   company
   systemCode
   targetProcessID
   sourceProcessID
   sourceTaskNum
   ds
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company identifier.  """  
      self.systemCode:str = obj["systemCode"]
      """  The database system code.  """  
      self.targetProcessID:str = obj["targetProcessID"]
      """  Process Set ID to move task into  """  
      self.sourceProcessID:str = obj["sourceProcessID"]
      """  Process Set ID to move task from  """  
      self.sourceTaskNum:int = obj["sourceTaskNum"]
      """  Process Task Num to move  """  
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

class MoveTaskToSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtProcessSetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtProcessSetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ProcessSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

