import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustBankSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustBankSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustBankSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustBankSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/CustBankSearches",headers=creds) as resp:
           return await resp.json()

async def post_CustBankSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustBankSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustBankRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustBankRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/CustBankSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustBankSearches_Company_CustNum_BankID(Company, CustNum, BankID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustBankSearch item
   Description: Calls GetByID to retrieve the CustBankSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/CustBankSearches(" + Company + "," + CustNum + "," + BankID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustBankSearches_Company_CustNum_BankID(Company, CustNum, BankID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustBankSearch for the service
   Description: Calls UpdateExt to update CustBankSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustBankRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/CustBankSearches(" + Company + "," + CustNum + "," + BankID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustBankSearches_Company_CustNum_BankID(Company, CustNum, BankID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustBankSearch item
   Description: Call UpdateExt to delete CustBankSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustBankSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/CustBankSearches(" + Company + "," + CustNum + "," + BankID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBankListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCustBank, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCustBank=" + whereClauseCustBank
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, bankID, epicorHeaders = None):
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
   params += "custNum=" + custNum
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustBank
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBankSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBankListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustBankListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBankRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustBankRow] = obj["value"]
      pass

class Erp_Tablesets_CustBankListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BankID:str = obj["BankID"]
      """  Customer Bank ID  """  
      self.BankName:str = obj["BankName"]
      """  Customer Bank Name  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  Bank Account Number for the Customer.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      """  Indicates primary bank for Customer.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account  """  
      self.Address1:str = obj["Address1"]
      """  Customer address, line 1  """  
      self.Address2:str = obj["Address2"]
      """  Customer address, line 2  """  
      self.Address3:str = obj["Address3"]
      """  Customer address, line 3  """  
      self.City:str = obj["City"]
      """  Customer city  """  
      self.State:str = obj["State"]
      """  Bank state or province  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Customer postal code (zip code)  """  
      self.Country:int = obj["Country"]
      """  Customer country code.  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Customer Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.LegalName:str = obj["LegalName"]
      """  Customer Legal Name  """  
      self.AgreeRef:str = obj["AgreeRef"]
      """  Agreement Reference  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.AgreeExpDate:str = obj["AgreeExpDate"]
      """  A date field, indicating when the agreement to withdraw money from the customer expires.  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransPersonName:str = obj["TransPersonName"]
      """  TransPersonName  """  
      self.CountryName:str = obj["CountryName"]
      self.BankRegionType:str = obj["BankRegionType"]
      """  Free Form Bank Region Type (Local or Foreign) . Used in localizations.  """  
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      """  Bank Branch Description  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BankID:str = obj["BankID"]
      """  Customer Bank ID  """  
      self.BankName:str = obj["BankName"]
      """  Customer Bank Name  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  Bank Account Number for the Customer.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      """  Indicates primary bank for Customer.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account  """  
      self.Address1:str = obj["Address1"]
      """  Customer address, line 1  """  
      self.Address2:str = obj["Address2"]
      """  Customer address, line 2  """  
      self.Address3:str = obj["Address3"]
      """  Customer address, line 3  """  
      self.City:str = obj["City"]
      """  Customer city  """  
      self.State:str = obj["State"]
      """  Bank state or province  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Customer postal code (zip code)  """  
      self.Country:int = obj["Country"]
      """  Customer country code.  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Customer Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.LegalName:str = obj["LegalName"]
      """  Customer Legal Name  """  
      self.AgreeRef:str = obj["AgreeRef"]
      """  Agreement Reference  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.AgreeExpDate:str = obj["AgreeExpDate"]
      """  A date field, indicating when the agreement to withdraw money from the customer expires.  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransPersonName:str = obj["TransPersonName"]
      """  TransPersonName  """  
      self.TransPersonName2:str = obj["TransPersonName2"]
      """  TransPersonName2  """  
      self.TransPersonName3:str = obj["TransPersonName3"]
      """  TransPersonName3  """  
      self.TransPersonName4:str = obj["TransPersonName4"]
      """  TransPersonName4  """  
      self.TransPersonName5:str = obj["TransPersonName5"]
      """  TransPersonName5  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MX Tax ID  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  Mexico SAT Code  """  
      self.PayID:str = obj["PayID"]
      """  A customer alias used to make and receive payments.  """  
      self.BankRegionType:str = obj["BankRegionType"]
      """  Free Form Bank Region Type (Local or Foreign) . Used in localizations.  """  
      self.CountryName:str = obj["CountryName"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   custNum
   bankID
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.bankID:str = obj["bankID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CustBankListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BankID:str = obj["BankID"]
      """  Customer Bank ID  """  
      self.BankName:str = obj["BankName"]
      """  Customer Bank Name  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  Bank Account Number for the Customer.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      """  Indicates primary bank for Customer.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account  """  
      self.Address1:str = obj["Address1"]
      """  Customer address, line 1  """  
      self.Address2:str = obj["Address2"]
      """  Customer address, line 2  """  
      self.Address3:str = obj["Address3"]
      """  Customer address, line 3  """  
      self.City:str = obj["City"]
      """  Customer city  """  
      self.State:str = obj["State"]
      """  Bank state or province  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Customer postal code (zip code)  """  
      self.Country:int = obj["Country"]
      """  Customer country code.  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Customer Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.LegalName:str = obj["LegalName"]
      """  Customer Legal Name  """  
      self.AgreeRef:str = obj["AgreeRef"]
      """  Agreement Reference  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.AgreeExpDate:str = obj["AgreeExpDate"]
      """  A date field, indicating when the agreement to withdraw money from the customer expires.  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransPersonName:str = obj["TransPersonName"]
      """  TransPersonName  """  
      self.CountryName:str = obj["CountryName"]
      self.BankRegionType:str = obj["BankRegionType"]
      """  Free Form Bank Region Type (Local or Foreign) . Used in localizations.  """  
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      """  Bank Branch Description  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBankListTableset:
   def __init__(self, obj):
      self.CustBankList:list[Erp_Tablesets_CustBankListRow] = obj["CustBankList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BankID:str = obj["BankID"]
      """  Customer Bank ID  """  
      self.BankName:str = obj["BankName"]
      """  Customer Bank Name  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  Bank Account Number for the Customer.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      """  Indicates primary bank for Customer.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account  """  
      self.Address1:str = obj["Address1"]
      """  Customer address, line 1  """  
      self.Address2:str = obj["Address2"]
      """  Customer address, line 2  """  
      self.Address3:str = obj["Address3"]
      """  Customer address, line 3  """  
      self.City:str = obj["City"]
      """  Customer city  """  
      self.State:str = obj["State"]
      """  Bank state or province  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Customer postal code (zip code)  """  
      self.Country:int = obj["Country"]
      """  Customer country code.  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Customer Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.LegalName:str = obj["LegalName"]
      """  Customer Legal Name  """  
      self.AgreeRef:str = obj["AgreeRef"]
      """  Agreement Reference  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.AgreeExpDate:str = obj["AgreeExpDate"]
      """  A date field, indicating when the agreement to withdraw money from the customer expires.  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransPersonName:str = obj["TransPersonName"]
      """  TransPersonName  """  
      self.TransPersonName2:str = obj["TransPersonName2"]
      """  TransPersonName2  """  
      self.TransPersonName3:str = obj["TransPersonName3"]
      """  TransPersonName3  """  
      self.TransPersonName4:str = obj["TransPersonName4"]
      """  TransPersonName4  """  
      self.TransPersonName5:str = obj["TransPersonName5"]
      """  TransPersonName5  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MX Tax ID  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  Mexico SAT Code  """  
      self.PayID:str = obj["PayID"]
      """  A customer alias used to make and receive payments.  """  
      self.BankRegionType:str = obj["BankRegionType"]
      """  Free Form Bank Region Type (Local or Foreign) . Used in localizations.  """  
      self.CountryName:str = obj["CountryName"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBankSearchTableset:
   def __init__(self, obj):
      self.CustBank:list[Erp_Tablesets_CustBankRow] = obj["CustBank"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCustBankSearchTableset:
   def __init__(self, obj):
      self.CustBank:list[Erp_Tablesets_CustBankRow] = obj["CustBank"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   bankID
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.bankID:str = obj["bankID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBankSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBankListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustBank_input:
   """ Required : 
   ds
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustBankSearchTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewCustBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustBankSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCustBank
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCustBank:str = obj["whereClauseCustBank"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBankSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCustBankSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustBankSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustBankSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustBankSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

