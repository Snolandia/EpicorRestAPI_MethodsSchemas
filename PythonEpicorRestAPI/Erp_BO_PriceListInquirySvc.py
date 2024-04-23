import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceListInquirySvc
# Description: Price List Inquiry contains tables of price breaks for price lists based on parts.
The records of those tables  represent an "at least this quantity"
which needs to be ordered to kick in the corresponding discount percent
or unit price.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustID
   Description: Get filter values from the Customer.
   OperationID: ChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDiscountPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDiscountPercent
   Description: Update NetPrice when the discount percent changes.
   OperationID: ChangeDiscountPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDiscountPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscountPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Get filter values from the Part.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToNum
   Description: Get filter values from the ShipTo.
   OperationID: ChangeShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyByCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyByCustID
   Description: Get currency values from the Customer.
   OperationID: GetCurrencyByCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyByCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyByCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceListInquiry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceListInquiry
   Description: Get the PriceListInquiry records for the inquiry parameters.
   OperationID: GetPriceListInquiry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceListInquiry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInquiry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColumnChangingCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ColumnChangingCustID
   Description: Called when Customer ID changes.  Returns default values for the customer.
   OperationID: ColumnChangingCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColumnChangingCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnChangingCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColumnChangingShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ColumnChangingShipToNum
   Description: Called when Ship To Num changes.  Returns default values for the ship To.
   OperationID: ColumnChangingShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColumnChangingShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnChangingShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceListInquiryCriteriaDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceListInquiryCriteriaDefaults
   Description: Assigns default values for Price List Inquiry criteria
   OperationID: GetPriceListInquiryCriteriaDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceListInquiryCriteriaDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInquiryCriteriaDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCustID_input:
   """ Required : 
   cCustID
   """  
   def __init__(self, obj):
      self.cCustID:str = obj["cCustID"]
      """  The Customer ID  """  
      pass

class ChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCustName:str = obj["parameters"]
      self.cShipToNum:str = obj["parameters"]
      self.cCustGroupCode:str = obj["parameters"]
      self.dDiscountPercent:int = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDiscountPercent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceListInquiryTableset] = obj["ds"]
      pass

class ChangeDiscountPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceListInquiryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   cPartNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The part number  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cProdCode:str = obj["parameters"]
      self.cPartDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeShipToNum_input:
   """ Required : 
   cCustID
   cShipToNum
   """  
   def __init__(self, obj):
      self.cCustID:str = obj["cCustID"]
      """  The Customer ID  """  
      self.cShipToNum:str = obj["cShipToNum"]
      """  The Ship To Number  """  
      pass

class ChangeShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCustName:str = obj["parameters"]
      pass

      """  output parameters  """  

class ColumnChangingCustID_input:
   """ Required : 
   custID
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      """  Customer ID  """  
      pass

class ColumnChangingCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.custNum:int = obj["parameters"]
      self.customerName:str = obj["parameters"]
      self.groupCode:str = obj["parameters"]
      self.currencyCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class ColumnChangingShipToNum_input:
   """ Required : 
   custID
   shipToNum
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class ColumnChangingShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.customerName:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique set of characters entered by the user to identify the Price List master within the company.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLGrupBrk:bool = obj["GlobalPLGrupBrk"]
      """  Marks this PLGrupBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button (P or D)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """   Unique set of characters entered by the user to identify
