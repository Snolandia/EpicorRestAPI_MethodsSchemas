import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ACTTypeRevisionSvc
# Description: ACTType Revision business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ACTTypeRevisions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ACTTypeRevisions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ACTTypeRevisions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions",headers=creds) as resp:
           return await resp.json()

async def post_ACTTypeRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ACTTypeRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ACTTypeRevisions_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ACTTypeRevision item
   Description: Calls GetByID to retrieve the ACTTypeRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ACTTypeRevision
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ACTTypeRevisions_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ACTTypeRevision for the service
   Description: Calls UpdateExt to update ACTTypeRevision. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ACTTypeRevision
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ACTTypeRevisionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ACTTypeRevisions_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ACTTypeRevision item
   Description: Call UpdateExt to delete ACTTypeRevision item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ACTTypeRevision
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/ACTTypeRevisions(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ACTTypeRevisionListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseACTTypeRevision, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseACTTypeRevision=" + whereClauseACTTypeRevision
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysRowID, epicorHeaders = None):
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
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfRevisions
   Description: Gets List of revisions available for Export/Delete.
   OperationID: GetListOfRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRevisionsDataInStringFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevisionsDataInStringFormat
   Description: Get set of parameters lists in string format.
   OperationID: GetRevisionsDataInStringFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisionsDataInStringFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionsDataInStringFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillRevisionsTableForImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillRevisionsTableForImport
   Description: Get the list of revisions for import (system revisions).
   OperationID: FillRevisionsTableForImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillRevisionsTableForImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillRevisionsTableForImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillTempTableForImportFromFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillTempTableForImportFromFile
   Description: Returns dataset with the list of revisions loaded form file.
   OperationID: FillTempTableForImportFromFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillTempTableForImportFromFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillTempTableForImportFromFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevisionsStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevisionsStatus
   Description: Change status for all revisions.
   OperationID: ChangeRevisionsStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevisionsStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionsStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadBookMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadBookMap
   Description: Get Book/Segment mapping data.
   OperationID: LoadBookMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadBookMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadBookMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBookMappingInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBookMappingInfo
   Description: Update Book Mapping Data.
   OperationID: UpdateBookMappingInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBookMappingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBookMappingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBooksExistsRevisionUsedBothBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBooksExistsRevisionUsedBothBooks
   Description: Check that books exist.
   OperationID: CheckBooksExistsRevisionUsedBothBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBooksExistsRevisionUsedBothBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBooksExistsRevisionUsedBothBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSourceBooksExistsRevisionUsedBothBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSourceBooksExistsRevisionUsedBothBooks
   Description: Check Source Books Exists.
   OperationID: CheckSourceBooksExistsRevisionUsedBothBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSourceBooksExistsRevisionUsedBothBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSourceBooksExistsRevisionUsedBothBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMapBookForAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMapBookForAll
   Description: Update Mapping Book ds on ColumnChanged event for Map Book.
   OperationID: UpdateMapBookForAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMapBookForAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMapBookForAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckNoBookingRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckNoBookingRule
   Description: Check there is no booking rules for the mapped book.
   OperationID: CheckNoBookingRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckNoBookingRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNoBookingRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidBookMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidBookMapping
   Description: Checks that Book Mapping is valid.
   OperationID: IsValidBookMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidBookMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidBookMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_createAdditionalBooksForAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method createAdditionalBooksForAll
   Description: Create additional books for all mapped books.
   OperationID: createAdditionalBooksForAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/createAdditionalBooksForAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAdditionalBooksForAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_btnAddMappedBook_OnClick(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method btnAddMappedBook_OnClick
   Description: Creates additional Mapped book on btnAddMappedBook click.
   OperationID: btnAddMappedBook_OnClick
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/btnAddMappedBook_OnClick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/btnAddMappedBook_OnClick_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMapSegmentsTableFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMapSegmentsTableFilter
   Description: Get filter for the Map Segments list.
   OperationID: GetMapSegmentsTableFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMapSegmentsTableFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapSegmentsTableFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearBooksForAllTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearBooksForAllTypes
   Description: Clear books data for all types.
   OperationID: ClearBooksForAllTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearBooksForAllTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearBooksForAllTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetMapSegments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetMapSegments
   Description: Upadate Table with Map Segments on the Book Mapping panel after Target Book changes in table of mapping books.
   OperationID: SetMapSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetMapSegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetMapSegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckImportedBookPackages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckImportedBookPackages
   Description: Check imported book packages.
   OperationID: CheckImportedBookPackages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckImportedBookPackages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckImportedBookPackages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SinchronizeDataAfterABTVerValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SinchronizeDataAfterABTVerValidation
   Description: Include changes after ABTVer Validation.
   OperationID: SinchronizeDataAfterABTVerValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SinchronizeDataAfterABTVerValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SinchronizeDataAfterABTVerValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ACTTypeRevisionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTTypeRevisionListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ACTTypeRevisionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ACTTypeRevisionRow] = obj["value"]
      pass

