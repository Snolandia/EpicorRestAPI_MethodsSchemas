import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ContractRenewalSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ContractRenewalSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContractRenewalSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContractRenewalSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContractRenewalSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches",headers=creds) as resp:
           return await resp.json()

async def post_ContractRenewalSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContractRenewalSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContractRenewalSearch item
   Description: Calls GetByID to retrieve the ContractRenewalSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContractRenewalSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContractRenewalSearch for the service
   Description: Calls UpdateExt to update ContractRenewalSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContractRenewalSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ContractRenewalSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContractRenewalSearches_Company_ContractNum_RenewalNbr(Company, ContractNum, RenewalNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContractRenewalSearch item
   Description: Call UpdateExt to delete ContractRenewalSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContractRenewalSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param RenewalNbr: Desc: RenewalNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/ContractRenewalSearches(" + Company + "," + ContractNum + "," + RenewalNbr + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ContractRenewalSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseContractRenewalSearch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseContractRenewalSearch=" + whereClauseContractRenewalSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(contractNum, renewalNbr, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
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
   params += "contractNum=" + contractNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "renewalNbr=" + renewalNbr

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRenewals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRenewals
   Description: Returns the renewals
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContractRenewalSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContractRenewalSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContractRenewalSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContractRenewalSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractRenewalSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ContractRenewalSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContractRenewalSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ContractRenewalSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ContractRenewalSearchRow] = obj["value"]
      pass

class Erp_Tablesets_ContractRenewalSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
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
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
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
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustBTName:str = obj["CustBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContractRenewalSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.QuotedRenewal:bool = obj["QuotedRenewal"]
      """  Indicates if the renwal will automatically generate a quote.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
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
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date the renewal was created.  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
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
      self.RenewalComment:str = obj["RenewalComment"]
      """  Used to establish invoice comments about the overall Renewal.  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.ContractCode:str = obj["ContractCode"]
      """  It is the same as the contract type but applied to renewals  """  
      self.Modifier:str = obj["Modifier"]
      """  The unit of measure of time that the renewal contract lasts.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract is valid for renewal  """  
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustNum:int = obj["CustNum"]
      self.CustBTName:str = obj["CustBTName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   contractNum
   renewalNbr
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      self.renewalNbr:int = obj["renewalNbr"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ContractRenewalSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
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
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
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
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustBTName:str = obj["CustBTName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContractRenewalSearchListTableset:
   def __init__(self, obj):
      self.ContractRenewalSearchList:list[Erp_Tablesets_ContractRenewalSearchListRow] = obj["ContractRenewalSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ContractRenewalSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.QuotedRenewal:bool = obj["QuotedRenewal"]
      """  Indicates if the renwal will automatically generate a quote.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
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
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Contract.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service Contract entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date the renewal was created.  """  
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
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number of the last recurring invoice.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that Ties the Contract record to a packing slip detail line  """  
      self.RecurringInv:bool = obj["RecurringInv"]
      """  Indicates that Service Contract with this Code will generate recurring invoices.  """  
      self.RecurringFreq:str = obj["RecurringFreq"]
      """  The frequency that recurring invoices are generated only 'monthly' for now.  """  
      self.PricePer:str = obj["PricePer"]
      """  Price modifier for unit price field Daily, monthly, Contract(Full length of the contract)  """  
      self.LastInvGen:bool = obj["LastInvGen"]
      """  This flag is set to TRUE after the last recurring invoice is generated for the contract.  """  
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
      self.RenewalComment:str = obj["RenewalComment"]
      """  Used to establish invoice comments about the overall Renewal.  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InvcTiming:str = obj["InvcTiming"]
      """  InvcTiming  """  
      self.ContractCode:str = obj["ContractCode"]
      """  It is the same as the contract type but applied to renewals  """  
      self.Modifier:str = obj["Modifier"]
      """  The unit of measure of time that the renewal contract lasts.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Indicates how often an invoice is generated for the contract  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract is valid for renewal  """  
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustNum:int = obj["CustNum"]
      self.CustBTName:str = obj["CustBTName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ContractRenewalSearchTableset:
   def __init__(self, obj):
      self.ContractRenewalSearch:list[Erp_Tablesets_ContractRenewalSearchRow] = obj["ContractRenewalSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtContractRenewalSearchTableset:
   def __init__(self, obj):
      self.ContractRenewalSearch:list[Erp_Tablesets_ContractRenewalSearchRow] = obj["ContractRenewalSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   contractNum
   renewalNbr
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      self.renewalNbr:int = obj["renewalNbr"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewContractRenewalSearch_input:
   """ Required : 
   ds
   contractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      pass

class GetNewContractRenewalSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRenewals_input:
   """ Required : 
   customerNum
   WhereClause
   SortByClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.customerNum:int = obj["customerNum"]
      """  customer number to return renewals for  """  
      self.WhereClause:str = obj["WhereClause"]
      """  WhereClause to filter the Parent records.  """  
      self.SortByClause:str = obj["SortByClause"]
      """  To sort by the detail records.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRenewals_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseContractRenewalSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseContractRenewalSearch:str = obj["whereClauseContractRenewalSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtContractRenewalSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtContractRenewalSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ContractRenewalSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

