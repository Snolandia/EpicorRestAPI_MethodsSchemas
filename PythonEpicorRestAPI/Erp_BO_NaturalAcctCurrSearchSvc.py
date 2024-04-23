import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NaturalAcctCurrSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NaturalAcctCurrSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Get Rows
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NaturalAcctCurrSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_NaturalAcctCurrSearchListRow:
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
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      """  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      """  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      """  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      """  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      """  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      """  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      """  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      """  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      """  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      """  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      """  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      """  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  """  
      self.ISONumber:int = obj["ISONumber"]
      """  ISO unique identifier  """  
      self.StoreID:str = obj["StoreID"]
      """  Store ID for Credit Card Processing  """  
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      """  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      """  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  """  
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Allowed:bool = obj["Allowed"]
      self.Revalue:int = obj["Revalue"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_NaturalAcctCurrSearchListRow:
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
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      """  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      """  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      """  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      """  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      """  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      """  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      """  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      """  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      """  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      """  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      """  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      """  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  """  
      self.ISONumber:int = obj["ISONumber"]
      """  ISO unique identifier  """  
      self.StoreID:str = obj["StoreID"]
      """  Store ID for Credit Card Processing  """  
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      """  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      """  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  """  
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Allowed:bool = obj["Allowed"]
      self.Revalue:int = obj["Revalue"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NaturalAcctCurrSearchListTableset:
   def __init__(self, obj):
      self.NaturalAcctCurrSearchList:list[Erp_Tablesets_NaturalAcctCurrSearchListRow] = obj["NaturalAcctCurrSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where Clause ExpressShip  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NaturalAcctCurrSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

