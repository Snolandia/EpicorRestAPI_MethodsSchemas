import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PurchaseAdvisorSvc
# Description: Purchase Advisor
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Run this method when the partnumber on the detail screen changes .
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantOnOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantOnOrder
   Description: Rebuild the On Order list when the plant changes.  Prior to calling this
procedure, the RowMod field in all ttPAOnOrder records must be set to "U"
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePlantOnOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantOnOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantOnOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantPurchasedBefore(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantPurchasedBefore
   Description: Rebuild the Purchased Before list when the plant changes.  Prior to calling this
procedure, the RowMod field in all ttPAPurchasedBefore records must be set to "U"
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePlantPurchasedBefore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantPurchasedBefore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantPurchasedBefore_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPurchaseAdvisor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPurchaseAdvisor
   Description: Get the PurchaseAdvisor records from the parameters.
   OperationID: GetPurchaseAdvisor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPurchaseAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurchaseAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSupplierPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSupplierPriceList
   Description: Method to call to get the dataset based on a specific part.
   OperationID: GetSupplierPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplierPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplierPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangePartNum_input:
   """ Required : 
   newPartNum
   sysRowID
   rowType
   isSubstitute
   ds
   """  
   def __init__(self, obj):
      self.newPartNum:str = obj["newPartNum"]
      """  New Part Number  """  
      self.sysRowID:str = obj["sysRowID"]
      """  Sys Row ID for match (conflict resolution only)  """  
      self.rowType:str = obj["rowType"]
      """  Row Type for match (conflict resolution only)  """  
      self.isSubstitute:bool = obj["isSubstitute"]
      """  True whether it is a Substitute Part  """  
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newPartNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantOnOrder_input:
   """ Required : 
   ds
   cPartNum
   iPONum
   cPlant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      self.cPartNum:str = obj["cPartNum"]
      """  The part number  """  
      self.iPONum:int = obj["iPONum"]
      """  The PO number  """  
      self.cPlant:str = obj["cPlant"]
      """  The plant  """  
      pass

class ChangePlantOnOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantPurchasedBefore_input:
   """ Required : 
   ds
   cPartNum
   cPlant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      self.cPartNum:str = obj["cPartNum"]
      """  The part number  """  
      self.cPlant:str = obj["cPlant"]
      """  The plant  """  
      pass

class ChangePlantPurchasedBefore_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PAApprovedVendorsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.APVType:str = obj["APVType"]
      self.VendorNum:int = obj["VendorNum"]
      self.ClassID:str = obj["ClassID"]
      self.CustNum:int = obj["CustNum"]
      self.OpCode:str = obj["OpCode"]
      self.CustID:str = obj["CustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.VendID:str = obj["VendID"]
      self.VendorName:str = obj["VendorName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PACompliantVendPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.ClassID:str = obj["ClassID"]
      self.OpCode:str = obj["OpCode"]
      self.PUM:str = obj["PUM"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendID:str = obj["VendID"]
      self.VendorName:str = obj["VendorName"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.RestrictionName:str = obj["RestrictionName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PACompliantVendorsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.ClassID:str = obj["ClassID"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendID:str = obj["VendID"]
      self.VendorName:str = obj["VendorName"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.RestrictionName:str = obj["RestrictionName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAOnOrderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.VendorName:str = obj["VendorName"]
      self.RelQty:int = obj["RelQty"]
      self.UnitCost:int = obj["UnitCost"]
      self.DocUnitCost:int = obj["DocUnitCost"]
      self.CostPerCode:str = obj["CostPerCode"]
      self.PUM:str = obj["PUM"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DueDate:str = obj["DueDate"]
      """  DueDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.RelPromiseDt:str = obj["RelPromiseDt"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.POType:str = obj["POType"]
      self.LeadTime:int = obj["LeadTime"]
      """  Lead Time is set based on the following hierarchy: 1 - PartXRefVend.LeadTime, 2 - VendPart.LeadTime, 3 - PartPlant.LeadTime  """  
      self.UnreceivedQty:int = obj["UnreceivedQty"]
      """  The unreceived quantity  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAPurchasedBeforeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.SeqNum:int = obj["SeqNum"]
      self.ReceiptDate:str = obj["ReceiptDate"]
      self.VendorName:str = obj["VendorName"]
      self.VendorQty:int = obj["VendorQty"]
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      self.ActLead:int = obj["ActLead"]
      self.OrderDate:str = obj["OrderDate"]
      self.DueDate:str = obj["DueDate"]
      self.PUM:str = obj["PUM"]
      self.CostPerCode:str = obj["CostPerCode"]
      self.SeqType:str = obj["SeqType"]
      self.PONum:int = obj["PONum"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.UnitCost:int = obj["UnitCost"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurchaseAdvisorAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurchaseAdvisorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.PONum:int = obj["PONum"]
      self.APVType:str = obj["APVType"]
      self.ClassID:str = obj["ClassID"]
      self.OpCode:str = obj["OpCode"]
      self.CustNum:int = obj["CustNum"]
      self.PurchasedBefore:bool = obj["PurchasedBefore"]
      self.AnyOnOrder:bool = obj["AnyOnOrder"]
      self.AnyOnHand:bool = obj["AnyOnHand"]
      self.ApprovedVendors:bool = obj["ApprovedVendors"]
      self.DispPurchasedBefore:str = obj["DispPurchasedBefore"]
      self.DispAnyOnOrder:str = obj["DispAnyOnOrder"]
      self.DispAnyOnHand:str = obj["DispAnyOnHand"]
      self.DispApprovedVendors:str = obj["DispApprovedVendors"]
      self.SupplierPriceListExists:bool = obj["SupplierPriceListExists"]
      """  Indicates if there are supplier price lists  """  
      self.CompliantVendors:bool = obj["CompliantVendors"]
      self.DispCompliantVendors:str = obj["DispCompliantVendors"]
      self.CompliantVendParts:bool = obj["CompliantVendParts"]
      self.DispCompliantVendParts:str = obj["DispCompliantVendParts"]
      self.Question:str = obj["Question"]
      """  Question  """  
      self.QuestionType:str = obj["QuestionType"]
      """  Question Type  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The Part Description if exists otherwise "Non Part"  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurchaseAdvisorTableset:
   def __init__(self, obj):
      self.PurchaseAdvisor:list[Erp_Tablesets_PurchaseAdvisorRow] = obj["PurchaseAdvisor"]
      self.PurchaseAdvisorAttch:list[Erp_Tablesets_PurchaseAdvisorAttchRow] = obj["PurchaseAdvisorAttch"]
      self.PAOnOrder:list[Erp_Tablesets_PAOnOrderRow] = obj["PAOnOrder"]
      self.PAPurchasedBefore:list[Erp_Tablesets_PAPurchasedBeforeRow] = obj["PAPurchasedBefore"]
      self.PAApprovedVendors:list[Erp_Tablesets_PAApprovedVendorsRow] = obj["PAApprovedVendors"]
      self.PACompliantVendors:list[Erp_Tablesets_PACompliantVendorsRow] = obj["PACompliantVendors"]
      self.PACompliantVendPart:list[Erp_Tablesets_PACompliantVendPartRow] = obj["PACompliantVendPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SupplierPriceListTableset:
   def __init__(self, obj):
      self.SupplierVendPart:list[Erp_Tablesets_SupplierVendPartRow] = obj["SupplierVendPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SupplierVendPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor. 
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The date which this vendor/part information is effective.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.BaseUnitPrice:int = obj["BaseUnitPrice"]
      """   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number that the Vendor uses to identify the item.  """  
      self.PriceFormat:str = obj["PriceFormat"]
      """  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  """  
      self.MinimumPrice:int = obj["MinimumPrice"]
      """   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  """  
      self.Reference:str = obj["Reference"]
      """  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description of Part. Used only for Non Part master parts.  """  
      self.RFQNum:int = obj["RFQNum"]
      """   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  """  
      self.RFQLine:int = obj["RFQLine"]
      """   Related RFQ Line number. 
Note: Zero for price breaks created by master maintenance programs.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Suppliers Quantity on Hand  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  Date Suppliers Quantity was updated  """  
      self.OnHandTime:int = obj["OnHandTime"]
      """  Time Suppliers Quantity was updated  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this Price  """  
      self.SupplierResponseReady:bool = obj["SupplierResponseReady"]
      """  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Vantage.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's Name  """  
      self.VendPartNum:str = obj["VendPartNum"]
      """  Supplier Part  """  
      self.MfgName:str = obj["MfgName"]
      """  Manufacturer's Name.  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      self.Id:int = obj["Id"]
      """  Id Counter of the total of data.  """  
      self.MfgPartNumber:str = obj["MfgPartNumber"]
      """  Manufacturer Part Number (not deprecated)  """  
      self.PrimaryVendor:bool = obj["PrimaryVendor"]
      self.PurchaseDefault:bool = obj["PurchaseDefault"]
      """  PartXRefVend's Purchase Default field  """  
      self.MarketLeadTime:str = obj["MarketLeadTime"]
      """  PartXRefMfg's LeadTime  """  
      self.LifecycleStatus:str = obj["LifecycleStatus"]
      """  LifecycleStatus  """  
      self.MfgNum:int = obj["MfgNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetPurchaseAdvisor_input:
   """ Required : 
   cPartNum
   iPONum
   cAPVType
   cClassID
   cOpCode
   iCustNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number  """  
      self.iPONum:int = obj["iPONum"]
      """  The Purchase Order Number  """  
      self.cAPVType:str = obj["cAPVType"]
      """  The APVType for Approved Vendors  """  
      self.cClassID:str = obj["cClassID"]
      """  The Class ID  """  
      self.cOpCode:str = obj["cOpCode"]
      """  The Op Code  """  
      self.iCustNum:int = obj["iCustNum"]
      """  The customer number  """  
      pass

class GetPurchaseAdvisor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurchaseAdvisorTableset] = obj["returnObj"]
      pass

class GetSupplierPriceList_input:
   """ Required : 
   cPartNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number to retrieve the dataset for  """  
      pass

class GetSupplierPriceList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupplierPriceListTableset] = obj["returnObj"]
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

