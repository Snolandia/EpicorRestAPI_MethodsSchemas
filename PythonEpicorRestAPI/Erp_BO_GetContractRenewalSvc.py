import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GetContractRenewalSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ExpireDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireDate
   Description: ExpireDate .
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildContractRenewalList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildContractRenewalList
   Description: This method returns three possible lists of selected Contract (FSContHd) and/or
Renewal (FSRenewal) records.  This should be called to return a list containing the
key fields of selected records. Since each record has two key fields the list
could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into three lists if needed.
   OperationID: BuildContractRenewalList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildContractRenewalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildContractRenewalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildContractRenewalListFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildContractRenewalListFromList
   Description: This method returns three possible lists of selected Contract (FSContHd) and/or
Renewal (FSRenewal) records.  This should be called to return a list containing the
key fields of selected records. Since each record has two key fields the list
could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into three lists if needed.
This method  created to call from Kinetic UI
   OperationID: BuildContractRenewalListFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildContractRenewalListFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildContractRenewalListFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsCustom(ipCustList, ipTypeList, ipExpireDate, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: This methods will return all Contract Renewal records (copy of GetRenewal method)
that meet the selection criteria.  This method will try
to mirror functionality of the base GetRows method and it called from Kinetic UI Proc
RenewContracts when user searches for the contract renewal
   OperationID: Get_GetRowsCustom
      :param ipCustList: Desc: The where clause to restrict Customers   Required: True   Allow empty value : True
      :param ipTypeList: Desc: The where clause to restrict Types   Required: True   Allow empty value : True
      :param ipExpireDate: Desc: The where clause to restrict Date   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipCustList=" + ipCustList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipTypeList=" + ipTypeList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipExpireDate=" + ipExpireDate
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRenewals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRenewals
   Description: This method returns the ttContractRenewal dataset consisting of expired or soon to expire
contracts (FSContHd) and renewals (FSRenewal) mixed records with some calculated columns added.
   OperationID: GetRenewals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildContractRenewalListFromList_input:
   """ Required : 
   ipContRenewMainList
   """  
   def __init__(self, obj):
      self.ipContRenewMainList:str = obj["ipContRenewMainList"]
      """  The main listof selected Contract/Renewal records  """  
      pass

class BuildContractRenewalListFromList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opContRenewList1:str = obj["parameters"]
      self.opContRenewList2:str = obj["parameters"]
      self.opContRenewList3:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildContractRenewalList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GetContractRenewalTableset] = obj["ds"]
      pass

class BuildContractRenewalList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opContRenewList1:str = obj["parameters"]
      self.opContRenewList2:str = obj["parameters"]
      self.opContRenewList3:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_GetContractRenewalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ContractRenewalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.QuotedRenewal:bool = obj["QuotedRenewal"]
      """  Indicates if the renwal will automatically generate a quote.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteAccepted:bool = obj["QuoteAccepted"]
      """  Indicates the Quote has been accepted.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  This is the contract code assigned to the renewal.  """  
      self.ShipRenewal:bool = obj["ShipRenewal"]
      """  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this contract is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this contract is linked to  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.Selected:bool = obj["Selected"]
      """  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      self.Modifier:str = obj["Modifier"]
      self.CustID:str = obj["CustID"]
      self.ContractCode:str = obj["ContractCode"]
      self.ContractCodeDesc:str = obj["ContractCodeDesc"]
      self.RACodeDesc:str = obj["RACodeDesc"]
      self.ContractTotal:int = obj["ContractTotal"]
      """  Total Contract Amount  """  
      self.DocContractTotal:int = obj["DocContractTotal"]
      """  Total Contract Amount  """  
      self.Rpt1ContractTotal:int = obj["Rpt1ContractTotal"]
      self.Rpt2ContractTotal:int = obj["Rpt2ContractTotal"]
      self.Rpt3ContractTotal:int = obj["Rpt3ContractTotal"]
      self.RenewalTotal:int = obj["RenewalTotal"]
      """  Total Renewal Amount  """  
      self.DocRenewalTotal:int = obj["DocRenewalTotal"]
      self.Rpt1RenewalTotal:int = obj["Rpt1RenewalTotal"]
      self.Rpt2RenewalTotal:int = obj["Rpt2RenewalTotal"]
      self.Rpt3RenewalTotal:int = obj["Rpt3RenewalTotal"]
      self.ExpireDate:str = obj["ExpireDate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GetContractRenewalTableset:
   def __init__(self, obj):
      self.ContractRenewal:list[Erp_Tablesets_ContractRenewalRow] = obj["ContractRenewal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExpireDate_input:
   """ Required : 
   ExpirationDate
   EffectiveDAte
   Duration
   modifier
   """  
   def __init__(self, obj):
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.EffectiveDAte:str = obj["EffectiveDAte"]
      self.Duration:int = obj["Duration"]
      self.modifier:str = obj["modifier"]
      pass

class ExpireDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRenewals_input:
   """ Required : 
   ipCustList
   ipTypeList
   ipExpireDate
   ds
   """  
   def __init__(self, obj):
      self.ipCustList:str = obj["ipCustList"]
      """  The Customer Number list to filter the records with  """  
      self.ipTypeList:str = obj["ipTypeList"]
      """  The Contract Type list to filter the records with  """  
      self.ipExpireDate:str = obj["ipExpireDate"]
      """  The Expire Date filter  """  
      self.ds:list[Erp_Tablesets_GetContractRenewalTableset] = obj["ds"]
      pass

class GetRenewals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetContractRenewalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   ipCustList
   ipTypeList
   ipExpireDate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipCustList:str = obj["ipCustList"]
      """  The where clause to restrict Customers  """  
      self.ipTypeList:str = obj["ipTypeList"]
      """  The where clause to restrict Types  """  
      self.ipExpireDate:str = obj["ipExpireDate"]
      """  The where clause to restrict Date  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GetContractRenewalTableset] = obj["returnObj"]
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

