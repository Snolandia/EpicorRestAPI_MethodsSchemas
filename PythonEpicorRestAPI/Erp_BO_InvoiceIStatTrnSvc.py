import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InvoiceIStatTrnSvc
# Description: Intrastat entry for AP Invoices and AR Invoices
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_APGetInvoiceIStatTrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method APGetInvoiceIStatTrn
   Description: Gets the InvoiceIStatTrn record for an APInvDtl record.
   OperationID: APGetInvoiceIStatTrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/APGetInvoiceIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/APGetInvoiceIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ARGetInvoiceIStatTrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ARGetInvoiceIStatTrn
   Description: Gets the InvoiceIStatTrn record for an AR InvcDtl record.
   OperationID: ARGetInvoiceIStatTrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ARGetInvoiceIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ARGetInvoiceIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCommodityCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCommodityCode
   Description: Method to call when changing the commodity code.  Validates the code and
updates CommodityCodeDescription field for the code.
   OperationID: ChangeCommodityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFOB(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFOB
   Description: Method to call when changing the FOB code.  Validates the code and
updates FOBDescription field for the code.
   OperationID: ChangeFOB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFOB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFOB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipVia(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipVia
   Description: Method to call when changing the ship via code.  Validates the code and
updates ShipViaDescription field for the code.
   OperationID: ChangeShipVia
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateIStatTrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateIStatTrn
   Description: Updates/creates the IStatTrn record.
   OperationID: UpdateIStatTrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFlowList(epicorHeaders = None):
   """  
   Summary: Invoke method GetFlowList
   Description: Returns the Flow List.
   OperationID: GetFlowList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class APGetInvoiceIStatTrn_input:
   """ Required : 
   InVendorNum
   InInvoiceNum
   InInvoiceLine
   forTracker
   """  
   def __init__(self, obj):
      self.InVendorNum:int = obj["InVendorNum"]
      """  The vendor number of the invoice detail line  """  
      self.InInvoiceNum:str = obj["InInvoiceNum"]
      """  The invoice number of the invoice detail line  """  
      self.InInvoiceLine:int = obj["InInvoiceLine"]
      """  The line number of the invoice detail line  """  
      self.forTracker:bool = obj["forTracker"]
      """  This flag indicates that this function is called for Tracker  """  
      pass

class APGetInvoiceIStatTrn_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["returnObj"]
      pass

class ARGetInvoiceIStatTrn_input:
   """ Required : 
   InInvoiceNum
   InInvoiceLine
   forTracker
   """  
   def __init__(self, obj):
      self.InInvoiceNum:int = obj["InInvoiceNum"]
      """  The invoice number of the invoice detail line  """  
      self.InInvoiceLine:int = obj["InInvoiceLine"]
      """  The line number of the invoice detail line  """  
      self.forTracker:bool = obj["forTracker"]
      """  This flag indicates that this function is called for Tracker  """  
      pass

class ARGetInvoiceIStatTrn_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["returnObj"]
      pass

class ChangeCommodityCode_input:
   """ Required : 
   ProposedCommodityCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedCommodityCode:str = obj["ProposedCommodityCode"]
      """  The proposed commodity code  """  
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

class ChangeCommodityCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFOB_input:
   """ Required : 
   ProposedFOB
   ds
   """  
   def __init__(self, obj):
      self.ProposedFOB:str = obj["ProposedFOB"]
      """  The proposed FOB code  """  
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

class ChangeFOB_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipVia_input:
   """ Required : 
   ProposedShipViaCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedShipViaCode:str = obj["ProposedShipViaCode"]
      """  The proposed ship via code  """  
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

class ChangeShipVia_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IStatTrnRow:
   def __init__(self, obj):
      self.Flow:str = obj["Flow"]
      """  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  """  
      self.Period:str = obj["Period"]
      """  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.Amount:int = obj["Amount"]
      """  Value of transported goods excluding taxes but including miscellaneous charges.  """  
      self.Terms:str = obj["Terms"]
      """  Delivery terms.  """  
      self.TransactionType:str = obj["TransactionType"]
      """  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.ISCountryCode:str = obj["ISCountryCode"]
      """  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  """  
      self.ISShipViaCode:str = obj["ISShipViaCode"]
      """  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border.  """  
      self.FlowSpec:str = obj["FlowSpec"]
      """  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  Currency indicator. Primarily used to cover the transitional period for the Euro.  """  
      self.Description:str = obj["Description"]
      """  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  """  
      self.SuppUnits:int = obj["SuppUnits"]
      """  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted Flag  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "ShipVia" table.  """  
      self.FOB:str = obj["FOB"]
      """  The code for the FOB policy.  """  
      self.TaxID:str = obj["TaxID"]
      """  Optional field used to record the customer/vendor State Tax Identification number.  """  
      self.InvAmount:int = obj["InvAmount"]
      """  Value of transported goods excluding taxes and miscellaneous charges.  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.NotReported:bool = obj["NotReported"]
      """  Not Reported Flag  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StampID:str = obj["StampID"]
      """  Free form stamp to indicate the record has been reported to the authorities.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.TaricCode:str = obj["TaricCode"]
      """  European Union integrated tariff.  """  
      self.EUPreference:str = obj["EUPreference"]
      """  European Union preference.  """  
      self.ExtraTrade:bool = obj["ExtraTrade"]
      """  Extra trade transaction indicator.  """  
      self.CommodityFlow:str = obj["CommodityFlow"]
      """  Commodity flow refers to the nature of a (cross-border) movement of goods.  """  
      self.CustomsProcedure:str = obj["CustomsProcedure"]
      """  Indicates which requested procedure and preceding procedure applies to the customs declaration.  """  
      self.ISCustomsDeclCountry:str = obj["ISCustomsDeclCountry"]
      """  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  """  
      self.ISEUBorderCrossingCountry:str = obj["ISEUBorderCrossingCountry"]
      """  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  """  
      self.IntraEUTransportMode:str = obj["IntraEUTransportMode"]
      """  The mode of transport refers to the mode of transport within the EU.  """  
      self.ContainerShip:bool = obj["ContainerShip"]
      """  Indicates whether or not there is transport by container.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  """  
      self.DocInvAmount:int = obj["DocInvAmount"]
      """  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  """  
      self.InvCurrencyCode:str = obj["InvCurrencyCode"]
      """  A unique code that identifies the invoice currency.  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EUThirdParty  """  
      self.CountryDescr:str = obj["CountryDescr"]
      """  Country description  """  
      self.CountryOfOriginDescr:str = obj["CountryOfOriginDescr"]
      """  Description of country of origin  """  
      self.CustIDSuppID:str = obj["CustIDSuppID"]
      """  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  """  
      self.CustSuppName:str = obj["CustSuppName"]
      self.DelivTermsDescr:str = obj["DelivTermsDescr"]
      """  Delivery Terms description  """  
      self.EntrPointDescr:str = obj["EntrPointDescr"]
      """  Entry Point description  """  
      self.Generate2Line:bool = obj["Generate2Line"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.ManualEntry:bool = obj["ManualEntry"]
      self.ModeOfTransportDescr:str = obj["ModeOfTransportDescr"]
      """  Mode of Transport description  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RegionDescr:str = obj["RegionDescr"]
      """  Region description  """  
      self.ReportID:str = obj["ReportID"]
      self.SpecDescr:str = obj["SpecDescr"]
      """  Spec description  """  
      self.TranTypeDescr:str = obj["TranTypeDescr"]
      """  Transaction Type description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeSuppUnitsUOM:str = obj["CommodityCodeSuppUnitsUOM"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.InvCurrencyCurrDesc:str = obj["InvCurrencyCurrDesc"]
      self.InvCurrencyCurrSymbol:str = obj["InvCurrencyCurrSymbol"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvoiceIStatTrnTableset:
   def __init__(self, obj):
      self.IStatTrn:list[Erp_Tablesets_IStatTrnRow] = obj["IStatTrn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetFlowList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Flow List  """  
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

class UpdateIStatTrn_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

class UpdateIStatTrn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvoiceIStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

