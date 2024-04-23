import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaskSvc
# Description: The Task main object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Tasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Tasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Tasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks",headers=creds) as resp:
           return await resp.json()

async def post_Tasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Tasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Task item
   Description: Calls GetByID to retrieve the Task item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Task
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Task for the service
   Description: Calls UpdateExt to update Task. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Task
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Task item
   Description: Call UpdateExt to delete Task item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Task
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_TaskCnts(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskCnts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")/TaskCnts",headers=creds) as resp:
           return await resp.json()

async def get_Tasks_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskCnt item
   Description: Calls GetByID to retrieve the TaskCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskCnt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/Tasks(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + ")/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskCnts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskCnts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts",headers=creds) as resp:
           return await resp.json()

async def post_TaskCnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskCnt item
   Description: Calls GetByID to retrieve the TaskCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, PerConLnkRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskCnt for the service
   Description: Calls UpdateExt to update TaskCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskCnts_Company_RelatedToFile_Key1_Key2_Key3_TaskSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, TaskSeqNum, PerConLnkRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskCnt item
   Description: Call UpdateExt to delete TaskCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param TaskSeqNum: Desc: TaskSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/TaskCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + TaskSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTask, whereClauseTaskCnt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTask=" + whereClauseTask
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskCnt=" + whereClauseTaskCnt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToFile, key1, key2, key3, taskSeqNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "relatedToFile=" + relatedToFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taskSeqNum=" + taskSeqNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignDefaultsFromQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignDefaultsFromQuote
   Description: Assigns defaults for the task when is created from a Quote.
   OperationID: AssignDefaultsFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignDefaultsFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignDefaultsFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCompleteIncludingNextTaskWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCompleteIncludingNextTaskWarning
   Description: Executes thw Changecomplete logic and provides an optional warning message for quotes that have subsequent tasks and more than one task will be updateable.
