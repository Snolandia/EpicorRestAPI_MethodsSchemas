import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WFGroupSvc
# Description: WFGroup Busness Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WFGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WFGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WFGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WFGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups",headers=creds) as resp:
           return await resp.json()

async def post_WFGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WFGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WFGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WFGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WFGroups_Company_WorkflowType_WFGroupID(Company, WorkflowType, WFGroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WFGroup item
   Description: Calls GetByID to retrieve the WFGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WFGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WFGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups(" + Company + "," + WorkflowType + "," + WFGroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WFGroups_Company_WorkflowType_WFGroupID(Company, WorkflowType, WFGroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WFGroup for the service
   Description: Calls UpdateExt to update WFGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WFGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WFGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups(" + Company + "," + WorkflowType + "," + WFGroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WFGroups_Company_WorkflowType_WFGroupID(Company, WorkflowType, WFGroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WFGroup item
   Description: Call UpdateExt to delete WFGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WFGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups(" + Company + "," + WorkflowType + "," + WFGroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WFGroups_Company_WorkflowType_WFGroupID_WFGrpMbrs(Company, WorkflowType, WFGroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WFGrpMbrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WFGrpMbrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WFGrpMbrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups(" + Company + "," + WorkflowType + "," + WFGroupID + ")/WFGrpMbrs",headers=creds) as resp:
           return await resp.json()

async def get_WFGroups_Company_WorkflowType_WFGroupID_WFGrpMbrs_Company_WorkflowType_WFGroupID_SalesRepCode(Company, WorkflowType, WFGroupID, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WFGrpMbr item
   Description: Calls GetByID to retrieve the WFGrpMbr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WFGrpMbr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WFGrpMbrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGroups(" + Company + "," + WorkflowType + "," + WFGroupID + ")/WFGrpMbrs(" + Company + "," + WorkflowType + "," + WFGroupID + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WFGrpMbrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WFGrpMbrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WFGrpMbrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WFGrpMbrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGrpMbrs",headers=creds) as resp:
           return await resp.json()

async def post_WFGrpMbrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WFGrpMbrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WFGrpMbrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WFGrpMbrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGrpMbrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WFGrpMbrs_Company_WorkflowType_WFGroupID_SalesRepCode(Company, WorkflowType, WFGroupID, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WFGrpMbr item
   Description: Calls GetByID to retrieve the WFGrpMbr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WFGrpMbr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WFGrpMbrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGrpMbrs(" + Company + "," + WorkflowType + "," + WFGroupID + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WFGrpMbrs_Company_WorkflowType_WFGroupID_SalesRepCode(Company, WorkflowType, WFGroupID, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WFGrpMbr for the service
   Description: Calls UpdateExt to update WFGrpMbr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WFGrpMbr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WFGrpMbrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGrpMbrs(" + Company + "," + WorkflowType + "," + WFGroupID + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WFGrpMbrs_Company_WorkflowType_WFGroupID_SalesRepCode(Company, WorkflowType, WFGroupID, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WFGrpMbr item
   Description: Call UpdateExt to delete WFGrpMbr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WFGrpMbr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkflowType: Desc: WorkflowType   Required: True   Allow empty value : True
      :param WFGroupID: Desc: WFGroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/WFGrpMbrs(" + Company + "," + WorkflowType + "," + WFGroupID + "," + SalesRepCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WFGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWFGroup, whereClauseWFGrpMbr, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseWFGroup=" + whereClauseWFGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWFGrpMbr=" + whereClauseWFGrpMbr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(workflowType, wfGroupID, epicorHeaders = None):
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
   params += "workflowType=" + workflowType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "wfGroupID=" + wfGroupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteWFGrpMbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteWFGrpMbr
   Description: Delete WFGroup record by parameters
   OperationID: DeleteWFGrpMbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteWFGrpMbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteWFGrpMbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTaskSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTaskSets
   Description: This method gets the available TaskSets for the TaskSet combo in the
WFGroupEntry.
   OperationID: GetAvailTaskSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailTaskSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSalesRepCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSalesRepCode
   Description: Method to call when changing the SalesRepCode.
   OperationID: OnChangeSalesRepCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSalesRepCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalesRepCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReassignWorkflow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReassignWorkflow
   Description: Reassign Work Flow
   OperationID: ReassignWorkflow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReassignWorkflow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReassignWorkflow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWFGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWFGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWFGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWFGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWFGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWFGrpMbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWFGrpMbr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWFGrpMbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWFGrpMbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWFGrpMbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WFGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WFGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WFGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WFGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WFGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WFGrpMbrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WFGrpMbrRow] = obj["value"]
      pass

class Erp_Tablesets_WFGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this workflow group.  Valid values are "ECO" for ECO tasks, "HELPDESK" for Help Desk tasks, "TIME" for Time tasks, and "EXPENSE" for Expense tasks.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Unique identifier of the workflow group assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  A description of the workflow group.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  The default task set (TaskSet.TaskSetID) for the group.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this group can be attached to a new ECO Group.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The group's primary person's code (SalesRep.PrimeSalesRepCode) in the WorkForce Master File. When adding a person to a workflow group, one person must be marked as the primary person for the group.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WFGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this workflow group.  Valid values are "ECO" for ECO tasks, "HELPDESK" for Help Desk tasks, "TIME" for Time tasks, and "EXPENSE" for Expense tasks.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Unique identifier of the workflow group assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  A description of the workflow group.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  The default task set (TaskSet.TaskSetID) for the group.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this group can be attached to a new ECO Group.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The group's primary person's code (SalesRep.PrimeSalesRepCode) in the WorkForce Master File. When adding a person to a workflow group, one person must be marked as the primary person for the group.  """  
      self.Comment:str = obj["Comment"]
      """  Workflow group comments.  """  
      self.ParentWFGroupID:str = obj["ParentWFGroupID"]
      """  Unique identifier of the parent workflow group associated to this workflow group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefTaskSetDescription:str = obj["DefTaskSetDescription"]
      self.PrimeSalesRepName:str = obj["PrimeSalesRepName"]
      self.ParentWFGroupIDDescription:str = obj["ParentWFGroupIDDescription"]
      """  Parent WF Group description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WFGrpMbrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  Workflow type of the workflow group.  Currently the only possible value is "ECO" - ECO tasks  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group (WFGroup.WFGroupID) that this record is related to.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The (Salesrep.SalesRepCode) code of the person that is a member of this group.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  The Role (RoleCD.RoleCode) that this member performs in the workflow group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimarySalesRep:bool = obj["PrimarySalesRep"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   workflowType
   wfGroupID
   """  
   def __init__(self, obj):
      self.workflowType:str = obj["workflowType"]
      self.wfGroupID:str = obj["wfGroupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteWFGrpMbr_input:
   """ Required : 
   cWorkflowType
   cWFGroupID
   cSalesRepCode
   """  
   def __init__(self, obj):
      self.cWorkflowType:str = obj["cWorkflowType"]
      """  Work Flow Type  """  
      self.cWFGroupID:str = obj["cWFGroupID"]
      """  Work Flow Group Code  """  
      self.cSalesRepCode:str = obj["cSalesRepCode"]
      """  Sales Rep Code  """  
      pass

class DeleteWFGrpMbr_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtWFGroupTableset:
   def __init__(self, obj):
      self.WFGroup:list[Erp_Tablesets_WFGroupRow] = obj["WFGroup"]
      self.WFGrpMbr:list[Erp_Tablesets_WFGrpMbrRow] = obj["WFGrpMbr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WFGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this workflow group.  Valid values are "ECO" for ECO tasks, "HELPDESK" for Help Desk tasks, "TIME" for Time tasks, and "EXPENSE" for Expense tasks.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Unique identifier of the workflow group assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  A description of the workflow group.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  The default task set (TaskSet.TaskSetID) for the group.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this group can be attached to a new ECO Group.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The group's primary person's code (SalesRep.PrimeSalesRepCode) in the WorkForce Master File. When adding a person to a workflow group, one person must be marked as the primary person for the group.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WFGroupListTableset:
   def __init__(self, obj):
      self.WFGroupList:list[Erp_Tablesets_WFGroupListRow] = obj["WFGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WFGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow of this workflow group.  Valid values are "ECO" for ECO tasks, "HELPDESK" for Help Desk tasks, "TIME" for Time tasks, and "EXPENSE" for Expense tasks.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  Unique identifier of the workflow group assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  A description of the workflow group.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  The default task set (TaskSet.TaskSetID) for the group.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this group can be attached to a new ECO Group.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The group's primary person's code (SalesRep.PrimeSalesRepCode) in the WorkForce Master File. When adding a person to a workflow group, one person must be marked as the primary person for the group.  """  
      self.Comment:str = obj["Comment"]
      """  Workflow group comments.  """  
      self.ParentWFGroupID:str = obj["ParentWFGroupID"]
      """  Unique identifier of the parent workflow group associated to this workflow group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefTaskSetDescription:str = obj["DefTaskSetDescription"]
      self.PrimeSalesRepName:str = obj["PrimeSalesRepName"]
      self.ParentWFGroupIDDescription:str = obj["ParentWFGroupIDDescription"]
      """  Parent WF Group description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WFGroupTableset:
   def __init__(self, obj):
      self.WFGroup:list[Erp_Tablesets_WFGroupRow] = obj["WFGroup"]
      self.WFGrpMbr:list[Erp_Tablesets_WFGrpMbrRow] = obj["WFGrpMbr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WFGrpMbrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  Workflow type of the workflow group.  Currently the only possible value is "ECO" - ECO tasks  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group (WFGroup.WFGroupID) that this record is related to.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The (Salesrep.SalesRepCode) code of the person that is a member of this group.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  The Role (RoleCD.RoleCode) that this member performs in the workflow group.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimarySalesRep:bool = obj["PrimarySalesRep"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailTaskSets_input:
   """ Required : 
   cCurrentWorkflowType
   """  
   def __init__(self, obj):
      self.cCurrentWorkflowType:str = obj["cCurrentWorkflowType"]
      """  cCurrent Work Flow Type  """  
      pass

class GetAvailTaskSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   workflowType
   wfGroupID
   """  
   def __init__(self, obj):
      self.workflowType:str = obj["workflowType"]
      self.wfGroupID:str = obj["wfGroupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WFGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WFGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WFGroupTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WFGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewWFGroup_input:
   """ Required : 
   ds
   workflowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      self.workflowType:str = obj["workflowType"]
      pass

class GetNewWFGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWFGrpMbr_input:
   """ Required : 
   ds
   workflowType
   wfGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      self.workflowType:str = obj["workflowType"]
      self.wfGroupID:str = obj["wfGroupID"]
      pass

class GetNewWFGrpMbr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWFGroup
   whereClauseWFGrpMbr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWFGroup:str = obj["whereClauseWFGroup"]
      self.whereClauseWFGrpMbr:str = obj["whereClauseWFGrpMbr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WFGroupTableset] = obj["returnObj"]
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

class OnChangeSalesRepCode_input:
   """ Required : 
   proposedSalesRep
   ds
   """  
   def __init__(self, obj):
      self.proposedSalesRep:str = obj["proposedSalesRep"]
      """  The proposed SalesRepCode  """  
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

class OnChangeSalesRepCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReassignWorkflow_input:
   """ Required : 
   cCurrentWorkflowType
   cCurrentWFGroupID
   cCurrentSalesRepCode
   cNewSalesRepCode
   cReassignOption
   lReassignOpenTasks
   ds
   """  
   def __init__(self, obj):
      self.cCurrentWorkflowType:str = obj["cCurrentWorkflowType"]
      """  cCurrent Work Flow Type  """  
      self.cCurrentWFGroupID:str = obj["cCurrentWFGroupID"]
      """  Current Work Flow Group Code  """  
      self.cCurrentSalesRepCode:str = obj["cCurrentSalesRepCode"]
      """  Current Sales Rep Code  """  
      self.cNewSalesRepCode:str = obj["cNewSalesRepCode"]
      """  New Sales Rep Code  """  
      self.cReassignOption:str = obj["cReassignOption"]
      """  Reassign Option  """  
      self.lReassignOpenTasks:bool = obj["lReassignOpenTasks"]
      """  Reassign Open Tasks:true/false  """  
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

class ReassignWorkflow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWFGroupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWFGroupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WFGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