the Price List master within the company.  """  
      self.PartNum:str = obj["PartNum"]
      """  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLPartBrk:bool = obj["GlobalPLPartBrk"]
      """  Marks this PLPartBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button. (D or P)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceListInquiryCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.GroupCode:str = obj["GroupCode"]
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.ProdCode:str = obj["ProdCode"]
      self.Quantity:int = obj["Quantity"]
      self.SelectCustomer:str = obj["SelectCustomer"]
      """  Retrieve for (C)ustomer or Customer (G)roup  """  
      self.SelectPart:str = obj["SelectPart"]
      """  Retrieve for (P)art or Product (G)roup  """  
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.UOMCode:str = obj["UOMCode"]
      self.Warehouse:str = obj["Warehouse"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceListInquiryCriteriaTableset:
   def __init__(self, obj):
      self.PriceListInquiryCriteria:list[Erp_Tablesets_PriceListInquiryCriteriaRow] = obj["PriceListInquiryCriteria"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceListInquiryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BasePriceList:str = obj["BasePriceList"]
      self.QuantityBreakList:str = obj["QuantityBreakList"]
      self.DiscountPercent:int = obj["DiscountPercent"]
      self.BasePrice:int = obj["BasePrice"]
      self.BreakPrice:int = obj["BreakPrice"]
      self.NetPrice:int = obj["NetPrice"]
      self.Warehouse:str = obj["Warehouse"]
      self.Quantity:int = obj["Quantity"]
      self.UOMCode:str = obj["UOMCode"]
      self.DiscountListCode:str = obj["DiscountListCode"]
      """  Discount List code selected for the inquiry selection  """  
      self.PartUnitPrice:int = obj["PartUnitPrice"]
      """  Part Unit Price saved from Part master record  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Value to store the discount amount for the selected price list  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceListInquiryTableset:
   def __init__(self, obj):
      self.PriceListInquiry:list[Erp_Tablesets_PriceListInquiryRow] = obj["PriceListInquiry"]
      self.PriceLstGroups:list[Erp_Tablesets_PriceLstGroupsRow] = obj["PriceLstGroups"]
      self.PLGrupBrk:list[Erp_Tablesets_PLGrupBrkRow] = obj["PLGrupBrk"]
      self.PriceLstParts:list[Erp_Tablesets_PriceLstPartsRow] = obj["PriceLstParts"]
      self.PLPartBrk:list[Erp_Tablesets_PLPartBrkRow] = obj["PLPartBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrencyByCustID_input:
   """ Required : 
   cCustID
   """  
   def __init__(self, obj):
      self.cCustID:str = obj["cCustID"]
      """  The Customer ID  """  
      pass

class GetCurrencyByCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cCurrencyCode:str = obj["parameters"]
      self.cCurrencyCurrDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   custNum
   SysRowID
   rowType
   uomCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.custNum:int = obj["custNum"]
      """  Customer number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetPriceListInquiryCriteriaDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceListInquiryCriteriaTableset] = obj["ds"]
      pass

class GetPriceListInquiryCriteriaDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceListInquiryCriteriaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPriceListInquiry_input:
   """ Required : 
   icCustID
   icShipToNum
   icPartNum
   icCustGroupCode
   icProductCode
   idQuantity
   icUOMCode
   icWarehouseCode
   icCurrencyCode
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.icCustID:str = obj["icCustID"]
      """  The Customer ID  """  
      self.icShipToNum:str = obj["icShipToNum"]
      """  The Part Number  """  
      self.icPartNum:str = obj["icPartNum"]
      """  The Ship To Number  """  
      self.icCustGroupCode:str = obj["icCustGroupCode"]
      """  The Customer Group Code  """  
      self.icProductCode:str = obj["icProductCode"]
      """  The Product Code  """  
      self.idQuantity:int = obj["idQuantity"]
      """  The Quantity  """  
      self.icUOMCode:str = obj["icUOMCode"]
      """  The UOM Code  """  
      self.icWarehouseCode:str = obj["icWarehouseCode"]
      """  The Warehouse Code  """  
      self.icCurrencyCode:str = obj["icCurrencyCode"]
      """  The Currency Code  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize parameter  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePages parameter  """  
      pass

class GetPriceListInquiry_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceListInquiryTableset] = obj["returnObj"]
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

class ValidUOM_input:
   """ Required : 
   prodGroup
   iPartNum
   iUOM
   """  
   def __init__(self, obj):
      self.prodGroup:str = obj["prodGroup"]
      self.iPartNum:str = obj["iPartNum"]
      self.iUOM:str = obj["iUOM"]
      pass

class ValidUOM_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

