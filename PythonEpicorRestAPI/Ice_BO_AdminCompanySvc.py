import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AdminCompanySvc
# Description: Company maintenance business object for use by Admin Console
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AdminCompanies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AdminCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AdminCompanies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AdminCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies",headers=creds) as resp:
           return await resp.json()

async def post_AdminCompanies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AdminCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AdminCompanies_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AdminCompany item
   Description: Calls GetByID to retrieve the AdminCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AdminCompany
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AdminCompanies_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AdminCompany for the service
   Description: Calls UpdateExt to update AdminCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AdminCompany
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AdminCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AdminCompanies_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AdminCompany item
   Description: Call UpdateExt to delete AdminCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AdminCompany
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/AdminCompanies(" + Company + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AdminCompanyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAdminCompany, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAdminCompany=" + whereClauseAdminCompany
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, epicorHeaders = None):
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
   params += "company=" + company

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddCompany
   Description: This method adds a new company.
   OperationID: AddCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetProductionInstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetProductionInstance
   Description: Update the global licensing portal and mark the production instance as true / false.
   OperationID: SetProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetProductionInstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLicense
   Description: This method updates the installation id of a license for a Company.
   OperationID: AssignLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCountryCodeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCountryCodeID
   Description: This method updates the CGC codes for a Company.
   OperationID: ChangeCountryCodeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountryCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountryCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCountryCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCountryCode
   Description: This method updates the CGC codes for a Company.
   OperationID: ChangeCountryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCompanyName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCompanyName
   Description: This method updates the name for a Company.
   OperationID: ChangeCompanyName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompanyName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompanyName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByCompanyId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByCompanyId
   Description: This method deletes the Company with the specified id and
and all of the associated data for the company.
   OperationID: DeleteByCompanyId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByCompanyId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByCompanyId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBySysRowId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBySysRowId
   Description: This method deletes the Company with the specified id and
and all of the associated data for the company.
   OperationID: DeleteBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByCompanyId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByCompanyId
   Description: This method retrieves details of the Company with the specified id.
   OperationID: GetByCompanyId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCompanyId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCompanyId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListBySysRowId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListBySysRowId
   Description: This method retrieves details of the Company with the specified id.
   OperationID: GetListBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyList
   Description: Returns a list of all companies. regardless visibility.
   OperationID: GetCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExposeCurrencyData(epicorHeaders = None):
   """  
   Summary: Invoke method ExposeCurrencyData
   Description: Determines whether or not admin console should expose currency functionality.
   OperationID: ExposeCurrencyData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExposeCurrencyData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetServerLogTraceSettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetServerLogTraceSettings
   Description: Returns a dataset with the current trace settings for use at the administration console.
   OperationID: GetServerLogTraceSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServerLogTraceSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetServerLogTraceSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetServerLogTraceSettings
   Description: Sets the trace section configuration depending on the dataset sent to it.
   OperationID: SetServerLogTraceSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetServerLogTraceSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetServerLogTraceSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCompaniesTelemetryOptStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCompaniesTelemetryOptStatus
   Description: Changes the opt out status of multiple companies
   OperationID: ChangeCompaniesTelemetryOptStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompaniesTelemetryOptStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompaniesTelemetryOptStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompaniesTelemetryOptStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCompaniesTelemetryOptStatus
   Description: Gets the Opt status of multiple companies
   OperationID: GetCompaniesTelemetryOptStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompaniesTelemetryOptStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompaniesTelemetryOptStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlobalSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlobalSetting
   Description: Get configuration strings from Ice.GlobalSetting and Ice.GlobalSettingAttribute table
   OperationID: GetGlobalSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlobalSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlobalSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCgcCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCgcCode
   Description: This method get the CGC Code given the guid of the country.
   OperationID: GetCgcCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCgcCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCgcCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLicenseInfoViewerAppUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicenseInfoViewerAppUrl
   Description: Gets the license viewer URL.
   OperationID: GetLicenseInfoViewerAppUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseInfoViewerAppUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UpdateIsLiveFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateIsLiveFlag
   Description: Updates the IsLive flag in Cosmos DB.
   OperationID: UpdateIsLiveFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIsLiveFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIsLiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAdminCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAdminCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAdminCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAdminCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAdminCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminCompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AdminCompanyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminCompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AdminCompanyRow] = obj["value"]
      pass

class Ice_Tablesets_AdminCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Product:str = obj["Product"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Product:str = obj["Product"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddCompany_input:
   """ Required : 
   companyID
   companyName
   installationID
   currencyCode
   decimalsGeneral
   decimalsCost
   decimalsPrice
   countryCode
   countryGroupCode
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for the new Company  """  
      self.companyName:str = obj["companyName"]
      """  Name for the new Company  """  
      self.installationID:str = obj["installationID"]
      """  Installation id for license to be assigned for the new Company  """  
      self.currencyCode:str = obj["currencyCode"]
      """  The base currency code for the new Company  """  
      self.decimalsGeneral:int = obj["decimalsGeneral"]
      """  General Decimals for the base currency code for the new Company  """  
      self.decimalsCost:int = obj["decimalsCost"]
      """  Unit Cost Decimals for the base currency code for the new Company  """  
      self.decimalsPrice:int = obj["decimalsPrice"]
      """  Unit Prices Decimals for the base currency code for the new Company  """  
      self.countryCode:str = obj["countryCode"]
      """  The Country code to use for Country Specific Functionality.  """  
      self.countryGroupCode:str = obj["countryGroupCode"]
      """  The Country Group code to use for Country Specific Functionality.  """  
      pass

class AddCompany_output:
   def __init__(self, obj):
      pass

class AssignLicense_input:
   """ Required : 
   companyID
   installationID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for the Company  """  
      self.installationID:str = obj["installationID"]
      """  Installation Id of license to be assigned to the Company  """  
      pass

class AssignLicense_output:
   def __init__(self, obj):
      pass

class ChangeCompaniesTelemetryOptStatus_input:
   """ Required : 
   action
   companies
   """  
   def __init__(self, obj):
      self.action:str = obj["action"]
      """  available options are OptOut, OptIn  """  
      self.companies:str = obj["companies"]
      """  if no entries are sent all companies are changed  """  
      pass

class ChangeCompaniesTelemetryOptStatus_output:
   def __init__(self, obj):
      pass

class ChangeCompanyName_input:
   """ Required : 
   companyID
   companyName
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for the Company  """  
      self.companyName:str = obj["companyName"]
      """  New name for the Company  """  
      pass

class ChangeCompanyName_output:
   def __init__(self, obj):
      pass

class ChangeCountryCodeID_input:
   """ Required : 
   companyID
   countryCodeID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for the Company  """  
      self.countryCodeID:str = obj["countryCodeID"]
      """  The country code ID.  """  
      pass

class ChangeCountryCodeID_output:
   def __init__(self, obj):
      pass

class ChangeCountryCode_input:
   """ Required : 
   companyID
   countryCode
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for the Company  """  
      self.countryCode:str = obj["countryCode"]
      """  The country code ID.  """  
      pass

class ChangeCountryCode_output:
   def __init__(self, obj):
      pass

class DeleteByCompanyId_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Id for Company to be deleted  """  
      pass

