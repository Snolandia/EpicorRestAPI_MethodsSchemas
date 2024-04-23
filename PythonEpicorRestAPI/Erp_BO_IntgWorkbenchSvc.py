import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IntgWorkbenchSvc
# Description: Purpose:
Parameters:  none
Notes:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IntgWorkbenches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IntgWorkbenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IntgWorkbenches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntQueInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches",headers=creds) as resp:
           return await resp.json()

async def post_IntgWorkbenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IntgWorkbenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IntgWorkbenches_IntQueID(IntQueID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IntgWorkbench item
   Description: Calls GetByID to retrieve the IntgWorkbench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetById_IntgWorkbench
      :param IntQueID: Desc: IntQueID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IntgWorkbenches_IntQueID(IntQueID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IntgWorkbench for the service
   Description: Calls UpdateExt to update IntgWorkbench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: UpdateExt_IntgWorkbench
      :param IntQueID: Desc: IntQueID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IntgWorkbenches_IntQueID(IntQueID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IntgWorkbench item
   Description: Call UpdateExt to delete IntgWorkbench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: DeleteUpdateExt_IntgWorkbench
      :param IntQueID: Desc: IntQueID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntQueInListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIntQueIn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseIntQueIn=" + whereClauseIntQueIn
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(intQueID, epicorHeaders = None):
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
   params += "intQueID=" + intQueID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList for specified table and column
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessIntQueIn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessIntQueIn
   Description: Process the IntQueIn record.  Either 'R'egister, 'V'alidate, or 'T'ranslate
   OperationID: ProcessIntQueIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessIntQueIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessIntQueIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByObject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByObject
   Description: Given a list of Groups/Objects we will delete the IntQueIn and all the IM records related to each one of them.
   OperationID: DeleteByObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateIMRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateIMRecord
   Description: Update the IntQueIn record.
   OperationID: UpdateIMRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIMRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIMRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIMHierarchy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIMHierarchy
   Description: Retrieve the IntQueIn record.
   OperationID: GetIMHierarchy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIMHierarchy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIMHierarchy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIMRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIMRecord
   Description: Retrieve the IntQueIn record.
   OperationID: GetIMRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIMRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIMRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_buildGenericBuffer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method buildGenericBuffer
   Description: Retrieve the IntQueIn record.
   OperationID: buildGenericBuffer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/buildGenericBuffer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildGenericBuffer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetErrorRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetErrorRows
   Description: To retrieve the list of errors from failed attempts to import data from external
systems.  This allows a UI to combine onto one screen the 18 browses of the separate
maintenance programs in the External Systems Integration / Operations menu in
Vantage v6.10.
Note that separate BOs are used for viewing / updating the details of each
type (table);  this BO only provides the list of rows needing attention, with
minimal description intended to be sufficient for labeling nodes in a tree view.
It should be possible for the UI to construct calls to GetByID() in the appropriate
BO to load the appropriate sheet for any of the different types.
            
There is an input parameter for each of these types, for which there should be a corresponding
checkbox.  The rows for a given type will only be fetched if its corresponding input is TRUE.
   OperationID: GetErrorRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetErrorRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetErrorRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeleteByGroupOptions(epicorHeaders = None):
   """  
   Summary: Invoke method GetDeleteByGroupOptions
   Description: Returns a dataset to store Delete By Group options
   OperationID: GetDeleteByGroupOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeleteByGroupOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteByGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByGroups
   Description: Delete groups by options selected
   OperationID: DeleteByGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIntQueIn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIntQueIn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIntQueIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIntQueIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIntQueIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IntQueInListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IntQueInRow] = obj["value"]
      pass

class Erp_Tablesets_IntQueInListRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key6:str = obj["Key6"]
      """  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key7:str = obj["Key7"]
      """  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key8:str = obj["Key8"]
      """  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.TransStatus:str = obj["TransStatus"]
      """   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type  """  
      self.Action:str = obj["Action"]
      """  Values are: "Add", "Upd" and "Del"  """  
      self.CreateDCDUserID:str = obj["CreateDCDUserID"]
      """  User Id that created the Queue record. DCDUserID.  """  
      self.ExternalRef:str = obj["ExternalRef"]
      """  For use by external interfacing software only.  """  
      self.Complete:bool = obj["Complete"]
      """  Is this Queue record ready to be deleted?  """  
      self.IntError:bool = obj["IntError"]
      """  Errors exist in this Intermediate Record relating to the Intermediate Status.  """  
      self.Key9:str = obj["Key9"]
      """  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key10:str = obj["Key10"]
      """  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key11:str = obj["Key11"]
      """  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key12:str = obj["Key12"]
      """  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key13:str = obj["Key13"]
      """  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key14:str = obj["Key14"]
      """  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key15:str = obj["Key15"]
      """  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransTypeDescription:str = obj["TransTypeDescription"]
      """  Description based on the TransType field.  """  
      self.InDate:str = obj["InDate"]
      """  Derived from IntQueId when possible  """  
      self.InTime:str = obj["InTime"]
      """  Derived from IntQueId when possible.  Time of day in HH:MM format.  """  
      self.Reference:str = obj["Reference"]
      """  Holds identifier (e.g. InvoiceNum)  """  
      self.Ident:str = obj["Ident"]
      """  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key6:str = obj["Key6"]
      """  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key7:str = obj["Key7"]
      """  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key8:str = obj["Key8"]
      """  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.TransStatus:str = obj["TransStatus"]
      """   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type  """  
      self.Action:str = obj["Action"]
      """  Values are: "Add", "Upd" and "Del"  """  
      self.CreateDCDUserID:str = obj["CreateDCDUserID"]
      """  User Id that created the Queue record. DCDUserID.  """  
      self.ExternalRef:str = obj["ExternalRef"]
      """  For use by external interfacing software only.  """  
      self.Complete:bool = obj["Complete"]
      """  Is this Queue record ready to be deleted?  """  
      self.IntError:bool = obj["IntError"]
      """  Errors exist in this Intermediate Record relating to the Intermediate Status.  """  
      self.Key9:str = obj["Key9"]
      """  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key10:str = obj["Key10"]
      """  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key11:str = obj["Key11"]
      """  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key12:str = obj["Key12"]
      """  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key13:str = obj["Key13"]
      """  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key14:str = obj["Key14"]
      """  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key15:str = obj["Key15"]
      """  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.OptionFlags:int = obj["OptionFlags"]
      """  OptionFlags  """  
      self.Data:str = obj["Data"]
      """  Data  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InTime:str = obj["InTime"]
      """  Derived from IntQueId when possible.  Time of day in HH:MM format.  """  
      self.IntQueIDChar:str = obj["IntQueIDChar"]
      self.Reference:str = obj["Reference"]
      """  Holds identifier (e.g. InvoiceNum)  """  
      self.TransTypeDescription:str = obj["TransTypeDescription"]
      """  Description based on the TransType field.  """  
      self.ErrorList:str = obj["ErrorList"]
      """  List of errors at the IntQueIn level, before reaching the child records.  """  
      self.Ident:str = obj["Ident"]
      """  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  """  
      self.InDate:str = obj["InDate"]
      """  Derived from IntQueId when possible  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByGroups_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IWBDeleteByGroupTableset] = obj["ds"]
      pass

class DeleteByGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IWBDeleteByGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   intQueID
   """  
   def __init__(self, obj):
      self.intQueID:int = obj["intQueID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteByObject_input:
   """ Required : 
   ipRelatedToFile
   """  
   def __init__(self, obj):
      self.ipRelatedToFile:str = obj["ipRelatedToFile"]
      """  List of Groups/Objects (suing the RelatedToFile field as code) to be deleted.
            Valid Values = ABCCode,APInvHed,InvcHead,Customer,Supplier,Vendor,Part,CustCnt,POHeader,RcvHead,GLJrnHed,Currency,CurrRateGrp.  """  
      pass

class DeleteByObject_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GenericIMTableset:
   def __init__(self, obj):
      self.GenericWorkBuffer:list[Erp_Tablesets_GenericWorkBufferRow] = obj["GenericWorkBuffer"]
      self.IMHierarchy:list[Erp_Tablesets_IMHierarchyRow] = obj["IMHierarchy"]
      self.IntgValidationError:list[Erp_Tablesets_IntgValidationErrorRow] = obj["IntgValidationError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GenericWorkBufferRow:
   def __init__(self, obj):
      self.ColFormat:str = obj["ColFormat"]
      self.ColLabel:str = obj["ColLabel"]
      self.ColName:str = obj["ColName"]
      self.ColType:str = obj["ColType"]
      self.ColValue:str = obj["ColValue"]
      self.Company:str = obj["Company"]
      self.RelatedToFile:str = obj["RelatedToFile"]
      self.IntQueID:int = obj["IntQueID"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID of the related record  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMHierarchyRow:
   def __init__(self, obj):
      self.IMTablename:str = obj["IMTablename"]
      self.IntQueID:int = obj["IntQueID"]
      self.IntError:bool = obj["IntError"]
      """  Errors exist in this Intermediate Record relating to the Intermediate Status.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IWBDeleteByGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.APInvoice:bool = obj["APInvoice"]
      """  Delete AP Invoices  """  
      self.ARInvoice:bool = obj["ARInvoice"]
      """  Delete AR Invoices  """  
      self.Customer:bool = obj["Customer"]
      """  Delete Customers  """  
      self.Supplier:bool = obj["Supplier"]
      """  Delete Suppliers  """  
      self.Part:bool = obj["Part"]
      """  Delete Parts  """  
      self.CustContact:bool = obj["CustContact"]
      """  Delete Customer Contacts  """  
      self.Import:bool = obj["Import"]
      """  Delete Imports  """  
      self.PurchaseOrder:bool = obj["PurchaseOrder"]
      """  Delete Purchase Orders  """  
      self.Receipt:bool = obj["Receipt"]
      """  Delete Receipts  """  
      self.GLJournal:bool = obj["GLJournal"]
      """  Delete GL Journals  """  
      self.Currency:bool = obj["Currency"]
      """  Delete Currencies  """  
      self.CurrRateGrp:bool = obj["CurrRateGrp"]
      """  Delete Currency Rate Groups  """  
      self.CurrExRate:bool = obj["CurrExRate"]
      """  Delete Currency Exchange Rates  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IWBDeleteByGroupTableset:
   def __init__(self, obj):
      self.IWBDeleteByGroup:list[Erp_Tablesets_IWBDeleteByGroupRow] = obj["IWBDeleteByGroup"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IntQueInListRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key6:str = obj["Key6"]
      """  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key7:str = obj["Key7"]
      """  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key8:str = obj["Key8"]
      """  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.TransStatus:str = obj["TransStatus"]
      """   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type  """  
      self.Action:str = obj["Action"]
      """  Values are: "Add", "Upd" and "Del"  """  
      self.CreateDCDUserID:str = obj["CreateDCDUserID"]
      """  User Id that created the Queue record. DCDUserID.  """  
      self.ExternalRef:str = obj["ExternalRef"]
      """  For use by external interfacing software only.  """  
      self.Complete:bool = obj["Complete"]
      """  Is this Queue record ready to be deleted?  """  
      self.IntError:bool = obj["IntError"]
      """  Errors exist in this Intermediate Record relating to the Intermediate Status.  """  
      self.Key9:str = obj["Key9"]
      """  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key10:str = obj["Key10"]
      """  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key11:str = obj["Key11"]
      """  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key12:str = obj["Key12"]
      """  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key13:str = obj["Key13"]
      """  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key14:str = obj["Key14"]
      """  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key15:str = obj["Key15"]
      """  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransTypeDescription:str = obj["TransTypeDescription"]
      """  Description based on the TransType field.  """  
      self.InDate:str = obj["InDate"]
      """  Derived from IntQueId when possible  """  
      self.InTime:str = obj["InTime"]
      """  Derived from IntQueId when possible.  Time of day in HH:MM format.  """  
      self.Reference:str = obj["Reference"]
      """  Holds identifier (e.g. InvoiceNum)  """  
      self.Ident:str = obj["Ident"]
      """  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInListTableset:
   def __init__(self, obj):
      self.IntQueInList:list[Erp_Tablesets_IntQueInListRow] = obj["IntQueInList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IntQueInRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key6:str = obj["Key6"]
      """  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key7:str = obj["Key7"]
      """  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key8:str = obj["Key8"]
      """  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.TransStatus:str = obj["TransStatus"]
      """   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type  """  
      self.Action:str = obj["Action"]
      """  Values are: "Add", "Upd" and "Del"  """  
      self.CreateDCDUserID:str = obj["CreateDCDUserID"]
      """  User Id that created the Queue record. DCDUserID.  """  
      self.ExternalRef:str = obj["ExternalRef"]
      """  For use by external interfacing software only.  """  
      self.Complete:bool = obj["Complete"]
      """  Is this Queue record ready to be deleted?  """  
      self.IntError:bool = obj["IntError"]
      """  Errors exist in this Intermediate Record relating to the Intermediate Status.  """  
      self.Key9:str = obj["Key9"]
      """  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key10:str = obj["Key10"]
      """  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key11:str = obj["Key11"]
      """  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key12:str = obj["Key12"]
      """  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key13:str = obj["Key13"]
      """  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key14:str = obj["Key14"]
      """  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.Key15:str = obj["Key15"]
      """  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  """  
      self.OptionFlags:int = obj["OptionFlags"]
      """  OptionFlags  """  
      self.Data:str = obj["Data"]
      """  Data  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InTime:str = obj["InTime"]
      """  Derived from IntQueId when possible.  Time of day in HH:MM format.  """  
      self.IntQueIDChar:str = obj["IntQueIDChar"]
      self.Reference:str = obj["Reference"]
      """  Holds identifier (e.g. InvoiceNum)  """  
      self.TransTypeDescription:str = obj["TransTypeDescription"]
      """  Description based on the TransType field.  """  
      self.ErrorList:str = obj["ErrorList"]
      """  List of errors at the IntQueIn level, before reaching the child records.  """  
      self.Ident:str = obj["Ident"]
      """  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  """  
      self.InDate:str = obj["InDate"]
      """  Derived from IntQueId when possible  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntgValidationErrorRow:
   def __init__(self, obj):
      self.IntQueId:int = obj["IntQueId"]
      """  The unique value for this Queue record.  A concatination of the Date (DDMMCCYY), Time (SSSSS), and a program generated Sequence (9999999) from the IntQueCtrl table.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtSystemId:str = obj["ExtSystemId"]
      """  Code for the external package to be interfaced with  """  
      self.ExtCompanyId:str = obj["ExtCompanyId"]
      """  The ID of the interfaced company  """  
      self.Seq:int = obj["Seq"]
      """  Error sequence.  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Description of error encountered during attempted import.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntgWorkbenchTableset:
   def __init__(self, obj):
      self.IntQueIn:list[Erp_Tablesets_IntQueInRow] = obj["IntQueIn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtIntgWorkbenchTableset:
   def __init__(self, obj):
      self.IntQueIn:list[Erp_Tablesets_IntQueInRow] = obj["IntQueIn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   intQueID
   """  
   def __init__(self, obj):
      self.intQueID:int = obj["intQueID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  specific tableName  """  
      self.fieldName:str = obj["fieldName"]
      """  specific fieldName  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDeleteByGroupOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IWBDeleteByGroupTableset] = obj["returnObj"]
      pass

class GetErrorRows_input:
   """ Required : 
   pcRelatedToList
   whereClauseIntQueIn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.pcRelatedToList:str = obj["pcRelatedToList"]
      """  (optional)A tilde-delimited list of values for the RelatedTo field to match.  """  
      self.whereClauseIntQueIn:str = obj["whereClauseIntQueIn"]
      """  (optional)Where conditions for the IntQueIn* tables.  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetErrorRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetIMHierarchy_input:
   """ Required : 
   ipFileName
   pIntQueID
   extSystemID
   ttGenericIMTablesetDS
   """  
   def __init__(self, obj):
      self.ipFileName:str = obj["ipFileName"]
      """  RelatedToFile  """  
      self.pIntQueID:int = obj["pIntQueID"]
      """  IntQueID  """  
      self.extSystemID:str = obj["extSystemID"]
      """  extSystemID  """  
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

class GetIMHierarchy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

      """  output parameters  """  

class GetIMRecord_input:
   """ Required : 
   ipRelatedToFile
   pIntQueID
   gSysRowID
   ttGenericIMTablesetDS
   """  
   def __init__(self, obj):
      self.ipRelatedToFile:str = obj["ipRelatedToFile"]
      """  RelatedToFile  """  
      self.pIntQueID:int = obj["pIntQueID"]
      """  IntQueID  """  
      self.gSysRowID:str = obj["gSysRowID"]
      """  SysRowID  """  
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

class GetIMRecord_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
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
      self.returnObj:list[Erp_Tablesets_IntQueInListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIntQueIn_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["ds"]
      pass

class GetNewIntQueIn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIntQueIn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIntQueIn:str = obj["whereClauseIntQueIn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["returnObj"]
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

class ProcessIntQueIn_input:
   """ Required : 
   pIntQueID
   tableName
   extSystemID
   pRunValidation
   pRunRegistration
   ttGenericIMTableset
   """  
   def __init__(self, obj):
      self.pIntQueID:int = obj["pIntQueID"]
      """  IntQueID  """  
      self.tableName:str = obj["tableName"]
      """  specific tablename  """  
      self.extSystemID:str = obj["extSystemID"]
      """  type of extSystem  """  
      self.pRunValidation:bool = obj["pRunValidation"]
      """  flag to run validation check  """  
      self.pRunRegistration:bool = obj["pRunRegistration"]
      """  flag to run registration  """  
      self.ttGenericIMTableset:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTableset"]
      pass

class ProcessIntQueIn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrMsgs:str = obj["parameters"]
      self.ttGenericIMTableset:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTableset"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIntgWorkbenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIntgWorkbenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateIMRecord_input:
   """ Required : 
   ipRelatedToFile
   pIntQueID
   gSysRowID
   colName
   ttGenericIMTablesetDS
   """  
   def __init__(self, obj):
      self.ipRelatedToFile:str = obj["ipRelatedToFile"]
      """  RelatedToFile  """  
      self.pIntQueID:int = obj["pIntQueID"]
      """  IntQueID  """  
      self.gSysRowID:str = obj["gSysRowID"]
      """  SysRowID  """  
      self.colName:str = obj["colName"]
      """  column Name that was updated  """  
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

class UpdateIMRecord_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IntgWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class buildGenericBuffer_input:
   """ Required : 
   ipRelatedToFile
   pIntQueID
   ttGenericIMTablesetDS
   """  
   def __init__(self, obj):
      self.ipRelatedToFile:str = obj["ipRelatedToFile"]
      """  RelatedToFile  """  
      self.pIntQueID:int = obj["pIntQueID"]
      """  IntQueID  """  
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

class buildGenericBuffer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ttGenericIMTablesetDS:list[Erp_Tablesets_GenericIMTableset] = obj["ttGenericIMTablesetDS"]
      pass

      """  output parameters  """  

