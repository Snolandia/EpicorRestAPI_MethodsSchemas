import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TEApprovalTaskSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TEApprovalTasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TEApprovalTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TEApprovalTasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks",headers=creds) as resp:
           return await resp.json()

async def post_TEApprovalTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TEApprovalTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TEApprovalTasks_Company_TaskSetID(Company, TaskSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TEApprovalTask item
   Description: Calls GetByID to retrieve the TEApprovalTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TEApprovalTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks(" + Company + "," + TaskSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TEApprovalTasks_Company_TaskSetID(Company, TaskSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TEApprovalTask for the service
   Description: Calls UpdateExt to update TEApprovalTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TEApprovalTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks(" + Company + "," + TaskSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TEApprovalTasks_Company_TaskSetID(Company, TaskSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TEApprovalTask item
   Description: Call UpdateExt to delete TEApprovalTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TEApprovalTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks(" + Company + "," + TaskSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TEApprovalTasks_Company_TaskSetID_TaskSMilestones(Company, TaskSetID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskSMilestones items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSMilestones1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMilestoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks(" + Company + "," + TaskSetID + ")/TaskSMilestones",headers=creds) as resp:
           return await resp.json()

async def get_TEApprovalTasks_Company_TaskSetID_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSMilestone item
   Description: Calls GetByID to retrieve the TaskSMilestone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMilestone1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TEApprovalTasks(" + Company + "," + TaskSetID + ")/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskSMilestones items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSMilestones
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMilestoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones",headers=creds) as resp:
           return await resp.json()

async def post_TaskSMilestones(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSMilestones
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSMilestone item
   Description: Calls GetByID to retrieve the TaskSMilestone item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMilestone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskSMilestone for the service
   Description: Calls UpdateExt to update TaskSMilestone. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSMilestone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSMilestoneRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskSMilestones_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskSMilestone item
   Description: Call UpdateExt to delete TaskSMilestone item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSMilestone
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSDtls(Company, TaskSetID, TaskSetSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskSDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtls",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSDtl item
   Description: Calls GetByID to retrieve the TaskSDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSMstoneAprvrs(Company, TaskSetID, TaskSetSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskSMstoneAprvrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSMstoneAprvrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMstoneAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSMstoneAprvrs",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSMstoneAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSMstoneAprvr item
   Description: Calls GetByID to retrieve the TaskSMstoneAprvr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMstoneAprvr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSMstoneAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSMstoneAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSNxts(Company, TaskSetID, TaskSetSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskSNxts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSNxts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSNxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSNxts",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMilestones_Company_TaskSetID_TaskSetSeq_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company, TaskSetID, TaskSetSeq, NextTaskSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSNxt item
   Description: Calls GetByID to retrieve the TaskSNxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSNxt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param NextTaskSeq: Desc: NextTaskSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMilestones(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskSDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls",headers=creds) as resp:
           return await resp.json()

async def post_TaskSDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSDtl item
   Description: Calls GetByID to retrieve the TaskSDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskSDtl for the service
   Description: Calls UpdateExt to update TaskSDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskSDtls_Company_TaskSetID_TaskSetSeq(Company, TaskSetID, TaskSetSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskSDtl item
   Description: Call UpdateExt to delete TaskSDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtls_Company_TaskSetID_TaskSetSeq_TaskSDtlAprvrs(Company, TaskSetID, TaskSetSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaskSDtlAprvrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaskSDtlAprvrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtlAprvrs",headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtls_Company_TaskSetID_TaskSetSeq_TaskSDtlAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSDtlAprvr item
   Description: Calls GetByID to retrieve the TaskSDtlAprvr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtlAprvr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSDtlAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtls(" + Company + "," + TaskSetID + "," + TaskSetSeq + ")/TaskSDtlAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtlAprvrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskSDtlAprvrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSDtlAprvrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSDtlAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtlAprvrs",headers=creds) as resp:
           return await resp.json()

async def post_TaskSDtlAprvrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSDtlAprvrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSDtlAprvrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSDtlAprvrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtlAprvrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskSDtlAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSDtlAprvr item
   Description: Calls GetByID to retrieve the TaskSDtlAprvr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSDtlAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSDtlAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtlAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskSDtlAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskSDtlAprvr for the service
   Description: Calls UpdateExt to update TaskSDtlAprvr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSDtlAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSDtlAprvrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtlAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskSDtlAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskSDtlAprvr item
   Description: Call UpdateExt to delete TaskSDtlAprvr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSDtlAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSDtlAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSMstoneAprvrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskSMstoneAprvrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSMstoneAprvrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSMstoneAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMstoneAprvrs",headers=creds) as resp:
           return await resp.json()

async def post_TaskSMstoneAprvrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSMstoneAprvrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSMstoneAprvrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSMstoneAprvrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMstoneAprvrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskSMstoneAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSMstoneAprvr item
   Description: Calls GetByID to retrieve the TaskSMstoneAprvr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSMstoneAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSMstoneAprvrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMstoneAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskSMstoneAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskSMstoneAprvr for the service
   Description: Calls UpdateExt to update TaskSMstoneAprvr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSMstoneAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSMstoneAprvrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMstoneAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskSMstoneAprvrs_Company_TaskSetID_TaskSetSeq_SalesRepCode(Company, TaskSetID, TaskSetSeq, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskSMstoneAprvr item
   Description: Call UpdateExt to delete TaskSMstoneAprvr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSMstoneAprvr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSMstoneAprvrs(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaskSNxts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaskSNxts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskSNxts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSNxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSNxts",headers=creds) as resp:
           return await resp.json()

async def post_TaskSNxts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskSNxts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSNxts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company, TaskSetID, TaskSetSeq, NextTaskSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaskSNxt item
   Description: Calls GetByID to retrieve the TaskSNxt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskSNxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param NextTaskSeq: Desc: NextTaskSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company, TaskSetID, TaskSetSeq, NextTaskSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaskSNxt for the service
   Description: Calls UpdateExt to update TaskSNxt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskSNxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param NextTaskSeq: Desc: NextTaskSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskSNxtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaskSNxts_Company_TaskSetID_TaskSetSeq_NextTaskSeq(Company, TaskSetID, TaskSetSeq, NextTaskSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaskSNxt item
   Description: Call UpdateExt to delete TaskSNxt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskSNxt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskSetID: Desc: TaskSetID   Required: True   Allow empty value : True
      :param TaskSetSeq: Desc: TaskSetSeq   Required: True
      :param NextTaskSeq: Desc: NextTaskSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/TaskSNxts(" + Company + "," + TaskSetID + "," + TaskSetSeq + "," + NextTaskSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaskSet, whereClauseTaskSMilestone, whereClauseTaskSDtl, whereClauseTaskSDtlAprvr, whereClauseTaskSMstoneAprvr, whereClauseTaskSNxt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseTaskSet=" + whereClauseTaskSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskSMilestone=" + whereClauseTaskSMilestone
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskSDtl=" + whereClauseTaskSDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskSDtlAprvr=" + whereClauseTaskSDtlAprvr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskSMstoneAprvr=" + whereClauseTaskSMstoneAprvr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaskSNxt=" + whereClauseTaskSNxt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taskSetID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "taskSetID=" + taskSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDWAddlParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDWAddlParams
   Description: Returns a DataSet given the primary key.  Contains additional parameter
considerations for the data returned.
   OperationID: GetByIDWAddlParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDWAddlParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDWAddlParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskApprovalsTreeFormattedString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskApprovalsTreeFormattedString
   Description: Return approvals task tree as string
   OperationID: GetTaskApprovalsTreeFormattedString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskApprovalsTreeFormattedString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskApprovalsTreeFormattedString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaskSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaskSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaskSMilestone(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaskSMilestone
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSMilestone
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskSMilestone_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSMilestone_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaskSDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaskSDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskSDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaskSNxt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaskSNxt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskSNxt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskSNxt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskSNxt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TEApprovalTaskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlAprvrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSDtlAprvrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMilestoneRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSMilestoneRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSMstoneAprvrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSMstoneAprvrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSNxtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSNxtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaskSetRow] = obj["value"]
      pass

class Erp_Tablesets_TaskSDtlAprvrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID).  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Unique identifier that determines the sequence of this task in the task set.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the related task master record (TaskMast.TaskID).  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Description of the task.  """  
      self.Milestone:bool = obj["Milestone"]
      """  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  """  
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      """  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  """  
      self.WinAllowed:bool = obj["WinAllowed"]
      """  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  """  
      self.LoseAllowed:bool = obj["LoseAllowed"]
      """  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  """  
      self.DaysToComplete:int = obj["DaysToComplete"]
      """  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      """  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  """  
      self.CompletionAction:str = obj["CompletionAction"]
      """   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  """  
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.SubmitTask:bool = obj["SubmitTask"]
      """  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StageDescription:str = obj["StageDescription"]
      self.FirstMilestone:bool = obj["FirstMilestone"]
      self.ParentTaskDescription:str = obj["ParentTaskDescription"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.TaskAnyApprover:bool = obj["TaskAnyApprover"]
      self.TETaskType:bool = obj["TETaskType"]
      """  Flag to tell us whether the associated TaskID has a TaskType that is Time and Expense.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaskIDTaskDescription:str = obj["TaskIDTaskDescription"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSMilestoneRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID).  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Unique identifier that determines the sequence of this task in the task set.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the related task master record (TaskMast.TaskID).  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Description of the task.  """  
      self.Milestone:bool = obj["Milestone"]
      """  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  """  
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      """  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  """  
      self.WinAllowed:bool = obj["WinAllowed"]
      """  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  """  
      self.LoseAllowed:bool = obj["LoseAllowed"]
      """  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  """  
      self.DaysToComplete:int = obj["DaysToComplete"]
      """  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      """  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  """  
      self.StageDescription:str = obj["StageDescription"]
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.SubmitTask:bool = obj["SubmitTask"]
      """  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  """  
      self.FirstMilestone:bool = obj["FirstMilestone"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.TaskAnyApprover:bool = obj["TaskAnyApprover"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSMstoneAprvrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSNxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID) record.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  The TaskSDtl.TaskSetSeq value of the milestone for which you are defining a next milestone.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  The TaskSDtl.TaskSetSeq value of the next milestone.  """  
      self.DefaultNext:bool = obj["DefaultNext"]
      """  If this next milestone is marked as the default (TaskSNxt.DefaultNext = True) then it will by default be the next milestone.  However, another milestone set up in the TaskSNxt table could be manually selected based on the outcome of the current milestone.  """  
      self.DefaultNextForReject:bool = obj["DefaultNextForReject"]
      """  Indicates if this is the default next milestone when a time or expense is rejected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.StageDescription:str = obj["StageDescription"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.WinAllowed:bool = obj["WinAllowed"]
      self.LoseAllowed:bool = obj["LoseAllowed"]
      self.DefaultRejectAllowed:bool = obj["DefaultRejectAllowed"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetSeqTaskDescription:str = obj["TaskSetSeqTaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.TaskSetDescription:str = obj["TaskSetDescription"]
      """  Description of the task set.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  The DCDUserID of the person that created this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeUserID:str = obj["ChangeUserID"]
      """  The DCDUserID of the person that last changed the record.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this task set can be used for new quotes or eco groups.  """  
      self.FirstTaskSeq:int = obj["FirstTaskSeq"]
      """  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTESubmitTask:bool = obj["HasTESubmitTask"]
      """  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  W  """  
      self.WFDescription:str = obj["WFDescription"]
      """  Workflow type description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.TaskSetDescription:str = obj["TaskSetDescription"]
      """  Description of the task set.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  The DCDUserID of the person that created this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeUserID:str = obj["ChangeUserID"]
      """  The DCDUserID of the person that last changed the record.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this task set can be used for new quotes or eco groups.  """  
      self.FirstTaskSeq:int = obj["FirstTaskSeq"]
      """  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTESubmitTask:bool = obj["HasTESubmitTask"]
      """  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  W  """  
      self.WFDescription:str = obj["WFDescription"]
      """  Workflow type description.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   taskSetID
   """  
   def __init__(self, obj):
      self.taskSetID:str = obj["taskSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TEApprovalTaskTableset:
   def __init__(self, obj):
      self.TaskSet:list[Erp_Tablesets_TaskSetRow] = obj["TaskSet"]
      self.TaskSMilestone:list[Erp_Tablesets_TaskSMilestoneRow] = obj["TaskSMilestone"]
      self.TaskSDtl:list[Erp_Tablesets_TaskSDtlRow] = obj["TaskSDtl"]
      self.TaskSDtlAprvr:list[Erp_Tablesets_TaskSDtlAprvrRow] = obj["TaskSDtlAprvr"]
      self.TaskSMstoneAprvr:list[Erp_Tablesets_TaskSMstoneAprvrRow] = obj["TaskSMstoneAprvr"]
      self.TaskSNxt:list[Erp_Tablesets_TaskSNxtRow] = obj["TaskSNxt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaskSDtlAprvrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID).  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Unique identifier that determines the sequence of this task in the task set.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the related task master record (TaskMast.TaskID).  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Description of the task.  """  
      self.Milestone:bool = obj["Milestone"]
      """  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  """  
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      """  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  """  
      self.WinAllowed:bool = obj["WinAllowed"]
      """  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  """  
      self.LoseAllowed:bool = obj["LoseAllowed"]
      """  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  """  
      self.DaysToComplete:int = obj["DaysToComplete"]
      """  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      """  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  """  
      self.CompletionAction:str = obj["CompletionAction"]
      """   The action to take when the task is completed.  Applies to milestones only.  Used for time and expense tasks.  Values are:
SUB - Submit.  The time or expense record status is set to submitted when the milestone is complete.
APP - Approve.  The time or expense record is approved when the milestone is complete.  """  
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.SubmitTask:bool = obj["SubmitTask"]
      """  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StageDescription:str = obj["StageDescription"]
      self.FirstMilestone:bool = obj["FirstMilestone"]
      self.ParentTaskDescription:str = obj["ParentTaskDescription"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.TaskAnyApprover:bool = obj["TaskAnyApprover"]
      self.TETaskType:bool = obj["TETaskType"]
      """  Flag to tell us whether the associated TaskID has a TaskType that is Time and Expense.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaskIDTaskDescription:str = obj["TaskIDTaskDescription"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSMilestoneRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID).  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Unique identifier that determines the sequence of this task in the task set.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the related task master record (TaskMast.TaskID).  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Description of the task.  """  
      self.Milestone:bool = obj["Milestone"]
      """  A task that is marked as a Milestone must be completed before the Next Milestone or the Next Milestone's related tasks can be completed.  Only one Milestone task can be active at any point in time.  """  
      self.ParentTaskSeq:int = obj["ParentTaskSeq"]
      """  Used to group non-milestone tasks to a parent milestone task.  When the next milestone task is creates the milestone and all its children will be created and available for completing.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """  This field only applies to milestone tasks.  Determines what stage or state the related quote or ECO group is in while this milestone is active.  """  
      self.WinAllowed:bool = obj["WinAllowed"]
      """  This field only applies to milestone tasks for Opportunities and Quotes. When completing this task the win function will be allowed. Only  """  
      self.LoseAllowed:bool = obj["LoseAllowed"]
      """  This field only applies to milestone tasks for opportunities and quotes. When completing this task the Lose function will be allowed.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the task set can move to the next milestone. If a Milestone task has mandatory related tasks, the milestone cannot be completed until the mandatory related tasks are completed.  """  
      self.DaysToComplete:int = obj["DaysToComplete"]
      """  The number of days this task normally takes to complete. This is used to determine when one task can end and the next task can begin.  For example, when a task is assigned the Task.DueDate is calculated as the Task.StartDate plus the TaskSDtl.DaysToComplete.  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  This field only applies to milestone tasks for ECO groups.  Determines whether or not revisions can be checked in when this milestone is active.  """  
      self.WFCompleteAllowed:bool = obj["WFCompleteAllowed"]
      """  This applies only to milestone tasks for ECO groups.  If set to true, then the milestone can be completed without requiring a next milestone which essentially completes the task set.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCd.RoleCode of person who would normally be assigned this task when it is created.  """  
      self.StageDescription:str = obj["StageDescription"]
      self.AutoComplete:bool = obj["AutoComplete"]
      """  Applies to milestones.  Auto complete the milestone when the related tasks are completed.  """  
      self.SubmitTask:bool = obj["SubmitTask"]
      """  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  """  
      self.FirstMilestone:bool = obj["FirstMilestone"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.TaskAnyApprover:bool = obj["TaskAnyApprover"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSMstoneAprvrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TaskSetID:str = obj["TaskSetID"]
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSNxtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the related task set (TaskSet.TaskSetID) record.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  The TaskSDtl.TaskSetSeq value of the milestone for which you are defining a next milestone.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  The TaskSDtl.TaskSetSeq value of the next milestone.  """  
      self.DefaultNext:bool = obj["DefaultNext"]
      """  If this next milestone is marked as the default (TaskSNxt.DefaultNext = True) then it will by default be the next milestone.  However, another milestone set up in the TaskSNxt table could be manually selected based on the outcome of the current milestone.  """  
      self.DefaultNextForReject:bool = obj["DefaultNextForReject"]
      """  Indicates if this is the default next milestone when a time or expense is rejected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.StageDescription:str = obj["StageDescription"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.WinAllowed:bool = obj["WinAllowed"]
      self.LoseAllowed:bool = obj["LoseAllowed"]
      self.DefaultRejectAllowed:bool = obj["DefaultRejectAllowed"]
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetSeqTaskDescription:str = obj["TaskSetSeqTaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.TaskSetDescription:str = obj["TaskSetDescription"]
      """  Description of the task set.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  The DCDUserID of the person that created this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeUserID:str = obj["ChangeUserID"]
      """  The DCDUserID of the person that last changed the record.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this task set can be used for new quotes or eco groups.  """  
      self.FirstTaskSeq:int = obj["FirstTaskSeq"]
      """  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTESubmitTask:bool = obj["HasTESubmitTask"]
      """  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  W  """  
      self.WFDescription:str = obj["WFDescription"]
      """  Workflow type description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskSetListTableset:
   def __init__(self, obj):
      self.TaskSetList:list[Erp_Tablesets_TaskSetListRow] = obj["TaskSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaskSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.TaskSetDescription:str = obj["TaskSetDescription"]
      """  Description of the task set.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  The DCDUserID of the person that created this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeUserID:str = obj["ChangeUserID"]
      """  The DCDUserID of the person that last changed the record.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this task set can be used for new quotes or eco groups.  """  
      self.FirstTaskSeq:int = obj["FirstTaskSeq"]
      """  Identifies the first Milestone task for the task set. The first milestone will be considered as the Active Milestone when a task set is assigned.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.ECOCheckOutAllowed:bool = obj["ECOCheckOutAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckOutAllowed is set to this value.  """  
      self.ECOCheckInAllowed:bool = obj["ECOCheckInAllowed"]
      """  When a TaskSet is initially added to an ECOGroup the ECOGroup CheckInAllowed is set to this value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTESubmitTask:bool = obj["HasTESubmitTask"]
      """  Indicates if the task set contains a submit milestone task.  Used by the UI in rowrules to determine if First Milestone for milestones is enabled or not.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  W  """  
      self.WFDescription:str = obj["WFDescription"]
      """  Workflow type description.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtTEApprovalTaskTableset:
   def __init__(self, obj):
      self.TaskSet:list[Erp_Tablesets_TaskSetRow] = obj["TaskSet"]
      self.TaskSMilestone:list[Erp_Tablesets_TaskSMilestoneRow] = obj["TaskSMilestone"]
      self.TaskSDtl:list[Erp_Tablesets_TaskSDtlRow] = obj["TaskSDtl"]
      self.TaskSDtlAprvr:list[Erp_Tablesets_TaskSDtlAprvrRow] = obj["TaskSDtlAprvr"]
      self.TaskSMstoneAprvr:list[Erp_Tablesets_TaskSMstoneAprvrRow] = obj["TaskSMstoneAprvr"]
      self.TaskSNxt:list[Erp_Tablesets_TaskSNxtRow] = obj["TaskSNxt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDWAddlParams_input:
   """ Required : 
   inWFGroupID
   inEmpID
   inProjectID
   """  
   def __init__(self, obj):
      self.inWFGroupID:str = obj["inWFGroupID"]
      self.inEmpID:str = obj["inEmpID"]
      self.inProjectID:str = obj["inProjectID"]
      pass

class GetByIDWAddlParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   taskSetID
   """  
   def __init__(self, obj):
      self.taskSetID:str = obj["taskSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaskSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaskSDtl_input:
   """ Required : 
   ds
   taskSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      self.taskSetID:str = obj["taskSetID"]
      pass

class GetNewTaskSDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaskSMilestone_input:
   """ Required : 
   ds
   taskSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      self.taskSetID:str = obj["taskSetID"]
      pass

class GetNewTaskSMilestone_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaskSNxt_input:
   """ Required : 
   ds
   taskSetID
   taskSetSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      self.taskSetID:str = obj["taskSetID"]
      self.taskSetSeq:int = obj["taskSetSeq"]
      pass

class GetNewTaskSNxt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaskSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

class GetNewTaskSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaskSet
   whereClauseTaskSMilestone
   whereClauseTaskSDtl
   whereClauseTaskSDtlAprvr
   whereClauseTaskSMstoneAprvr
   whereClauseTaskSNxt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaskSet:str = obj["whereClauseTaskSet"]
      self.whereClauseTaskSMilestone:str = obj["whereClauseTaskSMilestone"]
      self.whereClauseTaskSDtl:str = obj["whereClauseTaskSDtl"]
      self.whereClauseTaskSDtlAprvr:str = obj["whereClauseTaskSDtlAprvr"]
      self.whereClauseTaskSMstoneAprvr:str = obj["whereClauseTaskSMstoneAprvr"]
      self.whereClauseTaskSNxt:str = obj["whereClauseTaskSNxt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaskApprovalsTreeFormattedString_input:
   """ Required : 
   inWFGroupID
   inEmpID
   inProjectID
   """  
   def __init__(self, obj):
      self.inWFGroupID:str = obj["inWFGroupID"]
      self.inEmpID:str = obj["inEmpID"]
      self.inProjectID:str = obj["inProjectID"]
      pass

class GetTaskApprovalsTreeFormattedString_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTEApprovalTaskTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTEApprovalTaskTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TEApprovalTaskTableset] = obj["ds"]
      pass

      """  output parameters  """  

