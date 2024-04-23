import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendBankSearchSvc
# Description: Search of Vendor Bank
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VendBankSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendBankSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBankSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches",headers=creds) as resp:
           return await resp.json()

async def post_VendBankSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBankSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendBankRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendBankSearches_Company_VendorNum_BankID(Company, VendorNum, BankID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendBankSearch item
   Description: Calls GetByID to retrieve the VendBankSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendBankSearches_Company_VendorNum_BankID(Company, VendorNum, BankID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendBankSearch for the service
   Description: Calls UpdateExt to update VendBankSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendBankSearches_Company_VendorNum_BankID(Company, VendorNum, BankID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendBankSearch item
   Description: Call UpdateExt to delete VendBankSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/VendBankSearches(" + Company + "," + VendorNum + "," + BankID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendBank, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseVendBank=" + whereClauseVendBank
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, bankID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "bankID=" + bankID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendBank
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendBankSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendBankListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendBankRow] = obj["value"]
      pass

class Erp_Tablesets_VendBankListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      """  Bank Branch Description  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.DFIIdentification:str = obj["DFIIdentification"]
      """  DFIIdentification  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.FeeOwnership:str = obj["FeeOwnership"]
      """  FeeOwnership  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.BankCustNumberStartPos:int = obj["BankCustNumberStartPos"]
      """  BankCustNumberStartPos  """  
      self.BankCustNumberLen:int = obj["BankCustNumberLen"]
      """  BankCustNumberLen  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BankType:str = obj["BankType"]
      """  Bank type of electronic payment transactions  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.NOChequeCode:str = obj["NOChequeCode"]
      """  Norway CSF: Determines where bank cheque is sent.  """  
      self.NOFeeCostCode:str = obj["NOFeeCostCode"]
      """  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  """  
      self.ReceiverName:str = obj["ReceiverName"]
      """  Receiver Name.  Used in Japan localizations.  """  
      self.ReceivingBankName:str = obj["ReceivingBankName"]
      """  Receiving Bank Name.  Used in Japan localizations.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchName:str = obj["ReceivingBranchName"]
      """  Receiving Branch Name.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.SEBankFeeCostOwner:str = obj["SEBankFeeCostOwner"]
      """  SEBankFeeCostOwner  """  
      self.PEDetractionsNBA:bool = obj["PEDetractionsNBA"]
      """  PEDetractionsNBA  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MX SAT Code  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MX SAT Name Short  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MX SAT Name Full  """  
      self.DKCreditorNum:str = obj["DKCreditorNum"]
      """  DKCreditorNum  """  
      self.PayID:str = obj["PayID"]
      """  A supplier alias used to make and receive payments.  """  
      self.ClearSystemIDCode:str = obj["ClearSystemIDCode"]
      """  ClearSystemIDCode  """  
      self.MemberID:str = obj["MemberID"]
      """  MemberID  """  
      self.BCountry:int = obj["BCountry"]
      self.CHScrPOBankAcctNum:str = obj["CHScrPOBankAcctNum"]
      """  Postal Account Number in format XX-#####V-P (CSF Switzerland)  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BCountryNumDescription:str = obj["BCountryNumDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   bankID
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.bankID:str = obj["bankID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtVendBankSearchTableset:
   def __init__(self, obj):
      self.VendBank:list[Erp_Tablesets_VendBankRow] = obj["VendBank"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendBankListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      """  Bank Branch Description  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendBankListTableset:
   def __init__(self, obj):
      self.VendBankList:list[Erp_Tablesets_VendBankListRow] = obj["VendBankList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.DFIIdentification:str = obj["DFIIdentification"]
      """  DFIIdentification  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.FeeOwnership:str = obj["FeeOwnership"]
      """  FeeOwnership  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.BankCustNumberStartPos:int = obj["BankCustNumberStartPos"]
      """  BankCustNumberStartPos  """  
      self.BankCustNumberLen:int = obj["BankCustNumberLen"]
      """  BankCustNumberLen  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BankType:str = obj["BankType"]
      """  Bank type of electronic payment transactions  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.NOChequeCode:str = obj["NOChequeCode"]
      """  Norway CSF: Determines where bank cheque is sent.  """  
      self.NOFeeCostCode:str = obj["NOFeeCostCode"]
      """  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  """  
      self.ReceiverName:str = obj["ReceiverName"]
      """  Receiver Name.  Used in Japan localizations.  """  
      self.ReceivingBankName:str = obj["ReceivingBankName"]
      """  Receiving Bank Name.  Used in Japan localizations.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchName:str = obj["ReceivingBranchName"]
      """  Receiving Branch Name.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.SEBankFeeCostOwner:str = obj["SEBankFeeCostOwner"]
      """  SEBankFeeCostOwner  """  
      self.PEDetractionsNBA:bool = obj["PEDetractionsNBA"]
      """  PEDetractionsNBA  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MX SAT Code  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MX SAT Name Short  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MX SAT Name Full  """  
      self.DKCreditorNum:str = obj["DKCreditorNum"]
      """  DKCreditorNum  """  
      self.PayID:str = obj["PayID"]
      """  A supplier alias used to make and receive payments.  """  
      self.ClearSystemIDCode:str = obj["ClearSystemIDCode"]
      """  ClearSystemIDCode  """  
      self.MemberID:str = obj["MemberID"]
      """  MemberID  """  
      self.BCountry:int = obj["BCountry"]
      self.CHScrPOBankAcctNum:str = obj["CHScrPOBankAcctNum"]
      """  Postal Account Number in format XX-#####V-P (CSF Switzerland)  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BCountryNumDescription:str = obj["BCountryNumDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendBankSearchTableset:
   def __init__(self, obj):
      self.VendBank:list[Erp_Tablesets_VendBankRow] = obj["VendBank"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   bankID
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.bankID:str = obj["bankID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendBankListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewVendBank_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendBankSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendBankSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendBank
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendBank:str = obj["whereClauseVendBank"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendBankSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtVendBankSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendBankSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendBankSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendBankSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