class Erp_Tablesets_ACTTypeRevisionListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates that record is selected.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.SegmentsForMap:str = obj["SegmentsForMap"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.DelRev:bool = obj["DelRev"]
      """  Indicates if current revision is selected to be deleted or not.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeRevisionRow:
   def __init__(self, obj):
      self.ABTVer:str = obj["ABTVer"]
      """  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  """  
      self.Activate:bool = obj["Activate"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.BooksForMap:str = obj["BooksForMap"]
      self.DelRev:bool = obj["DelRev"]
      """  Indicates if current revision is selected to be deleted or not.  """  
      self.FileName:str = obj["FileName"]
      self.ImportABT:bool = obj["ImportABT"]
      """  Import ABT.  """  
      self.ImportBR:bool = obj["ImportBR"]
      self.NewCode:str = obj["NewCode"]
      """  New Revision Code.  """  
      self.PackageList:str = obj["PackageList"]
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.ReplaceExisting:bool = obj["ReplaceExisting"]
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.SegmentsForMap:str = obj["SegmentsForMap"]
      self.Selected:bool = obj["Selected"]
      """  Indicates that record is selected.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseUpdateMode:bool = obj["UseUpdateMode"]
      """  Indicates Update mode.  """  
      self.XMLData:str = obj["XMLData"]
      self.ChangeStatusSelected:bool = obj["ChangeStatusSelected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeRevisionsStatus_input:
   """ Required : 
   selectionMode
   status
   newRevName
   ds
   """  
   def __init__(self, obj):
      self.selectionMode:str = obj["selectionMode"]
      self.status:bool = obj["status"]
      self.newRevName:str = obj["newRevName"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class ChangeRevisionsStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBooksExistsRevisionUsedBothBooks_input:
   """ Required : 
   mapBook
   company
   importBook
   package
   rowIdent
   ds
   """  
   def __init__(self, obj):
      self.mapBook:str = obj["mapBook"]
      self.company:str = obj["company"]
      self.importBook:str = obj["importBook"]
      self.package:str = obj["package"]
      self.rowIdent:str = obj["rowIdent"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class CheckBooksExistsRevisionUsedBothBooks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckImportedBookPackages_input:
   """ Required : 
   CurrentCompany
   CompaniesList
   xml_ACTTypeRevision
   xml_MappingInfo
   """  
   def __init__(self, obj):
      self.CurrentCompany:str = obj["CurrentCompany"]
      self.CompaniesList:str = obj["CompaniesList"]
      self.xml_ACTTypeRevision:str = obj["xml_ACTTypeRevision"]
      self.xml_MappingInfo:str = obj["xml_MappingInfo"]
      pass

class CheckImportedBookPackages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.warnMess:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckNoBookingRule_input:
   """ Required : 
   chkAllTypes
   currentBookID
   ds
   """  
   def __init__(self, obj):
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.currentBookID:str = obj["currentBookID"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class CheckNoBookingRule_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckSourceBooksExistsRevisionUsedBothBooks_input:
   """ Required : 
   company
   importBook
   package
   rowIdent
   ds
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.importBook:str = obj["importBook"]
      self.package:str = obj["package"]
      self.rowIdent:str = obj["rowIdent"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class CheckSourceBooksExistsRevisionUsedBothBooks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ClearBooksForAllTypes_input:
   """ Required : 
   chkAllTypes
   CompaniesList
   ds
   """  
   def __init__(self, obj):
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.CompaniesList:str = obj["CompaniesList"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class ClearBooksForAllTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ACTTypeRevisionListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates that record is selected.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.SegmentsForMap:str = obj["SegmentsForMap"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.DelRev:bool = obj["DelRev"]
      """  Indicates if current revision is selected to be deleted or not.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeRevisionListTableset:
   def __init__(self, obj):
      self.ACTTypeRevisionList:list[Erp_Tablesets_ACTTypeRevisionListRow] = obj["ACTTypeRevisionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ACTTypeRevisionRow:
   def __init__(self, obj):
      self.ABTVer:str = obj["ABTVer"]
      """  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  """  
      self.Activate:bool = obj["Activate"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.BooksForMap:str = obj["BooksForMap"]
      self.DelRev:bool = obj["DelRev"]
      """  Indicates if current revision is selected to be deleted or not.  """  
      self.FileName:str = obj["FileName"]
      self.ImportABT:bool = obj["ImportABT"]
      """  Import ABT.  """  
      self.ImportBR:bool = obj["ImportBR"]
      self.NewCode:str = obj["NewCode"]
      """  New Revision Code.  """  
      self.PackageList:str = obj["PackageList"]
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.ReplaceExisting:bool = obj["ReplaceExisting"]
      self.RevisionCode:str = obj["RevisionCode"]
      """  A user-defined code of revision (unique within one account transaction type).  """  
      self.RevisionStatus:str = obj["RevisionStatus"]
      """   Status of the Revision. Allowed values are: "Active", "Draft", "Blocked". 
Active - indicates that exactly this Revision of an GL Transaction Type will be used when functional module initiates a corresponding business event. As soon as a Revision becomes "Active", it should become read-only for user. Only one Revision for each GL Transaction Type may be "Active".
 
Draft -  indicates a newly created Revision, which will not be used in any run-time processing. Each newly created Revision should automatically be put into "Draft" status. "Draft" Revision is open for editing. Each GL Transaction Type may have any number of Draft Revisions.
Blocked - indicates a Revision which was previously "Active" but is not anymore and is stored for traceability purposes. The "Blocked" Revision should be read-only.  """  
      self.RType:str = obj["RType"]
      """  Standard or Exteded  """  
      self.SegmentsForMap:str = obj["SegmentsForMap"]
      self.Selected:bool = obj["Selected"]
      """  Indicates that record is selected.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseUpdateMode:bool = obj["UseUpdateMode"]
      """  Indicates Update mode.  """  
      self.XMLData:str = obj["XMLData"]
      self.ChangeStatusSelected:bool = obj["ChangeStatusSelected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ACTTypeRevisionTableset:
   def __init__(self, obj):
      self.ACTTypeRevision:list[Erp_Tablesets_ACTTypeRevisionRow] = obj["ACTTypeRevision"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BookMappingRow:
   def __init__(self, obj):
      self.ABTVer:str = obj["ABTVer"]
      """  Version of VBD Stucture. If version is changed , VBD Structure merge process will be started during conversion.  """  
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.AdditionalMapBook:bool = obj["AdditionalMapBook"]
      self.Company:str = obj["Company"]
      """  Company.  """  
      self.FilterColumn:str = obj["FilterColumn"]
      self.ForAllTypes:str = obj["ForAllTypes"]
      self.FromXML:bool = obj["FromXML"]
      self.HasEmptyData:bool = obj["HasEmptyData"]
      """  flag if has empty Data.  """  
      self.ImportBook:str = obj["ImportBook"]
      """  Import Book ID.  """  
      self.MapBook:str = obj["MapBook"]
      self.MappedFrom:str = obj["MappedFrom"]
      self.Package:str = obj["Package"]
      self.PatchABTVer:str = obj["PatchABTVer"]
      """  Patch VBD Version  """  
      self.PatchRulesetVer:str = obj["PatchRulesetVer"]
      self.RevisionName:str = obj["RevisionName"]
      """  Revision Name.  """  
      self.RulesetVer:str = obj["RulesetVer"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BookMappingTableset:
   def __init__(self, obj):
      self.BookMapping:list[Erp_Tablesets_BookMappingRow] = obj["BookMapping"]
      self.MapComp:list[Erp_Tablesets_MapCompRow] = obj["MapComp"]
      self.MapRevision:list[Erp_Tablesets_MapRevisionRow] = obj["MapRevision"]
      self.SegmentMapping:list[Erp_Tablesets_SegmentMappingRow] = obj["SegmentMapping"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MapCompRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company.  """  
      self.FilterColumn:str = obj["FilterColumn"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MapRevisionRow:
   def __init__(self, obj):
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.Company:str = obj["Company"]
      """  Company.  """  
      self.Description:str = obj["Description"]
      self.FilterColumn:str = obj["FilterColumn"]
      self.HasEmptyData:bool = obj["HasEmptyData"]
      self.RevisionName:str = obj["RevisionName"]
      """  Revision Name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegmentMappingRow:
   def __init__(self, obj):
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.AdditionalMapBook:bool = obj["AdditionalMapBook"]
      self.Company:str = obj["Company"]
      """  Company.  """  
      self.DispMapSegmentNum:int = obj["DispMapSegmentNum"]
      self.FilterColumn:str = obj["FilterColumn"]
      self.ForAllTypes:str = obj["ForAllTypes"]
      self.ImportBook:str = obj["ImportBook"]
      """  Import Book ID.  """  
      self.ImportSegmentName:str = obj["ImportSegmentName"]
      """  Name of source segment.  """  
      self.ImportSegmentNum:int = obj["ImportSegmentNum"]
      """  Number of source segment.  """  
      self.MapBook:str = obj["MapBook"]
      self.MapSegmentName:str = obj["MapSegmentName"]
      """  Name of target segment.  """  
      self.MapSegmentNum:int = obj["MapSegmentNum"]
      """  Number of target segment.  """  
      self.Package:str = obj["Package"]
      """  Package ID.  """  
      self.RevisionName:str = obj["RevisionName"]
      """  Revision Name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtACTTypeRevisionTableset:
   def __init__(self, obj):
      self.ACTTypeRevision:list[Erp_Tablesets_ACTTypeRevisionRow] = obj["ACTTypeRevision"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillRevisionsTableForImport_input:
   """ Required : 
   package
   glTranType
   import
   inUpdateMode
   replaceExisting
   activate
   newName
   ds
   """  
   def __init__(self, obj):
      self.package:str = obj["package"]
      self.glTranType:str = obj["glTranType"]
      self.import_:bool = obj["import"]
      self.inUpdateMode:bool = obj["inUpdateMode"]
      self.replaceExisting:bool = obj["replaceExisting"]
      self.activate:bool = obj["activate"]
      self.newName:str = obj["newName"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class FillRevisionsTableForImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opwarningAboutSkippedRevisions:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class FillTempTableForImportFromFile_input:
   """ Required : 
   fileName
   import
   inUpdateMode
   replaceExisting
   activate
   newName
   ds
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      self.import_:bool = obj["import"]
      self.inUpdateMode:bool = obj["inUpdateMode"]
      self.replaceExisting:bool = obj["replaceExisting"]
      self.activate:bool = obj["activate"]
      self.newName:str = obj["newName"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class FillTempTableForImportFromFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opwarningAboutSkippedRevisions:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["returnObj"]
      pass

class GetListOfRevisions_input:
   """ Required : 
   ipDelRev
   ds
   """  
   def __init__(self, obj):
      self.ipDelRev:bool = obj["ipDelRev"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class GetListOfRevisions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ACTTypeRevisionListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMapSegmentsTableFilter_input:
   """ Required : 
   chkAllTypes
   ACTTypeName
   RevisionName
   Package
   Company
   ImportBook
   MapBook
   """  
   def __init__(self, obj):
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.RevisionName:str = obj["RevisionName"]
      self.Package:str = obj["Package"]
      self.Company:str = obj["Company"]
      self.ImportBook:str = obj["ImportBook"]
      self.MapBook:str = obj["MapBook"]
      pass

class GetMapSegmentsTableFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newfilter:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRevisionsDataInStringFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class GetRevisionsDataInStringFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opListOfACTTypeNames:str = obj["parameters"]
      self.opListOfACTTypeUIDs:str = obj["parameters"]
      self.opListOfFileNames:str = obj["parameters"]
      self.opListOfNewCodes:str = obj["parameters"]
      self.opListOfRevisionCodes:str = obj["parameters"]
      self.opListSelectedToDelete:str = obj["parameters"]
      self.opListSelectedToExport:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseACTTypeRevision
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseACTTypeRevision:str = obj["whereClauseACTTypeRevision"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["returnObj"]
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

class IsValidBookMapping_input:
   """ Required : 
   chkAllTypes
   ds
   """  
   def __init__(self, obj):
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class IsValidBookMapping_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadBookMap_input:
   """ Required : 
   manualSelectionBooks
   CompaniesList
   ds
   bm_ds
   """  
   def __init__(self, obj):
      self.manualSelectionBooks:bool = obj["manualSelectionBooks"]
      self.CompaniesList:str = obj["CompaniesList"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      self.bm_ds:list[Erp_Tablesets_BookMappingTableset] = obj["bm_ds"]
      pass

class LoadBookMap_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.xmlACTTypeRevisionsInfo:str = obj["parameters"]
      self.xmlMappingInfo:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      self.bm_ds:list[Erp_Tablesets_BookMappingTableset] = obj["bm_ds"]
      pass

      """  output parameters  """  

class SetMapSegments_input:
   """ Required : 
   chkAllTypes
   bookSysRowID
   company
   bookID
   coaCode
   CompaniesList
   existsEmptyData
   ds
   """  
   def __init__(self, obj):
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.bookSysRowID:str = obj["bookSysRowID"]
      self.company:str = obj["company"]
      self.bookID:str = obj["bookID"]
      self.coaCode:str = obj["coaCode"]
      self.CompaniesList:str = obj["CompaniesList"]
      self.existsEmptyData:bool = obj["existsEmptyData"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class SetMapSegments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.existsEmptyData:bool = obj["existsEmptyData"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SinchronizeDataAfterABTVerValidation_input:
   """ Required : 
   xml_ACTTypeRevision
   ds
   """  
   def __init__(self, obj):
      self.xml_ACTTypeRevision:str = obj["xml_ACTTypeRevision"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class SinchronizeDataAfterABTVerValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.xml_ACTTypeRevision:str = obj["parameters"]
      self.isAnyRevsToImport:bool = obj["isAnyRevsToImport"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateBookMappingInfo_input:
   """ Required : 
   xmlMappingInfo
   ds
   bm_ds
   """  
   def __init__(self, obj):
      self.xmlMappingInfo:str = obj["xmlMappingInfo"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      self.bm_ds:list[Erp_Tablesets_BookMappingTableset] = obj["bm_ds"]
      pass

class UpdateBookMappingInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.xmlMappingInfoUpdated:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      self.bm_ds:list[Erp_Tablesets_BookMappingTableset] = obj["bm_ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtACTTypeRevisionTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtACTTypeRevisionTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMapBookForAll_input:
   """ Required : 
   company
   prevMapBook
   importBook
   newMapBookID
   package
   ds
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.prevMapBook:str = obj["prevMapBook"]
      self.importBook:str = obj["importBook"]
      self.newMapBookID:str = obj["newMapBookID"]
      self.package:str = obj["package"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class UpdateMapBookForAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ACTTypeRevisionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class btnAddMappedBook_OnClick_input:
   """ Required : 
   curBookID
   chkAllTypes
   ManualSelectionBooks
   ds
   """  
   def __init__(self, obj):
      self.curBookID:str = obj["curBookID"]
      self.chkAllTypes:bool = obj["chkAllTypes"]
      self.ManualSelectionBooks:bool = obj["ManualSelectionBooks"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class btnAddMappedBook_OnClick_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class createAdditionalBooksForAll_input:
   """ Required : 
   ManualSelectionBooks
   ds
   """  
   def __init__(self, obj):
      self.ManualSelectionBooks:bool = obj["ManualSelectionBooks"]
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

class createAdditionalBooksForAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BookMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

