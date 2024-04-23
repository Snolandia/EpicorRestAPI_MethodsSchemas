import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARRecTrackerSvc
# Description: AR Rec Tracker
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSelectionDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectionDefaults
   Description: Get selection criteria defaults
   OperationID: GetSelectionDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectionDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSubLedgerMovements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSubLedgerMovements
   Description: This method gets all the movements records for the range of dates
   OperationID: GetSubLedgerMovements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSubLedgerMovements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubLedgerMovements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLMovements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLMovements
   Description: This method gets all jounal records for the range of dates
   OperationID: GetGLMovements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLMovements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLMovements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRecTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRecTotals
   Description: This method gets the totals for a group of glaccounts
   OperationID: GetRecTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRecTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRecTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllRecs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllRecs
   Description: This method gets all records
   OperationID: GetAllRecs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllRecs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDiffs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDiffs
   Description: This method gets just the differences
   OperationID: GetDiffs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDiffs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiffs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookID
   Description: This method is called when the BookID is changed.
   OperationID: OnChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ARMovementRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.TranType:str = obj["TranType"]
      """  Transaction type for the movement record created (Invoice, Cash, Adjustment, etc.)  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Internal cash receipt Number for the related cash receipt record that generated the movement  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Invoice number that is impacted by the movement record  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Reference invoice or credit memo number that generated the movement record against the corresponding invoice  """  
      self.TranRef:str = obj["TranRef"]
      """  Transaction reference for the movement record (Invoice number, Check number, etc.)  """  
      self.MovementNum:int = obj["MovementNum"]
      """  Unique integer for the movement transaction  """  
      self.TranDate:str = obj["TranDate"]
      """  Apply date of the movement's corresponding transaction  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number associated with the transaction.  This must be valid in the Customer table.  """  
      self.LegalNum:str = obj["LegalNum"]
      """  Legal number of the invoice/document that is impacted by the movement record  """  
      self.TranLegalNumber:str = obj["TranLegalNumber"]
      """  Legal number of the document that generated the movement record  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the document that generated the movement record  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of the movement in base currency  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Amount of the movement in document currency  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Amount of the movement in first reporting currency if defined  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Amount of the movement in second reporting currency if defined  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Amount of the movement in third reporting currency if defined  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales order number against which the movement is generated  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line against which the movement is generated  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Sales order release against which the movement is generated  """  
      self.Subledger:str = obj["Subledger"]
      """  Subledger of the movement record to differentiate between receivables, deposits, advance bill, etc.  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized gain/loss  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates the movement record is posted  """  
      self.BalUpdated:bool = obj["BalUpdated"]
      """  Indicates the movement record has updated the ARBalance table.  If real time balance updates are not enabled, this field will remain false until the balance update process is run.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  System date and time of the generated movements  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustName:str = obj["CustName"]
      self.CustID:str = obj["CustID"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARRecAllRecsRow:
   def __init__(self, obj):
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      self.CreditAmount:int = obj["CreditAmount"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustNum:int = obj["CustNum"]
      self.DebitAmount:int = obj["DebitAmount"]
      self.DifferenceAmt:int = obj["DifferenceAmt"]
      self.DocTranAmt:int = obj["DocTranAmt"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalLine:int = obj["JournalLine"]
      self.JournalNum:int = obj["JournalNum"]
      self.LegalNum:str = obj["LegalNum"]
      self.TranAmt:int = obj["TranAmt"]
      self.TranDate:str = obj["TranDate"]
      self.TranLegalNum:str = obj["TranLegalNum"]
      self.TranRef:str = obj["TranRef"]
      self.TranType:str = obj["TranType"]
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      self.MovementNum:int = obj["MovementNum"]
      self.GLDate:str = obj["GLDate"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BookTranAmt:int = obj["BookTranAmt"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARRecDiffsRow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CustNum:int = obj["CustNum"]
      self.DifferenceAmt:int = obj["DifferenceAmt"]
      self.DifferenceReason:str = obj["DifferenceReason"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.GLAmount:int = obj["GLAmount"]
      self.GLDate:str = obj["GLDate"]
      self.GLMovementNum:int = obj["GLMovementNum"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalLine:int = obj["JournalLine"]
      self.JournalNum:int = obj["JournalNum"]
      self.LegalNum:str = obj["LegalNum"]
      self.MovementNum:int = obj["MovementNum"]
      self.TranDate:str = obj["TranDate"]
      self.TranAmt:int = obj["TranAmt"]
      self.TranLegalNum:str = obj["TranLegalNum"]
      self.TranRef:str = obj["TranRef"]
      self.TranType:str = obj["TranType"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.DocTranAmt:int = obj["DocTranAmt"]
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BookTranAmt:int = obj["BookTranAmt"]
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Rpt1WithholdAmt  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Rpt2WithholdAmt  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Rpt3WithholdAmt  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  WithholdAmt  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARRecTotalsRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.GLAccount:str = obj["GLAccount"]
      self.GLClosingBal:int = obj["GLClosingBal"]
      self.GLMovements:int = obj["GLMovements"]
      self.GLOpenBal:int = obj["GLOpenBal"]
      self.SubGLClosingBal:int = obj["SubGLClosingBal"]
      self.SubGLMovements:int = obj["SubGLMovements"]
      self.SubGLOpenBal:int = obj["SubGLOpenBal"]
      self.VarClosingBal:int = obj["VarClosingBal"]
      self.VarMovements:int = obj["VarMovements"]
      self.VarOpenBal:int = obj["VarOpenBal"]
      self.DocSubGLOpenBal:int = obj["DocSubGLOpenBal"]
      self.Rpt1SubGLOpenBal:int = obj["Rpt1SubGLOpenBal"]
      self.Rpt2SubGLOpenBal:int = obj["Rpt2SubGLOpenBal"]
      self.Rpt3SubGLOpenBal:int = obj["Rpt3SubGLOpenBal"]
      self.DocSubGLMovements:int = obj["DocSubGLMovements"]
      self.Rpt1SubGLMovements:int = obj["Rpt1SubGLMovements"]
      self.Rpt2SubGLMovements:int = obj["Rpt2SubGLMovements"]
      self.Rpt3SubGLMovements:int = obj["Rpt3SubGLMovements"]
      self.Rpt2SubGLClosingBal:int = obj["Rpt2SubGLClosingBal"]
      self.DocSubGLClosingBal:int = obj["DocSubGLClosingBal"]
      self.Rpt1SubGLClosingBal:int = obj["Rpt1SubGLClosingBal"]
      self.Rpt3SubGLClosingBal:int = obj["Rpt3SubGLClosingBal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARRecTrackerRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.COACode:str = obj["COACode"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalPeriodEnd:int = obj["FiscalPeriodEnd"]
      self.FiscalPeriodStart:int = obj["FiscalPeriodStart"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.GLAccount:str = obj["GLAccount"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.SegValue1:str = obj["SegValue1"]
      self.SegValue10:str = obj["SegValue10"]
      self.SegValue11:str = obj["SegValue11"]
      self.SegValue12:str = obj["SegValue12"]
      self.SegValue13:str = obj["SegValue13"]
      self.SegValue14:str = obj["SegValue14"]
      self.SegValue15:str = obj["SegValue15"]
      self.SegValue16:str = obj["SegValue16"]
      self.SegValue17:str = obj["SegValue17"]
      self.SegValue18:str = obj["SegValue18"]
      self.SegValue19:str = obj["SegValue19"]
      self.SegValue2:str = obj["SegValue2"]
      self.SegValue20:str = obj["SegValue20"]
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      self.SegValue5:str = obj["SegValue5"]
      self.SegValue6:str = obj["SegValue6"]
      self.SegValue7:str = obj["SegValue7"]
      self.SegValue8:str = obj["SegValue8"]
      self.SegValue9:str = obj["SegValue9"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARRecTrackerTableset:
   def __init__(self, obj):
      self.ARRecTracker:list[Erp_Tablesets_ARRecTrackerRow] = obj["ARRecTracker"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARRecTrackerTotTableset:
   def __init__(self, obj):
      self.ARMovement:list[Erp_Tablesets_ARMovementRow] = obj["ARMovement"]
      self.ARRecAllRecs:list[Erp_Tablesets_ARRecAllRecsRow] = obj["ARRecAllRecs"]
      self.ARRecDiffs:list[Erp_Tablesets_ARRecDiffsRow] = obj["ARRecDiffs"]
      self.ARRecTotals:list[Erp_Tablesets_ARRecTotalsRow] = obj["ARRecTotals"]
      self.GLJrnDtl:list[Erp_Tablesets_GLJrnDtlRow] = obj["GLJrnDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COOneTimeDesc:str = obj["COOneTimeDesc"]
      """   Colombia Loc field            
