import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CheckDigitSvc
# Description: Check Digit Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CheckDigits(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CheckDigits items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckDigits
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckDigitRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits",headers=creds) as resp:
           return await resp.json()

async def post_CheckDigits(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckDigits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckDigitRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CheckDigitRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CheckDigits_CountryISOCode_CheckDigitID(CountryISOCode, CheckDigitID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckDigit item
   Description: Calls GetByID to retrieve the CheckDigit item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckDigit
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckDigitRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits(" + CountryISOCode + "," + CheckDigitID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CheckDigits_CountryISOCode_CheckDigitID(CountryISOCode, CheckDigitID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CheckDigit for the service
   Description: Calls UpdateExt to update CheckDigit. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckDigit
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckDigitRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits(" + CountryISOCode + "," + CheckDigitID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CheckDigits_CountryISOCode_CheckDigitID(CountryISOCode, CheckDigitID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CheckDigit item
   Description: Call UpdateExt to delete CheckDigit item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckDigit
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits(" + CountryISOCode + "," + CheckDigitID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CheckDigits_CountryISOCode_CheckDigitID_CheckDigitUsages(CountryISOCode, CheckDigitID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CheckDigitUsages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CheckDigitUsages1
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckDigitUsageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits(" + CountryISOCode + "," + CheckDigitID + ")/CheckDigitUsages",headers=creds) as resp:
           return await resp.json()

async def get_CheckDigits_CountryISOCode_CheckDigitID_CheckDigitUsages_CountryISOCode_CheckDigitID_UsageFeature(CountryISOCode, CheckDigitID, UsageFeature, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckDigitUsage item
   Description: Calls GetByID to retrieve the CheckDigitUsage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckDigitUsage1
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param UsageFeature: Desc: UsageFeature   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckDigitUsageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigits(" + CountryISOCode + "," + CheckDigitID + ")/CheckDigitUsages(" + CountryISOCode + "," + CheckDigitID + "," + UsageFeature + ")",headers=creds) as resp:
           return await resp.json()

async def get_CheckDigitUsages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CheckDigitUsages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckDigitUsages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckDigitUsageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigitUsages",headers=creds) as resp:
           return await resp.json()

async def post_CheckDigitUsages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckDigitUsages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckDigitUsageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CheckDigitUsageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigitUsages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CheckDigitUsages_CountryISOCode_CheckDigitID_UsageFeature(CountryISOCode, CheckDigitID, UsageFeature, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckDigitUsage item
   Description: Calls GetByID to retrieve the CheckDigitUsage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckDigitUsage
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param UsageFeature: Desc: UsageFeature   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckDigitUsageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigitUsages(" + CountryISOCode + "," + CheckDigitID + "," + UsageFeature + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CheckDigitUsages_CountryISOCode_CheckDigitID_UsageFeature(CountryISOCode, CheckDigitID, UsageFeature, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CheckDigitUsage for the service
   Description: Calls UpdateExt to update CheckDigitUsage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckDigitUsage
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param UsageFeature: Desc: UsageFeature   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckDigitUsageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigitUsages(" + CountryISOCode + "," + CheckDigitID + "," + UsageFeature + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CheckDigitUsages_CountryISOCode_CheckDigitID_UsageFeature(CountryISOCode, CheckDigitID, UsageFeature, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CheckDigitUsage item
   Description: Call UpdateExt to delete CheckDigitUsage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckDigitUsage
      :param CountryISOCode: Desc: CountryISOCode   Required: True   Allow empty value : True
      :param CheckDigitID: Desc: CheckDigitID   Required: True   Allow empty value : True
      :param UsageFeature: Desc: UsageFeature   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/CheckDigitUsages(" + CountryISOCode + "," + CheckDigitID + "," + UsageFeature + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckDigitListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCheckDigit, whereClauseCheckDigitUsage, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCheckDigit=" + whereClauseCheckDigit
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCheckDigitUsage=" + whereClauseCheckDigitUsage
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(countryISOCode, checkDigitID, epicorHeaders = None):
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
   params += "countryISOCode=" + countryISOCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "checkDigitID=" + checkDigitID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetUsageFeatureList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUsageFeatureList
   OperationID: GetUsageFeatureList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUsageFeatureList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsageFeatureList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentCountryISOCode(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentCountryISOCode
   Description: Get country ISO Code current company
   OperationID: GetCurrentCountryISOCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentCountryISOCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckCheckDigitUsage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCheckDigitUsage
   Description: uniqueness check CheckDigitUsage
   OperationID: CheckCheckDigitUsage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCheckDigitUsage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCheckDigitUsage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCheckDigitUsage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCheckDigitUsage
   Description: Update CheckDigitUsage table. Standard update not worked for keyed field
   OperationID: UpdateCheckDigitUsage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCheckDigitUsage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCheckDigitUsage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCheckDigit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCheckDigit
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckDigit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCheckDigit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckDigit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCheckDigitUsage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCheckDigitUsage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckDigitUsage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCheckDigitUsage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckDigitUsage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CheckDigitSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckDigitListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckDigitListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckDigitRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckDigitRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckDigitUsageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckDigitUsageRow] = obj["value"]
      pass

class Erp_Tablesets_CheckDigitListRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Modulus:int = obj["Modulus"]
      """  Modulus  """  
      self.ProductType:int = obj["ProductType"]
      """  ProductType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckDigitRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Weight:str = obj["Weight"]
      """  Weight  """  
      self.Modulus:int = obj["Modulus"]
      """  Modulus  """  
      self.UseLengthInCheckDigit:bool = obj["UseLengthInCheckDigit"]
      """  UseLengthInCheckDigit  """  
      self.ProductType:int = obj["ProductType"]
      """  ProductType  """  
      self.SpecialRemainder:int = obj["SpecialRemainder"]
      """  SpecialRemainder  """  
      self.RemainderCharacter:str = obj["RemainderCharacter"]
      """  RemainderCharacter  """  
      self.RemainderFormat:str = obj["RemainderFormat"]
      """  RemainderFormat  """  
      self.StartFromLeft:bool = obj["StartFromLeft"]
      """  StartFromLeft  """  
      self.IsRecursive:bool = obj["IsRecursive"]
      """  IsRecursive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckDigitUsageRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.UsageFeature:int = obj["UsageFeature"]
      """  UsageFeature  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckCheckDigitUsage_input:
   """ Required : 
   checkDigitID
   usageFeature
   """  
   def __init__(self, obj):
      self.checkDigitID:str = obj["checkDigitID"]
      """  see table CheckDigitUsage.CheckDigitID  """  
      self.usageFeature:int = obj["usageFeature"]
      """  see table CheckDigitUsage.UsageFeature  """  
      pass

class CheckCheckDigitUsage_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   countryISOCode
   checkDigitID
   """  
   def __init__(self, obj):
      self.countryISOCode:str = obj["countryISOCode"]
      self.checkDigitID:str = obj["checkDigitID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CheckDigitListRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Modulus:int = obj["Modulus"]
      """  Modulus  """  
      self.ProductType:int = obj["ProductType"]
      """  ProductType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckDigitListTableset:
   def __init__(self, obj):
      self.CheckDigitList:list[Erp_Tablesets_CheckDigitListRow] = obj["CheckDigitList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CheckDigitRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Weight:str = obj["Weight"]
      """  Weight  """  
      self.Modulus:int = obj["Modulus"]
      """  Modulus  """  
      self.UseLengthInCheckDigit:bool = obj["UseLengthInCheckDigit"]
      """  UseLengthInCheckDigit  """  
      self.ProductType:int = obj["ProductType"]
      """  ProductType  """  
      self.SpecialRemainder:int = obj["SpecialRemainder"]
      """  SpecialRemainder  """  
      self.RemainderCharacter:str = obj["RemainderCharacter"]
      """  RemainderCharacter  """  
      self.RemainderFormat:str = obj["RemainderFormat"]
      """  RemainderFormat  """  
      self.StartFromLeft:bool = obj["StartFromLeft"]
      """  StartFromLeft  """  
      self.IsRecursive:bool = obj["IsRecursive"]
      """  IsRecursive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckDigitTableset:
   def __init__(self, obj):
      self.CheckDigit:list[Erp_Tablesets_CheckDigitRow] = obj["CheckDigit"]
      self.CheckDigitUsage:list[Erp_Tablesets_CheckDigitUsageRow] = obj["CheckDigitUsage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CheckDigitUsageRow:
   def __init__(self, obj):
      self.CountryISOCode:str = obj["CountryISOCode"]
      """  CountryISOCode  """  
      self.CheckDigitID:str = obj["CheckDigitID"]
      """  CheckDigitID  """  
      self.UsageFeature:int = obj["UsageFeature"]
      """  UsageFeature  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCheckDigitTableset:
   def __init__(self, obj):
      self.CheckDigit:list[Erp_Tablesets_CheckDigitRow] = obj["CheckDigit"]
      self.CheckDigitUsage:list[Erp_Tablesets_CheckDigitUsageRow] = obj["CheckDigitUsage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   countryISOCode
   checkDigitID
   """  
   def __init__(self, obj):
      self.countryISOCode:str = obj["countryISOCode"]
      self.checkDigitID:str = obj["checkDigitID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CheckDigitTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CheckDigitTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CheckDigitTableset] = obj["returnObj"]
      pass

class GetCurrentCountryISOCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Current Company Country ISO Code  """  
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
      self.returnObj:list[Erp_Tablesets_CheckDigitListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCheckDigitUsage_input:
   """ Required : 
   ds
   countryISOCode
   checkDigitID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      self.countryISOCode:str = obj["countryISOCode"]
      self.checkDigitID:str = obj["checkDigitID"]
      pass

class GetNewCheckDigitUsage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCheckDigit_input:
   """ Required : 
   ds
   countryISOCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      self.countryISOCode:str = obj["countryISOCode"]
      pass

class GetNewCheckDigit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCheckDigit
   whereClauseCheckDigitUsage
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCheckDigit:str = obj["whereClauseCheckDigit"]
      self.whereClauseCheckDigitUsage:str = obj["whereClauseCheckDigitUsage"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CheckDigitTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUsageFeatureList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetUsageFeatureList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class UpdateCheckDigitUsage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

class UpdateCheckDigitUsage_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCheckDigitTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCheckDigitTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CheckDigitTableset] = obj["ds"]
      pass

      """  output parameters  """  

