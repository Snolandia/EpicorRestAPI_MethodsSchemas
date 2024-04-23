import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLAccountSvc
# Description: The GL Account service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLAccounts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAccounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccounts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts",headers=creds) as resp:
           return await resp.json()

async def post_GLAccounts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAccountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAccounts_Company_COACode_GLAccount1(Company, COACode, GLAccount1, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccount item
   Description: Calls GetByID to retrieve the GLAccount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount1: Desc: GLAccount1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAccountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAccounts_Company_COACode_GLAccount1(Company, COACode, GLAccount1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAccount for the service
   Description: Calls UpdateExt to update GLAccount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount1: Desc: GLAccount1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAccounts_Company_COACode_GLAccount1(Company, COACode, GLAccount1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAccount item
   Description: Call UpdateExt to delete GLAccount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount1: Desc: GLAccount1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/GLAccounts(" + Company + "," + COACode + "," + GLAccount1 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLAccount, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLAccount=" + whereClauseGLAccount
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, glAccount, epicorHeaders = None):
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
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glAccount=" + glAccount

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetGLAccountGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLAccountGlobalFields
   Description: Get GLAccount global fields
   OperationID: GetGLAccountGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLAccountGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLAccountGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckActive
   Description: Verify the active flag against segment values
   OperationID: CheckActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountActiveChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountActiveChanging
   Description: Called when the Active flag on the GL Account is changing.
Performs validations when marking an account is active.
Checks for GL Control Code references when marking an account as inactive.
   OperationID: GLAccountActiveChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountActiveChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountActiveChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLControlReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLControlReferences
   Description: Returns a dataset of GL Control Codes that reference the account
   OperationID: GetGLControlReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLControlReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLControlReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckEffFrom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEffFrom
   Description: Verify the effective from is not earlier than any segment effective from
   OperationID: CheckEffFrom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEffFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEffFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckEffTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEffTo
   Description: Verify the effective to is not later than any segment effective to
   OperationID: CheckEffTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEffTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEffTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchFilter
   Description: Search GLAccount with account filter applied
   OperationID: GLAccountSearchFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchList
   Description: Search GLAccount in DataSetList mode.
   OperationID: GLAccountSearchList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GLAccountSearchRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLAccountSearchRows
   Description: Search GLAccount in DataSetRows mode.
   OperationID: GLAccountSearchRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLAccountSearchRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLAccountSearchRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAccount
   Description: Validate GL Account
   OperationID: ValidateAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOACode
   Description: Returns a description and Global COA flags of the entered COA code
   OperationID: ValidateCOACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GlAccountExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GlAccountExists
   Description: Return true if mentioned GL Account exists for the COA
   OperationID: GlAccountExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GlAccountExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlAccountExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetControlledCombination(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetControlledCombination
   Description: This method returns only controlled combination of segments from full GLAccount
   OperationID: GetControlledCombination
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetControlledCombination_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetControlledCombination_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckExcludeInInclude(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckExcludeInInclude
   Description: COA Segments validation step before mass Preview/Generation/Delete of gl accounts.
   OperationID: CheckExcludeInInclude
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExcludeInInclude_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExcludeInInclude_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLAcctDispAndDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLAcctDispAndDesc
   Description: This method should be called from UI GL Account control for Display and Description generation
   OperationID: GetGLAcctDispAndDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLAcctDispAndDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLAcctDispAndDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGLAccount
   Description: This method should be called from UI GL Account control for account validation
   OperationID: ValidateGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PutListInCorrectFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PutListInCorrectFormat
   Description: Prepare a list of Categories/Segment Codes for further Generate/Delete Accounts procedures.
   OperationID: PutListInCorrectFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PutListInCorrectFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PutListInCorrectFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeDelete
   Description: Return confirmation message if needed for MultiCompany/Global accounts before deletion.
   OperationID: CheckBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAccount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAccountListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAccountRow] = obj["value"]
      pass

class Erp_Tablesets_GLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account may recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount1:str = obj["GLAccount1"]
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account may recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXConcept:str = obj["MXConcept"]
      """  MXConcept  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.GLBGLAccountFlag:bool = obj["GLBGLAccountFlag"]
      """  GLBGLAccountFlag  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Global COA Flag  """  
      self.GlobalFlag:bool = obj["GlobalFlag"]
      """  Global Flag  """  
      self.DeleteOverride:bool = obj["DeleteOverride"]
      """  Indicates the user has chosen to delete the account even if there is a record in GLBGLAccount.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckActive_input:
   """ Required : 
   ipActive
   ds
   """  
   def __init__(self, obj):
      self.ipActive:bool = obj["ipActive"]
      """  Proposed value of active  """  
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class CheckActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBeforeDelete_input:
   """ Required : 
   coa
   glAccount
   """  
   def __init__(self, obj):
      self.coa:str = obj["coa"]
      """  Chart of Accounts of GL Account to check.  """  
      self.glAccount:str = obj["glAccount"]
      """  GL Account to check before trying to delete.  """  
      pass

class CheckBeforeDelete_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CheckEffFrom_input:
   """ Required : 
   ipEffFrom
   ds
   """  
   def __init__(self, obj):
      self.ipEffFrom:str = obj["ipEffFrom"]
      """  Effective From Date to validate  """  
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class CheckEffFrom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckEffTo_input:
   """ Required : 
   ipEffTo
   ds
   """  
   def __init__(self, obj):
      self.ipEffTo:str = obj["ipEffTo"]
      """  Effective To Date to validate  """  
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class CheckEffTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckExcludeInInclude_input:
   """ Required : 
   sIncFrom
   sIncTo
   sExcFrom
   sExcTo
   """  
   def __init__(self, obj):
      self.sIncFrom:str = obj["sIncFrom"]
      self.sIncTo:str = obj["sIncTo"]
      self.sExcFrom:str = obj["sExcFrom"]
      self.sExcTo:str = obj["sExcTo"]
      pass

class CheckExcludeInInclude_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.sErrMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultsOnAdd_input:
   """ Required : 
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account being added  """  
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class DefaultsOnAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account may recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The value of this field is the concatenation of the first three controlled display order segments.  For example, if a chart has 5 controlled segments that are displayed in the following order: seg5->seg3->seg4->seg2->seg1, this field contains the concatention of seg5->seg3->seg4 up to th  """  
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      """  Text that describes the account.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountListTableset:
   def __init__(self, obj):
      self.GLAccountList:list[Erp_Tablesets_GLAccountListRow] = obj["GLAccountList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLAccountRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Accounts is used.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this account is active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account begins to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account may recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXConcept:str = obj["MXConcept"]
      """  MXConcept  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.GLBGLAccountFlag:bool = obj["GLBGLAccountFlag"]
      """  GLBGLAccountFlag  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Global COA Flag  """  
      self.GlobalFlag:bool = obj["GlobalFlag"]
      """  Global Flag  """  
      self.DeleteOverride:bool = obj["DeleteOverride"]
      """  Indicates the user has chosen to delete the account even if there is a record in GLBGLAccount.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      pass

class Erp_Tablesets_GLAccountTableset:
   def __init__(self, obj):
      self.GLAccount:list[Erp_Tablesets_GLAccountRow] = obj["GLAccount"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLCntrlAcctReferencesTableset:
   def __init__(self, obj):
      self.GLCntrlAcct:list[Erp_Tablesets_GLCntrlAcctRow] = obj["GLCntrlAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLCntrlAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.GLCTAcctNum:int = obj["GLCTAcctNum"]
      """  This field in combination with GLControlType references the GLCTAcctCntxt record that this record was created from.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.GlobalGLCntrlAcct:bool = obj["GlobalGLCntrlAcct"]
      """  Marks this GLCntrlAcct as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsRequired:bool = obj["IsRequired"]
      """  Indicates if an account is required for this record.  Data source is the GLCTAcctCntxt table.  """  
      self.UseMasterChart:bool = obj["UseMasterChart"]
      """  Indicates if the Master Chart is being used for this record.  The data source for this field is GLCTAcctCntxt.  """  
      self.COAName:str = obj["COAName"]
      """  The name of the Master Chart of Accounts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGLAccountTableset:
   def __init__(self, obj):
      self.GLAccount:list[Erp_Tablesets_GLAccountRow] = obj["GLAccount"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GLAccountActiveChanging_input:
   """ Required : 
   proposedActive
   ds
   """  
   def __init__(self, obj):
      self.proposedActive:bool = obj["proposedActive"]
      """  Proposed Active value  """  
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class GLAccountActiveChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      self.glControlCodeReferences:bool = obj["glControlCodeReferences"]
      pass

      """  output parameters  """  

class GLAccountSearchFilter_input:
   """ Required : 
   whereClause
   descContains
   effFrom
   effTo
   coaCode
   plantList
   pageSize
   absolutePage
   accountMask
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.descContains:str = obj["descContains"]
      self.effFrom:str = obj["effFrom"]
      self.effTo:str = obj["effTo"]
      self.coaCode:str = obj["coaCode"]
      """  COACode  """  
      self.plantList:str = obj["plantList"]
      """  COACode  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.accountMask:str = obj["accountMask"]
      pass

class GLAccountSearchFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GLAccountSearchList_input:
   """ Required : 
   WhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.PageSize:int = obj["PageSize"]
      self.AbsolutePage:int = obj["AbsolutePage"]
      pass

class GLAccountSearchList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GLAccountSearchRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GLAccountSearchRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountTableset] = obj["returnObj"]
      pass

class GetControlledCombination_input:
   """ Required : 
   company
   COACode
   GLAccount
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company name  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GLAccount with dynamic values  """  
      pass

class GetControlledCombination_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGLAccountGlobalFields_input:
   """ Required : 
   GLAccount
   CoaCode
   GlobalLock
   """  
   def __init__(self, obj):
      self.GLAccount:str = obj["GLAccount"]
      """  GLAccount  """  
      self.CoaCode:str = obj["CoaCode"]
      """  COA Code  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Flag GlobalLock  """  
      pass

class GetGLAccountGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Return list of global fields  """  
      pass

class GetGLAcctDispAndDesc_input:
   """ Required : 
   COACode
   GLAccount
   ExtCompanyID
   isBalanceAcct
   balanceType
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  COA Code value  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Account value  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company ID  """  
      self.isBalanceAcct:bool = obj["isBalanceAcct"]
      """  Is balancing account?  """  
      self.balanceType:str = obj["balanceType"]
      """  Balance type  """  
      pass

class GetGLAcctDispAndDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.glAcctDisp:str = obj["parameters"]
      self.glAcctDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetGLControlReferences_input:
   """ Required : 
   coaCode
   glAccount
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.glAccount:str = obj["glAccount"]
      """  GL Account  """  
      pass

class GetGLControlReferences_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCntrlAcctReferencesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAccountListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLAccount_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLAccount
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLAccount:str = obj["whereClauseGLAccount"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAccountTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GlAccountExists_input:
   """ Required : 
   ipCOACode
   ipGLAccount
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      pass

class GlAccountExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Return true if mentioned GL Account exists for the COA  """  
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

class PutListInCorrectFormat_input:
   """ Required : 
   inpList
   """  
   def __init__(self, obj):
      self.inpList:str = obj["inpList"]
      pass

class PutListInCorrectFormat_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAccountTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAccountTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAccount_input:
   """ Required : 
   ipCOACode
   ipGLAccount
   ipNbrSegments
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ipNbrSegments:int = obj["ipNbrSegments"]
      """  Segment Number  """  
      pass

class ValidateAccount_output:
   def __init__(self, obj):
      pass

class ValidateCOACode_input:
   """ Required : 
   coaCode
   glAccount
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code entered  """  
      self.glAccount:str = obj["glAccount"]
      """  GL Account entered  """  
      pass

class ValidateCOACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opGlobalCOA:bool = obj["opGlobalCOA"]
      pass

      """  output parameters  """  

class ValidateGLAccount_input:
   """ Required : 
   COACode
   GLAccount
   ExtCompanyID
   RestrictID
   EffectiveDate
   ValidateDynamicSegment
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  COA Code value  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Account value  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company ID  """  
      self.RestrictID:str = obj["RestrictID"]
      """  UI Code value  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Effective Date  """  
      self.ValidateDynamicSegment:bool = obj["ValidateDynamicSegment"]
      """  Validate Dynamic Segments value  """  
      pass

class ValidateGLAccount_output:
   def __init__(self, obj):
      pass