This field is used as external calculated only.  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """   Colombia Loc field.           
This field is used as external calculated only.  """  
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      """  DEA Code  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEA End Date  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEA Start Date  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  Deferred Expense  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.HeaderCommentText:str = obj["HeaderCommentText"]
      """  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  """  
      self.LineReference:str = obj["LineReference"]
      """  Manual GL Journal Line Reference.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  Manual GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  Manual GL Journal Line Reference Holder Name.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  Manual GL Journal Line Reference Type.  """  
      self.MovementNum:int = obj["MovementNum"]
      self.OrigApplyDate:str = obj["OrigApplyDate"]
      """  Apply Date of the Original Transaction  """  
      self.OrigJrnlLine:int = obj["OrigJrnlLine"]
      """  Journal line of the original transaction that was reversed.  """  
      self.OrigJrnlNbr:int = obj["OrigJrnlNbr"]
      """  Journal number of the original transaction that was reversed.  """  
      self.OrigJrnlYear:int = obj["OrigJrnlYear"]
      """  Fiscal year of the original transaction that was reversed.  """  
      self.OrigJrnlYearSuffix:str = obj["OrigJrnlYearSuffix"]
      """  Fiscal year suffix of the original transaction that was reversed.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevApplyDate:str = obj["RevApplyDate"]
      """  Apply date of the reversing transaction  """  
      self.RevJrnlLine:int = obj["RevJrnlLine"]
      """  Journal line of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlNbr:int = obj["RevJrnlNbr"]
      """  Journal number of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYear:int = obj["RevJrnlYear"]
      """  Fiscal year of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYearSuffix:str = obj["RevJrnlYearSuffix"]
      """  Fiscal year suffix of the latest journal entry made to reverse a transaction.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BookCurrencySymbol:str = obj["BookCurrencySymbol"]
      self.EntityDescription:str = obj["EntityDescription"]
      """  Description of the entity the journal detail is for  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAccount:str = obj["GLAccountGLAccount"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.SrcGLAccountGLShortAcct:str = obj["SrcGLAccountGLShortAcct"]
      self.SrcGLAccountAccountDesc:str = obj["SrcGLAccountAccountDesc"]
      self.SrcGLAccountGLAcctDisp:str = obj["SrcGLAccountGLAcctDisp"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllRecs_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipStartPeriod
   ipEndPeriod
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Calendar  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Period Start  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  Period End  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

class GetAllRecs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDiffs_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipStartPeriod
   ipEndPeriod
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Calendar  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Period Start  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  Period End  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

class GetDiffs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetGLMovements_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipStartPeriod
   ipEndPeriod
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal Calendar  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Period Start  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  Period End  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

class GetGLMovements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRecTotals_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipStartPeriod
   ipEndPeriod
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal Calendar  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Period Start  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  Period End  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

class GetRecTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectionDefaults_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARRecTrackerTableset] = obj["returnObj"]
      pass

class GetSubLedgerMovements_input:
   """ Required : 
   ipBookID
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ipStartPeriod
   ipEndPeriod
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  Fiscal Calendar  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.ipStartPeriod:int = obj["ipStartPeriod"]
      """  Period Start  """  
      self.ipEndPeriod:int = obj["ipEndPeriod"]
      """  Period End  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
      pass

class GetSubLedgerMovements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTotTableset] = obj["ds"]
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

class OnChangeBookID_input:
   """ Required : 
   cInBookID
   ds
   """  
   def __init__(self, obj):
      self.cInBookID:str = obj["cInBookID"]
      """  Proposed BookID  """  
      self.ds:list[Erp_Tablesets_ARRecTrackerTableset] = obj["ds"]
      pass

class OnChangeBookID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARRecTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARRecTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

