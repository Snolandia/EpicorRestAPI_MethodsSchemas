import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesPersonWBSvc
# Description: SalesPersonWorkbench Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCustomers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomers
   Description: Retrieve all the records from Customer table
   OperationID: GetCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfContacts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfContacts
   Description: Retrieve a list of Contacts
   OperationID: GetListOfContacts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfContacts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfContacts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfCRMCalls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfCRMCalls
   Description: Retrieve a list of CRM Calls
   OperationID: GetListOfCRMCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfCRMCalls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfCRMCalls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfInvoices
   Description: Retrieve a list of invoice
   OperationID: GetListOfInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfJobs
   Description: Retrieve all the records from JobHead, OrderHed,OrderRel and OrderDtl table
   OperationID: GetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfOrders
   Description: Retrieve a list of orders
   OperationID: GetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfQuotes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfQuotes
   Description: Retrieve a list of Quotes
   OperationID: GetListOfQuotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfQuotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfQuotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfRMAs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfRMAs
   Description: Retrieve a list of RMAs
   OperationID: GetListOfRMAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfRMAs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfRMAs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfServiceCalls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfServiceCalls
   Description: Retrieve a list of Service Call
   OperationID: GetListOfServiceCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfServiceCalls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfServiceCalls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfSites(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfSites
   Description: Retrieve a list of Ship To
   OperationID: GetListOfSites
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfSites_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfSites_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfShipments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfShipments
   Description: Retrieve a list of Shipments
   OperationID: GetListOfShipments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfShipments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfShipments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListOfTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOfTasks
   Description: Retrieve a list of Task
   OperationID: GetListOfTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_SalesPersonWBCRMCallRow:
   def __init__(self, obj):
      self.CallCustNum:int = obj["CallCustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallShipToNum:str = obj["CallShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  """  
      self.CallText:str = obj["CallText"]
      """  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  """  
      self.CallVConNum:int = obj["CallVConNum"]
      """  Used to uniquely identify the contact record for the related vendor or purchase point.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConNum:int = obj["ConNum"]
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      self.SysRowID:str = obj["SysRowID"]
      self.ContactFirstName:str = obj["ContactFirstName"]
      """  Contact's first name.  """  
      self.ContactLastName:str = obj["ContactLastName"]
      """  Contact's last name.  """  
      self.ContactName:str = obj["ContactName"]
      """  Full name of the contact.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBContactRow:
   def __init__(self, obj):
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone numbe  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.Name:str = obj["Name"]
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.SysRowID:str = obj["SysRowID"]
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBCustomerRow:
   def __init__(self, obj):
      self.Address1:str = obj["Address1"]
      """  The first line of the customer's main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the customer's main address.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Country:str = obj["Country"]
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Used to define the type of the customer record.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBInvoiceRow:
   def __init__(self, obj):
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Country:str = obj["Country"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """   There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments,  and "Mis" = Miscellaneous.
The setting of this field affects invoice entry:
"Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.
"Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.
"Deposit" invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.
"Miscellaneous" - These invoices may or may not reference a Sales Order.
If Invoice is generated in Project Billing then there are following options:
"PFF" - Fixed Fee project;
"PCP" - Cost Plus project;
"PTM" - Time and Material project;
"PPP" - Progress Payment project.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.ProdGrupDesc:str = obj["ProdGrupDesc"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  """  
      self.ProdQty:int = obj["ProdQty"]
      """   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.SysRowID:str = obj["SysRowID"]
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.FSCustNum:int = obj["FSCustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.FSPartNum:str = obj["FSPartNum"]
      """  The PartNum field identifies the Part  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBOrderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Country:str = obj["Country"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the order line item, rounded according to the Base currency Round rule  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.NeedByDateDtl:str = obj["NeedByDateDtl"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the OrderDtl.NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.ProdGrupDesc:str = obj["ProdGrupDesc"]
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.RequestDateDtl:str = obj["RequestDateDtl"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderDtl.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.WebOrder:bool = obj["WebOrder"]
      """  Not editable, When SF Synch creates orders, this flag is set to YES.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBQuoteRow:
   def __init__(self, obj):
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Country:str = obj["Country"]
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity  """  
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.ProdCodeDesc:str = obj["ProdCodeDesc"]
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBRMARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  Reference to a customers accounts payable debit memo.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this RMA.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  """  
      self.OpenRMADtl:bool = obj["OpenRMADtl"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBServiceCallRow:
   def __init__(self, obj):
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBShipmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.OnTime:int = obj["OnTime"]
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderRel.ReqDate.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBSiteRow:
   def __init__(self, obj):
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesPersonWBTableset:
   def __init__(self, obj):
      self.SalesPersonWBCustomer:list[Erp_Tablesets_SalesPersonWBCustomerRow] = obj["SalesPersonWBCustomer"]
      self.SalesPersonWBContact:list[Erp_Tablesets_SalesPersonWBContactRow] = obj["SalesPersonWBContact"]
      self.SalesPersonWBCRMCall:list[Erp_Tablesets_SalesPersonWBCRMCallRow] = obj["SalesPersonWBCRMCall"]
      self.SalesPersonWBInvoice:list[Erp_Tablesets_SalesPersonWBInvoiceRow] = obj["SalesPersonWBInvoice"]
      self.SalesPersonWBJob:list[Erp_Tablesets_SalesPersonWBJobRow] = obj["SalesPersonWBJob"]
      self.SalesPersonWBOrder:list[Erp_Tablesets_SalesPersonWBOrderRow] = obj["SalesPersonWBOrder"]
      self.SalesPersonWBQuote:list[Erp_Tablesets_SalesPersonWBQuoteRow] = obj["SalesPersonWBQuote"]
      self.SalesPersonWBRMA:list[Erp_Tablesets_SalesPersonWBRMARow] = obj["SalesPersonWBRMA"]
      self.SalesPersonWBServiceCall:list[Erp_Tablesets_SalesPersonWBServiceCallRow] = obj["SalesPersonWBServiceCall"]
      self.SalesPersonWBShipment:list[Erp_Tablesets_SalesPersonWBShipmentRow] = obj["SalesPersonWBShipment"]
      self.SalesPersonWBSite:list[Erp_Tablesets_SalesPersonWBSiteRow] = obj["SalesPersonWBSite"]
      self.SalesPersonWBTask:list[Erp_Tablesets_SalesPersonWBTaskRow] = obj["SalesPersonWBTask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SalesPersonWBTaskRow:
   def __init__(self, obj):
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.SysRowID:str = obj["SysRowID"]
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      """  List of all ship to territories for the customer  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      """  Indicates if the record is inactive.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetCustomers_input:
   """ Required : 
   whereClause
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where Clause to restrict data from Customers  """  
      self.sortBy:str = obj["sortBy"]
      """  sortBy Selected  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adapter  """  
      pass

class GetCustomers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfCRMCalls_input:
   """ Required : 
   ds
   custNum
   callDesc
   origDateStart
   origDateEnd
   salesRepCode
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.callDesc:str = obj["callDesc"]
      """  Call Description  """  
      self.origDateStart:str = obj["origDateStart"]
      """  Create Date Start  """  
      self.origDateEnd:str = obj["origDateEnd"]
      """  Create Date End  """  
      self.salesRepCode:str = obj["salesRepCode"]
      """  Sales Rep Code  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfCRMCalls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfContacts_input:
   """ Required : 
   ds
   perConID
   custNum
   name
   firstName
   middleName
   lastName
   func
   faxNum
   phoneNum
   eMailAddress
   cellPhoneNum
   pagerNum
   homeNum
   altNum
   prefix
   suffix
   initials
   webSite
   iM
   twitter
   linkedIn
   faceBook
   address1
   address2
   address3
   city
   state
   zip
   corpName
   comment
   contactTitle
   reportsTo
   roleCode
   countryNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.perConID:int = obj["perConID"]
      """  Person Contac ID  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.name:str = obj["name"]
      """  Name  """  
      self.firstName:str = obj["firstName"]
      """  First Name  """  
      self.middleName:str = obj["middleName"]
      """  Middle Name  """  
      self.lastName:str = obj["lastName"]
      """  Last Name  """  
      self.func:str = obj["func"]
      """  Func  """  
      self.faxNum:str = obj["faxNum"]
      """  Fax Number  """  
      self.phoneNum:str = obj["phoneNum"]
      """  Phone Number  """  
      self.eMailAddress:str = obj["eMailAddress"]
      """  Email Address  """  
      self.cellPhoneNum:str = obj["cellPhoneNum"]
      """  CellPhone Number  """  
      self.pagerNum:str = obj["pagerNum"]
      """  Pager Number  """  
      self.homeNum:str = obj["homeNum"]
      """  Home Number  """  
      self.altNum:str = obj["altNum"]
      """  Alt Number  """  
      self.prefix:str = obj["prefix"]
      """  Prefix  """  
      self.suffix:str = obj["suffix"]
      """  Suffix  """  
      self.initials:str = obj["initials"]
      """  Initials  """  
      self.webSite:str = obj["webSite"]
      """  WebSite  """  
      self.iM:str = obj["iM"]
      """  IM  """  
      self.twitter:str = obj["twitter"]
      """  Twitter  """  
      self.linkedIn:str = obj["linkedIn"]
      """  LinkedIn  """  
      self.faceBook:str = obj["faceBook"]
      """  Facebook  """  
      self.address1:str = obj["address1"]
      """  Address 1  """  
      self.address2:str = obj["address2"]
      """  Address 2  """  
      self.address3:str = obj["address3"]
      """  Address 3  """  
      self.city:str = obj["city"]
      """  City  """  
      self.state:str = obj["state"]
      """  Satte  """  
      self.zip:str = obj["zip"]
      """  Zip Code  """  
      self.corpName:str = obj["corpName"]
      """  Corp Name  """  
      self.comment:str = obj["comment"]
      """  Comment  """  
      self.contactTitle:str = obj["contactTitle"]
      """  Contact Title  """  
      self.reportsTo:str = obj["reportsTo"]
      """  Report To  """  
      self.roleCode:str = obj["roleCode"]
      """  Role Code  """  
      self.countryNum:int = obj["countryNum"]
      """  Country Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfContacts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfInvoices_input:
   """ Required : 
   ds
   invoiceNum
   orderNum
   legalNumber
   custNum
   startDueDate
   endDueDate
   status
   type
   prodCode
   packSlip
   partNum
   plant
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.invoiceNum:int = obj["invoiceNum"]
      """  Invoice Numbre  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.legalNumber:str = obj["legalNumber"]
      """  Legal Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.startDueDate:str = obj["startDueDate"]
      """  Start Due Date  """  
      self.endDueDate:str = obj["endDueDate"]
      """  End Due Date  """  
      self.status:bool = obj["status"]
      """  Invoice Status  """  
      self.type:str = obj["type"]
      """  Invoice Type  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.packSlip:int = obj["packSlip"]
      """  Pack Slip  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfJobs_input:
   """ Required : 
   ds
   jobNum
   jobNumStart
   jobNumEnd
   custNum
   equipID
   orderShipByStart
   orderShipByEnd
   jobStartDate
   jobDueDate
   jobType
   jobClosed
   jobComplete
   jobReleased
   jobEngineered
   jobFirm
   jobHeld
   prodQty
   orderNum
   callNum
   prodCode
   partNum
   plant
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.jobNumStart:str = obj["jobNumStart"]
      """  Job Number Start  """  
      self.jobNumEnd:str = obj["jobNumEnd"]
      """  Job Number End  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.equipID:str = obj["equipID"]
      """  Equip ID  """  
      self.orderShipByStart:str = obj["orderShipByStart"]
      """  Order Ship By Start  """  
      self.orderShipByEnd:str = obj["orderShipByEnd"]
      """  Order Ship By End  """  
      self.jobStartDate:str = obj["jobStartDate"]
      """  Job Start Date  """  
      self.jobDueDate:str = obj["jobDueDate"]
      """  Job Due Date  """  
      self.jobType:str = obj["jobType"]
      """  Job Type  """  
      self.jobClosed:bool = obj["jobClosed"]
      """  Job Closed  """  
      self.jobComplete:bool = obj["jobComplete"]
      """  Job Complete  """  
      self.jobReleased:bool = obj["jobReleased"]
      """  Job Released  """  
      self.jobEngineered:bool = obj["jobEngineered"]
      """  Job Engineered  """  
      self.jobFirm:bool = obj["jobFirm"]
      """  Job Firm  """  
      self.jobHeld:bool = obj["jobHeld"]
      """  Job Held  """  
      self.prodQty:int = obj["prodQty"]
      """  Production Quantity  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.callNum:int = obj["callNum"]
      """  Call Number  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfJobs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfOrders_input:
   """ Required : 
   ds
   orderNum
   custNum
   poNum
   needByStart
   needByEnd
   shipByStart
   shipByEnd
   status
   prodCode
   partNum
   plant
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.poNum:str = obj["poNum"]
      """  Purchase Order Number  """  
      self.needByStart:str = obj["needByStart"]
      self.needByEnd:str = obj["needByEnd"]
      """  Need By End  """  
      self.shipByStart:str = obj["shipByStart"]
      """  Ship By Start  """  
      self.shipByEnd:str = obj["shipByEnd"]
      """  Ship By End  """  
      self.status:bool = obj["status"]
      """  Order Status  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.partNum:str = obj["partNum"]
      """  Part Num  """  
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfQuotes_input:
   """ Required : 
   ds
   quoteNum
   custNum
   poNum
   dueDateStart
   dueDateEnd
   expirationDateStart
   expirationDateEnd
   expired
   quoted
   prodCode
   partNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.poNum:str = obj["poNum"]
      """  Purchase Order Number  """  
      self.dueDateStart:str = obj["dueDateStart"]
      """  Due Date Start  """  
      self.dueDateEnd:str = obj["dueDateEnd"]
      """  Due Date End  """  
      self.expirationDateStart:str = obj["expirationDateStart"]
      """  Expiration Date Start  """  
      self.expirationDateEnd:str = obj["expirationDateEnd"]
      """  Expiration Date End  """  
      self.expired:bool = obj["expired"]
      """  Expired  """  
      self.quoted:bool = obj["quoted"]
      """  Quoted  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfQuotes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfRMAs_input:
   """ Required : 
   ds
   rmaNum
   custNum
   rmaStatus
   orderNum
   partNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.rmaNum:int = obj["rmaNum"]
      """  RMA Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.rmaStatus:bool = obj["rmaStatus"]
      """  RMA Status  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfRMAs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfServiceCalls_input:
   """ Required : 
   ds
   callNum
   custNum
   shipToNum
   callPriority
   callCode
   hdCaseNum
   openCall
   invoiced
   voidCall
   partNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      """  Call Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Number  """  
      self.callPriority:str = obj["callPriority"]
      """  Call Priority  """  
      self.callCode:str = obj["callCode"]
      """  Call Code  """  
      self.hdCaseNum:int = obj["hdCaseNum"]
      """  HD Case  """  
      self.openCall:bool = obj["openCall"]
      """  Open Call  """  
      self.invoiced:bool = obj["invoiced"]
      """  Invoiced  """  
      self.voidCall:bool = obj["voidCall"]
      """  Void Call  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfServiceCalls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfShipments_input:
   """ Required : 
   ds
   packNum
   custNum
   shipPerson
   shipDateStart
   shipDateEnd
   shipStatus
   readyToInvoice
   invoiced
   voided
   orderNum
   shipToNum
   partNum
   plant
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      """  Pack Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.shipPerson:str = obj["shipPerson"]
      """  Ship Person  """  
      self.shipDateStart:str = obj["shipDateStart"]
      """  Ship Date Start  """  
      self.shipDateEnd:str = obj["shipDateEnd"]
      """  Ship Date End  """  
      self.shipStatus:str = obj["shipStatus"]
      """  Ship Status  """  
      self.readyToInvoice:bool = obj["readyToInvoice"]
      """  Ready to Invoice  """  
      self.invoiced:bool = obj["invoiced"]
      """  Invoiced  """  
      self.voided:bool = obj["voided"]
      """  Voided  """  
      self.orderNum:int = obj["orderNum"]
      """  Order Number  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Num  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfShipments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfSites_input:
   """ Required : 
   ds
   shipToNum
   custNum
   name
   city
   state
   zip
   phoneNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Number  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.name:str = obj["name"]
      """  Name  """  
      self.city:str = obj["city"]
      """  City  """  
      self.state:str = obj["state"]
      """  State  """  
      self.zip:str = obj["zip"]
      """  Zip Code  """  
      self.phoneNum:str = obj["phoneNum"]
      """  Phone Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfSites_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListOfTasks_input:
   """ Required : 
   ds
   custNum
   taskDescription
   dueDateStart
   dueDateEnd
   startDateStart
   startDateEnd
   taskStatus
   taskConclusion
   quoteNum
   dataTag
   sortBy
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesPersonWBTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.taskDescription:str = obj["taskDescription"]
      """  Task Description  """  
      self.dueDateStart:str = obj["dueDateStart"]
      """  Due Date Start  """  
      self.dueDateEnd:str = obj["dueDateEnd"]
      """  Due Date End  """  
      self.startDateStart:str = obj["startDateStart"]
      """  Start Date Start  """  
      self.startDateEnd:str = obj["startDateEnd"]
      """  Start Date End  """  
      self.taskStatus:bool = obj["taskStatus"]
      """  Task Status  """  
      self.taskConclusion:str = obj["taskConclusion"]
      """  Task Conclusion  """  
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.dataTag:str = obj["dataTag"]
      """  Data Tag  """  
      self.sortBy:str = obj["sortBy"]
      """  The sort by, used to define the field to be used to sort the records  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used to define the amount of records to retrieve  """  
      pass

class GetListOfTasks_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesPersonWBTableset] = obj["returnObj"]
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

