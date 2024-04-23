import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COAActCatSvc
# Description: COAActCat Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COAActCats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COAActCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAActCats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/COAActCats",headers=creds) as resp:
           return await resp.json()

async def post_COAActCats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAActCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COAActCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COAActCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/COAActCats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COAActCats_Company_COACode_CategoryID(Company, COACode, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COAActCat item
   Description: Calls GetByID to retrieve the COAActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COAActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COAActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/COAActCats(" + Company + "," + COACode + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COAActCats_Company_COACode_CategoryID(Company, COACode, CategoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COAActCat for the service
   Description: Calls UpdateExt to update COAActCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COAActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COAActCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/COAActCats(" + Company + "," + COACode + "," + CategoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COAActCats_Company_COACode_CategoryID(Company, COACode, CategoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COAActCat item
   Description: Call UpdateExt to delete COAActCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COAActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/COAActCats(" + Company + "," + COACode + "," + CategoryID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAActCatListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOAActCat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOAActCat=" + whereClauseCOAActCat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, categoryID, epicorHeaders = None):
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
   params += "categoryID=" + categoryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildParentCategoryList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildParentCategoryList
   Description: returns a list-delimited of available parent categories
in id,description pairs for selection
   OperationID: BuildParentCategoryList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildParentCategoryList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildParentCategoryList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSubcategoryList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSubcategoryList
   Description: Returns a list of subcategories for the particular COA category
   OperationID: GetSubcategoryList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSubcategoryList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubcategoryList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOACode
   Description: Checks COACode entered
   OperationID: CheckCOACode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOACode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOACode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckNetIncome(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckNetIncome
   Description: Checks net income flag when the column changes
   OperationID: CheckNetIncome
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckNetIncome_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNetIncome_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckType
   Description: Checks type flag when the column changes
   OperationID: CheckType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyCategories(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyCategories
   Description: This method copy Account Categories from one COA (Chart Of Account) to another COA.
   OperationID: CopyCategories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyCategories_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyCategories_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultCoa(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultCoa
   Description: returns a COA code, Master flag and description of default COA code
   OperationID: GetDefaultCoa
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultCoa_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateCOACode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCOACode
   Description: returns a description and Master COA flag of the entered COA code
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOAGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOAGlobalFields
   Description: none
   OperationID: GetCOAGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOAGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildParentCategoryListWithIncomeParameter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildParentCategoryListWithIncomeParameter
   Description: BuildParentCategoryList method copy with netIncome input parameter.
   OperationID: BuildParentCategoryListWithIncomeParameter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildParentCategoryListWithIncomeParameter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildParentCategoryListWithIncomeParameter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOAActCat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOAActCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOAActCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOAActCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOAActCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAActCatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAActCatListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAActCatListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAActCatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAActCatRow] = obj["value"]
      pass

class Erp_Tablesets_COAActCatListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.Description:str = obj["Description"]
      """  Text describing this category  """  
      self.Type:str = obj["Type"]
      """   Indicates if this cateory is reatled to a balance shee account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """   Indicates the balance for this account is usually a Debit or Credit amount.  Valid values are:
D - Debit
C - Credit  """  
      self.ParentCategory:str = obj["ParentCategory"]
      """  The value of the parent category ID.  Parent/Child category relationships are used by the Fincancial Report Designer.  For example, Assets as the parent category and Current Assets as the child.  """  
      self.Sequence:int = obj["Sequence"]
      """  This number idicates the point at which this child cateogry is placed under its parent category.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """  Value of the Parent category's ID.  """  
      self.NetIncome:bool = obj["NetIncome"]
      """  When Net Income equals Yes this cateogry reflects the summarized balance of all Income Accounts.  It is recommended that one category be marked as NetIncome = Yes to be used for Balance Sheet purposes.  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if new natural account segment values are created with journal detail matching enabled.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParentCatDesc:str = obj["ParentCatDesc"]
      """  Parent Category Description  """  
      self.BalanceText:str = obj["BalanceText"]
      self.ConsolidationTypeDescription:str = obj["ConsolidationTypeDescription"]
      """  Consoldation Type Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.Description:str = obj["Description"]
      """  Text describing this category  """  
      self.Type:str = obj["Type"]
      """   Indicates if this cateory is reatled to a balance shee account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """   Indicates the balance for this account is usually a Debit or Credit amount.  Valid values are:
D - Debit
C - Credit  """  
      self.ParentCategory:str = obj["ParentCategory"]
      """  The value of the parent category ID.  Parent/Child category relationships are used by the Fincancial Report Designer.  For example, Assets as the parent category and Current Assets as the child.  """  
      self.Sequence:int = obj["Sequence"]
      """  This number idicates the point at which this child cateogry is placed under its parent category.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """  Value of the Parent category's ID.  """  
      self.NetIncome:bool = obj["NetIncome"]
      """  When Net Income equals Yes this cateogry reflects the summarized balance of all Income Accounts.  It is recommended that one category be marked as NetIncome = Yes to be used for Balance Sheet purposes.  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if new natural account segment values are created with journal detail matching enabled.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCashBank:bool = obj["CNIsCashBank"]
      """  CNIsCashBank  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.GlbCatFlag:bool = obj["GlbCatFlag"]
      """  Global Category Flag  """  
      self.GlbCatShape:bool = obj["GlbCatShape"]
      """  Global Category Shape  """  
      self.GlbCOAActCatFlag:bool = obj["GlbCOAActCatFlag"]
      """  Global COAAct Category Flag  """  
      self.ParentCatDesc:str = obj["ParentCatDesc"]
      """  Parent Category Description  """  
      self.BalanceText:str = obj["BalanceText"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConsolidationTypeDescription:str = obj["ConsolidationTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildParentCategoryListWithIncomeParameter_input:
   """ Required : 
   cCategory
   cType
   cCOACode
   cIncome
   """  
   def __init__(self, obj):
      self.cCategory:str = obj["cCategory"]
      self.cType:str = obj["cType"]
      self.cCOACode:str = obj["cCOACode"]
      self.cIncome:bool = obj["cIncome"]
      pass

class BuildParentCategoryListWithIncomeParameter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cParentCatList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildParentCategoryList_input:
   """ Required : 
   cCategory
   cType
   cCOACode
   """  
   def __init__(self, obj):
      self.cCategory:str = obj["cCategory"]
      """  Unique identifier of this category of accounts  """  
      self.cType:str = obj["cType"]
      """  Indicates if this category is a (B)alance Sheet or (I)ncome statement category.  """  
      self.cCOACode:str = obj["cCOACode"]
      """  COA Code of the account category.  """  
      pass

class BuildParentCategoryList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cParentCatList:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCOACode_input:
   """ Required : 
   newCoaCode
   """  
   def __init__(self, obj):
      self.newCoaCode:str = obj["newCoaCode"]
      """  COA code entered  """  
      pass

class CheckCOACode_output:
   def __init__(self, obj):
      pass

class CheckNetIncome_input:
   """ Required : 
   ipNetIncome
   ipCOACode
   ipCategoryID
   ds
   """  
   def __init__(self, obj):
      self.ipNetIncome:bool = obj["ipNetIncome"]
      """  proposed net income flag  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipCategoryID:str = obj["ipCategoryID"]
      """  Category ID  """  
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

class CheckNetIncome_output:
   def __init__(self, obj):
      pass

class CheckType_input:
   """ Required : 
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      """  proposed net income flag  """  
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

class CheckType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyCategories_input:
   """ Required : 
   fromCOACode
   toCOACode
   """  
   def __init__(self, obj):
      self.fromCOACode:str = obj["fromCOACode"]
      """  COA code to copy from  """  
      self.toCOACode:str = obj["toCOACode"]
      """  COA code to create  """  
      pass

class CopyCategories_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAActCatTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   coACode
   categoryID
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.categoryID:str = obj["categoryID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_COAActCatListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.Description:str = obj["Description"]
      """  Text describing this category  """  
      self.Type:str = obj["Type"]
      """   Indicates if this cateory is reatled to a balance shee account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """   Indicates the balance for this account is usually a Debit or Credit amount.  Valid values are:
D - Debit
C - Credit  """  
      self.ParentCategory:str = obj["ParentCategory"]
      """  The value of the parent category ID.  Parent/Child category relationships are used by the Fincancial Report Designer.  For example, Assets as the parent category and Current Assets as the child.  """  
      self.Sequence:int = obj["Sequence"]
      """  This number idicates the point at which this child cateogry is placed under its parent category.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """  Value of the Parent category's ID.  """  
      self.NetIncome:bool = obj["NetIncome"]
      """  When Net Income equals Yes this cateogry reflects the summarized balance of all Income Accounts.  It is recommended that one category be marked as NetIncome = Yes to be used for Balance Sheet purposes.  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if new natural account segment values are created with journal detail matching enabled.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ParentCatDesc:str = obj["ParentCatDesc"]
      """  Parent Category Description  """  
      self.BalanceText:str = obj["BalanceText"]
      self.ConsolidationTypeDescription:str = obj["ConsolidationTypeDescription"]
      """  Consoldation Type Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAActCatListTableset:
   def __init__(self, obj):
      self.COAActCatList:list[Erp_Tablesets_COAActCatListRow] = obj["COAActCatList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COAActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.Description:str = obj["Description"]
      """  Text describing this category  """  
      self.Type:str = obj["Type"]
      """   Indicates if this cateory is reatled to a balance shee account or income statement account.  Valid values are:
B - Balance Sheet
I - Income Statement  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """   Indicates the balance for this account is usually a Debit or Credit amount.  Valid values are:
D - Debit
C - Credit  """  
      self.ParentCategory:str = obj["ParentCategory"]
      """  The value of the parent category ID.  Parent/Child category relationships are used by the Fincancial Report Designer.  For example, Assets as the parent category and Current Assets as the child.  """  
      self.Sequence:int = obj["Sequence"]
      """  This number idicates the point at which this child cateogry is placed under its parent category.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """  Value of the Parent category's ID.  """  
      self.NetIncome:bool = obj["NetIncome"]
      """  When Net Income equals Yes this cateogry reflects the summarized balance of all Income Accounts.  It is recommended that one category be marked as NetIncome = Yes to be used for Balance Sheet purposes.  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if new natural account segment values are created with journal detail matching enabled.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCashBank:bool = obj["CNIsCashBank"]
      """  CNIsCashBank  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.GlbCatFlag:bool = obj["GlbCatFlag"]
      """  Global Category Flag  """  
      self.GlbCatShape:bool = obj["GlbCatShape"]
      """  Global Category Shape  """  
      self.GlbCOAActCatFlag:bool = obj["GlbCOAActCatFlag"]
      """  Global COAAct Category Flag  """  
      self.ParentCatDesc:str = obj["ParentCatDesc"]
      """  Parent Category Description  """  
      self.BalanceText:str = obj["BalanceText"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConsolidationTypeDescription:str = obj["ConsolidationTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAActCatTableset:
   def __init__(self, obj):
      self.COAActCat:list[Erp_Tablesets_COAActCatRow] = obj["COAActCat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCOAActCatTableset:
   def __init__(self, obj):
      self.COAActCat:list[Erp_Tablesets_COAActCatRow] = obj["COAActCat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   coACode
   categoryID
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      self.categoryID:str = obj["categoryID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAActCatTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAActCatTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAActCatTableset] = obj["returnObj"]
      pass

class GetCOAGlobalFields_input:
   """ Required : 
   COACode
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      pass

class GetCOAGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultCoa_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultCoaCode:str = obj["parameters"]
      self.defaultCoaDescription:str = obj["parameters"]
      self.isDefaultCoaMaster:bool = obj["isDefaultCoaMaster"]
      self.glbFlag:bool = obj["glbFlag"]
      self.globalCOA:bool = obj["globalCOA"]
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
      self.returnObj:list[Erp_Tablesets_COAActCatListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCOAActCat_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewCOAActCat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOAActCat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOAActCat:str = obj["whereClauseCOAActCat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAActCatTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSubcategoryList_input:
   """ Required : 
   category
   """  
   def __init__(self, obj):
      self.category:str = obj["category"]
      """  Unique identifier of this category of accounts  """  
      pass

class GetSubcategoryList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of subcategories for the particular COA category  """  
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOAActCatTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOAActCatTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAActCatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCOACode_input:
   """ Required : 
   coaCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code entered  """  
      pass

class ValidateCOACode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.coaDescription:str = obj["parameters"]
      self.coaMaster:bool = obj["coaMaster"]
      self.glbFlag:bool = obj["glbFlag"]
      self.globalCOA:bool = obj["globalCOA"]
      pass

      """  output parameters  """  

