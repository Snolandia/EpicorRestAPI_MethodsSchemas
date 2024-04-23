import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PayMethodSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PayMethodSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PayMethodSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethodSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches",headers=creds) as resp:
           return await resp.json()

async def post_PayMethodSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethodSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PayMethodSearches_Company_PMUID(Company, PMUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayMethodSearch item
   Description: Calls GetByID to retrieve the PayMethodSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PayMethodSearches_Company_PMUID(Company, PMUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PayMethodSearch for the service
   Description: Calls UpdateExt to update PayMethodSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethodSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PayMethodSearches_Company_PMUID(Company, PMUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PayMethodSearch item
   Description: Call UpdateExt to delete PayMethodSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethodSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePayMethod, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePayMethod=" + whereClausePayMethod
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pmUID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "pmUID=" + pmUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PayMethodListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PayMethodRow] = obj["value"]
      pass

class Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.OnlyBankCurr:bool = obj["OnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.SummarizePerCustomer:bool = obj["SummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.DefPayCode:str = obj["DefPayCode"]
      """  Default Payment Code  """  
      self.AutoBankRec:bool = obj["AutoBankRec"]
      """  Auto Bank Reconciliation  """  
      self.SenderRef:str = obj["SenderRef"]
      """  Sender Reference  """  
      self.RegNum:str = obj["RegNum"]
      """  Registration Number  """  
      self.Test:bool = obj["Test"]
      """  Checkbox to indicate test transmissions  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Reimbursable  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.OverPayPct:int = obj["OverPayPct"]
      """  Contains the overpayment threshold allowed for ar invoices in bank file import.  """  
      self.UnderPayPct:int = obj["UnderPayPct"]
      """  Contains the underpayment threshold allowed for ar invoices in bank file import.  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIGenMethod:int = obj["PIGenMethod"]
      """  Payment Instrument Generation Method  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.GlobalPayMethod:bool = obj["GlobalPayMethod"]
      """  Marks this PayMethod as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.DepositSlips:int = obj["DepositSlips"]
      """  DepositSlips  """  
      self.IsPositiveBalance:bool = obj["IsPositiveBalance"]
      """  IsPositiveBalance  """  
      self.APGrouping:int = obj["APGrouping"]
      """  Specifies how the payments are processed in a bank - individually or in a batch  """  
      self.APIDGeneration:bool = obj["APIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARGrouping:int = obj["ARGrouping"]
      """  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  """  
      self.ARIDGeneration:bool = obj["ARIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARIDTiming:int = obj["ARIDTiming"]
      """  Specify at what moment the application groups AR receipts in batches  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  EFTDebitMemoHandlingCode  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  EFTDebitMemoDueDate  """  
      self.EFTProductNumDate:str = obj["EFTProductNumDate"]
      """  EFTProductNumDate  """  
      self.EFTProductNumber:int = obj["EFTProductNumber"]
      """  EFTProductNumber  """  
      self.SEPO3Payment:bool = obj["SEPO3Payment"]
      """  SEPO3Payment  """  
      self.SECrossBrdPayMethod:str = obj["SECrossBrdPayMethod"]
      """  SECrossBrdPayMethod  """  
      self.SECurrPocket:str = obj["SECurrPocket"]
      """  SECurrPocket  """  
      self.SEErrorHandling:str = obj["SEErrorHandling"]
      """  SEErrorHandling  """  
      self.SEUseIBAN:str = obj["SEUseIBAN"]
      """  SEUseIBAN  """  
      self.SEPath:str = obj["SEPath"]
      """  SEPath  """  
      self.SECreateErrorLog:bool = obj["SECreateErrorLog"]
      """  SECreateErrorLog  """  
      self.SEFileForEachPayCurr:bool = obj["SEFileForEachPayCurr"]
      """  SEFileForEachPayCurr  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  NOTelepayPayment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  NOTelepayReply  """  
      self.DEFeeRule:str = obj["DEFeeRule"]
      """  DEFeeRule  """  
      self.DESerialNum:int = obj["DESerialNum"]
      """  DESerialNum  """  
      self.DEStateNum:str = obj["DEStateNum"]
      """  DEStateNum  """  
      self.DELastUseDate:str = obj["DELastUseDate"]
      """  DELastUseDate  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXPaymentType:int = obj["MXPaymentType"]
      """  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATDesc:str = obj["MXSATDesc"]
      """  MXSATDesc  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      """  PymtProposal  """  
      self.AutoCheckNum:bool = obj["AutoCheckNum"]
      """  AutoCheckNum  """  
      self.EnterPymtTotal:bool = obj["EnterPymtTotal"]
      """  EnterPymtTotal  """  
      self.CheckNumSeq:int = obj["CheckNumSeq"]
      """  CheckNumSeq  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KAmtThreshold:int = obj["US1099KAmtThreshold"]
      """  Form 1099-K Third Party Network Amount Threshold  """  
      self.US1099KTranThreshold:int = obj["US1099KTranThreshold"]
      """  Form 1099-K Third Party Network Transaction Threshold  """  
      self.COPayForm:str = obj["COPayForm"]
      """  COPayForm  """  
      self.COPayMethod:str = obj["COPayMethod"]
      """  COPayMethod  """  
      self.TypeCode:str = obj["TypeCode"]
      """  UNCL4461  """  
      self.EnableThresholds:bool = obj["EnableThresholds"]
      """  Indicates if the threshold fields are enabled  """  
      self.IsCZLocalization:bool = obj["IsCZLocalization"]
      self.PMSourceModule:str = obj["PMSourceModule"]
      """  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  """  
      self.EnableAPInfo:bool = obj["EnableAPInfo"]
      """  EnableAPInfo  """  
      self.COPayMethodDesc:str = obj["COPayMethodDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.EFTHeadType:int = obj["EFTHeadType"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   pmUID
   """  
   def __init__(self, obj):
      self.pmUID:int = obj["pmUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PayMethodListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodListTableset:
   def __init__(self, obj):
      self.PayMethodList:list[Erp_Tablesets_PayMethodListRow] = obj["PayMethodList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.Name:str = obj["Name"]
      """  Name of the payment method  """  
      self.Type:int = obj["Type"]
      """   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Indicates the electronic interface that shall be used for the payment method  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.OnlyBankCurr:bool = obj["OnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.SummarizePerCustomer:bool = obj["SummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.DefPayCode:str = obj["DefPayCode"]
      """  Default Payment Code  """  
      self.AutoBankRec:bool = obj["AutoBankRec"]
      """  Auto Bank Reconciliation  """  
      self.SenderRef:str = obj["SenderRef"]
      """  Sender Reference  """  
      self.RegNum:str = obj["RegNum"]
      """  Registration Number  """  
      self.Test:bool = obj["Test"]
      """  Checkbox to indicate test transmissions  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Reimbursable  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.OverPayPct:int = obj["OverPayPct"]
      """  Contains the overpayment threshold allowed for ar invoices in bank file import.  """  
      self.UnderPayPct:int = obj["UnderPayPct"]
      """  Contains the underpayment threshold allowed for ar invoices in bank file import.  """  
      self.PIType:str = obj["PIType"]
      """  Payment Instrument Type  """  
      self.PIGenMethod:int = obj["PIGenMethod"]
      """  Payment Instrument Generation Method  """  
      self.PIApprove:bool = obj["PIApprove"]
      """  Payment Instrument Approve flag  """  
      self.GlobalPayMethod:bool = obj["GlobalPayMethod"]
      """  Marks this PayMethod as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System Row ID - GUID  """  
      self.DepositSlips:int = obj["DepositSlips"]
      """  DepositSlips  """  
      self.IsPositiveBalance:bool = obj["IsPositiveBalance"]
      """  IsPositiveBalance  """  
      self.APGrouping:int = obj["APGrouping"]
      """  Specifies how the payments are processed in a bank - individually or in a batch  """  
      self.APIDGeneration:bool = obj["APIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARGrouping:int = obj["ARGrouping"]
      """  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  """  
      self.ARIDGeneration:bool = obj["ARIDGeneration"]
      """  When this check box is selected, the application uses identifiers generated via an EI program during processing  """  
      self.ARIDTiming:int = obj["ARIDTiming"]
      """  Specify at what moment the application groups AR receipts in batches  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  EFTDebitMemoHandlingCode  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  EFTDebitMemoDueDate  """  
      self.EFTProductNumDate:str = obj["EFTProductNumDate"]
      """  EFTProductNumDate  """  
      self.EFTProductNumber:int = obj["EFTProductNumber"]
      """  EFTProductNumber  """  
      self.SEPO3Payment:bool = obj["SEPO3Payment"]
      """  SEPO3Payment  """  
      self.SECrossBrdPayMethod:str = obj["SECrossBrdPayMethod"]
      """  SECrossBrdPayMethod  """  
      self.SECurrPocket:str = obj["SECurrPocket"]
      """  SECurrPocket  """  
      self.SEErrorHandling:str = obj["SEErrorHandling"]
      """  SEErrorHandling  """  
      self.SEUseIBAN:str = obj["SEUseIBAN"]
      """  SEUseIBAN  """  
      self.SEPath:str = obj["SEPath"]
      """  SEPath  """  
      self.SECreateErrorLog:bool = obj["SECreateErrorLog"]
      """  SECreateErrorLog  """  
      self.SEFileForEachPayCurr:bool = obj["SEFileForEachPayCurr"]
      """  SEFileForEachPayCurr  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  NOTelepayPayment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  NOTelepayReply  """  
      self.DEFeeRule:str = obj["DEFeeRule"]
      """  DEFeeRule  """  
      self.DESerialNum:int = obj["DESerialNum"]
      """  DESerialNum  """  
      self.DEStateNum:str = obj["DEStateNum"]
      """  DEStateNum  """  
      self.DELastUseDate:str = obj["DELastUseDate"]
      """  DELastUseDate  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXPaymentType:int = obj["MXPaymentType"]
      """  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATDesc:str = obj["MXSATDesc"]
      """  MXSATDesc  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      """  PymtProposal  """  
      self.AutoCheckNum:bool = obj["AutoCheckNum"]
      """  AutoCheckNum  """  
      self.EnterPymtTotal:bool = obj["EnterPymtTotal"]
      """  EnterPymtTotal  """  
      self.CheckNumSeq:int = obj["CheckNumSeq"]
      """  CheckNumSeq  """  
      self.US1099KTranType:str = obj["US1099KTranType"]
      """  Form 1099-K Transaction Type  """  
      self.US1099KAmtThreshold:int = obj["US1099KAmtThreshold"]
      """  Form 1099-K Third Party Network Amount Threshold  """  
      self.US1099KTranThreshold:int = obj["US1099KTranThreshold"]
      """  Form 1099-K Third Party Network Transaction Threshold  """  
      self.COPayForm:str = obj["COPayForm"]
      """  COPayForm  """  
      self.COPayMethod:str = obj["COPayMethod"]
      """  COPayMethod  """  
      self.TypeCode:str = obj["TypeCode"]
      """  UNCL4461  """  
      self.EnableThresholds:bool = obj["EnableThresholds"]
      """  Indicates if the threshold fields are enabled  """  
      self.IsCZLocalization:bool = obj["IsCZLocalization"]
      self.PMSourceModule:str = obj["PMSourceModule"]
      """  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  """  
      self.EnableAPInfo:bool = obj["EnableAPInfo"]
      """  EnableAPInfo  """  
      self.COPayMethodDesc:str = obj["COPayMethodDesc"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.EFTHeadType:int = obj["EFTHeadType"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayMethodSearchTableset:
   def __init__(self, obj):
      self.PayMethod:list[Erp_Tablesets_PayMethodRow] = obj["PayMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPayMethodSearchTableset:
   def __init__(self, obj):
      self.PayMethod:list[Erp_Tablesets_PayMethodRow] = obj["PayMethod"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   pmUID
   """  
   def __init__(self, obj):
      self.pmUID:int = obj["pmUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayMethodSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayMethodSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PayMethodListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPayMethod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodSearchTableset] = obj["ds"]
      pass

class GetNewPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePayMethod
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePayMethod:str = obj["whereClausePayMethod"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayMethodSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPayMethodSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayMethodSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayMethodSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

