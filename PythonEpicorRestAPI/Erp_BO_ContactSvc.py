import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ContactSvc
# Description: The contact service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Contacts_Company_ContactName(Company, ContactName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Contact item
   Description: Calls GetByID to retrieve the Contact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Contact
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContactName: Desc: ContactName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContactRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/Contacts(" + Company + "," + ContactName + ")",headers=creds) as resp:
           return await resp.json()

async def get_Contacts_Company_ContactName_ContactCustomers_Company_CustNum(Company, ContactName, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContactCustomer item
   Description: Calls GetByID to retrieve the ContactCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContactCustomer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContactName: Desc: ContactName   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContactCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/Contacts(" + Company + "," + ContactName + ")/ContactCustomers(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContactCustomers_Company_CustNum(Company, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContactCustomer item
   Description: Calls GetByID to retrieve the ContactCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContactCustomer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContactCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/ContactCustomers(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCnts_Company_CustNum_ShipToNum_ConNum(Company, CustNum, ShipToNum, ConNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCnt item
   Description: Calls GetByID to retrieve the CustCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCnts_Company_CustNum_ShipToNum_ConNum_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCnts(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + ")/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCntAttches_Company_CustNum_ShipToNum_ConNum_DrawingSeq(Company, CustNum, ShipToNum, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntAttch item
   Description: Calls GetByID to retrieve the CustCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/CustCntAttches(" + Company + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipToes_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipTo item
   Description: Calls GetByID to retrieve the ShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/ShipToes(" + Company + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContactListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetByID(ContactName, CustNumList, inCustNum, inShipToNum, inConNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Get customers, ship to's and contacts by Contact Name.
   OperationID: Get_GetByID
      :param ContactName: Desc: The Contact Name   Required: True   Allow empty value : True
      :param CustNumList: Desc: Delimited list of customer numbers selected   Required: True   Allow empty value : True
      :param inCustNum: Desc: Specific Customer number.  Used for context menu   Required: True
      :param inShipToNum: Desc: Specific ShipTo Number.  Used for context menu   Required: True   Allow empty value : True
      :param inConNum: Desc: Specific Contact Number.  Used for context menu   Required: True
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
   params += "ContactName=" + ContactName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "CustNumList=" + CustNumList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inCustNum=" + inCustNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inShipToNum=" + inShipToNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inConNum=" + inConNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: List of contacts.
   OperationID: Get_GetList
      :param whereClause: Desc: Where condition   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CondenseContactList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CondenseContactList
   Description: Condenses the list of contacts.
   OperationID: CondenseContactList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CondenseContactList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CondenseContactList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: List of contacts.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustCntAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustCntAttch
   Description: Empty method so the adapter will add the attachment logic for CustCnt.
   OperationID: GetNewCustCntAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustCntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContactSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContactListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContactListRow] = obj["value"]
      pass

class Erp_Tablesets_ContactCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
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
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is displayed on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode of the default salesperson for the customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference a sales orders.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for the customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in ship to maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls whether or not this customer's statement will print when   printing of customer statements.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgements.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer will be included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Contains the CustGrup.GroupCode value of the customer group that the customer has been assigned to. This field is used by the application for sorting or filtering on reports and can also be associated with price lists.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for any order placed by customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the CustCnt.ConNum value of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Primary Billing Contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Primary Shipping Contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when the customer was established as a customer. Use the system date as a default when creating new customers.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why the customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The QMarkup.MarkupID value of the quote markup table which will be used to provide default markup percents in quote entry for this customer. If left blank the quote module will use the default quote markup table for the customer. (See EQSyst.MarkupID).  """  
      self.BillDay:int = obj["BillDay"]
      """   Represents the day of the week or month that this customer is invoiced on. The possible choices are determined by the Customer.Bill-Frequency field value.

When the Bill-Frequency is "W" (Weeky):
The valid values are 0-7 where 0=All Days,1=Sun,2=Mon,...,7=Sat.  

ll-frequency is 'M' (Monthly) this field contains the 1st -> 31st as possible choices to represent the day of the month to bill on.  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  Determines whether or not packing slips for the same Sales Order and Fiscal Period will combined into a single invoice or not. If the packing slips are for different sales orders for the customer or fall in different fiscal periods, seperate invoices will be created even when this field is set to Yes.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS","CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer’s open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer’s credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer’s credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer’s credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  Contains the Currency.CurrencyCode value of the customer's base currency.  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Contains the Currency.CurrencyCode value of the customer's base currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Contains the Country.CountryNum value of the country the customer is located in.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/City code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set to yes.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format used to format the customer's main address.  """  
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
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional custom address format used to format the customer's Bill To address.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Default email address for the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Determines whether or not the customer will accept partial shipments at the line or order level. This functionality is only available with the Advanced Material Management module.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Contains the AllocPri.PriorityCode value of the priority that this customer's orders receive. This functionality is only available with the Advanced Material Management module.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer will be able to access Customer Connect.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and Customer Connect DB.  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Used to define the type of the customer record.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this customer will be included in marketing lists.  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  Determines whether or not the customer's territory can be changed by system processes that could potentially change the territory from its current value.  """  
      self.CustURL:str = obj["CustURL"]
      """  The Customer's website URL.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  Determines whether or not shipments to this customer for different sales orders within the same fiscal period wil be consolidated into one invoice. (See Customer.OneInvPerPS - for the shipments from the same sales order are handled).  """  
      self.Bill_Frequency:str = obj["Bill_Frequency"]
      """  Used in conjunction with the Customer.BillDay field to determine on what days the customer can be invoiced on. See Customer.BillDay description for additional information.  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  Determines whether or not an external delivery note is required for the customer.  This field is available only when ExtCompany.SendShip is set to Yes.  This will provide the default for the ShipHead record.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      """  Determines whether or not the system should check existing orders for this customer to insure that the same PO number is not used twice by the customer.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:  
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based d  """  
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      """  Specifies the current customer can be an alternate bill to customer.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the plant values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Plant values will be used  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      """  This is the Vendor ID to be used when generating a Rebate for the customer  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      """  Indicates if the order should default as a credit card order.  Can be overriden at the order level.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChargeCode:str = obj["ChargeCode"]
      """  Unique Identifier for the Finance Charges  """  
      self.ContactName:str = obj["ContactName"]
      """  The contact's name.  """  
      self.AllocationDescription:str = obj["AllocationDescription"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Label that displays as the suffix behind the amount printed on checks  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """  The label that displays as the suffix behind the amount printed on checks.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  The special character used for this currency. This character displays on reports and programs near the currency amounts.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CustGrupGroupDesc:str = obj["CustGrupGroupDesc"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Service Home Delivery Type Code Description.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      """  The label that displays as the suffix behind the amount printed on checks.  """  
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      """  The symbol of the global currency linked to this currency record.  """  
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.MarkUpDescription:str = obj["MarkUpDescription"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContactListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.ContactName:str = obj["ContactName"]
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustNumList:str = obj["CustNumList"]
      """  A list of customer numbers that were selected for the contact name.  Delimited with ~.  """  
      self.ConNum:int = obj["ConNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContactRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The name of the current company.  """  
      self.FirstName:str = obj["FirstName"]
      """  The contact's full first name. This first name will default from the Contact Details sheet, but you can edit it within this field as well.  """  
      self.LastName:str = obj["LastName"]
      """  The contact's full last name. This last name will default from the Contact Details sheet, but you can edit it within this field as well.  """  
      self.ContactName:str = obj["ContactName"]
      """  The contact’s name.  """  
      self.CustNum:int = obj["CustNum"]
      """  The number of a Customer.  """  
      self.CustID:str = obj["CustID"]
      """  The unique identifier for a customer record. On certain reports or windows where space is limited, you may see only the ID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.CustNumList:str = obj["CustNumList"]
      """  Delimited list of Customer CustNum.  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Delimited list of Customer CustNum and Name (for Kinetic)  """  
      self.ShipToList:str = obj["ShipToList"]
      """  Delimited list of shipto CustNum and Name (for Kinetic)  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
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

class Erp_Tablesets_CustCntRow:
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
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
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
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
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
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the customer contact  is synchronized to an External CRM.  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  This field holds the id of this customer in the External CRM  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  This field holds the id of this customer contact in the External CRM  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      """   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  """  
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      """   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  """  
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      """   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToRow:
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
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.WIWebShipTo:bool = obj["WIWebShipTo"]
      """  WIWebShipTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  Check if the part is a run out part.  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  INSTRegistration  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MXFederalID:str = obj["MXFederalID"]
      """  MXFederalID  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.PEUBIGEOCode:str = obj["PEUBIGEOCode"]
      """  Geographical Location Code  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceDescription:str = obj["AGProvinceDescription"]
      self.CountryISOCode:str = obj["CountryISOCode"]
      self.CountryEUMember:bool = obj["CountryEUMember"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CondenseContactList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContactListTableset] = obj["ds"]
      pass

class CondenseContactList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContactListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ContactCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
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
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is displayed on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode of the default salesperson for the customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference a sales orders.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory assigned to the customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for the customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in ship to maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls whether or not this customer's statement will print when   printing of customer statements.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgements.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer will be included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Contains the CustGrup.GroupCode value of the customer group that the customer has been assigned to. This field is used by the application for sorting or filtering on reports and can also be associated with price lists.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for any order placed by customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the CustCnt.ConNum value of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Primary Billing Contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Primary Shipping Contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when the customer was established as a customer. Use the system date as a default when creating new customers.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why the customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The QMarkup.MarkupID value of the quote markup table which will be used to provide default markup percents in quote entry for this customer. If left blank the quote module will use the default quote markup table for the customer. (See EQSyst.MarkupID).  """  
      self.BillDay:int = obj["BillDay"]
      """   Represents the day of the week or month that this customer is invoiced on. The possible choices are determined by the Customer.Bill-Frequency field value.

When the Bill-Frequency is "W" (Weeky):
The valid values are 0-7 where 0=All Days,1=Sun,2=Mon,...,7=Sat.  

ll-frequency is 'M' (Monthly) this field contains the 1st -> 31st as possible choices to represent the day of the month to bill on.  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  Determines whether or not packing slips for the same Sales Order and Fiscal Period will combined into a single invoice or not. If the packing slips are for different sales orders for the customer or fall in different fiscal periods, seperate invoices will be created even when this field is set to Yes.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS","CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer’s open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer’s credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer’s credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer’s credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.Character01:str = obj["Character01"]
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  Contains the Currency.CurrencyCode value of the customer's base currency.  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Contains the Currency.CurrencyCode value of the customer's base currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Contains the Country.CountryNum value of the country the customer is located in.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/City code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set to yes.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format used to format the customer's main address.  """  
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
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional custom address format used to format the customer's Bill To address.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Default email address for the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Determines whether or not the customer will accept partial shipments at the line or order level. This functionality is only available with the Advanced Material Management module.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Contains the AllocPri.PriorityCode value of the priority that this customer's orders receive. This functionality is only available with the Advanced Material Management module.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer will be able to access Customer Connect.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and Customer Connect DB.  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Used to define the type of the customer record.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this customer will be included in marketing lists.  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  Determines whether or not the customer's territory can be changed by system processes that could potentially change the territory from its current value.  """  
      self.CustURL:str = obj["CustURL"]
      """  The Customer's website URL.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  Determines whether or not shipments to this customer for different sales orders within the same fiscal period wil be consolidated into one invoice. (See Customer.OneInvPerPS - for the shipments from the same sales order are handled).  """  
      self.Bill_Frequency:str = obj["Bill_Frequency"]
      """  Used in conjunction with the Customer.BillDay field to determine on what days the customer can be invoiced on. See Customer.BillDay description for additional information.  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  Determines whether or not an external delivery note is required for the customer.  This field is available only when ExtCompany.SendShip is set to Yes.  This will provide the default for the ShipHead record.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      """  Determines whether or not the system should check existing orders for this customer to insure that the same PO number is not used twice by the customer.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:  
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based d  """  
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      """  Specifies the current customer can be an alternate bill to customer.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the plant values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Plant values will be used  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      """  This is the Vendor ID to be used when generating a Rebate for the customer  """  
      self.RebateForm:str = obj["RebateForm"]
      """  Indicates if the rebate should be a Check or a Credit Memo  """  
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      """  Indicates if the order should default as a credit card order.  Can be overriden at the order level.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChargeCode:str = obj["ChargeCode"]
      """  Unique Identifier for the Finance Charges  """  
      self.ContactName:str = obj["ContactName"]
      """  The contact's name.  """  
      self.AllocationDescription:str = obj["AllocationDescription"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Label that displays as the suffix behind the amount printed on checks  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """  The label that displays as the suffix behind the amount printed on checks.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  The special character used for this currency. This character displays on reports and programs near the currency amounts.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CustGrupGroupDesc:str = obj["CustGrupGroupDesc"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Service Home Delivery Type Code Description.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      """  The label that displays as the suffix behind the amount printed on checks.  """  
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      """  The symbol of the global currency linked to this currency record.  """  
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.MarkUpDescription:str = obj["MarkUpDescription"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContactListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.ContactName:str = obj["ContactName"]
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustNumList:str = obj["CustNumList"]
      """  A list of customer numbers that were selected for the contact name.  Delimited with ~.  """  
      self.ConNum:int = obj["ConNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContactListTableset:
   def __init__(self, obj):
      self.ContactList:list[Erp_Tablesets_ContactListRow] = obj["ContactList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContactRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The name of the current company.  """  
      self.FirstName:str = obj["FirstName"]
      """  The contact's full first name. This first name will default from the Contact Details sheet, but you can edit it within this field as well.  """  
      self.LastName:str = obj["LastName"]
      """  The contact's full last name. This last name will default from the Contact Details sheet, but you can edit it within this field as well.  """  
      self.ContactName:str = obj["ContactName"]
      """  The contact’s name.  """  
      self.CustNum:int = obj["CustNum"]
      """  The number of a Customer.  """  
      self.CustID:str = obj["CustID"]
      """  The unique identifier for a customer record. On certain reports or windows where space is limited, you may see only the ID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.CustNumList:str = obj["CustNumList"]
      """  Delimited list of Customer CustNum.  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Delimited list of Customer CustNum and Name (for Kinetic)  """  
      self.ShipToList:str = obj["ShipToList"]
      """  Delimited list of shipto CustNum and Name (for Kinetic)  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContactTableset:
   def __init__(self, obj):
      self.Contact:list[Erp_Tablesets_ContactRow] = obj["Contact"]
      self.ContactCustomer:list[Erp_Tablesets_ContactCustomerRow] = obj["ContactCustomer"]
      self.CustCnt:list[Erp_Tablesets_CustCntRow] = obj["CustCnt"]
      self.CustCntAttch:list[Erp_Tablesets_CustCntAttchRow] = obj["CustCntAttch"]
      self.ShipTo:list[Erp_Tablesets_ShipToRow] = obj["ShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
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

class Erp_Tablesets_CustCntRow:
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
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
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
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
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
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the customer contact  is synchronized to an External CRM.  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  This field holds the id of this customer in the External CRM  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  This field holds the id of this customer contact in the External CRM  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      """   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  """  
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      """   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  """  
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      """   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipToRow:
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
      self.ResaleID:str = obj["ResaleID"]
      """  The State Tax Identification Number. Used in Order Entry and prints on Sales Acknowledgements.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The SalesTer.TerritoryID value of the territory the customer is assigned to.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  The CustCnt.ConNum of the default shipping contact for the ShipTo location. The primary shipping contact is used as a default in the shipping process.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Determines whether or not the ShipTo location is normally exempt from sales tax. Used as a default in invoice entry.  If the field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.EDIShipNum:str = obj["EDIShipNum"]
      """  A mutually agreed upon value that links a customer's EDI shipto record (an N1 / ST) to the Manufacturing System DB ShipTo record.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected in the ShipTo.Country field.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  The LangName.LangNameID value of the default Language assigned to the ShipTo location. This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Customer table. This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional custom address format for the ShipTo location.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The email address of the ShipTo location.  """  
      self.TerritorySelect:str = obj["TerritorySelect"]
      """   Determines how the ShipTo location should be assigned to a territory. There are 3 methods for Territory assignment in Ship-to:

Sync - Keep the ShipTo territory synchronized with the territory on the
       main customer record. (ShipTo.TerritoryID = Customer.TerritoryID)
Syst - Let the system (Get Territory) determine the territory to assign         to the ShipTo based on territory boundaries.
Lock - Check this method after assigning the territory manually to 
       prevent the system from attempting to reassign the territory.  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The pending sales territory that the customer will be assigned to based on changes to the territory boundaries.  This functionality is only available with the CRM module.  """  
      self.CreatedByEDI:bool = obj["CreatedByEDI"]
      """  Determines whether or not the ShipTo record was created by an EDI transaction.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier of the ShipTo from an external General Ledger interface such as the EuroFinancial integration.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  The TaxAuthorityCd.TaxAuthorityCode value of the Tax Authority assigned to this ShipTo location.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      """  Days to use in calculating the Order Detail Ship By date from the incoming need by date.  """  
      self.DemandDateType:str = obj["DemandDateType"]
      """   Indicates incoming date type.  Values are:
S - Shipping Date
N - Need By Date  """  
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      """  The number of days from today to give a warning when adding a new order release record from an incoming shipping schedule.  """  
      self.DemandAddAction:str = obj["DemandAddAction"]
      """  Indicates what type of action to take if the add lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      """  The number of days from today to give a warning when changing an order release record from an incoming shipping schedule.  This does not include changes to quantity or dates.  """  
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      """  Indicates what type of action to take if the change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      """  The number of days from today to give a warning when canceling an order release record from an incoming shipping schedule.  """  
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      """  Indicates what type of action to take if the cancel lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      """  The number of days from today to give a warning when adding a new order line record from an incoming shipping schedule.  """  
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      """  Indicates what type of action to take if the new line lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      """  The number of days from today to give a warning when changing the quantity on an order release record from an incoming shipping schedule.  """  
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      """  Indicates what type of action to take if the quantity change lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      """  The number of days from today to give a warning when changing the date on an order release record from an incoming shipping schedule.  """  
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      """  Indicates what type of action to take if the change date lead time is breeched.  Options are B (reject the change) or W (warning - alert that the lead time has been breeched but allow the record to be accepted).  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      """  Periodicity Code.  Must be a valid code in the Periodicity table.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the customer values will be used if overriden else the Site values  """  
      self.DemandUseCustomerValues:bool = obj["DemandUseCustomerValues"]
      """  Indicates if the demand fields from the customer should be used.  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      """  Indicates if the unit price between the demand and the contract should be validated.  If this flag is checked, and the prices are different, when the demand is accepted a record will be written to the DemandLog table.  """  
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      """  Indicates what type of action to take if the unit price between the demand and the contract is different.  Options are B (reject the change) or W (warning - alert that the unit price is different but allow the record to be accepted).  """  
      self.ExcFromVal:bool = obj["ExcFromVal"]
      """  A flag that indicates whether this address should be validated by the tax service.  """  
      self.AddressVal:bool = obj["AddressVal"]
      """  A flag indicating that an address has already been validated. This helps improve the performance of the bulk address validation process by allowing address that have already been validated to be skipped. This flag is set anytime a successful validation is performed, either by the bulk address validation or validation from the Customer form.  """  
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      """  Check for the part in the Part master.  """  
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      """  Indicates what type of action to take if the Check for Part options is selected and the part is not in the part master file.  Options are B (reject the change) or W (warning - alert that the part is not in the part master but allow the record to be accepted).  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Individual Pack IDs  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Third address line  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Non Standard Packaging  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Country portion of the address  """  
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      """  Used to determine if an address changed because of the tax integration.  If true, the tax integration changed the address.  """  
      self.IsAlternate:bool = obj["IsAlternate"]
      """  Indicates if this is a alternate ShipTo. An alternate is a Shipto that is valid for this customer, but is defined/maintained by the "master" customer. See ShipTo.MasterCustNum/MasterShiptoNum.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the CustNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto (IsAlternate). Contains the ShipToNum of the Shipto record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      """  Check for Revision  """  
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      """  Check for Revision Action  """  
      self.DemandCheckPartialShip:bool = obj["DemandCheckPartialShip"]
      """  Flag for checking partial Shipment for Demand Entry.  """  
      self.DemandCheckShipAction:str = obj["DemandCheckShipAction"]
      """  Check Partial Shipments Action: B =Stop  and W = Warning  """  
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      """  Define if at the moment of processing a demand the process should also close those rejected schedules that remain at demand entry  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      """  If this flags is turned on then Demand CTP will automatically be executed as a part of the demand to order process.  """  
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      """  Confirm or not the Capable to Promise jobs from Demand Entry  """  
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      """  If checked, Updates the date in Demand Entry  """  
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      """  This field will define the dates that will be validated as a part of the demand to order process. The valid values for this combo will be:  Need By (N), Ship By (S) and Both (B)  """  
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      """  The value on this field will define the action to be taken when validating CTP. The valid values for this combo box will be: Warning (W) and Stop (S)  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """   This field will define the dates that will be updated as a part of the demand to order process. The valid options will be:
Need By (N), Ship By (S) and Both  (B) NOTE .-In all the cases above the update of date will only be done if the CTP dates are beyond the dates on the file.  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      """  If true then demand will be rejected when one or more demand lines are not configured properly. Applies only to Configurable parts.  """  
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      """  Indicates the action to be taken if configuration values have not been entered for one or more demand lines.  """  
      self.WIWebShipTo:bool = obj["WIWebShipTo"]
      """  WIWebShipTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  Check if the part is a run out part.  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  Indicates what type of action to take if the Check for Run Out Part option is selected and the part is marked as a run out part.  Options are B (reject the change) or W (warning - alert that the part is marked as run out but allow the record to be accepted).  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  INSTRegistration  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MXFederalID:str = obj["MXFederalID"]
      """  MXFederalID  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.PEUBIGEOCode:str = obj["PEUBIGEOCode"]
      """  Geographical Location Code  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.DspFormatStr:str = obj["DspFormatStr"]
      """  Display Format String  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbShipto that is linking to this shipto  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      """  Indicates Integration with financial package (like EuroFin)  """  
      self.IntRunChangeCountry:bool = obj["IntRunChangeCountry"]
      """  Flag used for integrations whether to run the on change country logic.  """  
      self.PeriodicityDesc:str = obj["PeriodicityDesc"]
      self.PeriodicityList:str = obj["PeriodicityList"]
      """  List of available Periodicity values  """  
      self.PrimaryShipTo:bool = obj["PrimaryShipTo"]
      """  Used to indicate if primary shipto.  Updates Customer.ShipToNum field  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.TerritorySelectDescription:str = obj["TerritorySelectDescription"]
      self.TerrSelectFlag:str = obj["TerrSelectFlag"]
      """  Use this field to display/update; replaces TerritorySelect  """  
      self.AddrList:str = obj["AddrList"]
      """  Address in formatted delimited list  """  
      self.LanguageDescription:str = obj["LanguageDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceDescription:str = obj["AGProvinceDescription"]
      self.CountryISOCode:str = obj["CountryISOCode"]
      self.CountryEUMember:bool = obj["CountryEUMember"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.MasterCustIDBTName:str = obj["MasterCustIDBTName"]
      self.MasterCustIDCustID:str = obj["MasterCustIDCustID"]
      self.MasterCustIDName:str = obj["MasterCustIDName"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TATaxAuthorityDescription:str = obj["TATaxAuthorityDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetByID_input:
   """ Required : 
   ContactName
   CustNumList
   inCustNum
   inShipToNum
   inConNum
   """  
   def __init__(self, obj):
      self.ContactName:str = obj["ContactName"]
      """  The Contact Name  """  
      self.CustNumList:str = obj["CustNumList"]
      """  Delimited list of customer numbers selected  """  
      self.inCustNum:int = obj["inCustNum"]
      """  Specific Customer number.  Used for context menu  """  
      self.inShipToNum:str = obj["inShipToNum"]
      """  Specific ShipTo Number.  Used for context menu  """  
      self.inConNum:int = obj["inConNum"]
      """  Specific Contact Number.  Used for context menu  """  
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContactTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   whereClause
   shipToWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where condition  """  
      self.shipToWhereClause:str = obj["shipToWhereClause"]
      """  ShipTo Where condition  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContactListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      """  Where condition  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContactListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustCntAttch_input:
   """ Required : 
   CustNum
   ShipToNum
   ConNum
   """  
   def __init__(self, obj):
      self.CustNum:int = obj["CustNum"]
      """  The Customer Number  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Number  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number  """  
      pass

class GetNewCustCntAttch_output:
   def __init__(self, obj):
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

