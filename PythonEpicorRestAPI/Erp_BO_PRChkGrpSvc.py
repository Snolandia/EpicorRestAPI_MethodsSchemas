import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PRChkGrpSvc
# Description: Payroll Check Group.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PRChkGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRChkGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRChkGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps",headers=creds) as resp:
           return await resp.json()

async def post_PRChkGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRChkGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRChkGrps_Company_GroupID(Company, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRChkGrp item
   Description: Calls GetByID to retrieve the PRChkGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRChkGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRChkGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRChkGrp for the service
   Description: Calls UpdateExt to update PRChkGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRChkGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRChkGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRChkGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRChkGrp item
   Description: Call UpdateExt to delete PRChkGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRChkGrp
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/PRChkGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRChkGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRChkGrp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePRChkGrp=" + whereClausePRChkGrp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCheckDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCheckDate
   Description: Method to call to update the fiscal period fields for the new check date.
   OperationID: ChangeCheckDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCheckDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCheckDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostGroup
   Description: Method to call when posting checks for a specific group.  Posting of a group causes
the PRChkGrp record to be deleted from the database if all checks in the group posted correctly.
   OperationID: PostGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostGroup
   Description: Method to call before posting checks for a specific group.  It will check
to see if the register has printed or not.  The text for this question is returned
in RegisterText.  It will also check to see if payroll is interfaced with
G/L.  The text for this question is returned in InterfacedText.
For both questions, if the answer is yes, posting can continue,
otherwise posting is canceled.
   OperationID: PrePostGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdateCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdateCheck
   Description: Method to call to perform pre-validations on the update of a check group record.
The pre-validations involve asking the user various questions about
the changes being made and if the changes will be ok.
The validations are:
1) The check date is less than today or more than 14 days out
2) The check date changed, which will require taxes and deductions to be
recalculated.
3) The Deduction period value is zero.
If the user answers yes to all questions, the save can continue.  If
the user answers no to any question, the update is canceled.
This method should be called prior to the Update method.
   OperationID: PreUpdateCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdateCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdateCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockGroup
   Description: Method to call to unlock a group record.  This method should be called whenever
the group no longer needs to be locked.  The group no longer needs to be locked
when the payroll entry object is closed, or when a different group is selected.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsNoLock
   Description: The wrapper method for GetRows. Retrieve groups ignoring Active User lock
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateNoLock
   Description: The wrapper method for GetRows. Update the group ignoring Active User lock
   OperationID: UpdateNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGroupAccess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGroupAccess
   Description: The method validates that the user has access rights to the the group and payroll classes which are used in the group
   OperationID: CheckGroupAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRChkGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRChkGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRChkGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRChkGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRChkGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PRChkGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRChkGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRChkGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRChkGrpRow] = obj["value"]
      pass

