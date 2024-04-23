import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BankFundTranSvc
# Description: bo/BankFundTran/BankFundTran.p
           Bank Funds Transfer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeFromAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromAmt
   Description: This method validates the proposed Tranfer Amount and updates the dataset accordingly
   OperationID: ChangeFromAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromBank
   Description: This method validates the proposed from (source) bank and updates the dataset accordingly
   OperationID: ChangeFromBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateGrp
   Description: This method validates the proposed RateGrpCode and updates the dataset accordingly
   OperationID: ChangeRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTargetBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTargetBank
   Description: This method validates the proposed target bank and updates the dataset accordingly
   OperationID: ChangeTargetBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTargetBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTargetBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToAmt
   Description: This method validates the proposed To Tranfer Amount and updates the dataset accordingly
   OperationID: ChangeToAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranDate
   Description: This method validates the proposed Transaction date and updates the dataset according
to the new date/fiscal period
   OperationID: ChangeTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateBankTran(epicorHeaders = None):
   """  
   Summary: Invoke method CreateBankTran
   Description: This method creates the BankFundTran record for the user to edit
   OperationID: CreateBankTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CreateBankTranRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateBankTranRecords
   Description: This method creates 2 BankTran records before posting them
   OperationID: CreateBankTranRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateBankTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateBankTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBeforeTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBeforeTransfer
   Description: This method validates all entered data, that need to do before transfer.
   OperationID: ValidateBeforeTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBeforeTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBeforeTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByTranNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByTranNum
   Description: Returns dataset filled with data found by TranNum
   OperationID: GetByTranNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByTranNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTranNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBankTranRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBankTranRecords
   Description: This method upadtes 2 BankTran records and save them. Works only with unposted records.
   OperationID: UpdateBankTranRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBankTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBankTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PESelectDetractionInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PESelectDetractionInvoices
   Description: This procedure returns invoices with Detractions to be paid
   OperationID: PESelectDetractionInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PESelectDetractionInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PESelectDetractionInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PEUpdateInvcHeadRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PEUpdateInvcHeadRecords
   Description: This procedure updates selected InvcHead
   OperationID: PEUpdateInvcHeadRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEUpdateInvcHeadRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEUpdateInvcHeadRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFromAmt_input:
   """ Required : 
   docTranAmt
   ds
   isFirstBank
   """  
   def __init__(self, obj):
      self.docTranAmt:int = obj["docTranAmt"]
      """  Proposed Transaction Amount  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.isFirstBank:bool = obj["isFirstBank"]
      """  Indicates whether the source bank is the first bank selected  """  
      pass

class ChangeFromAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromBank_input:
   """ Required : 
   bankAcctID
   ds
   isFirstBank
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  Proposed From Bank Accout ID  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.isFirstBank:bool = obj["isFirstBank"]
      """  Indicates whether the source bank is the first bank selected  """  
      pass

class ChangeFromBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateGrp_input:
   """ Required : 
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Proposed RateGrpCode  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

class ChangeRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTargetBank_input:
   """ Required : 
   toBankAcctID
   ds
   isFirstBank
   """  
   def __init__(self, obj):
      self.toBankAcctID:str = obj["toBankAcctID"]
      """  Proposed Target Bank Accout ID  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.isFirstBank:bool = obj["isFirstBank"]
      """  Indicates whether the target bank is the first bank selected  """  
      pass

class ChangeTargetBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToAmt_input:
   """ Required : 
   toDocTranAmt
   ds
   isFirstBank
   """  
   def __init__(self, obj):
      self.toDocTranAmt:int = obj["toDocTranAmt"]
      """  Proposed To Transaction Amount  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.isFirstBank:bool = obj["isFirstBank"]
      """  Indicates whether the target bank is the first bank selected  """  
      pass

class ChangeToAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranDate_input:
   """ Required : 
   tranDate
   ds
   fromSourceBank
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      """  Proposed Transaction Date  """  
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.fromSourceBank:bool = obj["fromSourceBank"]
      """  Shows that transfer creation began from source bank (true, default) or target bank (false)  """  
      pass

class ChangeTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateBankTranRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

class CreateBankTranRecords_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateBankTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFundTranTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_BankFundTranTableset:
   def __init__(self, obj):
      self.BankFundsTransfer:list[Erp_Tablesets_BankFundsTransferRow] = obj["BankFundsTransfer"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankFundsTransferRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Relates record to a BankAcct.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID of the Transaction.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date that the transaction took place.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the Transaction  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person who entered the transaction (System Set).  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that the Transaction was entered into the system (System Set).  """  
      self.EntryTime:str = obj["EntryTime"]
      """  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  """  
      self.TranCleared:bool = obj["TranCleared"]
      """  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearPending:bool = obj["TranClearPending"]
      """  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.TranClearedAmt:int = obj["TranClearedAmt"]
      """  Amount that the Transaction was cleared for.  """  
      self.TranClearedPerson:str = obj["TranClearedPerson"]
      """  Person who cleared the transaction (System Set).  """  
      self.TranClearedDate:str = obj["TranClearedDate"]
      """  Date that the Transaction was cleared in the system (System Set).  """  
      self.TranClearedTime:str = obj["TranClearedTime"]
      """  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Number of related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Document amount of the Transaction  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that is used for this bank transaction.  """  
      self.DocTranClearedAmt:int = obj["DocTranClearedAmt"]
      """  Document amount that the Transaction was cleared for.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix that entry applies to.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.Voided:bool = obj["Voided"]
      """  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for the record.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document for the record.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.CNToCFICode:str = obj["CNToCFICode"]
      """  CNToCFICode  """  
      self.Plant:str = obj["Plant"]
      """  Multi-Site related Site  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      self.ToBankAcctID:str = obj["ToBankAcctID"]
      """  Transfer To BankAccount ID  """  
      self.ToBankDesc:str = obj["ToBankDesc"]
      """  Transfer To Bank Account Description  """  
      self.FromBalance:int = obj["FromBalance"]
      self.FromNewBalance:int = obj["FromNewBalance"]
      self.ToBalance:int = obj["ToBalance"]
      self.ToNewBalance:int = obj["ToNewBalance"]
      self.FromCurrSymbol:str = obj["FromCurrSymbol"]
      self.ToCurrSymbol:str = obj["ToCurrSymbol"]
      self.ToExchangeRate:int = obj["ToExchangeRate"]
      self.ToTranAmt:int = obj["ToTranAmt"]
      self.ToDocTranAmt:int = obj["ToDocTranAmt"]
      self.ToCurrencyCode:str = obj["ToCurrencyCode"]
      self.Rpt1ToTranAmt:int = obj["Rpt1ToTranAmt"]
      self.Rpt2ToTranAmt:int = obj["Rpt2ToTranAmt"]
      self.Rpt3ToTranAmt:int = obj["Rpt3ToTranAmt"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CNToCFICodeDescription:str = obj["CNToCFICodeDescription"]
      self.PECandidatesAmt:int = obj["PECandidatesAmt"]
      """  Peru CSF - Detractions candidates amount  """  
      self.PERemainingAmt:int = obj["PERemainingAmt"]
      """  Peru CSF - Detractions remaining amount  """  
      self.PESelectedAmt:int = obj["PESelectedAmt"]
      """  Peru CSF - Detractions selected amount  """  
      self.PEExchangeRate:int = obj["PEExchangeRate"]
      """  Peru CSF - Detraction Exchange Rate  """  
      self.ToPlant:str = obj["ToPlant"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctToPEDetNationalBank:bool = obj["BankAcctToPEDetNationalBank"]
      self.BankAcctToDescription:str = obj["BankAcctToDescription"]
      self.BankAcctToCurrencyCode:str = obj["BankAcctToCurrencyCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PEARInvSelRow:
   def __init__(self, obj):
      self.Selected:bool = obj["Selected"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.DetractionTaxAmt:int = obj["DetractionTaxAmt"]
      self.LastCashReceiptDate:str = obj["LastCashReceiptDate"]
      self.ProductCode:str = obj["ProductCode"]
      self.CustID:str = obj["CustID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocDetractionTaxAmt:int = obj["DocDetractionTaxAmt"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.CustBalance:int = obj["CustBalance"]
      self.CustAmount:int = obj["CustAmount"]
      self.Balance:int = obj["Balance"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.PECollectionsDate:str = obj["PECollectionsDate"]
      self.InvInCollections:bool = obj["InvInCollections"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PEARInvSelTableset:
   def __init__(self, obj):
      self.PEARInvSel:list[Erp_Tablesets_PEARInvSelRow] = obj["PEARInvSel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByTranNum_input:
   """ Required : 
   TranNum
   """  
   def __init__(self, obj):
      self.TranNum:int = obj["TranNum"]
      """  TarnNum  """  
      pass

class GetByTranNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFundTranTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
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

class PESelectDetractionInvoices_input:
   """ Required : 
   dsBankFundTran
   dsPEARInvSel
   """  
   def __init__(self, obj):
      self.dsBankFundTran:list[Erp_Tablesets_BankFundTranTableset] = obj["dsBankFundTran"]
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelTableset] = obj["dsPEARInvSel"]
      pass

class PESelectDetractionInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsBankFundTran:list[Erp_Tablesets_BankFundTranTableset] = obj["dsBankFundTran"]
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelTableset] = obj["dsPEARInvSel"]
      pass

      """  output parameters  """  

class PEUpdateInvcHeadRecords_input:
   """ Required : 
   dsBankFundTran
   dsPEARInvSel
   """  
   def __init__(self, obj):
      self.dsBankFundTran:list[Erp_Tablesets_BankFundTranTableset] = obj["dsBankFundTran"]
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelTableset] = obj["dsPEARInvSel"]
      pass

class PEUpdateInvcHeadRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsBankFundTran:list[Erp_Tablesets_BankFundTranTableset] = obj["dsBankFundTran"]
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelTableset] = obj["dsPEARInvSel"]
      pass

      """  output parameters  """  

class UpdateBankTranRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

class UpdateBankTranRecords_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBeforeTransfer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

class ValidateBeforeTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFundTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

