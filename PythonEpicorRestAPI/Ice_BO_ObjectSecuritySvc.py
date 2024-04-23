import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ObjectSecuritySvc
# Description: Service level security.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ObjectSecurities(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ObjectSecurities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ObjectSecurities
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities",headers=creds) as resp:
           return await resp.json()

async def post_ObjectSecurities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ObjectSecurities
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ObjectSecurities_Company_SecCode(Company, SecCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ObjectSecurity item
   Description: Calls GetByID to retrieve the ObjectSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ObjectSecurity
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ObjectSecurities_Company_SecCode(Company, SecCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ObjectSecurity for the service
   Description: Calls UpdateExt to update ObjectSecurity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ObjectSecurity
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
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ObjectSecurities_Company_SecCode(Company, SecCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ObjectSecurity item
   Description: Call UpdateExt to delete ObjectSecurity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ObjectSecurity
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurities(" + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ObjectSecurityMethods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ObjectSecurityMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ObjectSecurityMethods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ObjectSecurityMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods",headers=creds) as resp:
           return await resp.json()

async def post_ObjectSecurityMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ObjectSecurityMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ObjectSecurityMethods_Company_SecCode(Company, SecCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ObjectSecurityMethod item
   Description: Calls GetByID to retrieve the ObjectSecurityMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ObjectSecurityMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ObjectSecurityMethods_Company_SecCode(Company, SecCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ObjectSecurityMethod for the service
   Description: Calls UpdateExt to update ObjectSecurityMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ObjectSecurityMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ObjectSecurityMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ObjectSecurityMethods_Company_SecCode(Company, SecCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ObjectSecurityMethod item
   Description: Call UpdateExt to delete ObjectSecurityMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ObjectSecurityMethod
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/ObjectSecurityMethods(" + Company + "," + SecCode + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSecurity, whereClauseObjectSecurityMethod, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSecurity=" + whereClauseSecurity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseObjectSecurityMethod=" + whereClauseObjectSecurityMethod
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(secCode, epicorHeaders = None):
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
   params += "secCode=" + secCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckCompanyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCompanyInfo
   Description: This method is run before Update method to warn
           the user if the same record exists, the old record will be deleted during
           saving.
   OperationID: CheckCompanyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCompanyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCompanyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDEx
   Description: This method returns a dataset representing a Security with CompanyID,
which is allowable for the current company.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetServiceMethodList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetServiceMethodList
   Description: This method returns a list of the public methods for the given
service.
   OperationID: GetServiceMethodList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetServiceMethodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserGroupList(epicorHeaders = None):
   """  
   Summary: Invoke method GetUserGroupList
   Description: Get combined list of user and groups to use in MetaFx.
   OperationID: GetUserGroupList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserGroupList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNewSecCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNewSecCode
   Description: This method don't allow create new record, if there are records
           with the same code for all companies and for the current company.
           If there is only record for all companies, this method retuns the current
           company ID to allow create new record only for the current company.
   OperationID: ValidateNewSecCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNewSecCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNewSecCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddServices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddServices
   Description: This method will add new service to the ice.security table
   OperationID: AddServices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddServices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddServices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewObjectSecurityMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewObjectSecurityMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewObjectSecurityMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewObjectSecurityMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewObjectSecurityMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ObjectSecuritySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ObjectSecurityMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ObjectSecurityMethodRow] = obj["value"]
      pass

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

class Ice_Tablesets_ObjectSecurityMethodRow:
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
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.DisallowAll:bool = obj["DisallowAll"]
      self.DisallowAccess:str = obj["DisallowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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
class AddServices_input:
   """ Required : 
   directroyName
   password
   """  
   def __init__(self, obj):
      self.directroyName:str = obj["directroyName"]
      """  Dirextory name to serch for services: C:\_projects\ERP10CC\Current\Deployment\Server\Assemblies  """  
      self.password:str = obj["password"]
      """  System Password to run method  """  
      pass

class AddServices_output:
   def __init__(self, obj):
      pass

class CheckCompanyInfo_input:
   """ Required : 
   secCode
   pcCurCompOnly
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      """  The current security code  """  
      self.pcCurCompOnly:bool = obj["pcCurCompOnly"]
      """  The flag CurrentCompanyOnly  """  
      pass

class CheckCompanyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.rowExists:bool = obj["rowExists"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByIDEx_input:
   """ Required : 
   secCode
   pcComp
   strictPrimKey
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      """  The security code  """  
      self.pcComp:str = obj["pcComp"]
      """  The company  """  
      self.strictPrimKey:bool = obj["strictPrimKey"]
      """  If it is false, look for all recordes allowed for the current company  """  
      pass

class GetByIDEx_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ObjectSecurityTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ObjectSecurityTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ObjectSecurityTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ObjectSecurityTableset] = obj["returnObj"]
      pass

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

class GetNewObjectSecurityMethod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

class GetNewObjectSecurityMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSecurity_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

class GetNewSecurity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSubSecurity_input:
   """ Required : 
   ds
   parentSecCode
   secCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      self.parentSecCode:str = obj["parentSecCode"]
      """  The parent security code  """  
      self.secCode:str = obj["secCode"]
      """  The security code  """  
      pass

class GetNewSubSecurity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSecurity
   whereClauseObjectSecurityMethod
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSecurity:str = obj["whereClauseSecurity"]
      self.whereClauseObjectSecurityMethod:str = obj["whereClauseObjectSecurityMethod"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ObjectSecurityTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetServiceMethodList_input:
   """ Required : 
   secCode
   """  
   def __init__(self, obj):
      self.secCode:str = obj["secCode"]
      """  Service security code.  """  
      pass

class GetServiceMethodList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ServiceMethodListTableset] = obj["returnObj"]
      pass

class GetUserGroupList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UserGroupListTableset] = obj["returnObj"]
      pass

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

class Ice_Tablesets_ObjectSecurityMethodRow:
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
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAll:bool = obj["AllowAll"]
      self.AllowAccess:str = obj["AllowAccess"]
      self.DisallowAll:bool = obj["DisallowAll"]
      self.DisallowAccess:str = obj["DisallowAccess"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ObjectSecurityTableset:
   def __init__(self, obj):
      self.Security:list[Ice_Tablesets_SecurityRow] = obj["Security"]
      self.ObjectSecurityMethod:list[Ice_Tablesets_ObjectSecurityMethodRow] = obj["ObjectSecurityMethod"]
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

class Ice_Tablesets_ServiceMethodListRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  Method Name  """  
      self.Description:str = obj["Description"]
      """  Method description  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ServiceMethodListTableset:
   def __init__(self, obj):
      self.ServiceMethodList:list[Ice_Tablesets_ServiceMethodListRow] = obj["ServiceMethodList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtObjectSecurityTableset:
   def __init__(self, obj):
      self.Security:list[Ice_Tablesets_SecurityRow] = obj["Security"]
      self.ObjectSecurityMethod:list[Ice_Tablesets_ObjectSecurityMethodRow] = obj["ObjectSecurityMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserGroupListRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      """  User ID or Group Code  """  
      self.Name:str = obj["Name"]
      """  User or group name  """  
      self.Type:int = obj["Type"]
      """  Record type: 0 - User, 1-Group  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UserGroupListTableset:
   def __init__(self, obj):
      self.UserGroupList:list[Ice_Tablesets_UserGroupListRow] = obj["UserGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtObjectSecurityTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtObjectSecurityTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ObjectSecurityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateNewSecCode_input:
   """ Required : 
   newSecCode
   """  
   def __init__(self, obj):
      self.newSecCode:str = obj["newSecCode"]
      """  The new security code  """  
      pass

class ValidateNewSecCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.curComp:str = obj["parameters"]
      pass

      """  output parameters  """  

