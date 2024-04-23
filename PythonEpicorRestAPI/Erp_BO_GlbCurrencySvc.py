import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbCurrencySvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrencies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrencies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrencies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company, GlbCompany, GlbCurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrency item
   Description: Calls GetByID to retrieve the GlbCurrency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCurrencyCode: Desc: GlbCurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company, GlbCompany, GlbCurrencyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCurrency for the service
   Description: Calls UpdateExt to update GlbCurrency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCurrencyCode: Desc: GlbCurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCurrencies_Company_GlbCompany_GlbCurrencyCode(Company, GlbCompany, GlbCurrencyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCurrency item
   Description: Call UpdateExt to delete GlbCurrency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCurrencyCode: Desc: GlbCurrencyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/GlbCurrencies(" + Company + "," + GlbCompany + "," + GlbCurrencyCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrencyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbCurrency, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbCurrency=" + whereClauseGlbCurrency
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbCurrencyCode, epicorHeaders = None):
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
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCurrencyCode=" + glbCurrencyCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCurrency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrencyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrencyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrencyRow] = obj["value"]
      pass

class Erp_Tablesets_GlbCurrencyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.UnRealLossDiv:str = obj["UnRealLossDiv"]
      """   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  """  
      self.UnRealLossDept:str = obj["UnRealLossDept"]
      """   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.UnRealLossChart:str = obj["UnRealLossChart"]
      """   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  Currency Code from Source Company  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  Currency ID from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      self.RoundTolerance:int = obj["RoundTolerance"]
      self.ISONumber:int = obj["ISONumber"]
      self.StoreID:str = obj["StoreID"]
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkCurrencyID:str = obj["LinkCurrencyID"]
      """  Currency.CurrencyID to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.UnRealLossDiv:str = obj["UnRealLossDiv"]
      """   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  """  
      self.UnRealLossDept:str = obj["UnRealLossDept"]
      """   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.UnRealLossChart:str = obj["UnRealLossChart"]
      """   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  Currency Code from Source Company  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  Currency ID from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      self.RoundTolerance:int = obj["RoundTolerance"]
      self.ISONumber:int = obj["ISONumber"]
      self.StoreID:str = obj["StoreID"]
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  ISOCurrCode  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.LinkCurrencyCode:str = obj["LinkCurrencyCode"]
      """  Currency.CurrencyCode to link to (new or existing)  """  
      self.LinkCurrencyID:str = obj["LinkCurrencyID"]
      """  Currency.CurrencyID to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  Description of the local Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbCurrencyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.UnRealLossDiv:str = obj["UnRealLossDiv"]
      """   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  """  
      self.UnRealLossDept:str = obj["UnRealLossDept"]
      """   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.UnRealLossChart:str = obj["UnRealLossChart"]
      """   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  Currency Code from Source Company  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  Currency ID from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      self.RoundTolerance:int = obj["RoundTolerance"]
      self.ISONumber:int = obj["ISONumber"]
      self.StoreID:str = obj["StoreID"]
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkCurrencyID:str = obj["LinkCurrencyID"]
      """  Currency.CurrencyID to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrencyListTableset:
   def __init__(self, obj):
      self.GlbCurrencyList:list[Erp_Tablesets_GlbCurrencyListRow] = obj["GlbCurrencyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCurrencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.UnRealLossDiv:str = obj["UnRealLossDiv"]
      """   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  """  
      self.UnRealLossDept:str = obj["UnRealLossDept"]
      """   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.UnRealLossChart:str = obj["UnRealLossChart"]
      """   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  Currency Code from Source Company  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  Currency ID from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      self.RoundTolerance:int = obj["RoundTolerance"]
      self.ISONumber:int = obj["ISONumber"]
      self.StoreID:str = obj["StoreID"]
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  ISOCurrCode  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.LinkCurrencyCode:str = obj["LinkCurrencyCode"]
      """  Currency.CurrencyCode to link to (new or existing)  """  
      self.LinkCurrencyID:str = obj["LinkCurrencyID"]
      """  Currency.CurrencyID to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  Description of the local Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrencyTableset:
   def __init__(self, obj):
      self.GlbCurrency:list[Erp_Tablesets_GlbCurrencyRow] = obj["GlbCurrency"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbCurrencyTableset:
   def __init__(self, obj):
      self.GlbCurrency:list[Erp_Tablesets_GlbCurrencyRow] = obj["GlbCurrency"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrencyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrencyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrencyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrencyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbCurrency_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbCurrency
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbCurrency:str = obj["whereClauseGlbCurrency"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrencyTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbCurrencyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbCurrencyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

