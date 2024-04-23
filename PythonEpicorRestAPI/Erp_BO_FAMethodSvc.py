import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FAMethodSvc
# Description: FAMethod class
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FAMethods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAMethods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods",headers=creds) as resp:
           return await resp.json()

async def post_FAMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAMethods_Company_AssetMethod(Company, AssetMethod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAMethod item
   Description: Calls GetByID to retrieve the FAMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetMethod: Desc: AssetMethod   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAMethods_Company_AssetMethod(Company, AssetMethod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAMethod for the service
   Description: Calls UpdateExt to update FAMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetMethod: Desc: AssetMethod   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAMethods_Company_AssetMethod(Company, AssetMethod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAMethod item
   Description: Call UpdateExt to delete FAMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetMethod: Desc: AssetMethod   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAMethodListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFAMethod, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFAMethod=" + whereClauseFAMethod
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetMethod, epicorHeaders = None):
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
   params += "assetMethod=" + assetMethod

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AssignAnnualCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignAnnualCharge
   Description: Updates temp table depreciation method formulas.
   OperationID: AssignAnnualCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignAnnualCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAnnualCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignPeriodCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignPeriodCharge
   Description: To be called after changing FAMethod.PeriodChargeType field
   OperationID: AssignPeriodCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignPeriodCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignPeriodCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignAnnualFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignAnnualFormula
   Description: To be called after changing FAMethod.DisplayAnnualFormula
   OperationID: AssignAnnualFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignAnnualFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAnnualFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignPeriodFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignPeriodFormula
   Description: To be called after changing FAMethod.DisplayPeriodFormula
   OperationID: AssignPeriodFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignPeriodFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignPeriodFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAltMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAltMethod
   Description: To be called on leave of FAMethod.AltAssetMethod field
   OperationID: ChangeAltMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAltMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAltMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDepChargeBasis(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDepChargeBasis
   Description: Annual
            To be called on leave of FAMethod.DepChargeBasis field
   OperationID: ChangeDepChargeBasis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDepChargeBasis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDepChargeBasis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSwitchMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSwitchMethod
   Description: To be called on leave of FAMethod.SwitchMethod field
   OperationID: ChangeSwitchMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSwitchMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSwitchMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestSyntax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestSyntax
   Description: Test the formula syntax.
   OperationID: TestSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AnnualVariables(epicorHeaders = None):
   """  
   Summary: Invoke method AnnualVariables
   Description: Returns variables to create depreciation method formulas. Used in annual formula context menu.
   OperationID: AnnualVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnnualVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PeriodVariables(epicorHeaders = None):
   """  
   Summary: Invoke method PeriodVariables
   Description: Returns variables to create depreciation method period formulas. Used in period formula context menu.
   OperationID: PeriodVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PeriodVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_Functions(epicorHeaders = None):
   """  
   Summary: Invoke method Functions
   Description: Returns functions to create depreciation method formulas.
   OperationID: Functions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Functions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_Operators(epicorHeaders = None):
   """  
   Summary: Invoke method Operators
   Description: Returns operators to create depreciation method formulas.
   OperationID: Operators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Operators_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAMethodListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAMethodRow] = obj["value"]
      pass

class Erp_Tablesets_FAMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the depreciation methods table.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method.  """  
      self.Description:str = obj["Description"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.DepreciationMethod:str = obj["DepreciationMethod"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.Finalspread:bool = obj["Finalspread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if this depreciation method is used by an asset register.  """  
      self.AllowSwitch:bool = obj["AllowSwitch"]
      """  Indicates if this depreciation method is allowed to switch to another method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DepChargeBasis:str = obj["DepChargeBasis"]
      """  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  """  
      self.AnnualChargeType:str = obj["AnnualChargeType"]
      """  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  """  
      self.AnnualFormula:str = obj["AnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.PeriodChargeType:str = obj["PeriodChargeType"]
      """  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  """  
      self.ProrateType:str = obj["ProrateType"]
      """  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  """  
      self.SwitchMethod:str = obj["SwitchMethod"]
      """  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  """  
      self.SwitchPercent:int = obj["SwitchPercent"]
      """  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  """  
      self.PeriodFormula:str = obj["PeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InUseFlag:bool = obj["InUseFlag"]
      """  External In Use Flag.  """  
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.DisplayAnnualFormula:str = obj["DisplayAnnualFormula"]
      self.DisplayPeriodFormula:str = obj["DisplayPeriodFormula"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the depreciation methods table.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method.  """  
      self.Description:str = obj["Description"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.DepreciationMethod:str = obj["DepreciationMethod"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.Finalspread:bool = obj["Finalspread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if this depreciation method is used by an asset register.  """  
      self.AllowSwitch:bool = obj["AllowSwitch"]
      """  Indicates if this depreciation method is allowed to switch to another method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DepChargeBasis:str = obj["DepChargeBasis"]
      """  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  """  
      self.AnnualChargeType:str = obj["AnnualChargeType"]
      """  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  """  
      self.AnnualFormula:str = obj["AnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.PeriodChargeType:str = obj["PeriodChargeType"]
      """  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  """  
      self.ProrateType:str = obj["ProrateType"]
      """  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  """  
      self.SwitchMethod:str = obj["SwitchMethod"]
      """  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  """  
      self.SwitchPercent:int = obj["SwitchPercent"]
      """  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  """  
      self.PeriodFormula:str = obj["PeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RemYearsCalculation:str = obj["RemYearsCalculation"]
      """  Remaining Years parameter calculation basis.  """  
      self.InUseFlag:bool = obj["InUseFlag"]
      """  External In Use Flag.  """  
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.DisplayAnnualFormula:str = obj["DisplayAnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.DisplayPeriodFormula:str = obj["DisplayPeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AnnualVariables_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Variable list  """  
      pass

class AssignAnnualCharge_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class AssignAnnualCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignAnnualFormula_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class AssignAnnualFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignPeriodCharge_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class AssignPeriodCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignPeriodFormula_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class AssignPeriodFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAltMethod_input:
   """ Required : 
   ipAltMethod
   ds
   """  
   def __init__(self, obj):
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  alternative asset method that was entered.  """  
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class ChangeAltMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDepChargeBasis_input:
   """ Required : 
   ipDepCharge
   ds
   """  
   def __init__(self, obj):
      self.ipDepCharge:str = obj["ipDepCharge"]
      """  depreciation charge basis that was entered.  """  
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class ChangeDepChargeBasis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSwitchMethod_input:
   """ Required : 
   ipSwitchMethod
   ds
   """  
   def __init__(self, obj):
      self.ipSwitchMethod:str = obj["ipSwitchMethod"]
      """  switch method that was entered.  """  
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class ChangeSwitchMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   assetMethod
   """  
   def __init__(self, obj):
      self.assetMethod:str = obj["assetMethod"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FAMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the depreciation methods table.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method.  """  
      self.Description:str = obj["Description"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.DepreciationMethod:str = obj["DepreciationMethod"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.Finalspread:bool = obj["Finalspread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if this depreciation method is used by an asset register.  """  
      self.AllowSwitch:bool = obj["AllowSwitch"]
      """  Indicates if this depreciation method is allowed to switch to another method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DepChargeBasis:str = obj["DepChargeBasis"]
      """  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  """  
      self.AnnualChargeType:str = obj["AnnualChargeType"]
      """  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  """  
      self.AnnualFormula:str = obj["AnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.PeriodChargeType:str = obj["PeriodChargeType"]
      """  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  """  
      self.ProrateType:str = obj["ProrateType"]
      """  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  """  
      self.SwitchMethod:str = obj["SwitchMethod"]
      """  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  """  
      self.SwitchPercent:int = obj["SwitchPercent"]
      """  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  """  
      self.PeriodFormula:str = obj["PeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InUseFlag:bool = obj["InUseFlag"]
      """  External In Use Flag.  """  
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.DisplayAnnualFormula:str = obj["DisplayAnnualFormula"]
      self.DisplayPeriodFormula:str = obj["DisplayPeriodFormula"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAMethodListTableset:
   def __init__(self, obj):
      self.FAMethodList:list[Erp_Tablesets_FAMethodListRow] = obj["FAMethodList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the depreciation methods table.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method.  """  
      self.Description:str = obj["Description"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.DepreciationMethod:str = obj["DepreciationMethod"]
      """  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.Finalspread:bool = obj["Finalspread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if this depreciation method is used by an asset register.  """  
      self.AllowSwitch:bool = obj["AllowSwitch"]
      """  Indicates if this depreciation method is allowed to switch to another method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DepChargeBasis:str = obj["DepChargeBasis"]
      """  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  """  
      self.AnnualChargeType:str = obj["AnnualChargeType"]
      """  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  """  
      self.AnnualFormula:str = obj["AnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.PeriodChargeType:str = obj["PeriodChargeType"]
      """  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  """  
      self.ProrateType:str = obj["ProrateType"]
      """  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  """  
      self.SwitchMethod:str = obj["SwitchMethod"]
      """  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  """  
      self.SwitchPercent:int = obj["SwitchPercent"]
      """  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  """  
      self.PeriodFormula:str = obj["PeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RemYearsCalculation:str = obj["RemYearsCalculation"]
      """  Remaining Years parameter calculation basis.  """  
      self.InUseFlag:bool = obj["InUseFlag"]
      """  External In Use Flag.  """  
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.DisplayAnnualFormula:str = obj["DisplayAnnualFormula"]
      """  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  """  
      self.DisplayPeriodFormula:str = obj["DisplayPeriodFormula"]
      """  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAMethodTableset:
   def __init__(self, obj):
      self.FAMethod:list[Erp_Tablesets_FAMethodRow] = obj["FAMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFAMethodTableset:
   def __init__(self, obj):
      self.FAMethod:list[Erp_Tablesets_FAMethodRow] = obj["FAMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Functions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Function list  """  
      pass

class GetByID_input:
   """ Required : 
   assetMethod
   """  
   def __init__(self, obj):
      self.assetMethod:str = obj["assetMethod"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAMethodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAMethodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAMethodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAMethodListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFAMethod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class GetNewFAMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFAMethod
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFAMethod:str = obj["whereClauseFAMethod"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAMethodTableset] = obj["returnObj"]
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

class Operators_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Operator list  """  
      pass

class PeriodVariables_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Variable list  """  
      pass

class TestSyntax_input:
   """ Required : 
   ipFormulaToCheck
   ipDepChargeBasis
   """  
   def __init__(self, obj):
      self.ipFormulaToCheck:str = obj["ipFormulaToCheck"]
      """  Formula to check  """  
      self.ipDepChargeBasis:str = obj["ipDepChargeBasis"]
      """  DepChargeBasis Annual or Period  """  
      pass

class TestSyntax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSyntaxIsCorrect:bool = obj["opSyntaxIsCorrect"]
      self.opSyntaxMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAMethodTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAMethodTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAMethodTableset] = obj["ds"]
      pass

      """  output parameters  """  

