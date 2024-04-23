import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ETCAddrValidationSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Getit(epicorHeaders = None):
   """  
   Summary: Invoke method Getit
   Description: Called when the user chooses a new valid address.
   OperationID: Getit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Getit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofValidAddr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofValidAddr
   Description: Called when the user chooses a new valid address.
   OperationID: OnChangeofValidAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofValidAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofValidAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofAddr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofAddr
   Description: Called when the user changes the address.
   OperationID: OnChangeofAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAddr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAddr
   Description: Purpose:
Parameters:  none
Notes:
<param name="RequestID">RequestID</param><param name="ds">ETCAddrValidation data set</param>
   OperationID: SetAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ETCAddrValidationTableset:
   def __init__(self, obj):
      self.ETCAddress:list[Erp_Tablesets_ETCAddressRow] = obj["ETCAddress"]
      self.ETCMessage:list[Erp_Tablesets_ETCMessageRow] = obj["ETCMessage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ETCAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.City:str = obj["City"]
      """  City name  """  
      self.Country:str = obj["Country"]
      """  Country name  """  
      self.Line1:str = obj["Line1"]
      """  Address line 1  """  
      self.Line2:str = obj["Line2"]
      """  Address line 2  """  
      self.Line3:str = obj["Line3"]
      """  Address line 3  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal or ZIP code  """  
      self.Region:str = obj["Region"]
      """  State or province name  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.UpdateAddr:bool = obj["UpdateAddr"]
      """  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  """  
      self.RequestID:str = obj["RequestID"]
      """  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  """  
      self.AddressCode:str = obj["AddressCode"]
      """  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  """  
      self.CarrierRoute:str = obj["CarrierRoute"]
      """  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  """  
      self.ValidCity:str = obj["ValidCity"]
      """  City name  """  
      self.ValidCountry:str = obj["ValidCountry"]
      """  Country name  """  
      self.County:str = obj["County"]
      """  County name  """  
      self.FipsCode:str = obj["FipsCode"]
      """  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  """  
      self.ValidLine1:str = obj["ValidLine1"]
      """  Line one of the valid address returned by the tax integration.  """  
      self.ValidLine2:str = obj["ValidLine2"]
      """  Line two of the valid address returned by the tax integration.  """  
      self.ValidLine3:str = obj["ValidLine3"]
      """  Line three of the valid address returned by the tax integration.  """  
      self.ValidLine4:str = obj["ValidLine4"]
      """  Line four of the valid address returned by the tax integration.  """  
      self.ValidPostalCode:str = obj["ValidPostalCode"]
      """  Postal code returned by the tax integration.  """  
      self.PostNet:str = obj["PostNet"]
      """  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  """  
      self.ValidRegion:str = obj["ValidRegion"]
      """  State or province name or abbreviation returned by the tax integration.  """  
      self.ResultCode:str = obj["ResultCode"]
      """  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.ResultSeq:int = obj["ResultSeq"]
      """  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  """  
      self.CarrierRouteDesc:str = obj["CarrierRouteDesc"]
      """  Carrier Route description  """  
      self.AddressTypeDesc:str = obj["AddressTypeDesc"]
      """  Address type description  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ETCMessageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Details:str = obj["Details"]
      self.Helplink:str = obj["Helplink"]
      """  URL to help page for this message  """  
      self.Name:str = obj["Name"]
      """  Gets the name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  """  
      self.Severity:str = obj["Severity"]
      """  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.Source:str = obj["Source"]
      """  source of the message  """  
      self.Summary:str = obj["Summary"]
      """  concise summary of the message  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.RequestID:str = obj["RequestID"]
      """  Programitically assigned.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Getit_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["returnObj"]
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

class OnChangeofAddr_input:
   """ Required : 
   RequestID
   ds
   """  
   def __init__(self, obj):
      self.RequestID:str = obj["RequestID"]
      """  RequestID  """  
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

class OnChangeofAddr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.StatusFlag:bool = obj["StatusFlag"]
      self.ErrorFlag:bool = obj["ErrorFlag"]
      self.ErrorMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofValidAddr_input:
   """ Required : 
   RequestID
   ds
   """  
   def __init__(self, obj):
      self.RequestID:str = obj["RequestID"]
      """  RequestID  """  
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

class OnChangeofValidAddr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetAddr_input:
   """ Required : 
   RequestID
   ds
   """  
   def __init__(self, obj):
      self.RequestID:str = obj["RequestID"]
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

class SetAddr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

