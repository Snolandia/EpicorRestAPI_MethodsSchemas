import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysAgentSvc
# Description: SysAgent main object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysAgents(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysAgents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgents
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents",headers=creds) as resp:
           return await resp.json()

async def post_SysAgents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysAgents_AgentID(AgentID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgent item
   Description: Calls GetByID to retrieve the SysAgent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgent
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysAgents_AgentID(AgentID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysAgent for the service
   Description: Calls UpdateExt to update SysAgent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgent
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysAgents_AgentID(AgentID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysAgent item
   Description: Call UpdateExt to delete SysAgent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgent
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgents_AgentID_SysAgentScheds(AgentID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysAgentScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentScheds1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")/SysAgentScheds",headers=creds) as resp:
           return await resp.json()

async def get_SysAgents_AgentID_SysAgentScheds_AgentID_AgentSchedNum(AgentID, AgentSchedNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentSched item
   Description: Calls GetByID to retrieve the SysAgentSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentSched1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgents(" + AgentID + ")/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentScheds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysAgentScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentScheds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds",headers=creds) as resp:
           return await resp.json()

async def post_SysAgentScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysAgentScheds_AgentID_AgentSchedNum(AgentID, AgentSchedNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentSched item
   Description: Calls GetByID to retrieve the SysAgentSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentSched
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysAgentScheds_AgentID_AgentSchedNum(AgentID, AgentSchedNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysAgentSched for the service
   Description: Calls UpdateExt to update SysAgentSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentSched
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysAgentScheds_AgentID_AgentSchedNum(AgentID, AgentSchedNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysAgentSched item
   Description: Call UpdateExt to delete SysAgentSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentSched
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentScheds_AgentID_AgentSchedNum_SysAgentTasks(AgentID, AgentSchedNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysAgentTasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentTasks1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")/SysAgentTasks",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentScheds_AgentID_AgentSchedNum_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID, AgentSchedNum, AgentTaskNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentTask item
   Description: Calls GetByID to retrieve the SysAgentTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTask1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentScheds(" + AgentID + "," + AgentSchedNum + ")/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysAgentTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentTasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks",headers=creds) as resp:
           return await resp.json()

async def post_SysAgentTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID, AgentSchedNum, AgentTaskNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentTask item
   Description: Calls GetByID to retrieve the SysAgentTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTask
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID, AgentSchedNum, AgentTaskNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysAgentTask for the service
   Description: Calls UpdateExt to update SysAgentTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentTask
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum(AgentID, AgentSchedNum, AgentTaskNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysAgentTask item
   Description: Call UpdateExt to delete SysAgentTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentTask
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum_SysAgentTaskParams(AgentID, AgentSchedNum, AgentTaskNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysAgentTaskParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysAgentTaskParams1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")/SysAgentTaskParams",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTasks_AgentID_AgentSchedNum_AgentTaskNum_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID, AgentSchedNum, AgentTaskNum, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentTaskParam item
   Description: Calls GetByID to retrieve the SysAgentTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTaskParam1
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTasks(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + ")/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTaskParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysAgentTaskParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysAgentTaskParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams",headers=creds) as resp:
           return await resp.json()

async def post_SysAgentTaskParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysAgentTaskParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID, AgentSchedNum, AgentTaskNum, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysAgentTaskParam item
   Description: Calls GetByID to retrieve the SysAgentTaskParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysAgentTaskParam
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID, AgentSchedNum, AgentTaskNum, ParamName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysAgentTaskParam for the service
   Description: Calls UpdateExt to update SysAgentTaskParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysAgentTaskParam
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysAgentTaskParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysAgentTaskParams_AgentID_AgentSchedNum_AgentTaskNum_ParamName(AgentID, AgentSchedNum, AgentTaskNum, ParamName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysAgentTaskParam item
   Description: Call UpdateExt to delete SysAgentTaskParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysAgentTaskParam
      :param AgentID: Desc: AgentID   Required: True   Allow empty value : True
      :param AgentSchedNum: Desc: AgentSchedNum   Required: True   Allow empty value : True
      :param AgentTaskNum: Desc: AgentTaskNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/SysAgentTaskParams(" + AgentID + "," + AgentSchedNum + "," + AgentTaskNum + "," + ParamName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysAgentListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysAgent, whereClauseSysAgentSched, whereClauseSysAgentTask, whereClauseSysAgentTaskParam, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseSysAgent=" + whereClauseSysAgent
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysAgentSched=" + whereClauseSysAgentSched
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysAgentTask=" + whereClauseSysAgentTask
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysAgentTaskParam=" + whereClauseSysAgentTaskParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(agentID, epicorHeaders = None):
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
   params += "agentID=" + agentID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_SetSysAgentStatusToStarted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSysAgentStatusToStarted
   Description: Sets the given SysAgent to a status of started. Also sets the NextRunOn date of any of the agent's schedules with a type of 'Startup'.
   OperationID: SetSysAgentStatusToStarted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysAgentStatusToStarted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysAgentStatusToStarted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSysAgentStatusToStopped(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSysAgentStatusToStopped
   Description: Sets the system agent status to stopped.
   OperationID: SetSysAgentStatusToStopped
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSysAgentStatusToStopped_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSysAgentStatusToStopped_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIdForTaskAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIdForTaskAgent
   Description: Gets the SysAgent record and its associated schedules for use by the task agent.
   OperationID: GetByIdForTaskAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIdForTaskAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIdForTaskAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetScheduleProcessingStartedOn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetScheduleProcessingStartedOn
   Description: Deletes the SysAgentSchedProcessing record for the given schedule.
   OperationID: ResetScheduleProcessingStartedOn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetScheduleProcessingStartedOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetScheduleProcessingStartedOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PurgeTaskHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PurgeTaskHistory
   Description: Purges the SysTask rows that have History set to true and are older than our purge date.
   OperationID: PurgeTaskHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PurgeTaskHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PurgeTaskHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PurgeReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PurgeReports
   Description: Purges reports and their associated data that are older than the specified purge date.
   OperationID: PurgeReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PurgeReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PurgeReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAgentSchedList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAgentSchedList
   Description: To return a dataset of SysAgentSched records for a given agent id.
   OperationID: GetAgentSchedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAgentSchedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgentSchedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSchedListForDefaultAgent(epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedListForDefaultAgent
   Description: Get list of schedules for default agent.
   OperationID: GetSchedListForDefaultAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedListForDefaultAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultTaskAgentID(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultTaskAgentID
   Description: Returns the default Task Agent ID.
   OperationID: GetDefaultTaskAgentID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTaskAgentID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultTaskAgent(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultTaskAgent
   Description: Gets the default task agent.  If no SysAgent record exists will return an empty tableset.
   OperationID: GetDefaultTaskAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTaskAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RetryTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetryTask
   Description: Queues a task to be reran at configured intervals set up to the maximum amount of allowed attempts.
   OperationID: RetryTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetryTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetryTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysAgent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysAgentSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysAgentSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysAgentTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysAgentTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysAgentTaskParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysAgentTaskParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysAgentTaskParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysAgentTaskParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysAgentTaskParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysAgentListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysAgentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysAgentSchedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysAgentTaskParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysAgentTaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysAgentTaskRow] = obj["value"]
      pass

class Ice_Tablesets_SysAgentListRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentDesc:str = obj["AgentDesc"]
      """  System Agent Description  """  
      self.AgentStatus:str = obj["AgentStatus"]
      """  System Agent Status  """  
      self.Started:bool = obj["Started"]
      """  System Agent started  """  
      self.StartUser:str = obj["StartUser"]
      """  System Agent started by user  """  
      self.AutoStart:bool = obj["AutoStart"]
      """  Autostart System Agent  """  
      self.ProcessingDelay:int = obj["ProcessingDelay"]
      """  The delay between the time the agent is started and the time its schedules are processed  """  
      self.FileRootDir:str = obj["FileRootDir"]
      """   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  """  
      self.MaxSimultaneousTasks:int = obj["MaxSimultaneousTasks"]
      """  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DTStartTime:str = obj["DTStartTime"]
      self.ClientFileRootDir:str = obj["ClientFileRootDir"]
      self.ServerFileRootDir:str = obj["ServerFileRootDir"]
      self.ClientProgRootDir:str = obj["ClientProgRootDir"]
      self.ODBCPasswordPatchFld:str = obj["ODBCPasswordPatchFld"]
      """  Password to be used for ODBC connections  """  
      self.ODBCUserIDPatchFld:str = obj["ODBCUserIDPatchFld"]
      """  User ID to use for ODBC Connenctions (not a MfgSys user)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentDesc:str = obj["AgentDesc"]
      """  System Agent Description  """  
      self.AgentStatus:str = obj["AgentStatus"]
      """  System Agent Status  """  
      self.Started:bool = obj["Started"]
      """  System Agent started  """  
      self.StartedOn:str = obj["StartedOn"]
      """  StartedOn  """  
      self.StartUser:str = obj["StartUser"]
      """  System Agent started by user  """  
      self.AutoStart:bool = obj["AutoStart"]
      """  Autostart System Agent  """  
      self.ProcessingDelay:int = obj["ProcessingDelay"]
      """  The delay between the time the agent is started and the time its schedules are processed  """  
      self.SysUserID:str = obj["SysUserID"]
      """  SysUserID  """  
      self.SysPassWord:str = obj["SysPassWord"]
      """  SysPassWord  """  
      self.FileRootDir:str = obj["FileRootDir"]
      """   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  """  
      self.MaxSimultaneousTasks:int = obj["MaxSimultaneousTasks"]
      """  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.TaskPurgeIntervalDays:int = obj["TaskPurgeIntervalDays"]
      """  TaskPurgeIntervalDays  """  
      self.ReportPurgeIntervalTime:int = obj["ReportPurgeIntervalTime"]
      """  ReportPurgeIntervalTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysAppserverURL:str = obj["SysAppserverURL"]
      """  SysAppserverURL  """  
      self.SysDNSEndpointIdentity:str = obj["SysDNSEndpointIdentity"]
      """  SysDNSEndpointIdentity  """  
      self.ClientProgRootDir:str = obj["ClientProgRootDir"]
      self.DTStartTime:str = obj["DTStartTime"]
      self.ServerFileRootDir:str = obj["ServerFileRootDir"]
      self.SysPasswordMasked:str = obj["SysPasswordMasked"]
      """  Masked password field.  """  
      self.ClientFileRootDir:str = obj["ClientFileRootDir"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentSchedRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.SchedDesc:str = obj["SchedDesc"]
      """  Schedule Description  """  
      self.SchedType:str = obj["SchedType"]
      """  Once, Daily, Weekly, Monthly, Interval or Startup  """  
      self.NextRunOn:str = obj["NextRunOn"]
      """  NextRunOn  """  
      self.Recurrences:int = obj["Recurrences"]
      """  Recurrencies  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The task Agent will not run a task which has an effective date > the current date.  """  
      self.MonthlyOption:str = obj["MonthlyOption"]
      """  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  """  
      self.DayOfMonth:int = obj["DayOfMonth"]
      """  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  """  
      self.WeekOfMonth:str = obj["WeekOfMonth"]
      """  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  """  
      self.DayOfWeek:int = obj["DayOfWeek"]
      """  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  """  
      self.EveryNWeeks:int = obj["EveryNWeeks"]
      """  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.Mondays:bool = obj["Mondays"]
      """   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  """  
      self.Tuesdays:bool = obj["Tuesdays"]
      """   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  """  
      self.Wednesdays:bool = obj["Wednesdays"]
      """   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  """  
      self.Thursdays:bool = obj["Thursdays"]
      """   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  """  
      self.Fridays:bool = obj["Fridays"]
      """   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  """  
      self.Saturdays:bool = obj["Saturdays"]
      """   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  """  
      self.Sundays:bool = obj["Sundays"]
      """   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enable flag  """  
      self.AppSrvConnectionID:str = obj["AppSrvConnectionID"]
      """   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  """  
      self.IntervalTime:int = obj["IntervalTime"]
      """  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessingStartedOn:str = obj["ProcessingStartedOn"]
      """  ProcessingStartedOn  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.DayOfWeekWeekly:int = obj["DayOfWeekWeekly"]
      """  External field for Weekly Panel. Stores same value as DayOfWeek.  """  
      self.IntervalTimeHours:int = obj["IntervalTimeHours"]
      """  The interval of time (expressed as hhh) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.IntervalTimeMinutes:int = obj["IntervalTimeMinutes"]
      """  The minutes portion of the interval of time (expressed as mm) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.IntervalTimeSeconds:int = obj["IntervalTimeSeconds"]
      """  The seconds portion of the interval of time (expressed as ss) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.NextRunOnInTimeZone:str = obj["NextRunOnInTimeZone"]
      """  The next run on value in the schedules time zone.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentTaskParamRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  System Agent Task Number  """  
      self.ParamName:str = obj["ParamName"]
      """  Parameter Name  """  
      self.ParamLabel:str = obj["ParamLabel"]
      """  Parameter Label  """  
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
      """   Tokens are predefined values used to dynamically determine a value of a corresponding parameter.
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

class Ice_Tablesets_SysAgentTaskRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  System Agent Task Number  """  
      self.TaskDesc:str = obj["TaskDesc"]
      """  System Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """  Valid Values:  Process, Report  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.RunMethod:str = obj["RunMethod"]
      """  Method (internal procedure) of the "RunProcedure" that this task will perform.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  SubmittedOn  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  Submitted by user  """  
      self.ParamMaintProgram:str = obj["ParamMaintProgram"]
      """   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  """  
      self.Company:str = obj["Company"]
      """  Current Company when the task was created.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.ProcessSetSystemCode:str = obj["ProcessSetSystemCode"]
      """  ProcessSetSystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.ProcessTaskNum:int = obj["ProcessTaskNum"]
      """  ProcessTask.SysTaskNum that originated the schedule  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessSetCompany:str = obj["ProcessSetCompany"]
      """  ProcessSetCompany  """  
      self.NextRunOn:str = obj["NextRunOn"]
      """  Next Run on  """  
      self.SchedDesc:str = obj["SchedDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   agentID
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetAgentSchedList_input:
   """ Required : 
   agentID
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      """  Agent ID which you want the schedules for.  """  
      pass

class GetAgentSchedList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentSchedListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   agentID
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
      pass

class GetByIdForTaskAgent_input:
   """ Required : 
   agentID
   firstPass
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      """  The agent identifier.  """  
      self.firstPass:bool = obj["firstPass"]
      """  Indicates if startup type schedules should be included.  """  
      pass

class GetByIdForTaskAgent_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
      pass

class GetDefaultTaskAgentID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultAgentID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultTaskAgent_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysAgentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysAgentSched_input:
   """ Required : 
   ds
   agentID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      self.agentID:str = obj["agentID"]
      pass

class GetNewSysAgentSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysAgentTaskParam_input:
   """ Required : 
   ds
   agentID
   agentSchedNum
   agentTaskNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      self.agentID:str = obj["agentID"]
      self.agentSchedNum:int = obj["agentSchedNum"]
      self.agentTaskNum:int = obj["agentTaskNum"]
      pass

class GetNewSysAgentTaskParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysAgentTask_input:
   """ Required : 
   ds
   agentID
   agentSchedNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      self.agentID:str = obj["agentID"]
      self.agentSchedNum:int = obj["agentSchedNum"]
      pass

class GetNewSysAgentTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysAgent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

class GetNewSysAgent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysAgent
   whereClauseSysAgentSched
   whereClauseSysAgentTask
   whereClauseSysAgentTaskParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysAgent:str = obj["whereClauseSysAgent"]
      self.whereClauseSysAgentSched:str = obj["whereClauseSysAgentSched"]
      self.whereClauseSysAgentTask:str = obj["whereClauseSysAgentTask"]
      self.whereClauseSysAgentTaskParam:str = obj["whereClauseSysAgentTaskParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSchedListForDefaultAgent_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysAgentSchedListTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysAgentListRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentDesc:str = obj["AgentDesc"]
      """  System Agent Description  """  
      self.AgentStatus:str = obj["AgentStatus"]
      """  System Agent Status  """  
      self.Started:bool = obj["Started"]
      """  System Agent started  """  
      self.StartUser:str = obj["StartUser"]
      """  System Agent started by user  """  
      self.AutoStart:bool = obj["AutoStart"]
      """  Autostart System Agent  """  
      self.ProcessingDelay:int = obj["ProcessingDelay"]
      """  The delay between the time the agent is started and the time its schedules are processed  """  
      self.FileRootDir:str = obj["FileRootDir"]
      """   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  """  
      self.MaxSimultaneousTasks:int = obj["MaxSimultaneousTasks"]
      """  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DTStartTime:str = obj["DTStartTime"]
      self.ClientFileRootDir:str = obj["ClientFileRootDir"]
      self.ServerFileRootDir:str = obj["ServerFileRootDir"]
      self.ClientProgRootDir:str = obj["ClientProgRootDir"]
      self.ODBCPasswordPatchFld:str = obj["ODBCPasswordPatchFld"]
      """  Password to be used for ODBC connections  """  
      self.ODBCUserIDPatchFld:str = obj["ODBCUserIDPatchFld"]
      """  User ID to use for ODBC Connenctions (not a MfgSys user)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentListTableset:
   def __init__(self, obj):
      self.SysAgentList:list[Ice_Tablesets_SysAgentListRow] = obj["SysAgentList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysAgentRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentDesc:str = obj["AgentDesc"]
      """  System Agent Description  """  
      self.AgentStatus:str = obj["AgentStatus"]
      """  System Agent Status  """  
      self.Started:bool = obj["Started"]
      """  System Agent started  """  
      self.StartedOn:str = obj["StartedOn"]
      """  StartedOn  """  
      self.StartUser:str = obj["StartUser"]
      """  System Agent started by user  """  
      self.AutoStart:bool = obj["AutoStart"]
      """  Autostart System Agent  """  
      self.ProcessingDelay:int = obj["ProcessingDelay"]
      """  The delay between the time the agent is started and the time its schedules are processed  """  
      self.SysUserID:str = obj["SysUserID"]
      """  SysUserID  """  
      self.SysPassWord:str = obj["SysPassWord"]
      """  SysPassWord  """  
      self.FileRootDir:str = obj["FileRootDir"]
      """   Defines the root directory to user for files created by tasks run by this agent. This should be a shared directory, normally on the same machine as where the appserver is running. It should also be entered using UNC convention.
ex: \\mnsonoma\mfgsysdata  """  
      self.MaxSimultaneousTasks:int = obj["MaxSimultaneousTasks"]
      """  The Maximum number of Simultaneous Tasks that the System Agent should submit to the Main AppServer.  Used to keep the System Agent from overloading the Main AppServer with reports and processes when the maximum number of agents is known.  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.TaskPurgeIntervalDays:int = obj["TaskPurgeIntervalDays"]
      """  TaskPurgeIntervalDays  """  
      self.ReportPurgeIntervalTime:int = obj["ReportPurgeIntervalTime"]
      """  ReportPurgeIntervalTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysAppserverURL:str = obj["SysAppserverURL"]
      """  SysAppserverURL  """  
      self.SysDNSEndpointIdentity:str = obj["SysDNSEndpointIdentity"]
      """  SysDNSEndpointIdentity  """  
      self.ClientProgRootDir:str = obj["ClientProgRootDir"]
      self.DTStartTime:str = obj["DTStartTime"]
      self.ServerFileRootDir:str = obj["ServerFileRootDir"]
      self.SysPasswordMasked:str = obj["SysPasswordMasked"]
      """  Masked password field.  """  
      self.ClientFileRootDir:str = obj["ClientFileRootDir"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentSchedListRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.SchedDesc:str = obj["SchedDesc"]
      """  Schedule Description  """  
      self.SchedType:str = obj["SchedType"]
      """  Once, Daily, Weekly, Monthly, Interval or Startup  """  
      self.Recurrences:int = obj["Recurrences"]
      """  Recurrencies  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The task Agent will not run a task which has an effective date > the current date.  """  
      self.MonthlyOption:str = obj["MonthlyOption"]
      """  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  """  
      self.DayOfMonth:int = obj["DayOfMonth"]
      """  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  """  
      self.WeekOfMonth:str = obj["WeekOfMonth"]
      """  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  """  
      self.DayOfWeek:int = obj["DayOfWeek"]
      """  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  """  
      self.EveryNWeeks:int = obj["EveryNWeeks"]
      """  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  """  
      self.Mondays:bool = obj["Mondays"]
      """   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  """  
      self.Tuesdays:bool = obj["Tuesdays"]
      """   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  """  
      self.Wednesdays:bool = obj["Wednesdays"]
      """   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  """  
      self.Thursdays:bool = obj["Thursdays"]
      """   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  """  
      self.Fridays:bool = obj["Fridays"]
      """   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  """  
      self.Saturdays:bool = obj["Saturdays"]
      """   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  """  
      self.Sundays:bool = obj["Sundays"]
      """   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enable flag  """  
      self.AppSrvConnectionID:str = obj["AppSrvConnectionID"]
      """   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  """  
      self.IntervalTime:int = obj["IntervalTime"]
      """  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DTNextRunTime:str = obj["DTNextRunTime"]
      self.DTLastRunTime:str = obj["DTLastRunTime"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentSchedListTableset:
   def __init__(self, obj):
      self.SysAgentSchedList:list[Ice_Tablesets_SysAgentSchedListRow] = obj["SysAgentSchedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysAgentSchedRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.SchedDesc:str = obj["SchedDesc"]
      """  Schedule Description  """  
      self.SchedType:str = obj["SchedType"]
      """  Once, Daily, Weekly, Monthly, Interval or Startup  """  
      self.NextRunOn:str = obj["NextRunOn"]
      """  NextRunOn  """  
      self.Recurrences:int = obj["Recurrences"]
      """  Recurrencies  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The task Agent will not run a task which has an effective date > the current date.  """  
      self.MonthlyOption:str = obj["MonthlyOption"]
      """  Used for montly schedules indicating a if they want to  schedule for a specific day of the month or by a specific week day withing a specific week of a month. Valid values are "Day, Week"  """  
      self.DayOfMonth:int = obj["DayOfMonth"]
      """  Day of month that task is to be run. Pertains only to SchedType of Monthly. Values can be 1 - 31.  """  
      self.WeekOfMonth:str = obj["WeekOfMonth"]
      """  Qualifys the DayOfWeek for Monthly processes. Values can be; First, Second, Third, Fourth, Fifth, or Last.  """  
      self.DayOfWeek:int = obj["DayOfWeek"]
      """  Pertains only to Monthly schedules which are not defined as a specific day of the month or Weekly schedules. Represents the day of week ( 1 = Sun.... 7 = Sat) that the  process will run on. For Monthly schedules the WeekOfMonth value is also used to determine the actual run date.  """  
      self.EveryNWeeks:int = obj["EveryNWeeks"]
      """  For Weekly Schedules. Indicates that this should be run every n number of weeks. This along with DayOfWeek is used to determine the actual run date.  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.Mondays:bool = obj["Mondays"]
      """   Indicates if scheduled to run on Mondays.
Pertains only to SchedType = Daily.  """  
      self.Tuesdays:bool = obj["Tuesdays"]
      """   Indicates if scheduled to run on Tuesdays.
Pertains only to SchedType = Daily  """  
      self.Wednesdays:bool = obj["Wednesdays"]
      """   Indicates if scheduled to run on Wednesdays.
Pertains only to SchedType =  Daily.  """  
      self.Thursdays:bool = obj["Thursdays"]
      """   Indicates if scheduled to run on Thurdays.
Pertains only to SchedType = Daily.  """  
      self.Fridays:bool = obj["Fridays"]
      """   Indicates if scheduled to run on Fridays.
Pertains only to SchedType =Daily.  """  
      self.Saturdays:bool = obj["Saturdays"]
      """   Indicates if scheduled to run on Saturdays.
Pertains only to SchedType =  Daily  """  
      self.Sundays:bool = obj["Sundays"]
      """   Indicates if scheduled to run on Sundays.
Pertains only to SchedType = Daily  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enable flag  """  
      self.AppSrvConnectionID:str = obj["AppSrvConnectionID"]
      """   Progress AppServer ConnectionID that this task is using.
Format: appserver-host::appserver-name::global-unique-id  """  
      self.IntervalTime:int = obj["IntervalTime"]
      """  The interval of time (expressed as hhhmmss) that this schedule will be run. Example: Run Every 10 minutes would have a value of 0001000. Only pertains with SchedType = "Interval"  """  
      self.SecCode:str = obj["SecCode"]
      """  Menu Security Code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessingStartedOn:str = obj["ProcessingStartedOn"]
      """  ProcessingStartedOn  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.DayOfWeekWeekly:int = obj["DayOfWeekWeekly"]
      """  External field for Weekly Panel. Stores same value as DayOfWeek.  """  
      self.IntervalTimeHours:int = obj["IntervalTimeHours"]
      """  The interval of time (expressed as hhh) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.IntervalTimeMinutes:int = obj["IntervalTimeMinutes"]
      """  The minutes portion of the interval of time (expressed as mm) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.IntervalTimeSeconds:int = obj["IntervalTimeSeconds"]
      """  The seconds portion of the interval of time (expressed as ss) that this schedule will be run. Only pertains with SchedType = "Interval"  """  
      self.NextRunOnInTimeZone:str = obj["NextRunOnInTimeZone"]
      """  The next run on value in the schedules time zone.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysAgentTableset:
   def __init__(self, obj):
      self.SysAgent:list[Ice_Tablesets_SysAgentRow] = obj["SysAgent"]
      self.SysAgentSched:list[Ice_Tablesets_SysAgentSchedRow] = obj["SysAgentSched"]
      self.SysAgentTask:list[Ice_Tablesets_SysAgentTaskRow] = obj["SysAgentTask"]
      self.SysAgentTaskParam:list[Ice_Tablesets_SysAgentTaskParamRow] = obj["SysAgentTaskParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysAgentTaskParamRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  System Agent Task Number  """  
      self.ParamName:str = obj["ParamName"]
      """  Parameter Name  """  
      self.ParamLabel:str = obj["ParamLabel"]
      """  Parameter Label  """  
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
      """   Tokens are predefined values used to dynamically determine a value of a corresponding parameter.
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

class Ice_Tablesets_SysAgentTaskRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  System Agent Task Number  """  
      self.TaskDesc:str = obj["TaskDesc"]
      """  System Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """  Valid Values:  Process, Report  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.RunMethod:str = obj["RunMethod"]
      """  Method (internal procedure) of the "RunProcedure" that this task will perform.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  SubmittedOn  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  Submitted by user  """  
      self.ParamMaintProgram:str = obj["ParamMaintProgram"]
      """   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  """  
      self.Company:str = obj["Company"]
      """  Current Company when the task was created.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.ProcessSetSystemCode:str = obj["ProcessSetSystemCode"]
      """  ProcessSetSystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.ProcessTaskNum:int = obj["ProcessTaskNum"]
      """  ProcessTask.SysTaskNum that originated the schedule  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessSetCompany:str = obj["ProcessSetCompany"]
      """  ProcessSetCompany  """  
      self.NextRunOn:str = obj["NextRunOn"]
      """  Next Run on  """  
      self.SchedDesc:str = obj["SchedDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtSysAgentTableset:
   def __init__(self, obj):
      self.SysAgent:list[Ice_Tablesets_SysAgentRow] = obj["SysAgent"]
      self.SysAgentSched:list[Ice_Tablesets_SysAgentSchedRow] = obj["SysAgentSched"]
      self.SysAgentTask:list[Ice_Tablesets_SysAgentTaskRow] = obj["SysAgentTask"]
      self.SysAgentTaskParam:list[Ice_Tablesets_SysAgentTaskParamRow] = obj["SysAgentTaskParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class PurgeReports_input:
   """ Required : 
   purgeDate
   """  
   def __init__(self, obj):
      self.purgeDate:str = obj["purgeDate"]
      """  The purge date.  """  
      pass

class PurgeReports_output:
   def __init__(self, obj):
      pass

class PurgeTaskHistory_input:
   """ Required : 
   purgeDate
   """  
   def __init__(self, obj):
      self.purgeDate:str = obj["purgeDate"]
      """  The purge date.  """  
      pass

class PurgeTaskHistory_output:
   def __init__(self, obj):
      pass

class ResetScheduleProcessingStartedOn_input:
   """ Required : 
   agentId
   scheduleNum
   """  
   def __init__(self, obj):
      self.agentId:str = obj["agentId"]
      """  The agent identifier.  """  
      self.scheduleNum:int = obj["scheduleNum"]
      """  The schedule number.  """  
      pass

class ResetScheduleProcessingStartedOn_output:
   def __init__(self, obj):
      pass

class RetryTask_input:
   """ Required : 
   sysTaskNum
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class RetryTask_output:
   def __init__(self, obj):
      pass

class SetSysAgentStatusToStarted_input:
   """ Required : 
   agentId
   """  
   def __init__(self, obj):
      self.agentId:str = obj["agentId"]
      pass

class SetSysAgentStatusToStarted_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  False if the given Agent ID does not exist, otherwise true.  """  
      pass

class SetSysAgentStatusToStopped_input:
   """ Required : 
   AgentID
   killRunningTasks
   """  
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  The agent identifier.  """  
      self.killRunningTasks:bool = obj["killRunningTasks"]
      """  if set to `true` creates a SysTaskKill record for any running tasks.  """  
      pass

class SetSysAgentStatusToStopped_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysAgentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysAgentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

