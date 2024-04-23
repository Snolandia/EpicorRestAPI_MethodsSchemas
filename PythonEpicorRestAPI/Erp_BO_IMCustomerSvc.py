import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMCustomerSvc
# Description: Business Object to handle: Count, Get, Ack, Add, Update and Delete of Customer, ShipTo, CustCnt, CustBillTo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckCustomer
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountCustomer
   Description: Returns the count of existing IntQueOut records along with the count of updated customers in the database that IntQueOut records have not yet been created for
   OperationID: CountCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllCustomer
   Description: Generates IntQueOut and IMCustomer rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomer
   Description: Generates IntQueOut and IMCustomer rows since the last time this was called and then returns these along with any existing
   OperationID: GetCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddCustomer
   Description: Add customer and customer related tables
   OperationID: AddCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCustomer
   Description: Delete customer and customer related tables
   OperationID: DeleteCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCustomer
   Description: Update customer and customer related tables
   OperationID: UpdateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckCustomer_input:
   """ Required : 
   IMCustomerTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMCustomerTableset:list[Erp_Tablesets_IMCustomerTableset] = obj["IMCustomerTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class AddCustomer_input:
   """ Required : 
   IMCustomerTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMCustomerTableset:list[Erp_Tablesets_IMCustomerTableset] = obj["IMCustomerTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class CountCustomer_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteCustomer_input:
   """ Required : 
   IMCustomerTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMCustomerTableset:list[Erp_Tablesets_IMCustomerTableset] = obj["IMCustomerTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMCustBillToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Indicates the CustNum of the alternate Bill To Customer.  """  
      self.DefaultBillTo:bool = obj["DefaultBillTo"]
      """  Indicates whether this Alt Bill To is the default record or not.  """  
      self.InvoiceAddress:bool = obj["InvoiceAddress"]
      """  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.OurBankCode:str = obj["OurBankCode"]
      """  Our Bank Code  """  
      self.BTLegalName:str = obj["BTLegalName"]
      """  Full Legal name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FSACustomerNotSent:bool = obj["FSACustomerNotSent"]
      """  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMCustCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the customer's main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the customer's main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the customer's main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the customer's main address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.Country:str = obj["Country"]
      """  The country of the main customer address.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Contains the Currency.CurrencyCode value of the customer's base currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Contains the Country.CountryNum value of the country the customer is located in.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  """  
      self.BTName:str = obj["BTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.BTAddress1:str = obj["BTAddress1"]
      """  The first line of the customer's Bill To address.  """  
      self.BTAddress2:str = obj["BTAddress2"]
      """  The second line of the customer's Bill To address.  """  
      self.BTAddress3:str = obj["BTAddress3"]
      """  The second line of the customer's Bill To address.  """  
      self.BTCity:str = obj["BTCity"]
      """  The city portion of the customer's Bill To address.  """  
      self.BTState:str = obj["BTState"]
      """  The state or province portion of the customer's Bill To address.  """  
      self.BTZip:str = obj["BTZip"]
      """  The zip or postal code portion of the customer's Bill To address.  """  
      self.BTCountryNum:int = obj["BTCountryNum"]
      """  The Country.Countrynum value of the Country portion of the customer's Bill To address.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  Contains the Country.Description value of the Country portion of the customer's Bill To address.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The phone number related to the customer's Bill To Address.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The fax number of the customer's Bill To address.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Default email address for the customer.  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Used to define the type of the customer record.  """  
      self.CustURL:str = obj["CustURL"]
      """  The Customer's website URL.  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      """  Specifies the current customer can be an alternate bill to customer.  """  
      self.ValidSoldTo:bool = obj["ValidSoldTo"]
      """  Sold to customer in the AR Invoice Entry. The user will not be able to enter invoices for customers without this authorization  """  
      self.ValidShipTo:bool = obj["ValidShipTo"]
      """  Receive shipments for orders entered in OE. Unless the user selects this option, the user must enter a Ship-to address in the Order Entry form.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the customer has to be synchronized with Epicor FSA application.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMCustomerTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMCustBillTo:list[Erp_Tablesets_IMCustBillToRow] = obj["IMCustBillTo"]
      self.IMCustCnt:list[Erp_Tablesets_IMCustCntRow] = obj["IMCustCnt"]
      self.IMCustomer:list[Erp_Tablesets_IMCustomerRow] = obj["IMCustomer"]
      self.IMShipTo:list[Erp_Tablesets_IMShipToRow] = obj["IMShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMIntegrationKeyRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  The master file which the integration is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyTableset:
   def __init__(self, obj):
      self.IMIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyRow] = obj["IMIntegrationKey"]
      self.IMNaturalKeys:list[Erp_Tablesets_IMNaturalKeysRow] = obj["IMNaturalKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMNaturalKeysRow:
   def __init__(self, obj):
      self.KeyValue:str = obj["KeyValue"]
      self.KeyColumn:str = obj["KeyColumn"]
      self.Sequence:int = obj["Sequence"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllCustomer_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMCustomerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetCustomer_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMCustomerTableset] = obj["returnObj"]
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

class UpdateCustomer_input:
   """ Required : 
   IMCustomerTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMCustomerTableset:list[Erp_Tablesets_IMCustomerTableset] = obj["IMCustomerTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class UpdateCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