class DeleteByCompanyId_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteBySysRowId_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID for Company to be deleted  """  
      pass

class DeleteBySysRowId_output:
   def __init__(self, obj):
      pass

class ExposeCurrencyData_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetByCompanyId_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  CompanyId for Company to be retrieved  """  
      pass

class GetByCompanyId_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminCompanyListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AdminCompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AdminCompanyTableset] = obj["returnObj"]
      pass

class GetCgcCode_input:
   """ Required : 
   csfCountry
   """  
   def __init__(self, obj):
      self.csfCountry:str = obj["csfCountry"]
      """  Guid of the country  """  
      pass

class GetCgcCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCompaniesTelemetryOptStatus_input:
   """ Required : 
   companies
   """  
   def __init__(self, obj):
      self.companies:str = obj["companies"]
      """  if no entries are sent all companies are sent back  """  
      pass

class GetCompaniesTelemetryOptStatus_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  A dictionary of company, and telemetry either on or off  """  
      pass

class GetCompanyList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminCompanyListTableset] = obj["returnObj"]
      pass

class GetGlobalSetting_input:
   """ Required : 
   settingType
   settingName
   """  
   def __init__(self, obj):
      self.settingType:str = obj["settingType"]
      """  SettingType corresponding to the configuration.  """  
      self.settingName:str = obj["settingName"]
      """  SettingName is the key for the configuration.  """  
      pass

class GetGlobalSetting_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A string if the setting was found in either of the tables, else null.  """  
      pass

class GetLicenseInfoViewerAppUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  License Viewer App URL  """  
      pass

class GetListBySysRowId_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID for Company to be retrieved  """  
      pass

class GetListBySysRowId_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminCompanyListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AdminCompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAdminCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AdminCompanyTableset] = obj["ds"]
      pass

class GetNewAdminCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AdminCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAdminCompany
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAdminCompany:str = obj["whereClauseAdminCompany"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminCompanyTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetServerLogTraceSettings_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  A Ice.BO.AdminCompany.ServerLogTraceDS containing the trace settings.  """  
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

class Ice_Tablesets_AdminCompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Product:str = obj["Product"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminCompanyListTableset:
   def __init__(self, obj):
      self.AdminCompanyList:list[Ice_Tablesets_AdminCompanyListRow] = obj["AdminCompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AdminCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Product:str = obj["Product"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminCompanyTableset:
   def __init__(self, obj):
      self.AdminCompany:list[Ice_Tablesets_AdminCompanyRow] = obj["AdminCompany"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtAdminCompanyTableset:
   def __init__(self, obj):
      self.AdminCompany:list[Ice_Tablesets_AdminCompanyRow] = obj["AdminCompany"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class SetProductionInstance_input:
   """ Required : 
   licenseId
   companyId
   dbHash
   isSetAsProductionInstance
   """  
   def __init__(self, obj):
      self.licenseId:str = obj["licenseId"]
      """  LicenseId of the ERP10 instance  """  
      self.companyId:str = obj["companyId"]
      """  Id for the Company  """  
      self.dbHash:str = obj["dbHash"]
      """  DBHash of the ERP10 instance  """  
      self.isSetAsProductionInstance:bool = obj["isSetAsProductionInstance"]
      pass

class SetProductionInstance_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SetServerLogTraceSettings_input:
   """ Required : 
   traceDS
   """  
   def __init__(self, obj):
      self.traceDS      #schema had no properties on an object.
      pass

class SetServerLogTraceSettings_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAdminCompanyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAdminCompanyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateIsLiveFlag_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  company ID.  """  
      pass

class UpdateIsLiveFlag_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AdminCompanyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AdminCompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

