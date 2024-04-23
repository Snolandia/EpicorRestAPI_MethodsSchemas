import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LogInvGrpSvc
# Description: Logged AP Invoice Group business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LogInvGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LogInvGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LogInvGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogInvGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/LogInvGrps",headers=creds) as resp:
           return await resp.json()

async def post_LogInvGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LogInvGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LogInvGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LogInvGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/LogInvGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LogInvGrps_Company_GroupID(Company, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LogInvGrp item
   Description: Calls GetByID to retrieve the LogInvGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LogInvGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LogInvGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/LogInvGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LogInvGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LogInvGrp for the service
   Description: Calls UpdateExt to update LogInvGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LogInvGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LogInvGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/LogInvGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LogInvGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LogInvGrp item
   Description: Call UpdateExt to delete LogInvGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LogInvGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/LogInvGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LogInvGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLogInvGrp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLogInvGrp=" + whereClauseLogInvGrp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZeroAmtTaxRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes LogAPInvTax records which have zero amounts
Since Logged Invoices TAx logic calculates tax conditionally only for the first tax line the invoice could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLogInvGrpNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLogInvGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewLogInvGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLogInvGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogInvGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsNoLock
   Description: GetRows method with disabled ActiveUser functionality.
   OperationID: GetRowsNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofApplyDate
   Description: This method should be called to validate the new apply date entered by the user.
This method will additionally return a message to present to the user if the date is greater than
the client today date.
   OperationID: OnChangeofApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostGroupInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostGroupInvoices
   Description: Method to call before posting invoices for a specific group.  If the G/L module is installed,
this method will determine if A/P is interfaced with G/L.  If it is not, text of a question
is returned indicating this and asking if it is ok to continue.  This question should be
presented to the user in yes/no format.  If the user replies no, the PostGroupInvoices method
should not be called.  This method can also throw exceptions if certain configuration records
do not exist.  This method will also check if variances exist on the header or lines and return
message text asking the user if they would like to continue nor not with posting.
validationResult is a string divided by two delimiters, first delimiter is the index and second one the error message.
Index 0 -> LN Error
Index 1 -> GL Error
Index 2 -> Variance Error
Index 3 -> Tax Error
NOTE: to add a new message please continue with the next index if no error message is assigned to the list, please set string.Empty.
   OperationID: PrePostGroupInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGroupInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGroupInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockGroup
   Description: Method to call to unlock a group record.  This method should be called whenever
the group no longer needs to be locked.  The group no longer needs to be locked
when the invoice object is closed, or when a different group is selected.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLogInvGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLogInvGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLogInvGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLogInvGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLogInvGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LogInvGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogInvGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogInvGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LogInvGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LogInvGrpRow] = obj["value"]
      pass

class Erp_Tablesets_LogInvGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are;
"Invoice with no detail",
 "Invoice Total does not agree with vendor 's total"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseTotal:int = obj["BaseTotal"]
      self.DispPostErrorLog:str = obj["DispPostErrorLog"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogInvGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are;
"Invoice with no detail",
 "Invoice Total does not agree with vendor 's total"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseTotal:int = obj["BaseTotal"]
      self.DispPostErrorLog:str = obj["DispPostErrorLog"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteZeroAmtTaxRec_input:
   """ Required : 
   PostGroupID
   """  
   def __init__(self, obj):
      self.PostGroupID:str = obj["PostGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class DeleteZeroAmtTaxRec_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LogInvGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are;
"Invoice with no detail",
 "Invoice Total does not agree with vendor 's total"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseTotal:int = obj["BaseTotal"]
      self.DispPostErrorLog:str = obj["DispPostErrorLog"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogInvGrpListTableset:
   def __init__(self, obj):
      self.LogInvGrpList:list[Erp_Tablesets_LogInvGrpListRow] = obj["LogInvGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LogInvGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are;
"Invoice with no detail",
 "Invoice Total does not agree with vendor 's total"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseTotal:int = obj["BaseTotal"]
      self.DispPostErrorLog:str = obj["DispPostErrorLog"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LogInvGrpTableset:
   def __init__(self, obj):
      self.LogInvGrp:list[Erp_Tablesets_LogInvGrpRow] = obj["LogInvGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtLogInvGrpTableset:
   def __init__(self, obj):
      self.LogInvGrp:list[Erp_Tablesets_LogInvGrpRow] = obj["LogInvGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LogInvGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LogInvGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LogInvGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLogInvGrpNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

class GetNewLogInvGrpNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLogInvGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

class GetNewLogInvGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsNoLock_input:
   """ Required : 
   whereClauseLogInvGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLogInvGrp:str = obj["whereClauseLogInvGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLogInvGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLogInvGrp:str = obj["whereClauseLogInvGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LogInvGrpTableset] = obj["returnObj"]
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

class OnChangeofApplyDate_input:
   """ Required : 
   GroupID
   NewApplyDate
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  Group ID.  """  
      self.NewApplyDate:str = obj["NewApplyDate"]
      """  New Apply Date.  """  
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

class OnChangeofApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DateMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePostGroupInvoices_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The Group ID of the Group to post  """  
      pass

class PrePostGroupInvoices_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class UnlockGroup_input:
   """ Required : 
   InGroupID
   """  
   def __init__(self, obj):
      self.InGroupID:str = obj["InGroupID"]
      """  The group id of the group record to unlock  """  
      pass

class UnlockGroup_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLogInvGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLogInvGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LogInvGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

