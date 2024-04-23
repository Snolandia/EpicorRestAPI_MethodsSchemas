import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CorrectiveActionSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CorrectiveActions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CorrectiveActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CorrectiveActions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRCorActRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions",headers=creds) as resp:
           return await resp.json()

async def post_CorrectiveActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CorrectiveActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRCorActRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRCorActRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CorrectiveActions_Company_ActionID(Company, ActionID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CorrectiveAction item
   Description: Calls GetByID to retrieve the CorrectiveAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CorrectiveAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRCorActRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions(" + Company + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CorrectiveActions_Company_ActionID(Company, ActionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CorrectiveAction for the service
   Description: Calls UpdateExt to update CorrectiveAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CorrectiveAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRCorActRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions(" + Company + "," + ActionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CorrectiveActions_Company_ActionID(Company, ActionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CorrectiveAction item
   Description: Call UpdateExt to delete CorrectiveAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CorrectiveAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions(" + Company + "," + ActionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CorrectiveActions_Company_ActionID_DMRCorActAttches(Company, ActionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DMRCorActAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DMRCorActAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRCorActAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions(" + Company + "," + ActionID + ")/DMRCorActAttches",headers=creds) as resp:
           return await resp.json()

async def get_CorrectiveActions_Company_ActionID_DMRCorActAttches_Company_ActionID_DrawingSeq(Company, ActionID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRCorActAttch item
   Description: Calls GetByID to retrieve the DMRCorActAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRCorActAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRCorActAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/CorrectiveActions(" + Company + "," + ActionID + ")/DMRCorActAttches(" + Company + "," + ActionID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DMRCorActAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DMRCorActAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRCorActAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRCorActAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/DMRCorActAttches",headers=creds) as resp:
           return await resp.json()

async def post_DMRCorActAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRCorActAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRCorActAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRCorActAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/DMRCorActAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DMRCorActAttches_Company_ActionID_DrawingSeq(Company, ActionID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRCorActAttch item
   Description: Calls GetByID to retrieve the DMRCorActAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRCorActAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRCorActAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/DMRCorActAttches(" + Company + "," + ActionID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DMRCorActAttches_Company_ActionID_DrawingSeq(Company, ActionID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DMRCorActAttch for the service
   Description: Calls UpdateExt to update DMRCorActAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRCorActAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRCorActAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/DMRCorActAttches(" + Company + "," + ActionID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DMRCorActAttches_Company_ActionID_DrawingSeq(Company, ActionID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DMRCorActAttch item
   Description: Call UpdateExt to delete DMRCorActAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRCorActAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActionID: Desc: ActionID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/DMRCorActAttches(" + Company + "," + ActionID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRCorActListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDMRCorAct, whereClauseDMRCorActAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDMRCorAct=" + whereClauseDMRCorAct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDMRCorActAttch=" + whereClauseDMRCorActAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(actionID, epicorHeaders = None):
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
   params += "actionID=" + actionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ReopenDMRCorAct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReopenDMRCorAct
   Description: Call this method to reopen a particular DMR Corrective Action record.
   OperationID: ReopenDMRCorAct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenDMRCorAct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenDMRCorAct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyNonConfNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyNonConfNum
   Description: validate non-conformance number
   OperationID: VerifyNonConfNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyNonConfNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyNonConfNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyEmpId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyEmpId
   Description: Verify Employee ID
   OperationID: VerifyEmpId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyEmpId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyEmpId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindFirstCorrectiveAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindFirstCorrectiveAction
   Description: Find first DMRCorAct.ActionID
   OperationID: FindFirstCorrectiveAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindFirstCorrectiveAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindFirstCorrectiveAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRCorAct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRCorAct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRCorAct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRCorAct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRCorAct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRCorActAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRCorActAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRCorActAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRCorActAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRCorActAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CorrectiveActionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRCorActAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRCorActAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRCorActListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRCorActListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRCorActRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRCorActRow] = obj["value"]
      pass

class Erp_Tablesets_DMRCorActAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ActionID:int = obj["ActionID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRCorActListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of the corrective action.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the corrective action.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Non Conformance number  """  
      self.AsigndTo:str = obj["AsigndTo"]
      """  Assigned To  """  
      self.AuditBy:str = obj["AuditBy"]
      """  Auditted By  """  
      self.AuditCmts:str = obj["AuditCmts"]
      """  Audit Comments  """  
      self.CauseInv:str = obj["CauseInv"]
      """  Root Cause Investigation  """  
      self.Dept:str = obj["Dept"]
      """  Department  """  
      self.DateOpen:str = obj["DateOpen"]
      """  Date Open  """  
      self.DuDate:str = obj["DuDate"]
      """  Due date  """  
      self.AuditDt:str = obj["AuditDt"]
      """  Audit Date  """  
      self.ActionComp:str = obj["ActionComp"]
      """  Action Completion Date  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionID:int = obj["ActionID"]
      """  A unique id for the corrective action  """  
      self.CauseReasonCode:str = obj["CauseReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.CorrectiveActionReasonCode:str = obj["CorrectiveActionReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier linked to this Corrective Action  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Corrective Action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CauseReasonDesc:str = obj["CauseReasonDesc"]
      """  Root Cause Reason Description  """  
      self.ActionReasonDesc:str = obj["ActionReasonDesc"]
      """  Corrective Action Reason Description  """  
      self.DeptDescription:str = obj["DeptDescription"]
      """  Job Costing department description.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRCorActRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of the corrective action.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the corrective action.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Non Conformance number  """  
      self.AsigndTo:str = obj["AsigndTo"]
      """  Assigned To  """  
      self.AuditBy:str = obj["AuditBy"]
      """  Auditted By  """  
      self.AuditCmts:str = obj["AuditCmts"]
      """  Audit Comments  """  
      self.CauseInv:str = obj["CauseInv"]
      """  Root Cause Investigation  """  
      self.Dept:str = obj["Dept"]
      """  Department  """  
      self.DateOpen:str = obj["DateOpen"]
      """  Date Open  """  
      self.DuDate:str = obj["DuDate"]
      """  Due date  """  
      self.AuditDt:str = obj["AuditDt"]
      """  Audit Date  """  
      self.ActionComp:str = obj["ActionComp"]
      """  Action Completion Date  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionID:int = obj["ActionID"]
      """  A unique id for the corrective action  """  
      self.CauseReasonCode:str = obj["CauseReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.CorrectiveActionReasonCode:str = obj["CorrectiveActionReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier linked to this Corrective Action  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Corrective Action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CauseReasonDesc:str = obj["CauseReasonDesc"]
      """  Root Cause Reason Description  """  
      self.ActionReasonDesc:str = obj["ActionReasonDesc"]
      """  Corrective Action Reason Description  """  
      self.ReopenCorAct:bool = obj["ReopenCorAct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AsigndToName:str = obj["AsigndToName"]
      self.AsigndToLastName:str = obj["AsigndToLastName"]
      self.AsigndToFirstName:str = obj["AsigndToFirstName"]
      self.AuditByName:str = obj["AuditByName"]
      self.AuditByLastName:str = obj["AuditByLastName"]
      self.AuditByFirstName:str = obj["AuditByFirstName"]
      self.DeptDescription:str = obj["DeptDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   actionID
   """  
   def __init__(self, obj):
      self.actionID:int = obj["actionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CorrectiveActionTableset:
   def __init__(self, obj):
      self.DMRCorAct:list[Erp_Tablesets_DMRCorActRow] = obj["DMRCorAct"]
      self.DMRCorActAttch:list[Erp_Tablesets_DMRCorActAttchRow] = obj["DMRCorActAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DMRCorActAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ActionID:int = obj["ActionID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRCorActListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of the corrective action.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the corrective action.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Non Conformance number  """  
      self.AsigndTo:str = obj["AsigndTo"]
      """  Assigned To  """  
      self.AuditBy:str = obj["AuditBy"]
      """  Auditted By  """  
      self.AuditCmts:str = obj["AuditCmts"]
      """  Audit Comments  """  
      self.CauseInv:str = obj["CauseInv"]
      """  Root Cause Investigation  """  
      self.Dept:str = obj["Dept"]
      """  Department  """  
      self.DateOpen:str = obj["DateOpen"]
      """  Date Open  """  
      self.DuDate:str = obj["DuDate"]
      """  Due date  """  
      self.AuditDt:str = obj["AuditDt"]
      """  Audit Date  """  
      self.ActionComp:str = obj["ActionComp"]
      """  Action Completion Date  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionID:int = obj["ActionID"]
      """  A unique id for the corrective action  """  
      self.CauseReasonCode:str = obj["CauseReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.CorrectiveActionReasonCode:str = obj["CorrectiveActionReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier linked to this Corrective Action  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Corrective Action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CauseReasonDesc:str = obj["CauseReasonDesc"]
      """  Root Cause Reason Description  """  
      self.ActionReasonDesc:str = obj["ActionReasonDesc"]
      """  Corrective Action Reason Description  """  
      self.DeptDescription:str = obj["DeptDescription"]
      """  Job Costing department description.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRCorActListTableset:
   def __init__(self, obj):
      self.DMRCorActList:list[Erp_Tablesets_DMRCorActListRow] = obj["DMRCorActList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DMRCorActRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of the corrective action.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the corrective action.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Non Conformance number  """  
      self.AsigndTo:str = obj["AsigndTo"]
      """  Assigned To  """  
      self.AuditBy:str = obj["AuditBy"]
      """  Auditted By  """  
      self.AuditCmts:str = obj["AuditCmts"]
      """  Audit Comments  """  
      self.CauseInv:str = obj["CauseInv"]
      """  Root Cause Investigation  """  
      self.Dept:str = obj["Dept"]
      """  Department  """  
      self.DateOpen:str = obj["DateOpen"]
      """  Date Open  """  
      self.DuDate:str = obj["DuDate"]
      """  Due date  """  
      self.AuditDt:str = obj["AuditDt"]
      """  Audit Date  """  
      self.ActionComp:str = obj["ActionComp"]
      """  Action Completion Date  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionID:int = obj["ActionID"]
      """  A unique id for the corrective action  """  
      self.CauseReasonCode:str = obj["CauseReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.CorrectiveActionReasonCode:str = obj["CorrectiveActionReasonCode"]
      """  Corrective Actions use Reason Type "Q".  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier linked to this Corrective Action  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Corrective Action  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CauseReasonDesc:str = obj["CauseReasonDesc"]
      """  Root Cause Reason Description  """  
      self.ActionReasonDesc:str = obj["ActionReasonDesc"]
      """  Corrective Action Reason Description  """  
      self.ReopenCorAct:bool = obj["ReopenCorAct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AsigndToName:str = obj["AsigndToName"]
      self.AsigndToLastName:str = obj["AsigndToLastName"]
      self.AsigndToFirstName:str = obj["AsigndToFirstName"]
      self.AuditByName:str = obj["AuditByName"]
      self.AuditByLastName:str = obj["AuditByLastName"]
      self.AuditByFirstName:str = obj["AuditByFirstName"]
      self.DeptDescription:str = obj["DeptDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCorrectiveActionTableset:
   def __init__(self, obj):
      self.DMRCorAct:list[Erp_Tablesets_DMRCorActRow] = obj["DMRCorAct"]
      self.DMRCorActAttch:list[Erp_Tablesets_DMRCorActAttchRow] = obj["DMRCorActAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindFirstCorrectiveAction_input:
   """ Required : 
   whereClauseDMRCorAct
   """  
   def __init__(self, obj):
      self.whereClauseDMRCorAct:str = obj["whereClauseDMRCorAct"]
      pass

class FindFirstCorrectiveAction_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   actionID
   """  
   def __init__(self, obj):
      self.actionID:int = obj["actionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CorrectiveActionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CorrectiveActionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CorrectiveActionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRCorActListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDMRCorActAttch_input:
   """ Required : 
   ds
   actionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      self.actionID:int = obj["actionID"]
      pass

class GetNewDMRCorActAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRCorAct_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      pass

class GetNewDMRCorAct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDMRCorAct
   whereClauseDMRCorActAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDMRCorAct:str = obj["whereClauseDMRCorAct"]
      self.whereClauseDMRCorActAttch:str = obj["whereClauseDMRCorActAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CorrectiveActionTableset] = obj["returnObj"]
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

class ReopenDMRCorAct_input:
   """ Required : 
   ipActionID
   """  
   def __init__(self, obj):
      self.ipActionID:int = obj["ipActionID"]
      """  The Action ID of the Corrective Action to reopen  """  
      pass

class ReopenDMRCorAct_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CorrectiveActionTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCorrectiveActionTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCorrectiveActionTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CorrectiveActionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VerifyEmpId_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class VerifyEmpId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empName:str = obj["parameters"]
      pass

      """  output parameters  """  

class VerifyNonConfNum_input:
   """ Required : 
   nonConfNum
   DMRNum
   """  
   def __init__(self, obj):
      self.nonConfNum:int = obj["nonConfNum"]
      self.DMRNum:int = obj["DMRNum"]
      pass

class VerifyNonConfNum_output:
   def __init__(self, obj):
      pass

