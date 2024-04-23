import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ImportSubsidSvc
# Description: Import Consolidation from Subsidiary object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ImportSubsids(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportSubsids items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportSubsids
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids",headers=creds) as resp:
           return await resp.json()

async def post_ImportSubsids(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportSubsids
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportSubsids_Company_GenID(Company, GenID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportSubsid item
   Description: Calls GetByID to retrieve the ImportSubsid item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportSubsid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportSubsids_Company_GenID(Company, GenID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportSubsid for the service
   Description: Calls UpdateExt to update ImportSubsid. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportSubsid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportSubsids_Company_GenID(Company, GenID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportSubsid item
   Description: Call UpdateExt to delete ImportSubsid item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportSubsid
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/ImportSubsids(" + Company + "," + GenID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseConsImport, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseConsImport=" + whereClauseConsImport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(genID, epicorHeaders = None):
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
   params += "genID=" + genID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GroupChangeWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupChangeWarning
   Description: Purpose:
Parameters:
<param name="ipBook">book id</param><param name="ds">ImportSubsid dataset row</param><param name="warnMsg">A warning message is returned if the book changes and the gljrngrp exists.</param>
Notes:
   OperationID: GroupChangeWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupChangeWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupChangeWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJournal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJournal
   Description: Purpose:
Parameters:
<param name="ipJournalCode">journal code</param><param name="ds">ImportSubsid dataset row</param>
   OperationID: ValidateJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookCalendar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBookCalendar
   Description: Purpose: retrive the book's calendar so it can be displayed on the form.
Parameters:
<param name="ipBookID">book id</param><param name="ds">ImportSubsid dataset row</param>
Notes:
   OperationID: GetBookCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBookCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGroupID
   Description: Purpose:
Parameters:
<param name="ipGroupID">Journal Group to Create for this import</param><param name="ds">ImportSubsid dataset row</param><param name="opCreateGroup">prompt asking if it is okay to create the group</param>
Notes:
   OperationID: CheckGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call when validating fiscal year
   OperationID: CheckFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFiscalPeriod
   Description: This method provides a warning message to present to the user if the given
Fiscal Year/Period has already been imported.  The user should be given the
choice to import it again.
            
The user's answer to the question "This fiscal period has previously been imported. Do you want to import it again?"
should be stored in MCConGen.OkToRegenerate.
            
In v6.10 Vantage, the user was never warned of a duplicate import--the system just
quietly did as it was told.
            
An exception is thrown if:
- no MCConGen dataset row is found
- the given Fiscal Year/Period is not valid
   OperationID: CheckFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateJournal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateJournal
   Description: This method generates Journal Entries from a MCConsolImport dataset.
It is expected that the UI will first read a file from disk to create the
MCConsolImport dataset.
            
Each row in the MCConsolImport dataset that fails to "import" gets
updated with the reason for the failure in MCConsolImport.ImportErrorMsg,
and these are returned to the client;  if there are any technical failures,
such as improper datatypes in the input, all the
non-failing rows are backed out, and an exception is thrown.
Less serious failures, such as "Account not found", prevent only the import
of the problematic line--the remainder can still be accepted.
            
When successful, a MCConGen record is created in the database to indicate the
consolidation was performed.
            
An exception is thrown if:
- the GLJrnGrp indicated by the GroupId is nto found
- the fiscal period indicated by the GLJrnGrp is invalid
- the filename is blank
   OperationID: GenerateJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseInputFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseInputFile
   Description: Web support.
   OperationID: ParseInputFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseInputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseInputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportSubsidSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsImportRow] = obj["value"]
      pass

class Erp_Tablesets_ConsImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  This is the book the import file is being loaded to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ImportDate:str = obj["ImportDate"]
      """  Date the input file was imported  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Date used on the GLJrnDtl  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.JrnlHeadDesc:str = obj["JrnlHeadDesc"]
      """  Journal Header Description  """  
      self.ImportStatus:str = obj["ImportStatus"]
      """   Indicates the status of the Import from Subsidiary.
C = Complete  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  Import/Export file name.  """  
      self.GenerationLog:str = obj["GenerationLog"]
      """  The consolidation generation log.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToRegenerate:bool = obj["OkToRegenerate"]
      """  logical indicating if it is okay to regenerate  """  
      self.LastImportDate:str = obj["LastImportDate"]
      """  Date of Last Import  """  
      self.LastGroup:str = obj["LastGroup"]
      """  Last Journal Group imported  """  
      self.LastDescription:str = obj["LastDescription"]
      """  Description of the last import  """  
      self.LastGenID:int = obj["LastGenID"]
      """  Last generation ID  """  
      self.LastImportFile:str = obj["LastImportFile"]
      """  Last Import File Name  """  
      self.OkayToAddNewGroup:bool = obj["OkayToAddNewGroup"]
      """  Logical indicating the user wants to create a new GLJrnGrp record.  """  
      self.DisableGroupFields:bool = obj["DisableGroupFields"]
      """  Logical indicating the group fields are to be disabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  This is the book the import file is being loaded to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ImportDate:str = obj["ImportDate"]
      """  Date the input file was imported  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Date used on the GLJrnDtl  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.JrnlHeadDesc:str = obj["JrnlHeadDesc"]
      """  Journal Header Description  """  
      self.ImportStatus:str = obj["ImportStatus"]
      """   Indicates the status of the Import from Subsidiary.
C = Complete  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  Import/Export file name.  """  
      self.GenerationLog:str = obj["GenerationLog"]
      """  The consolidation generation log.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToRegenerate:bool = obj["OkToRegenerate"]
      """  logical indicating if it is okay to regenerate  """  
      self.LastImportDate:str = obj["LastImportDate"]
      """  Date of Last Import  """  
      self.LastGroup:str = obj["LastGroup"]
      """  Last Journal Group imported  """  
      self.LastDescription:str = obj["LastDescription"]
      """  Description of the last import  """  
      self.LastGenID:int = obj["LastGenID"]
      """  Last generation ID  """  
      self.LastImportFile:str = obj["LastImportFile"]
      """  Last Import File Name  """  
      self.OkayToAddNewGroup:bool = obj["OkayToAddNewGroup"]
      """  Logical indicating the user wants to create a new GLJrnGrp record.  """  
      self.DisableGroupFields:bool = obj["DisableGroupFields"]
      """  Logical indicating the group fields are to be disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckFiscalPeriod_input:
   """ Required : 
   ipFiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      """  fiscal period to validate  """  
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class CheckFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckFiscalYear_input:
   """ Required : 
   proposedFiscalYear
   proposedSuffix
   ipCalendar
   """  
   def __init__(self, obj):
      self.proposedFiscalYear:int = obj["proposedFiscalYear"]
      """  The proposed Fiscal Year  """  
      self.proposedSuffix:str = obj["proposedSuffix"]
      """  The proposed Fiscal Year suffix  """  
      self.ipCalendar:str = obj["ipCalendar"]
      """  Calendar ID  """  
      pass

class CheckFiscalYear_output:
   def __init__(self, obj):
      pass

class CheckGroupID_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class CheckGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      self.opCreateGroup:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   genID
   """  
   def __init__(self, obj):
      self.genID:int = obj["genID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ConsImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  This is the book the import file is being loaded to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ImportDate:str = obj["ImportDate"]
      """  Date the input file was imported  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Date used on the GLJrnDtl  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.JrnlHeadDesc:str = obj["JrnlHeadDesc"]
      """  Journal Header Description  """  
      self.ImportStatus:str = obj["ImportStatus"]
      """   Indicates the status of the Import from Subsidiary.
C = Complete  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  Import/Export file name.  """  
      self.GenerationLog:str = obj["GenerationLog"]
      """  The consolidation generation log.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToRegenerate:bool = obj["OkToRegenerate"]
      """  logical indicating if it is okay to regenerate  """  
      self.LastImportDate:str = obj["LastImportDate"]
      """  Date of Last Import  """  
      self.LastGroup:str = obj["LastGroup"]
      """  Last Journal Group imported  """  
      self.LastDescription:str = obj["LastDescription"]
      """  Description of the last import  """  
      self.LastGenID:int = obj["LastGenID"]
      """  Last generation ID  """  
      self.LastImportFile:str = obj["LastImportFile"]
      """  Last Import File Name  """  
      self.OkayToAddNewGroup:bool = obj["OkayToAddNewGroup"]
      """  Logical indicating the user wants to create a new GLJrnGrp record.  """  
      self.DisableGroupFields:bool = obj["DisableGroupFields"]
      """  Logical indicating the group fields are to be disabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsImportListTableset:
   def __init__(self, obj):
      self.ConsImportList:list[Erp_Tablesets_ConsImportListRow] = obj["ConsImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConsImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  This is the book the import file is being loaded to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ImportDate:str = obj["ImportDate"]
      """  Date the input file was imported  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Date used on the GLJrnDtl  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.JrnlHeadDesc:str = obj["JrnlHeadDesc"]
      """  Journal Header Description  """  
      self.ImportStatus:str = obj["ImportStatus"]
      """   Indicates the status of the Import from Subsidiary.
C = Complete  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  Import/Export file name.  """  
      self.GenerationLog:str = obj["GenerationLog"]
      """  The consolidation generation log.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToRegenerate:bool = obj["OkToRegenerate"]
      """  logical indicating if it is okay to regenerate  """  
      self.LastImportDate:str = obj["LastImportDate"]
      """  Date of Last Import  """  
      self.LastGroup:str = obj["LastGroup"]
      """  Last Journal Group imported  """  
      self.LastDescription:str = obj["LastDescription"]
      """  Description of the last import  """  
      self.LastGenID:int = obj["LastGenID"]
      """  Last generation ID  """  
      self.LastImportFile:str = obj["LastImportFile"]
      """  Last Import File Name  """  
      self.OkayToAddNewGroup:bool = obj["OkayToAddNewGroup"]
      """  Logical indicating the user wants to create a new GLJrnGrp record.  """  
      self.DisableGroupFields:bool = obj["DisableGroupFields"]
      """  Logical indicating the group fields are to be disabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  """  
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if all records for this group were posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFiscalPeriod:str = obj["DspFiscalPeriod"]
      """  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BookModeDisabled:bool = obj["BookModeDisabled"]
      """  Indicates that Book Mode cannot be changed by user  """  
      self.DspFiscalPeriodType:str = obj["DspFiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      self.BookIDDescription:str = obj["BookIDDescription"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.JournalCodeAllowStatJournals:bool = obj["JournalCodeAllowStatJournals"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportSubsidTableset:
   def __init__(self, obj):
      self.ConsImport:list[Erp_Tablesets_ConsImportRow] = obj["ConsImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MCConsolImportExportRow:
   def __init__(self, obj):
      self.DebitAmt:int = obj["DebitAmt"]
      """  Transaction amount.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  Transaction amount.  """  
      self.AcctDesc:str = obj["AcctDesc"]
      """  A character string made up of Div, Dept, Chart and Segment abbreviations concatenated into the full GL account description.  This should be formatted exactly how the user expects to see their account numbers (including separators).  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.SegValue1:str = obj["SegValue1"]
      self.GLAccount:str = obj["GLAccount"]
      """  GL Account  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segment Value 2  """  
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      """  Segment Value 4  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segment Value 5  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segment Value 6  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segment Value 7  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segment Value 8  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segment Value 9  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segment Value 11  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segment Value 12  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segment Value 13  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segment Value 14  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segment Value 15  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segment Value 16  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segment Value 17  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segment Value 18  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segment Value 19  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segment Value 20  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Company where the data originated  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Source Book ID  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Source GL Account  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source  Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Num  """  
      self.SrcCOACode:str = obj["SrcCOACode"]
      """  Source COA Code  """  
      self.SrcJournalLIne:int = obj["SrcJournalLIne"]
      """  Source Journal LIne  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MCConsolImportExportTableset:
   def __init__(self, obj):
      self.MCConsolImportExport:list[Erp_Tablesets_MCConsolImportExportRow] = obj["MCConsolImportExport"]
      self.GLJrnGrp:list[Erp_Tablesets_GLJrnGrpRow] = obj["GLJrnGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtImportSubsidTableset:
   def __init__(self, obj):
      self.ConsImport:list[Erp_Tablesets_ConsImportRow] = obj["ConsImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateJournal_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_MCConsolImportExportTableset] = obj["ds1"]
      pass

class GenerateJournal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_MCConsolImportExportTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class GetBookCalendar_input:
   """ Required : 
   ipBookID
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class GetBookCalendar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   genID
   """  
   def __init__(self, obj):
      self.genID:int = obj["genID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportSubsidTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportSubsidTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportSubsidTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewConsImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class GetNewConsImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseConsImport
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseConsImport:str = obj["whereClauseConsImport"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportSubsidTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GroupChangeWarning_input:
   """ Required : 
   ipBook
   ds
   """  
   def __init__(self, obj):
      self.ipBook:str = obj["ipBook"]
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class GroupChangeWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      self.warnMsg:str = obj["parameters"]
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

class ParseInputFile_input:
   """ Required : 
   sFileSubPath
   ds
   """  
   def __init__(self, obj):
      self.sFileSubPath:str = obj["sFileSubPath"]
      """  Imported file subpath of SpecialFolder.UserData.  """  
      self.ds:list[Erp_Tablesets_MCConsolImportExportTableset] = obj["ds"]
      pass

class ParseInputFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MCConsolImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImportSubsidTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImportSubsidTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateJournal_input:
   """ Required : 
   ipJournalCode
   ds
   """  
   def __init__(self, obj):
      self.ipJournalCode:str = obj["ipJournalCode"]
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

class ValidateJournal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportSubsidTableset] = obj["ds"]
      pass

      """  output parameters  """  