class Erp_Tablesets_PRChkGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user id that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  """  
      self.PEDate:str = obj["PEDate"]
      """  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  """  
      self.DeductionPeriod:int = obj["DeductionPeriod"]
      """   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  """  
      self.TaxesNeeded:bool = obj["TaxesNeeded"]
      """   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  """  
      self.ChecksPrinted:bool = obj["ChecksPrinted"]
      """  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  """  
      self.RegisterPrinted:bool = obj["RegisterPrinted"]
      """  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains posting error messages. Possible messages are;  """  
      self.UpdateAccrual:bool = obj["UpdateAccrual"]
      """  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludedPayFrequencies:str = obj["IncludedPayFrequencies"]
      self.ChecksInGroup:int = obj["ChecksInGroup"]
      self.BaseHours:int = obj["BaseHours"]
      self.PremiumHours:int = obj["PremiumHours"]
      self.TotalGross:int = obj["TotalGross"]
      self.TotalTaxes:int = obj["TotalTaxes"]
      self.TotalDeductions:int = obj["TotalDeductions"]
      self.NetAmount:int = obj["NetAmount"]
      self.PayClassesDescriptions:str = obj["PayClassesDescriptions"]
      self.NonPaidPayClasses:str = obj["NonPaidPayClasses"]
      self.NonPaidPayClassesDesc:str = obj["NonPaidPayClassesDesc"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.PRChecksExist:bool = obj["PRChecksExist"]
      self.DispPostErrors:str = obj["DispPostErrors"]
      self.EnablePrintChecks:bool = obj["EnablePrintChecks"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user id that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  """  
      self.PEDate:str = obj["PEDate"]
      """  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  """  
      self.DeductionPeriod:int = obj["DeductionPeriod"]
      """   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  """  
      self.TaxesNeeded:bool = obj["TaxesNeeded"]
      """   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  """  
      self.ChecksPrinted:bool = obj["ChecksPrinted"]
      """  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  """  
      self.RegisterPrinted:bool = obj["RegisterPrinted"]
      """  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains posting error messages. Possible messages are;  """  
      self.UpdateAccrual:bool = obj["UpdateAccrual"]
      """  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilePath:str = obj["FilePath"]
      """  FilePath  """  
      self.DownloadStatus:int = obj["DownloadStatus"]
      """  DownloadStatus  """  
      self.IncludeOutdatedLabor:bool = obj["IncludeOutdatedLabor"]
      """  IncludeOutdatedLabor  """  
      self.DispPostErrors:str = obj["DispPostErrors"]
      self.EnablePrintChecks:bool = obj["EnablePrintChecks"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.IncludedPayFrequencies:str = obj["IncludedPayFrequencies"]
      self.NetAmount:int = obj["NetAmount"]
      self.NonPaidPayClasses:str = obj["NonPaidPayClasses"]
      self.NonPaidPayClassesDesc:str = obj["NonPaidPayClassesDesc"]
      self.PayClassesDescriptions:str = obj["PayClassesDescriptions"]
      self.PRChecksExist:bool = obj["PRChecksExist"]
      self.PremiumHours:int = obj["PremiumHours"]
      self.TotalDeductions:int = obj["TotalDeductions"]
      self.TotalGross:int = obj["TotalGross"]
      self.TotalTaxes:int = obj["TotalTaxes"]
      self.BaseHours:int = obj["BaseHours"]
      self.ChecksInGroup:int = obj["ChecksInGroup"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBankAcctID_input:
   """ Required : 
   ProposedBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ProposedBankAcctID:str = obj["ProposedBankAcctID"]
      """  The proposed bank account id  """  
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class ChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCheckDate_input:
   """ Required : 
   ProposedCheckDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedCheckDate:str = obj["ProposedCheckDate"]
      """  The proposed check date  """  
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class ChangeCheckDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckGroupAccess_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The code group  """  
      pass

class CheckGroupAccess_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true - the user has access to the group, false - the user doesn't have access to the group  """  
      pass

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

class Erp_Tablesets_PRChkGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user id that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  """  
      self.PEDate:str = obj["PEDate"]
      """  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  """  
      self.DeductionPeriod:int = obj["DeductionPeriod"]
      """   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  """  
      self.TaxesNeeded:bool = obj["TaxesNeeded"]
      """   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  """  
      self.ChecksPrinted:bool = obj["ChecksPrinted"]
      """  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  """  
      self.RegisterPrinted:bool = obj["RegisterPrinted"]
      """  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains posting error messages. Possible messages are;  """  
      self.UpdateAccrual:bool = obj["UpdateAccrual"]
      """  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludedPayFrequencies:str = obj["IncludedPayFrequencies"]
      self.ChecksInGroup:int = obj["ChecksInGroup"]
      self.BaseHours:int = obj["BaseHours"]
      self.PremiumHours:int = obj["PremiumHours"]
      self.TotalGross:int = obj["TotalGross"]
      self.TotalTaxes:int = obj["TotalTaxes"]
      self.TotalDeductions:int = obj["TotalDeductions"]
      self.NetAmount:int = obj["NetAmount"]
      self.PayClassesDescriptions:str = obj["PayClassesDescriptions"]
      self.NonPaidPayClasses:str = obj["NonPaidPayClasses"]
      self.NonPaidPayClassesDesc:str = obj["NonPaidPayClassesDesc"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.PRChecksExist:bool = obj["PRChecksExist"]
      self.DispPostErrors:str = obj["DispPostErrors"]
      self.EnablePrintChecks:bool = obj["EnablePrintChecks"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkGrpListTableset:
   def __init__(self, obj):
      self.PRChkGrpList:list[Erp_Tablesets_PRChkGrpListRow] = obj["PRChkGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRChkGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing paychecks to be entered the user establishes a "Group ID".  All paychecks belong to a group until the group is posted.  The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the check date and fiscal period defaults for paychecks assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user id that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user id that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time.  Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check date to be used when printing checks for this group. Default to current system date. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is set based on this date.  """  
      self.PEDate:str = obj["PEDate"]
      """  This is used for printing on the checks, and controlling what labor records are used in the transfer from JC process.  """  
      self.PayWeekly:bool = obj["PayWeekly"]
      """  Indicates if employees with a PayFrequency = "Weekly" are to be paid in this check run group.  """  
      self.PayBiWeekly:bool = obj["PayBiWeekly"]
      """  Indicates if employees with a PayFrequency = "Biweekly" are to be paid in this check run group.  """  
      self.PaySemiMonthly:bool = obj["PaySemiMonthly"]
      """  Indicates if employees with a PayFrequency = "Semimonthly" are to be paid in this check run group.  """  
      self.PayMonthly:bool = obj["PayMonthly"]
      """  Indicates if employees with a PayFrequency = "Monthly" are to be paid in this check run group.  """  
      self.PayClasses:str = obj["PayClasses"]
      """  A list of employee classes  that are to be paid in this data entry group. Only employees where PREmpDat.ClassID are in this list are to be paid from this group. Use the system  "List-Delim" as the delimiter character.  """  
      self.DeductionPeriod:int = obj["DeductionPeriod"]
      """   Indicates which deduction period this payroll run is for.  Deductions for an employee will be taken when the corresponding period in the PREmpDed record is true.
Note: zero = no deductions will be taken.  """  
      self.TaxesNeeded:bool = obj["TaxesNeeded"]
      """   An internal flag to indicate if the tax calculation needs to be performed. If any check detail record is entered or modified which affects taxes this is set to Yes.  This includes changes in gross pay,  deductions,  and taxes.  When this is set to "Yes" the printing of checks, reports, and posting options are disabled.  When "NO"  the Calculate Tax option is disabled.
After the system does the calculations TaxesNeeded, ChecksPrinted, and RegisterPrinted is set to NO.  """  
      self.ChecksPrinted:bool = obj["ChecksPrinted"]
      """  Indicates if checks have been printed.  This is set to Yes during the check print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to control the posting option.  The post function is allowed when TaxesCalculated = Yes, ChecksPrinted = Yes and RegisterPrinted = Yes.  """  
      self.RegisterPrinted:bool = obj["RegisterPrinted"]
      """  An internal flag to indicate if the payroll register has been printed. This is set to Yes during the register print process. If any check detail record is entered or modified this is set to NO.  This includes changes in gross pay,  deductions,  and taxes. It is used to issue a warning message during the posting process if register has not been printed.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains posting error messages. Possible messages are;  """  
      self.UpdateAccrual:bool = obj["UpdateAccrual"]
      """  Indicates if the employees' vacation/sick remaining hours are to get updated with the period accrual.  The updating occurs as part of the posting process.  This is not accessible if this is a manual check group (ManualChecks = Yes) and it will always be set to NO.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilePath:str = obj["FilePath"]
      """  FilePath  """  
      self.DownloadStatus:int = obj["DownloadStatus"]
      """  DownloadStatus  """  
      self.IncludeOutdatedLabor:bool = obj["IncludeOutdatedLabor"]
      """  IncludeOutdatedLabor  """  
      self.DispPostErrors:str = obj["DispPostErrors"]
      self.EnablePrintChecks:bool = obj["EnablePrintChecks"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.IncludedPayFrequencies:str = obj["IncludedPayFrequencies"]
      self.NetAmount:int = obj["NetAmount"]
      self.NonPaidPayClasses:str = obj["NonPaidPayClasses"]
      self.NonPaidPayClassesDesc:str = obj["NonPaidPayClassesDesc"]
      self.PayClassesDescriptions:str = obj["PayClassesDescriptions"]
      self.PRChecksExist:bool = obj["PRChecksExist"]
      self.PremiumHours:int = obj["PremiumHours"]
      self.TotalDeductions:int = obj["TotalDeductions"]
      self.TotalGross:int = obj["TotalGross"]
      self.TotalTaxes:int = obj["TotalTaxes"]
      self.BaseHours:int = obj["BaseHours"]
      self.ChecksInGroup:int = obj["ChecksInGroup"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRChkGrpTableset:
   def __init__(self, obj):
      self.PRChkGrp:list[Erp_Tablesets_PRChkGrpRow] = obj["PRChkGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPRChkGrpTableset:
   def __init__(self, obj):
      self.PRChkGrp:list[Erp_Tablesets_PRChkGrpRow] = obj["PRChkGrp"]
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
      self.returnObj:list[Erp_Tablesets_PRChkGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRChkGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRChkGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRChkGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPRChkGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class GetNewPRChkGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsNoLock_input:
   """ Required : 
   whereClausePRChkGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRChkGrp:str = obj["whereClausePRChkGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRChkGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRChkGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRChkGrp:str = obj["whereClausePRChkGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRChkGrpTableset] = obj["returnObj"]
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

class PostGroup_input:
   """ Required : 
   PostGroupID
   """  
   def __init__(self, obj):
      self.PostGroupID:str = obj["PostGroupID"]
      """  The group id of the group of checks to be posted  """  
      pass

class PostGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PostErrors:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrePostGroup_input:
   """ Required : 
   PostGroupID
   """  
   def __init__(self, obj):
      self.PostGroupID:str = obj["PostGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class PrePostGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RegisterText:str = obj["parameters"]
      self.InterfacedText:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdateCheck_input:
   """ Required : 
   GroupID
   CheckDate
   DeductionPeriod
   ds
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  The group id  """  
      self.CheckDate:str = obj["CheckDate"]
      """  The check date  """  
      self.DeductionPeriod:int = obj["DeductionPeriod"]
      """  The deduction period to validate  """  
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class PreUpdateCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DateRangeText:str = obj["parameters"]
      self.RecalcTaxAndDedText:str = obj["parameters"]
      self.DeductionPeriodText:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.ds:list[Erp_Tablesets_UpdExtPRChkGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPRChkGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class UpdateNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PRChkGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

