import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CurrExRateSvc
# Description: Exchange Rate Group Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CurrExRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrExRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrExRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/CurrExRates",headers=creds) as resp:
           return await resp.json()

async def post_CurrExRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrExRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/CurrExRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrExRates_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, EffectiveDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrExRate item
   Description: Calls GetByID to retrieve the CurrExRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/CurrExRates(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrExRates_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, EffectiveDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrExRate for the service
   Description: Calls UpdateExt to update CurrExRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/CurrExRates(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrExRates_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company, RateGrpCode, SourceCurrCode, TargetCurrCode, EffectiveDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrExRate item
   Description: Call UpdateExt to delete CurrExRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param SourceCurrCode: Desc: SourceCurrCode   Required: True   Allow empty value : True
      :param TargetCurrCode: Desc: TargetCurrCode   Required: True   Allow empty value : True
      :param EffectiveDate: Desc: EffectiveDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/CurrExRates(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrExRateListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCurrExRate, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCurrExRate=" + whereClauseCurrExRate
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rateGrpCode, sourceCurrCode, targetCurrCode, effectiveDate, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "rateGrpCode=" + rateGrpCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sourceCurrCode=" + sourceCurrCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "targetCurrCode=" + targetCurrCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "effectiveDate=" + effectiveDate

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AllowHistUpdates(epicorHeaders = None):
   """  
   Summary: Invoke method AllowHistUpdates
   Description: This method exists solely for the purpose of allowing security for
updating Exchange Rate information to be defined.
   OperationID: AllowHistUpdates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowHistUpdates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AlternalGetNewCurrExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AlternalGetNewCurrExRate
   OperationID: AlternalGetNewCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AlternalGetNewCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AlternalGetNewCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrenciesDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrenciesDefaults
   Description: This method receive RateGrpCode and gives back default values for Source and Target Currencies.
The Default values for Source and Target currencies are found by searching for the first record in CurrConvRule
with RuleCode = 1 using the Current company and the given Rate Group Code as filters.
   OperationID: GetCurrenciesDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrenciesDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrenciesDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFilterDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFilterDates
   Description: Filter Exchange Rate Groups by Date and RateGrp.
   OperationID: GetListFilterDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFilterDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFilterDates
   Description: Filter Exchange Rate Groups by Date and RateGrp.
   OperationID: GetRowsFilterDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFilterDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFilterDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDAlternate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDAlternate
   OperationID: GetByIDAlternate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDAlternate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDAlternate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFilterDatesK(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFilterDatesK
   Description: Get Filter Dates
   OperationID: GetListFilterDatesK
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterDatesK_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterDatesK_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRateGrpData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRateGrpData
   Description: This method receive RateGrpCode and gives back RateGrpDesc.
   OperationID: GetRateGrpData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateGrpData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateGrpData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportExchangeRates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportExchangeRates
   Description: This method conditionally Imports Exchange records.
   OperationID: ImportExchangeRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportExchangeRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExchangeRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExRate
   Description: Method to call when changing the Exchange rate,
updates  db exchange rate for display.
   OperationID: ChangeExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCurrExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCurrExRate
   Description: This method look for at least one record for RateGroup and EffectiveDate if a record is found,
Creates a set of ttTable records for each record existing for this RateGroup and EffcetiveDate,
and then validate this records against the records of CurrConvRule, if there is any record that exist in CurrConvRule with RuleCode = 1
it must exist in the CurrExRate for the same RateGrp.
   OperationID: UpdateCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateEffectiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateEffectiveDate
   OperationID: UpdateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEffectiveDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEffectiveDate
   Description: Validates the date.
   OperationID: ValidateEffectiveDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEffectiveDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEffectiveDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRuleCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRuleCode
   OperationID: ValidateRuleCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRuleCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRuleCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrExRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrExRateListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrExRateRow] = obj["value"]
      pass

class Erp_Tablesets_CurrExRateListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayRate:int = obj["DisplayRate"]
      """  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indicates if the exchange rate is fixed and cannot be updated  """  
      self.SourceScaleFactor:int = obj["SourceScaleFactor"]
      """  Display factor for exchange rates  """  
      self.TargetScaleFactor:int = obj["TargetScaleFactor"]
      """  Display factor for exchange rates  """  
      self.HasHistory:bool = obj["HasHistory"]
      """  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  """  
      self.IsLastEffectiveDate:bool = obj["IsLastEffectiveDate"]
      """  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.HasSecurity:bool = obj["HasSecurity"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RuleCodeRuleCode:int = obj["RuleCodeRuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.RuleCodeDisplayMode:int = obj["RuleCodeDisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RuleCodeFixedRate:bool = obj["RuleCodeFixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      """  Description of the currency  """  
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      """  Description of the currency  """  
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrExRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayRate:int = obj["DisplayRate"]
      """  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indicates if the exchange rate is fixed and cannot be updated  """  
      self.SourceScaleFactor:int = obj["SourceScaleFactor"]
      """  Display factor for exchange rates  """  
      self.TargetScaleFactor:int = obj["TargetScaleFactor"]
      """  Display factor for exchange rates  """  
      self.HasHistory:bool = obj["HasHistory"]
      """  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  """  
      self.IsLastEffectiveDate:bool = obj["IsLastEffectiveDate"]
      """  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.HasSecurity:bool = obj["HasSecurity"]
      self.SouceCurrDspID:str = obj["SouceCurrDspID"]
      """  Source Currency ID with Scale Factor  """  
      self.TargetCurrDspID:str = obj["TargetCurrDspID"]
      """  Target Currency ID with Scale Factor  """  
      self.ScaleDescr:str = obj["ScaleDescr"]
      """  Describes Source/Target ratio  """  
      self.CurrRateActual:int = obj["CurrRateActual"]
      self.RuleCodeDesc:str = obj["RuleCodeDesc"]
      """  RuleCode Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RuleCodeRuleCode:int = obj["RuleCodeRuleCode"]
      self.RuleCodeFixedRate:bool = obj["RuleCodeFixedRate"]
      self.RuleCodeDisplayMode:int = obj["RuleCodeDisplayMode"]
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      self.SourceCurrMaintRate:bool = obj["SourceCurrMaintRate"]
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      self.TargetCurrMaintRate:bool = obj["TargetCurrMaintRate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AllowHistUpdates_output:
   def __init__(self, obj):
      pass

class AlternalGetNewCurrExRate_input:
   """ Required : 
   plRateGrpCode
   plEffectiveDate
   ds
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      self.plEffectiveDate:str = obj["plEffectiveDate"]
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

class AlternalGetNewCurrExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExRate_input:
   """ Required : 
   ProposedExRate
   pRateGrpCode
   pSourceCode
   pTargetCode
   pEffectiveDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedExRate:int = obj["ProposedExRate"]
      """  The proposed exchange rate  """  
      self.pRateGrpCode:str = obj["pRateGrpCode"]
      """  Rate Group Code of the record  """  
      self.pSourceCode:str = obj["pSourceCode"]
      """  Source currency code  """  
      self.pTargetCode:str = obj["pTargetCode"]
      """  Target currency code  """  
      self.pEffectiveDate:str = obj["pEffectiveDate"]
      """  Effective rate of the record  """  
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

class ChangeExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dspActualRate:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rateGrpCode
   sourceCurrCode
   targetCurrCode
   effectiveDate
   """  
   def __init__(self, obj):
      self.rateGrpCode:str = obj["rateGrpCode"]
      self.sourceCurrCode:str = obj["sourceCurrCode"]
      self.targetCurrCode:str = obj["targetCurrCode"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CurrExRateListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayRate:int = obj["DisplayRate"]
      """  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indicates if the exchange rate is fixed and cannot be updated  """  
      self.SourceScaleFactor:int = obj["SourceScaleFactor"]
      """  Display factor for exchange rates  """  
      self.TargetScaleFactor:int = obj["TargetScaleFactor"]
      """  Display factor for exchange rates  """  
      self.HasHistory:bool = obj["HasHistory"]
      """  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  """  
      self.IsLastEffectiveDate:bool = obj["IsLastEffectiveDate"]
      """  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.HasSecurity:bool = obj["HasSecurity"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RuleCodeRuleCode:int = obj["RuleCodeRuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.RuleCodeDisplayMode:int = obj["RuleCodeDisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RuleCodeFixedRate:bool = obj["RuleCodeFixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      """  Description of the currency  """  
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      """  Description of the currency  """  
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrExRateListTableset:
   def __init__(self, obj):
      self.CurrExRateList:list[Erp_Tablesets_CurrExRateListRow] = obj["CurrExRateList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CurrExRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayRate:int = obj["DisplayRate"]
      """  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indicates if the exchange rate is fixed and cannot be updated  """  
      self.SourceScaleFactor:int = obj["SourceScaleFactor"]
      """  Display factor for exchange rates  """  
      self.TargetScaleFactor:int = obj["TargetScaleFactor"]
      """  Display factor for exchange rates  """  
      self.HasHistory:bool = obj["HasHistory"]
      """  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  """  
      self.IsLastEffectiveDate:bool = obj["IsLastEffectiveDate"]
      """  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.HasSecurity:bool = obj["HasSecurity"]
      self.SouceCurrDspID:str = obj["SouceCurrDspID"]
      """  Source Currency ID with Scale Factor  """  
      self.TargetCurrDspID:str = obj["TargetCurrDspID"]
      """  Target Currency ID with Scale Factor  """  
      self.ScaleDescr:str = obj["ScaleDescr"]
      """  Describes Source/Target ratio  """  
      self.CurrRateActual:int = obj["CurrRateActual"]
      self.RuleCodeDesc:str = obj["RuleCodeDesc"]
      """  RuleCode Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RuleCodeRuleCode:int = obj["RuleCodeRuleCode"]
      self.RuleCodeFixedRate:bool = obj["RuleCodeFixedRate"]
      self.RuleCodeDisplayMode:int = obj["RuleCodeDisplayMode"]
      self.SourceCurrCurrName:str = obj["SourceCurrCurrName"]
      self.SourceCurrCurrDesc:str = obj["SourceCurrCurrDesc"]
      self.SourceCurrCurrencyID:str = obj["SourceCurrCurrencyID"]
      self.SourceCurrDocumentDesc:str = obj["SourceCurrDocumentDesc"]
      self.SourceCurrCurrSymbol:str = obj["SourceCurrCurrSymbol"]
      self.SourceCurrMaintRate:bool = obj["SourceCurrMaintRate"]
      self.TargetCurrDocumentDesc:str = obj["TargetCurrDocumentDesc"]
      self.TargetCurrCurrSymbol:str = obj["TargetCurrCurrSymbol"]
      self.TargetCurrCurrencyID:str = obj["TargetCurrCurrencyID"]
      self.TargetCurrCurrDesc:str = obj["TargetCurrCurrDesc"]
      self.TargetCurrCurrName:str = obj["TargetCurrCurrName"]
      self.TargetCurrMaintRate:bool = obj["TargetCurrMaintRate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrExRateTableset:
   def __init__(self, obj):
      self.CurrExRate:list[Erp_Tablesets_CurrExRateRow] = obj["CurrExRate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCurrExRateTableset:
   def __init__(self, obj):
      self.CurrExRate:list[Erp_Tablesets_CurrExRateRow] = obj["CurrExRate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDAlternate_input:
   """ Required : 
   rateGrpCode
   effectiveDate
   """  
   def __init__(self, obj):
      self.rateGrpCode:str = obj["rateGrpCode"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetByIDAlternate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   rateGrpCode
   sourceCurrCode
   targetCurrCode
   effectiveDate
   """  
   def __init__(self, obj):
      self.rateGrpCode:str = obj["rateGrpCode"]
      self.sourceCurrCode:str = obj["sourceCurrCode"]
      self.targetCurrCode:str = obj["targetCurrCode"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
      pass

class GetCurrenciesDefaults_input:
   """ Required : 
   proposedRateGrpCode
   """  
   def __init__(self, obj):
      self.proposedRateGrpCode:str = obj["proposedRateGrpCode"]
      """  The RateGrpCode introduced by the user.  """  
      pass

class GetCurrenciesDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plSourceCurrCode:str = obj["parameters"]
      self.plTargetCurrCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListFilterDatesK_input:
   """ Required : 
   WhereClause
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      pass

class GetListFilterDatesK_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateListTableset] = obj["returnObj"]
      pass

class GetListFilterDates_input:
   """ Required : 
   WhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  Where clause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetListFilterDates_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
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
      self.returnObj:list[Erp_Tablesets_CurrExRateListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCurrExRate_input:
   """ Required : 
   ds
   rateGrpCode
   sourceCurrCode
   targetCurrCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      self.rateGrpCode:str = obj["rateGrpCode"]
      self.sourceCurrCode:str = obj["sourceCurrCode"]
      self.targetCurrCode:str = obj["targetCurrCode"]
      pass

class GetNewCurrExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRateGrpData_input:
   """ Required : 
   proposedRateGrpCode
   """  
   def __init__(self, obj):
      self.proposedRateGrpCode:str = obj["proposedRateGrpCode"]
      """  The RateGrpCode selected by the user.  """  
      pass

class GetRateGrpData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plRateGrpCode:str = obj["parameters"]
      self.plRateGrpDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsFilterDates_input:
   """ Required : 
   whereClauseCurrExRate
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCurrExRate:str = obj["whereClauseCurrExRate"]
      """  Where clause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsFilterDates_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCurrExRate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCurrExRate:str = obj["whereClauseCurrExRate"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrExRateTableset] = obj["returnObj"]
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

class ImportExchangeRates_input:
   """ Required : 
   pFileName
   pListDelimiter
   pDateOrder
   pNumberFormat
   """  
   def __init__(self, obj):
      self.pFileName:str = obj["pFileName"]
      """  Name of the file to export  """  
      self.pListDelimiter:str = obj["pListDelimiter"]
      """  Selected Delimiter to use when parsing the import file  """  
      self.pDateOrder:str = obj["pDateOrder"]
      """  Selected date format that will be imported.  """  
      self.pNumberFormat:str = obj["pNumberFormat"]
      """  Selected numeric format that will be imported.  """  
      pass

class ImportExchangeRates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pSuccess:bool = obj["pSuccess"]
      pass

      """  output parameters  """  

class UpdateCurrExRate_input:
   """ Required : 
   pRateGrpCode
   pEffectiveDate
   ds
   """  
   def __init__(self, obj):
      self.pRateGrpCode:str = obj["pRateGrpCode"]
      """  The RateGrpCode selected by the user.  """  
      self.pEffectiveDate:str = obj["pEffectiveDate"]
      """  Effective Date selected by the user.  """  
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

class UpdateCurrExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateEffectiveDate_input:
   """ Required : 
   pEffectiveDate
   ds
   """  
   def __init__(self, obj):
      self.pEffectiveDate:str = obj["pEffectiveDate"]
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

class UpdateEffectiveDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrExRateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrExRateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrExRateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEffectiveDate_input:
   """ Required : 
   proposedRateGrpCode
   proposedEffectiveDate
   """  
   def __init__(self, obj):
      self.proposedRateGrpCode:str = obj["proposedRateGrpCode"]
      """  The RateGrpCode selected by the user.  """  
      self.proposedEffectiveDate:str = obj["proposedEffectiveDate"]
      """  Effective Date selected by the user.  """  
      pass

class ValidateEffectiveDate_output:
   def __init__(self, obj):
      pass

class ValidateRuleCode_input:
   """ Required : 
   plRateGrpCode
   """  
   def __init__(self, obj):
      self.plRateGrpCode:str = obj["plRateGrpCode"]
      pass

class ValidateRuleCode_output:
   def __init__(self, obj):
      pass