Use this method when you want the additional message sent back to the client.
   OperationID: ChangeCompleteIncludingNextTaskWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompleteIncludingNextTaskWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompleteIncludingNextTaskWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVoid
   Description: Performs next task check when the void column is changed.
   OperationID: ChangeVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeComplete
   Description: Assigns defaults for the task when the complete field is checked.
   OperationID: ChangeComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVoided(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVoided
   Description: Assigns defaults for the task when the task gets Voided.
   OperationID: ChangeVoided
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVoided_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVoided_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConclusion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConclusion
   Description: Assigns defaults for the task when the conclusion is changed.
   OperationID: ChangeConclusion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConclusion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConclusion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConName
   Description: Update TaskCnt information when the contact Name is changed.
   OperationID: ChangeConName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConPerConLnkRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConPerConLnkRowID
   Description: Update TaskCnt information when the contact PerConLnkRowID is changed.
   OperationID: ChangeConPerConLnkRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomer
   Description: Assigns defaults for the task when the customer changes.
   OperationID: ChangeCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomerContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomerContact
   Description: Assigns defaults for the task when the customer contact changes.
   OperationID: ChangeCustomerContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomerShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomerShipTo
   Description: Assigns defaults for the task when the customer changes.
   OperationID: ChangeCustomerShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaskShipToCust(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaskShipToCust
   Description: Assigns defaults for the task when the customer ship to changes.
   OperationID: ChangeTaskShipToCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskShipToCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskShipToCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaskShipToCustContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaskShipToCustContact
   Description: ChangeTaskShipToCustContact
   OperationID: ChangeTaskShipToCustContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskShipToCustContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskShipToCustContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeNextTaskSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeNextTaskSeq
   Description: Get the Next Task Description when the NextTaskSeq changes.
   OperationID: ChangeNextTaskSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNextTaskSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNextTaskSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSalesRep(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSalesRep
   Description: Assigns defaults for the task when the salesRep changes.
   OperationID: ChangeSalesRep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSalesRep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSalesRep_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaskID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaskID
   Description: Assigns defaults for the task when the task id changes.
   OperationID: ChangeTaskID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaskTimeDisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaskTimeDisp
   Description: Assigns the format for the task Start and End Time fields when their value changes.
   OperationID: ChangeTaskTimeDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskTimeDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskTimeDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTEApprovalAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTEApprovalAction
   Description: Assigns defaults for the task when the time or expense approval action changes.
   OperationID: ChangeTEApprovalAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTEApprovalAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTEApprovalAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateConclusion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateConclusion
   Description: Validates Task Conclusion
   OperationID: ValidateConclusion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateConclusion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConclusion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateVendorID
   Description: Validate Vendor ID.
   OperationID: ValidateVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePurPoint
   Description: Validate Vendor Purchase Point.
   OperationID: ValidatePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendor
   Description: Assigns defaults for the task when the vendor changes.
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorContact
   Description: Assigns defaults for the task when the vendor contact changes.
   OperationID: ChangeVendorContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorPP
   Description: Assigns defaults for the task when the vendor purchase point changes.
   OperationID: ChangeVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteForCreditLimit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteForCreditLimit
   OperationID: CheckQuoteForCreditLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteForCreditLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteForCreditLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PutCustomerOnCreditHold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PutCustomerOnCreditHold
   Description: PutCustomerOnCreditHold
   OperationID: PutCustomerOnCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PutCustomerOnCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PutCustomerOnCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCreditHoldMessageText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCreditHoldMessageText
   Description: Retrieve the customer on credit hold message text.
   OperationID: GetCreditHoldMessageText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCreditHoldMessageText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreditHoldMessageText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultEndDate(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultEndDate
   OperationID: GetDefaultEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetListApprovers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListApprovers
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetListApprovers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListApprovers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListApprovers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteLinesWOQtyMessageText(epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteLinesWOQtyMessageText
   Description: This method returns the message text for the case where there aren't any quote
lines with an order quantity.
   OperationID: GetQuoteLinesWOQtyMessageText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteLinesWOQtyMessageText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExistsUncompletedTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsUncompletedTasks
   Description: This method returns a true if there are remaining uncompleted tasks
   OperationID: ExistsUncompletedTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsUncompletedTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsUncompletedTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimarySalesRepForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimarySalesRepForUser
   Description: Gets the primary sales rep for the user
   OperationID: GetPrimarySalesRepForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimarySalesRepForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimarySalesRepForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRemainUncompletedTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRemainUncompletedTasks
   Description: Retrieve yes/no regarding if there are ramain uncompleted milestone tasks in HDCase.
   OperationID: GetRemainUncompletedTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRemainUncompletedTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRemainUncompletedTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Called from Customer tracker instead of GetRows for better performance
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskCnt
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetTaskCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskListByDateRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskListByDateRange
   Description: This method returns a list of Tasks to be viewed in the Task List screen based
a Sales Representative, Date Range, and sort options.  This method builds the where
clause instead of having the UI build the where clause on their end.  Although either
method could be used to build the Tree.
   OperationID: GetTaskListByDateRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskListByDateRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskListByDateRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskList
   Description: Deprecated method to get the list of Tasks to be viewed in the Task List screen based a Sales Representative, Date Range, and sort options.
   OperationID: GetTaskList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentTaskSeqNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentTaskSeqNum
   Description: GetCurrentTaskSeqNum
   OperationID: GetCurrentTaskSeqNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentTaskSeqNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentTaskSeqNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WorkFlowCompleteWithRemainingTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WorkFlowCompleteWithRemainingTask
   Description: Marks current Task as WorkflowComplete = true, and remaining tasks get completed
   OperationID: WorkFlowCompleteWithRemainingTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WorkFlowCompleteWithRemainingTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WorkFlowCompleteWithRemainingTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTaskCanBeVoided(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTaskCanBeVoided
   Description: CheckTaskCanBeVoided
   OperationID: CheckTaskCanBeVoided
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTaskCanBeVoided_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTaskCanBeVoided_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CanCompleteWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CanCompleteWorkflow
   Description: CanCompleteWorkflow
   OperationID: CanCompleteWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CanCompleteWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanCompleteWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TerritoryAuthorized(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TerritoryAuthorized
   Description: TerritoryAuthorized
   OperationID: TerritoryAuthorized
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TerritoryAuthorized_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TerritoryAuthorized_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidTask
   Description: Voids a task
   OperationID: VoidTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskTreeDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskTreeDataSet
   Description: Gets dataset for task tree view
   OperationID: GetTaskTreeDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskTreeDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskTreeDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportFile
   Description: Export file
   OperationID: ExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaskCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaskCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskCntRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskRow] = obj["value"]
      pass

class Erp_Tablesets_TaskCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related. Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record. Used so more than 1 Task can exist for a given record. The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type. The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.City:str = obj["City"]
      self.ContextLink:str = obj["ContextLink"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.Name:str = obj["Name"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.State:str = obj["State"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Zip:str = obj["Zip"]
      self.PerConID:int = obj["PerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  EmployeeName  """  
      self.TimeOrExp:str = obj["TimeOrExp"]
      """   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID, used only by Task Time and Expense search as a search results grid.  """  
      self.TransDate:str = obj["TransDate"]
      """  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum, used only by task time and expense approbal search as search results grid  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.StartTime:int = obj["StartTime"]
      """  Start Time for task.  Stored as seconds from midnight  """  
      self.EndTime:int = obj["EndTime"]
      """  End Time for task.  Stored as seconds from midnight  """  
      self.AnyApprover:bool = obj["AnyApprover"]
      """  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the Task has been Approved via Time and Expense Approval.  """  
      self.CompletionAction:str = obj["CompletionAction"]
      """   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  """  
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.RejectApproval:bool = obj["RejectApproval"]
      """  Used for time and expense tasks.  Indicates the transaction the task is linked to will be marked as rejected when the task is completed.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaskShipToCustNum:int = obj["TaskShipToCustNum"]
      """  TaskShipToCustNum  """  
      self.TaskShipToCustConNum:int = obj["TaskShipToCustConNum"]
      """  TaskShipToCustConNum  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.TaskPerConID:int = obj["TaskPerConID"]
      """  TaskPerConID  """  
      self.PrevTaskSetTask:bool = obj["PrevTaskSetTask"]
      """  PrevTaskSetTask  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.ChangeTimeDisp:str = obj["ChangeTimeDisp"]
      """  Temporary display field for Change Time  """  
      self.CurrentStageDescription:str = obj["CurrentStageDescription"]
      """  Current Stage Description  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.CustomerContactFax:str = obj["CustomerContactFax"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerContactPhone:str = obj["CustomerContactPhone"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DisableOnComplete:bool = obj["DisableOnComplete"]
      """  This is a boolean field to check if the Task is already completed or the user doesn't already complete the task.  """  
      self.DisableTasks:bool = obj["DisableTasks"]
      self.EndTimeDisp:str = obj["EndTimeDisp"]
      """  Temporary display field for End Time  """  
      self.FilterIncludeComplete:bool = obj["FilterIncludeComplete"]
      self.FilterStartAtDate:str = obj["FilterStartAtDate"]
      self.FilterStartAtQuote:int = obj["FilterStartAtQuote"]
      self.FilterTaskType:str = obj["FilterTaskType"]
      self.FilterType:str = obj["FilterType"]
      self.IsLoseable:bool = obj["IsLoseable"]
      self.IsWinnable:bool = obj["IsWinnable"]
      self.NewMilestoneTaskSeqNum:int = obj["NewMilestoneTaskSeqNum"]
      self.NextStage:str = obj["NextStage"]
      self.NextTaskList:str = obj["NextTaskList"]
      self.OrigMilestoneTaskSeqNum:int = obj["OrigMilestoneTaskSeqNum"]
      self.OtherSalesRepName:str = obj["OtherSalesRepName"]
      self.PromptCustCreditHoldWarning:bool = obj["PromptCustCreditHoldWarning"]
      self.PromptQuoteLinesWOQty:bool = obj["PromptQuoteLinesWOQty"]
      self.ReasonList:str = obj["ReasonList"]
      self.RejectAppAllowed:bool = obj["RejectAppAllowed"]
      """  Reject Approval Allowed - this option is available only for time and expense tasks  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the Sales Representative.  """  
      self.StartTimeDisp:str = obj["StartTimeDisp"]
      """  Temporary display field for Start Time  """  
      self.TaskCompletePasswordIsValid:bool = obj["TaskCompletePasswordIsValid"]
      """  Indicates if the password to complete the task is valid.  """  
      self.TaskCompletePasswordRequired:bool = obj["TaskCompletePasswordRequired"]
      """  Indicates if a password is required to complete the task  """  
      self.TaskShipToCustConName:str = obj["TaskShipToCustConName"]
      self.TaskShipToCustID:str = obj["TaskShipToCustID"]
      self.TaskShipToCustName:str = obj["TaskShipToCustName"]
      self.TaskSoldToCustNumAllowsShipTo3:bool = obj["TaskSoldToCustNumAllowsShipTo3"]
      """  This Column will store the value of the flag Customer.AllowShipTo3 for Task SoldTo Customers  """  
      self.TEApprovalAction:str = obj["TEApprovalAction"]
      """  Indicates whether a time or expense task is being approved or rejected.  """  
      self.TETask:bool = obj["TETask"]
      """  Indicates if this is a time or expense task.  UI fields are enabled/disasbled based on this.  """  
      self.VendorContactEmail:str = obj["VendorContactEmail"]
      self.VendorContactFax:str = obj["VendorContactFax"]
      self.VendorContactName:str = obj["VendorContactName"]
      self.VendorContactPhone:str = obj["VendorContactPhone"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      self.WorkflowComplete:bool = obj["WorkflowComplete"]
      self.CustomerContactEmail:str = obj["CustomerContactEmail"]
      self.CanBeVoided:bool = obj["CanBeVoided"]
      """  Used in Quote to verify if the task can be voided.  """  
      self.ConclusionList:str = obj["ConclusionList"]
      """  List of conclusion options  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChangeDcdUserIDName:str = obj["ChangeDcdUserIDName"]
      self.ReasonCodeHDDescription:str = obj["ReasonCodeHDDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.StatusCodeStatusDescription:str = obj["StatusCodeStatusDescription"]
      self.TaskConNumNameMiddleName:str = obj["TaskConNumNameMiddleName"]
      self.TaskConNumNameLastName:str = obj["TaskConNumNameLastName"]
      self.TaskConNumNameFirstName:str = obj["TaskConNumNameFirstName"]
      self.TaskConNumNameName:str = obj["TaskConNumNameName"]
      self.TaskConNumNameCorpName:str = obj["TaskConNumNameCorpName"]
      self.TaskConNumNameFaxNum:str = obj["TaskConNumNameFaxNum"]
      self.TaskConNumNamePhoneNum:str = obj["TaskConNumNamePhoneNum"]
      self.TaskCustNumInactive:bool = obj["TaskCustNumInactive"]
      self.TaskIDTaskDescription:str = obj["TaskIDTaskDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetSeqTaskDescription:str = obj["TaskSetSeqTaskDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignDefaultsFromQuote_input:
   """ Required : 
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Num of quote to assign values  """  
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class AssignDefaultsFromQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CanCompleteWorkflow_input:
   """ Required : 
   cRowIdent
   """  
   def __init__(self, obj):
      self.cRowIdent:str = obj["cRowIdent"]
      """  SysRowID  """  
      pass

class CanCompleteWorkflow_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ChangeCompleteIncludingNextTaskWarning_input:
   """ Required : 
   ds
   lProposedComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.lProposedComplete:bool = obj["lProposedComplete"]
      """  The proposed value for the complete flag  """  
      pass

class ChangeCompleteIncludingNextTaskWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.cMessage:str = obj["parameters"]
      self.nextTaskWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeComplete_input:
   """ Required : 
   ds
   lProposedComplete
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.lProposedComplete:bool = obj["lProposedComplete"]
      """  The proposed value for the complete flag  """  
      pass

class ChangeComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeConName_input:
   """ Required : 
   pName
   ds
   """  
   def __init__(self, obj):
      self.pName:str = obj["pName"]
      """  Proposed Name  """  
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeConName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeConPerConLnkRowID_input:
   """ Required : 
   pPerConLnkRowID
   ds
   """  
   def __init__(self, obj):
      self.pPerConLnkRowID:str = obj["pPerConLnkRowID"]
      """  Proposed PerConLnkRowID  """  
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeConPerConLnkRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeConclusion_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeConclusion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomerContact_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeCustomerContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomerShipTo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeCustomerShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeNextTaskSeq_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeNextTaskSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSalesRep_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeSalesRep_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTEApprovalAction_input:
   """ Required : 
   ds
   lProposedTEApprovalAction
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.lProposedTEApprovalAction:str = obj["lProposedTEApprovalAction"]
      """  The proposed value for approval action  """  
      pass

class ChangeTEApprovalAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaskID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeTaskID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaskShipToCustContact_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeTaskShipToCustContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaskShipToCust_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeTaskShipToCust_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaskTimeDisp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeTaskTimeDisp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorContact_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeVendorContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorPP_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendor_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVoid_input:
   """ Required : 
   proposedVoidValue
   ds
   """  
   def __init__(self, obj):
      self.proposedVoidValue:bool = obj["proposedVoidValue"]
      """  true or false depending upon whether or not the user ticked void or unticked it  """  
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeVoid_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.nextTaskWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeVoided_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ChangeVoided_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckQuoteForCreditLimit_input:
   """ Required : 
   iQuoteNum
   iCustNum
   """  
   def __init__(self, obj):
      self.iQuoteNum:int = obj["iQuoteNum"]
      """  Quote Number  """  
      self.iCustNum:int = obj["iCustNum"]
      """  Customer Number  """  
      pass

class CheckQuoteForCreditLimit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCreditLimitMessage:str = obj["parameters"]
      self.cCreditStatus:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTaskCanBeVoided_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID  """  
      pass

class CheckTaskCanBeVoided_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   taskSeqNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.taskSeqNum:int = obj["taskSeqNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaskCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related. Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record. Used so more than 1 Task can exist for a given record. The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type. The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.City:str = obj["City"]
      self.ContextLink:str = obj["ContextLink"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.Name:str = obj["Name"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.State:str = obj["State"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Zip:str = obj["Zip"]
      self.PerConID:int = obj["PerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  EmployeeName  """  
      self.TimeOrExp:str = obj["TimeOrExp"]
      """   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID, used only by Task Time and Expense search as a search results grid.  """  
      self.TransDate:str = obj["TransDate"]
      """  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum, used only by task time and expense approbal search as search results grid  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListTableset:
   def __init__(self, obj):
      self.TaskList:list[Erp_Tablesets_TaskListRow] = obj["TaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.StartTime:int = obj["StartTime"]
      """  Start Time for task.  Stored as seconds from midnight  """  
      self.EndTime:int = obj["EndTime"]
      """  End Time for task.  Stored as seconds from midnight  """  
      self.AnyApprover:bool = obj["AnyApprover"]
      """  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the Task has been Approved via Time and Expense Approval.  """  
      self.CompletionAction:str = obj["CompletionAction"]
      """   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  """  
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.RejectApproval:bool = obj["RejectApproval"]
      """  Used for time and expense tasks.  Indicates the transaction the task is linked to will be marked as rejected when the task is completed.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaskShipToCustNum:int = obj["TaskShipToCustNum"]
      """  TaskShipToCustNum  """  
      self.TaskShipToCustConNum:int = obj["TaskShipToCustConNum"]
      """  TaskShipToCustConNum  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.TaskPerConID:int = obj["TaskPerConID"]
      """  TaskPerConID  """  
      self.PrevTaskSetTask:bool = obj["PrevTaskSetTask"]
      """  PrevTaskSetTask  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.ChangeTimeDisp:str = obj["ChangeTimeDisp"]
      """  Temporary display field for Change Time  """  
      self.CurrentStageDescription:str = obj["CurrentStageDescription"]
      """  Current Stage Description  """  
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.CustomerContactFax:str = obj["CustomerContactFax"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerContactPhone:str = obj["CustomerContactPhone"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DisableOnComplete:bool = obj["DisableOnComplete"]
      """  This is a boolean field to check if the Task is already completed or the user doesn't already complete the task.  """  
      self.DisableTasks:bool = obj["DisableTasks"]
      self.EndTimeDisp:str = obj["EndTimeDisp"]
      """  Temporary display field for End Time  """  
      self.FilterIncludeComplete:bool = obj["FilterIncludeComplete"]
      self.FilterStartAtDate:str = obj["FilterStartAtDate"]
      self.FilterStartAtQuote:int = obj["FilterStartAtQuote"]
      self.FilterTaskType:str = obj["FilterTaskType"]
      self.FilterType:str = obj["FilterType"]
      self.IsLoseable:bool = obj["IsLoseable"]
      self.IsWinnable:bool = obj["IsWinnable"]
      self.NewMilestoneTaskSeqNum:int = obj["NewMilestoneTaskSeqNum"]
      self.NextStage:str = obj["NextStage"]
      self.NextTaskList:str = obj["NextTaskList"]
      self.OrigMilestoneTaskSeqNum:int = obj["OrigMilestoneTaskSeqNum"]
      self.OtherSalesRepName:str = obj["OtherSalesRepName"]
      self.PromptCustCreditHoldWarning:bool = obj["PromptCustCreditHoldWarning"]
      self.PromptQuoteLinesWOQty:bool = obj["PromptQuoteLinesWOQty"]
      self.ReasonList:str = obj["ReasonList"]
      self.RejectAppAllowed:bool = obj["RejectAppAllowed"]
      """  Reject Approval Allowed - this option is available only for time and expense tasks  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the Sales Representative.  """  
      self.StartTimeDisp:str = obj["StartTimeDisp"]
      """  Temporary display field for Start Time  """  
      self.TaskCompletePasswordIsValid:bool = obj["TaskCompletePasswordIsValid"]
      """  Indicates if the password to complete the task is valid.  """  
      self.TaskCompletePasswordRequired:bool = obj["TaskCompletePasswordRequired"]
      """  Indicates if a password is required to complete the task  """  
      self.TaskShipToCustConName:str = obj["TaskShipToCustConName"]
      self.TaskShipToCustID:str = obj["TaskShipToCustID"]
      self.TaskShipToCustName:str = obj["TaskShipToCustName"]
      self.TaskSoldToCustNumAllowsShipTo3:bool = obj["TaskSoldToCustNumAllowsShipTo3"]
      """  This Column will store the value of the flag Customer.AllowShipTo3 for Task SoldTo Customers  """  
      self.TEApprovalAction:str = obj["TEApprovalAction"]
      """  Indicates whether a time or expense task is being approved or rejected.  """  
      self.TETask:bool = obj["TETask"]
      """  Indicates if this is a time or expense task.  UI fields are enabled/disasbled based on this.  """  
      self.VendorContactEmail:str = obj["VendorContactEmail"]
      self.VendorContactFax:str = obj["VendorContactFax"]
      self.VendorContactName:str = obj["VendorContactName"]
      self.VendorContactPhone:str = obj["VendorContactPhone"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      self.WorkflowComplete:bool = obj["WorkflowComplete"]
      self.CustomerContactEmail:str = obj["CustomerContactEmail"]
      self.CanBeVoided:bool = obj["CanBeVoided"]
      """  Used in Quote to verify if the task can be voided.  """  
      self.ConclusionList:str = obj["ConclusionList"]
      """  List of conclusion options  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChangeDcdUserIDName:str = obj["ChangeDcdUserIDName"]
      self.ReasonCodeHDDescription:str = obj["ReasonCodeHDDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.StatusCodeStatusDescription:str = obj["StatusCodeStatusDescription"]
      self.TaskConNumNameMiddleName:str = obj["TaskConNumNameMiddleName"]
      self.TaskConNumNameLastName:str = obj["TaskConNumNameLastName"]
      self.TaskConNumNameFirstName:str = obj["TaskConNumNameFirstName"]
      self.TaskConNumNameName:str = obj["TaskConNumNameName"]
      self.TaskConNumNameCorpName:str = obj["TaskConNumNameCorpName"]
      self.TaskConNumNameFaxNum:str = obj["TaskConNumNameFaxNum"]
      self.TaskConNumNamePhoneNum:str = obj["TaskConNumNamePhoneNum"]
      self.TaskCustNumInactive:bool = obj["TaskCustNumInactive"]
      self.TaskIDTaskDescription:str = obj["TaskIDTaskDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetSeqTaskDescription:str = obj["TaskSetSeqTaskDescription"]
      self.TypeCodeTypeDescription:str = obj["TypeCodeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskTableset:
   def __init__(self, obj):
      self.Task:list[Erp_Tablesets_TaskRow] = obj["Task"]
      self.TaskCnt:list[Erp_Tablesets_TaskCntRow] = obj["TaskCnt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaskTreeDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Complete:bool = obj["Complete"]
      self.Description:str = obj["Description"]
      """  Description for the tree node  """  
      self.InternalSeq:int = obj["InternalSeq"]
      """  Unique internal sequence  """  
      self.IsTask:bool = obj["IsTask"]
      """  Indicates a task record exists for this row  """  
      self.Milestone:bool = obj["Milestone"]
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      self.TaskKey1:str = obj["TaskKey1"]
      self.TaskKey2:str = obj["TaskKey2"]
      self.TaskKey3:str = obj["TaskKey3"]
      self.TaskRelatedToFile:str = obj["TaskRelatedToFile"]
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      self.Voided:bool = obj["Voided"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskTreeHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.Description:str = obj["Description"]
      """  Description to show in the tree node  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskTreeTableset:
   def __init__(self, obj):
      self.TaskTreeHeader:list[Erp_Tablesets_TaskTreeHeaderRow] = obj["TaskTreeHeader"]
      self.TaskTreeDetail:list[Erp_Tablesets_TaskTreeDetailRow] = obj["TaskTreeDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaskTableset:
   def __init__(self, obj):
      self.Task:list[Erp_Tablesets_TaskRow] = obj["Task"]
      self.TaskCnt:list[Erp_Tablesets_TaskCntRow] = obj["TaskCnt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsUncompletedTasks_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class ExistsUncompletedTasks_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExportFile_input:
   """ Required : 
   ds
   filename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.filename:str = obj["filename"]
      pass

class ExportFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   taskSeqNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.taskSeqNum:int = obj["taskSeqNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCreditHoldMessageText_input:
   """ Required : 
   icCustID
   """  
   def __init__(self, obj):
      self.icCustID:str = obj["icCustID"]
      """  The customer id  """  
      pass

class GetCreditHoldMessageText_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ocMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrentTaskSeqNum_input:
   """ Required : 
   company
   relatedToFile
   key1
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      self.relatedToFile:str = obj["relatedToFile"]
      """  Task record is related to  """  
      self.key1:str = obj["key1"]
      """  ID or Number  """  
      pass

class GetCurrentTaskSeqNum_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetDefaultEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.endDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListApprovers_input:
   """ Required : 
   ipSalesRepCode
   ipApprovalStatus
   ipTime
   ipExpense
   ipSortby
   ipStartDate
   ipEndDate
   ipEmployeeNum
   ipProject
   ipPhase
   ipJobNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  IPsalesRepCode  """  
      self.ipApprovalStatus:str = obj["ipApprovalStatus"]
      """  Stauts of Tasks  """  
      self.ipTime:bool = obj["ipTime"]
      """  Include Time Transactions  """  
      self.ipExpense:bool = obj["ipExpense"]
      """  Include Expense transactions  """  
      self.ipSortby:str = obj["ipSortby"]
      """  Sort the data - currently not used  """  
      self.ipStartDate:str = obj["ipStartDate"]
      """  Starting date of the results set, blank will return all dates  """  
      self.ipEndDate:str = obj["ipEndDate"]
      """  Starting date of the results set, blank will return all dates  """  
      self.ipEmployeeNum:str = obj["ipEmployeeNum"]
      """  Search for time or expenses for a employee, blank for all  """  
      self.ipProject:str = obj["ipProject"]
      """  Search for time or expenses for a project, blank for al  """  
      self.ipPhase:str = obj["ipPhase"]
      """  Search for time or expenses for a phase depending of the previously selected project, blank for al  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Search for time or expenses for a job, blank for al  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  the absolute page  """  
      pass

class GetListApprovers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_TaskListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaskCnt_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   taskSeqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.taskSeqNum:int = obj["taskSeqNum"]
      pass

class GetNewTaskCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTask_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimarySalesRepForUser_input:
   """ Required : 
   userID
   """  
   def __init__(self, obj):
      self.userID:str = obj["userID"]
      pass

class GetPrimarySalesRepForUser_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetQuoteLinesWOQtyMessageText_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ocMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRemainUncompletedTasks_input:
   """ Required : 
   hdCaseNum
   taskSetId
   """  
   def __init__(self, obj):
      self.hdCaseNum:str = obj["hdCaseNum"]
      """  HDCase id  """  
      self.taskSetId:str = obj["taskSetId"]
      """  TaskSetId  """  
      pass

class GetRemainUncompletedTasks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.remainUncompletedTasks:bool = obj["remainUncompletedTasks"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseTask
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTask:str = obj["whereClauseTask"]
      """  Whereclause for Task table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseTask
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTask:str = obj["whereClauseTask"]
      """  Whereclause for Task table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTask
   whereClauseTaskCnt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTask:str = obj["whereClauseTask"]
      self.whereClauseTaskCnt:str = obj["whereClauseTaskCnt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaskCnt_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   taskSeqNum
   ds
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      """  Current RelatedToFile value  """  
      self.key1:str = obj["key1"]
      """  Current Key1 value  """  
      self.key2:str = obj["key2"]
      """  Current Key2 value  """  
      self.key3:str = obj["key3"]
      """  Current Key3 value  """  
      self.taskSeqNum:int = obj["taskSeqNum"]
      """  Current taskSeqNum value  """  
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class GetTaskCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTaskListByDateRange_input:
   """ Required : 
   salesRepCode
   includeComplete
   dateType
   startDate
   endDate
   filterStatus
   filterType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  Current SalesRep, blank to use default or code of SalesRep selected by user  """  
      self.includeComplete:bool = obj["includeComplete"]
      """  Include Complete Tasks or not  """  
      self.dateType:str = obj["dateType"]
      """  Options are startDate or dueDate  """  
      self.startDate:str = obj["startDate"]
      """  Starting date of the results set, null will return everything up to the ending date  """  
      self.endDate:str = obj["endDate"]
      """  Ending date of the results set, null will become the last day of the next month  """  
      self.filterStatus:str = obj["filterStatus"]
      """  A Specific Task Status to look for, blank for all  """  
      self.filterType:str = obj["filterType"]
      """  A specific Task Type to look for, blank for all  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  the absolute page  """  
      pass

class GetTaskListByDateRange_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaskList_input:
   """ Required : 
   salesRepCode
   includeComplete
   dateType
   startDate
   endDate
   filterStatus
   filterType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  Current SalesRep, blank to use default or code of SalesRep selected by user  """  
      self.includeComplete:bool = obj["includeComplete"]
      """  Include Complete Tasks or not  """  
      self.dateType:str = obj["dateType"]
      """  Options are startDate or dueDate  """  
      self.startDate:str = obj["startDate"]
      """  Starting date of the results set, blank will return everything up to the ending date  """  
      self.endDate:str = obj["endDate"]
      """  Ending date of the results set, blank will become the last day of the next month  """  
      self.filterStatus:str = obj["filterStatus"]
      """  A Specific Task Status to look for, blank for all  """  
      self.filterType:str = obj["filterType"]
      """  A specific Task Type to look for, blank for all  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  the absolute page  """  
      pass

class GetTaskList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaskTreeDataSet_input:
   """ Required : 
   taskSetID
   relatedToFile
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.taskSetID:str = obj["taskSetID"]
      """  Task Set ID  """  
      self.relatedToFile:str = obj["relatedToFile"]
      """  Related to file  """  
      self.key1:str = obj["key1"]
      """  Key1 for related to file  """  
      self.key2:str = obj["key2"]
      """  Key2 for related to file  """  
      self.key3:str = obj["key3"]
      """  Key3 for related to file  """  
      pass

class GetTaskTreeDataSet_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaskTreeTableset] = obj["returnObj"]
      pass

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

class PutCustomerOnCreditHold_input:
   """ Required : 
   iCreditStatus
   iCustNum
   """  
   def __init__(self, obj):
      self.iCreditStatus:str = obj["iCreditStatus"]
      """  Credit Status  """  
      self.iCustNum:int = obj["iCustNum"]
      """  Customer Number  """  
      pass

class PutCustomerOnCreditHold_output:
   def __init__(self, obj):
      pass

class TerritoryAuthorized_input:
   """ Required : 
   cCustID
   cShipToNum
   cTableName
   lPublishMessage
   """  
   def __init__(self, obj):
      self.cCustID:str = obj["cCustID"]
      """  Customer ID  """  
      self.cShipToNum:str = obj["cShipToNum"]
      """  Ship to Number  """  
      self.cTableName:str = obj["cTableName"]
      """  Table Name  """  
      self.lPublishMessage:bool = obj["lPublishMessage"]
      """  Publish Message not authorized to access  """  
      pass

class TerritoryAuthorized_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaskTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaskTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateConclusion_input:
   """ Required : 
   ds
   proposedConclusion
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.proposedConclusion:str = obj["proposedConclusion"]
      """  The proposed value for the Conclusion  """  
      pass

class ValidateConclusion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePurPoint_input:
   """ Required : 
   ds
   vendorID
   lProposedPurPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.vendorID:str = obj["vendorID"]
      """  Vendor ID parameter  """  
      self.lProposedPurPoint:str = obj["lProposedPurPoint"]
      """  The proposed value for vendor purchase point  """  
      pass

class ValidatePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateVendorID_input:
   """ Required : 
   ds
   lProposedVendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      self.lProposedVendorID:str = obj["lProposedVendorID"]
      """  The proposed value for vendor id  """  
      pass

class ValidateVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidTask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class VoidTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class WorkFlowCompleteWithRemainingTask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

class WorkFlowCompleteWithRemainingTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

