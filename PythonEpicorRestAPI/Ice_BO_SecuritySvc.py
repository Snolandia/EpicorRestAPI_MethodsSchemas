import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SecuritySvc
# Description: Security business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Securities(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Securities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Securities
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecurityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities",headers=creds) as resp:
           return await resp.json()

async def post_Securities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Securities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SecurityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SecurityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Securities_Company_SecCode(Company, SecCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Security item
   Description: Calls GetByID to retrieve the Security item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Security
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SecurityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Securities_Company_SecCode(Company, SecCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Security for the service
   Description: Calls UpdateExt to update Security. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Security
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SecurityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Securities_Company_SecCode(Company, SecCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Security item
   Description: Call UpdateExt to delete Security item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Security
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/Securities(" + Company + "," + SecCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecurityListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSecurity, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSecurity=" + whereClauseSecurity
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, secCode, epicorHeaders = None):
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "secCode=" + secCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDEx
   Description: This method returns a dataset representing a Security with a blank CompanyID
   OperationID: GetByIDEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupUserList(epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupUserList
   Description: This method returns a double-delimited list of value-name pairs of all
Users and Groups.  This could be used to provide a "picker list" as a
starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetGroupUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetListEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListEx
   Description: This method returns a list of Security, including those with blank Company ID
   OperationID: GetListEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMethodList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMethodList
   Description: This method returns a delimited list of the public methods for the given
object.  This could be used to provide a "picker list" as a starting point
when adding a new Security record related to a method.  These would look the
same as a Security record for an object, but with a SecCode field that has
been appended with "." + MethodName.
For example, a security record for the
   OperationID: GetMethodList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSubSecurity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSubSecurity
   Description: This method creates a new sub security row
   OperationID: GetNewSubSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSubSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSubSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopySecurityRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopySecurityRow
   Description: Copies an existing security row to a new row.
   OperationID: CopySecurityRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopySecurityRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopySecurityRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsEx
   Description: This method returns a list of Security, including those with blank Company ID
   OperationID: GetRowsEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GlobalRecordFound(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GlobalRecordFound
   OperationID: GlobalRecordFound
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GlobalRecordFound_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlobalRecordFound_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSecurity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSecurity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SecurityGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SecurityGetByID
   Description: Retrieve correct record based on tenancy.
   OperationID: SecurityGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SecurityGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SecurityGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SecCodeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SecCodeChanging
   Description: Find seccode if company was not supplied.
   OperationID: SecCodeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SecCodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SecCodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: Set field values prior to calling update method. Moved client code to the server.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSelectedAccess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSelectedAccess
   Description: Update select rows with new access type.
   OperationID: SetSelectedAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSelectedAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSelectedAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserRows(epicorHeaders = None):
   """  
   Summary: Invoke method AddUserRows
   Description: Add user and groups to Access table
   OperationID: AddUserRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AddSecurityInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddSecurityInfo
   Description: Populate access tables with access code.
   OperationID: AddSecurityInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSecurityInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSecurityInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyExistingSecCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyExistingSecCode
   Description: Copies an existing security row to a new row.
   OperationID: CopyExistingSecCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyExistingSecCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyExistingSecCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CGCCodeList(epicorHeaders = None):
   """  
   Summary: Invoke method CGCCodeList
   Description: Build cgccode list.
   OperationID: CGCCodeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CGCCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AllCompaniesChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AllCompaniesChanging
   Description: Verify if all company can be set
   OperationID: AllCompaniesChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AllCompaniesChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllCompaniesChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SecurityListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecurityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SecurityRow] = obj["value"]
      pass

class Ice_Tablesets_SecurityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account must have Security Manager privileges to access the options.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """  Sub-Security Code Sequence.  """  
      self.Disconnected:bool = obj["Disconnected"]
      """  Should this security code be available to a disconnect user?  If so, the value should be YES.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  """  
      self.CustWebAvailable:bool = obj["CustWebAvailable"]
      """   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecurityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.EntryList:str = obj["EntryList"]
      """  List of security groups the user belongs to.  """  
      self.NoEntryList:str = obj["NoEntryList"]
      """  List of security groups the user belongs to.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account must have Security Manager privileges to access the options.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ParentSecCode:str = obj["ParentSecCode"]
      """  Parent Security ID for a Sub-Security Code.  Only Set for Security Codes that are subcomponents of a regular security code.  For example: Costing information in Job Tracker.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """  Sub-Security Code Sequence.  """  
      self.Disconnected:bool = obj["Disconnected"]
      """  Should this security code be available to a disconnect user?  If so, the value should be YES.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if the menu item associated to this security code requires the employee to be a material handler.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  """  
      self.ServTech:bool = obj["ServTech"]
      """  Indicates if the menu item associated with this security code requires the employee goes out on service calls.  """  
      self.CustWebAvailable:bool = obj["CustWebAvailable"]
      """   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalSecurityMgr:bool = obj["GlobalSecurityMgr"]
      """  GlobalSecurityMgr  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AvailableUsers:str = obj["AvailableUsers"]
      self.DisallowAccess:str = obj["DisallowAccess"]
      self.DisallowAll:bool = obj["DisallowAll"]
      self.MenuOptions:str = obj["MenuOptions"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.Access:str = obj["Access"]
      self.CanModify:bool = obj["CanModify"]
      self.Preupdated:bool = obj["Preupdated"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddSecurityInfo_input:
   """ Required : 
   ds
   dsSecurityList
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      pass

class AddSecurityInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      pass

      """  output parameters  """  

class AddUserRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityAccessTableset] = obj["returnObj"]
      pass

class AllCompaniesChanging_input:
   """ Required : 
   secCode
   currentCompany
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      self.currentCompany:str = obj["currentCompany"]
      pass

class AllCompaniesChanging_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.company:str = obj["parameters"]
      self.companyVisibility:int = obj["parameters"]
      pass

      """  output parameters  """  

class CGCCodeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CopyExistingSecCode_input:
   """ Required : 
   sourceCompany
   sourceSecurityCode
   targetCompany
   targetSecurityCode
   """  
   def __init__(self, obj):
      self.sourceCompany:str = obj["sourceCompany"]
      """  The source company ID  """  
      self.sourceSecurityCode:str = obj["sourceSecurityCode"]
      """  The source security code.  """  
      self.targetCompany:str = obj["targetCompany"]
      """  Target company.  """  
      self.targetSecurityCode:str = obj["targetSecurityCode"]
      """  Target security code.  """  
      pass

class CopyExistingSecCode_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

class CopySecurityRow_input:
   """ Required : 
   ds
   sourceCompany
   sourceSecurityCode
   targetCompany
   targetSecurityCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.sourceCompany:str = obj["sourceCompany"]
      """  The source company ID  """  
      self.sourceSecurityCode:str = obj["sourceSecurityCode"]
      """  The source security code.  """  
      self.targetCompany:str = obj["targetCompany"]
      """  Target company.  """  
      self.targetSecurityCode:str = obj["targetSecurityCode"]
      """  Target security code.  """  
      pass

class CopySecurityRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   company
   secCode
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.secCode:str = obj["secCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByIDEx_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      """  The security code  """  
      pass

class GetByIDEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   secCode
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.secCode:str = obj["secCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

class GetGroupUserList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupUserList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListEx_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecurityListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMethodList_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      """  The security code for which you want the list of methods.  """  
      pass

class GetMethodList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.methodList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewSecurity_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewSecurity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSubSecurity_input:
   """ Required : 
   ds
   parentSecCode
   secCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.parentSecCode:str = obj["parentSecCode"]
      """  The parent security code  """  
      self.secCode:str = obj["secCode"]
      """  The security code  """  
      pass

class GetNewSubSecurity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsEx_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetRowsEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSecurity
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSecurity:str = obj["whereClauseSecurity"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GlobalRecordFound_input:
   """ Required : 
   SecCode
   """  
   def __init__(self, obj):
      self.SecCode:str = obj["SecCode"]
      pass

class GlobalRecordFound_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.Company:str = obj["parameters"]
      self.CompanyVisibility:int = obj["parameters"]
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

class Ice_Tablesets_GroupAccessRow:
   def __init__(self, obj):
      self.Access:str = obj["Access"]
      self.SecGroupCode:str = obj["SecGroupCode"]
      self.SecGroupDesc:str = obj["SecGroupDesc"]
      self.Select:bool = obj["Select"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecurityAccessTableset:
   def __init__(self, obj):
      self.GroupAccess:list[Ice_Tablesets_GroupAccessRow] = obj["GroupAccess"]
      self.UserAccess:list[Ice_Tablesets_UserAccessRow] = obj["UserAccess"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SecurityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account must have Security Manager privileges to access the options.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """  Sub-Security Code Sequence.  """  
      self.Disconnected:bool = obj["Disconnected"]
      """  Should this security code be available to a disconnect user?  If so, the value should be YES.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  """  
      self.CustWebAvailable:bool = obj["CustWebAvailable"]
      """   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecurityListTableset:
   def __init__(self, obj):
      self.SecurityList:list[Ice_Tablesets_SecurityListRow] = obj["SecurityList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SecurityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.EntryList:str = obj["EntryList"]
      """  List of security groups the user belongs to.  """  
      self.NoEntryList:str = obj["NoEntryList"]
      """  List of security groups the user belongs to.  """  
      self.SecurityMgr:bool = obj["SecurityMgr"]
      """  Indicates that the user account must have Security Manager privileges to access the options.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ParentSecCode:str = obj["ParentSecCode"]
      """  Parent Security ID for a Sub-Security Code.  Only Set for Security Codes that are subcomponents of a regular security code.  For example: Costing information in Job Tracker.  """  
      self.ParentSeqNum:int = obj["ParentSeqNum"]
      """  Sub-Security Code Sequence.  """  
      self.Disconnected:bool = obj["Disconnected"]
      """  Should this security code be available to a disconnect user?  If so, the value should be YES.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if the menu item associated to this security code requires the employee to be a Shipping/Receiving worker.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if menu item associated to this security code requires that the employee be a shop supervisor.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if the menu item associated to this security code requires the employee to be a material handler.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if the menu item associated with this security code requires the employee works on the manufacturing line.  """  
      self.ServTech:bool = obj["ServTech"]
      """  Indicates if the menu item associated with this security code requires the employee goes out on service calls.  """  
      self.CustWebAvailable:bool = obj["CustWebAvailable"]
      """   indicating if this menu is available in Web Menu for a customer.
If field cannot be changed if SysWebAvailable is set to no.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalSecurityMgr:bool = obj["GlobalSecurityMgr"]
      """  GlobalSecurityMgr  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AvailableUsers:str = obj["AvailableUsers"]
      self.DisallowAccess:str = obj["DisallowAccess"]
      self.DisallowAll:bool = obj["DisallowAll"]
      self.MenuOptions:str = obj["MenuOptions"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.Access:str = obj["Access"]
      self.CanModify:bool = obj["CanModify"]
      self.Preupdated:bool = obj["Preupdated"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecurityTableset:
   def __init__(self, obj):
      self.Security:list[Ice_Tablesets_SecurityRow] = obj["Security"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtSecurityTableset:
   def __init__(self, obj):
      self.Security:list[Ice_Tablesets_SecurityRow] = obj["Security"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserAccessRow:
   def __init__(self, obj):
      self.Access:str = obj["Access"]
      self.Name:str = obj["Name"]
      self.SecurityMgr:bool = obj["SecurityMgr"]
      self.UserID:str = obj["UserID"]
      self.Select:bool = obj["Select"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class PreUpdate_input:
   """ Required : 
   ds
   dsSecurityList
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      pass

      """  output parameters  """  

class SecCodeChanging_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      pass

class SecCodeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.company:str = obj["parameters"]
      pass

      """  output parameters  """  

class SecurityGetByID_input:
   """ Required : 
   company
   secCode
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.secCode:str = obj["secCode"]
      pass

class SecurityGetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityTableset] = obj["returnObj"]
      pass

class SetSelectedAccess_input:
   """ Required : 
   dsSecurityList
   table
   newAccess
   """  
   def __init__(self, obj):
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      self.table:str = obj["table"]
      self.newAccess:str = obj["newAccess"]
      pass

class SetSelectedAccess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSecurityList"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSecurityTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSecurityTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

