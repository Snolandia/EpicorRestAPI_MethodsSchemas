import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AutoTranReversalSvc
# Description: SrcGLTran
           Give the user the ability to select a group of GLJrnDtl lines, with one Journal Number.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckReverseDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReverseDate
   Description: Check if New Reversing Apply Date is valid or not.
   OperationID: CheckReverseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReverseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReverseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReverseDateRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReverseDateRowMod
   Description: Check if New Reversing Apply Date is valid or not. Returns updated row with RowMod = 'U'
   OperationID: CheckReverseDateRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReverseDateRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReverseDateRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClosePeriodChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClosePeriodChanged
   Description: Fiscal period should be recalculated if closing period changed
   OperationID: ClosePeriodChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePeriodChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePeriodChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClosePeriodChangedRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClosePeriodChangedRowMod
   Description: Fiscal period should be recalculated if closing period changed. Returns updated row with RowMod = 'U'
   OperationID: ClosePeriodChangedRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClosePeriodChangedRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClosePeriodChangedRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLinkingMemos(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLinkingMemos
   Description: Delete linking memos is posting was not run.
   OperationID: DeleteLinkingMemos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLinkingMemos_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLinkingMemos_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLTranList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLTranList
   Description: Get a list of GL journal Lines.
   OperationID: GetGLTranList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLTranList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLTranList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCurrentCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCurrentCompany
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetListCurrentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCurrentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCurrentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAmtToReverse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAmtToReverse
   Description: Purpose:  validate amount to reverse and update totals
Parameters:
<param name="ipAmtToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtToReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtToReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtToReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAmtToReverseRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAmtToReverseRowMod
   Description: Purpose:  validate amount to reverse and update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipAmtToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtToReverseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtToReverseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtToReverseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAmtStatToReverse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAmtStatToReverse
   Description: Purpose:  validate amount to reverse and update totals
Parameters:
<param name="ipAmtStatToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtStatToReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtStatToReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtStatToReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAmtStatToReverseRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAmtStatToReverseRowMod
   Description: Purpose:  validate amount to reverse and update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipAmtStatToReverse">amount to reverse</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeAmtStatToReverseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAmtStatToReverseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAmtStatToReverseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelected
   Description: Purpose:  Update totals
Parameters:
<param name="ipSelected">boolean indicating if the line is selected or deselected</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelectedRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelectedRowMod
   Description: Purpose:  Update totals. Returns updated row with RowMod = 'U'
Parameters:
<param name="ipSelected">boolean indicating if the line is selected or deselected</param><param name="ds">Epicor.Mfg.BO.AutoTranReversalDataSet</param>
Notes:
   OperationID: OnChangeSelectedRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectedRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectedRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Post(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Post
   Description: Post
   OperationID: Post
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Post_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Post_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoTranReversalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlListRow] = obj["value"]
      pass

class Erp_Tablesets_GLJrnDtlListRow:
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
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckReverseDateRowMod_input:
   """ Required : 
   reverseDate
   bookID
   ds
   """  
   def __init__(self, obj):
      self.reverseDate:str = obj["reverseDate"]
      """  Reversing Apply Date  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class CheckReverseDateRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckReverseDate_input:
   """ Required : 
   reverseDate
   bookID
   ds
   """  
   def __init__(self, obj):
      self.reverseDate:str = obj["reverseDate"]
      """  Reversing Apply Date  """  
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class CheckReverseDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ClosePeriodChangedRowMod_input:
   """ Required : 
   closePeriod
   ds
   """  
   def __init__(self, obj):
      self.closePeriod:int = obj["closePeriod"]
      """  Close Fiscal Period  """  
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class ClosePeriodChangedRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ClosePeriodChanged_input:
   """ Required : 
   closePeriod
   ds
   """  
   def __init__(self, obj):
      self.closePeriod:int = obj["closePeriod"]
      """  Close Fiscal Period  """  
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class ClosePeriodChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteLinkingMemos_input:
   """ Required : 
   iABTUID
   ds
   """  
   def __init__(self, obj):
      self.iABTUID:str = obj["iABTUID"]
      """  ABTUID of GLTransaction.  """  
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class DeleteLinkingMemos_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AutoTranReversalListTableset:
   def __init__(self, obj):
      self.GLJrnDtlList:list[Erp_Tablesets_GLJrnDtlListRow] = obj["GLJrnDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AutoTranReversalTableset:
   def __init__(self, obj):
      self.GLJournalLine:list[Erp_Tablesets_GLJournalLineRow] = obj["GLJournalLine"]
      self.GLJrnDtlMnlDEASch:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["GLJrnDtlMnlDEASch"]
      self.GLJrnLineReference:list[Erp_Tablesets_GLJrnLineReferenceRow] = obj["GLJrnLineReference"]
      self.SrcGLTran:list[Erp_Tablesets_SrcGLTranRow] = obj["SrcGLTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJournalLineRow:
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
      self.AmtStatAvailToReverse:int = obj["AmtStatAvailToReverse"]
      """  Difference between statistical amount and the statistical amount previously reversed.  """  
      self.AmtStatToReverse:int = obj["AmtStatToReverse"]
      """  Statistical Amount to Reverse  """  
      self.AmtToReverse:int = obj["AmtToReverse"]
      """  Book Amount to reverse.  """  
      self.AmtToReverseTrans:int = obj["AmtToReverseTrans"]
      """  Transaction amount to reverse.  Prorated based upon the total book amount of the transaction and the amount currently being reversed.  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      """  Book Currency Code  """  
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
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.IsDEAJournalLine:bool = obj["IsDEAJournalLine"]
      """  JournalLine is recognized Deferred Expense Amortization  """  
      self.IsDebitAmount:bool = obj["IsDebitAmount"]
      self.MemoJournalLine:int = obj["MemoJournalLine"]
      self.PartiallyReversed:bool = obj["PartiallyReversed"]
      """  Logical that indicates if the current GLJrnDtl has been partially reversed.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.ReversedAmt:int = obj["ReversedAmt"]
      """  Amount previously reversed.  """  
      self.ReversedAmtTrans:int = obj["ReversedAmtTrans"]
      """  Total transaction amount reversed.  """  
      self.ReversedStatAmt:int = obj["ReversedStatAmt"]
      self.Selected:bool = obj["Selected"]
      """  Logical indicating the journal line is selected for reversal.  """  
      self.StatAmt:int = obj["StatAmt"]
      self.StornoLineDescr:str = obj["StornoLineDescr"]
      self.TransAmt:int = obj["TransAmt"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.AmtAvailToReverse:int = obj["AmtAvailToReverse"]
      """  Difference between book amount and the amount previously reversed.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLAcctDispGLAcctDisp:str = obj["GLAcctDispGLAcctDisp"]
      self.GLAcctDispAccountDesc:str = obj["GLAcctDispAccountDesc"]
      self.GLAcctDispGLShortAcct:str = obj["GLAcctDispGLShortAcct"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlListRow:
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
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  AmortSeq  """  
      self.SchFiscalCalendarID:str = obj["SchFiscalCalendarID"]
      """  SchFiscalCalendarID  """  
      self.SchFiscalYear:int = obj["SchFiscalYear"]
      """  SchFiscalYear  """  
      self.SchFiscalYearSuffix:str = obj["SchFiscalYearSuffix"]
      """  SchFiscalYearSuffix  """  
      self.SchFiscalPeriod:int = obj["SchFiscalPeriod"]
      """  SchFiscalPeriod  """  
      self.AmortDate:str = obj["AmortDate"]
      """  AmortDate  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  AmortPercent  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  AmortAmt  """  
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      """  DocAmortAmt  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  PostedDate  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  Rpt1AmortAmt  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Document currency  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  Rpt2AmortAmt  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  Rpt3AmortAmt  """  
      self.GLBookID:str = obj["GLBookID"]
      """  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  """  
      self.GLJournalNum:int = obj["GLJournalNum"]
      """  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  """  
      self.DispAmortAmt:int = obj["DispAmortAmt"]
      """  DispAmortAmt  """  
      self.DispDocAmortAmt:int = obj["DispDocAmortAmt"]
      """  DispDocAmortAmt  """  
      self.HasReverseLines:bool = obj["HasReverseLines"]
      """  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  Account Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnLineReferenceRow:
   def __init__(self, obj):
      self.GLJrnLineID:str = obj["GLJrnLineID"]
      """  Identifier refers to GLJrnLine  """  
      self.RefType:str = obj["RefType"]
      """  Name of reference  """  
      self.RefValue:str = obj["RefValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SrcGLTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ABTUID:str = obj["ABTUID"]
      self.BookID:str = obj["BookID"]
      self.BookDescription:str = obj["BookDescription"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalCode:str = obj["JournalCode"]
      self.GroupID:str = obj["GroupID"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.PostedDate:str = obj["PostedDate"]
      self.Description:str = obj["Description"]
      self.Reverse:bool = obj["Reverse"]
      self.RedStorno:bool = obj["RedStorno"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      self.BookBalance:int = obj["BookBalance"]
      self.CreditAmount:int = obj["CreditAmount"]
      self.DebitAmount:int = obj["DebitAmount"]
      self.Balance:int = obj["Balance"]
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.TranState:str = obj["TranState"]
      self.MemoABTUID:str = obj["MemoABTUID"]
      """  This value is used for search Memos for reverse lines  """  
      self.MemoGLTranDesc:str = obj["MemoGLTranDesc"]
      """  This value is used for search memos reverse GL Journal lines.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      self.ReverseDate:str = obj["ReverseDate"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      """  Used by the UI for enabling/disabling the Red Storno prompt  """  
      self.TotBookSelDB:int = obj["TotBookSelDB"]
      """  Total Book Selected Debit Amount  """  
      self.TotBookSelCR:int = obj["TotBookSelCR"]
      """  Total Book Selected Credit Amount  """  
      self.TotBookSelBal:int = obj["TotBookSelBal"]
      """  Total Book Selected Balance.  This is the difference between the TotBookSelDB and TotBookSelCR.  """  
      self.TranPartiallyReversed:bool = obj["TranPartiallyReversed"]
      """  Logical indicating the journal transaction has been partially reversed.  """  
      self.TranCompletelyReversed:bool = obj["TranCompletelyReversed"]
      """  logical indicating if the transaction has been completely reversed  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  Closing fiscal period number  """  
      self.YearLastDate:bool = obj["YearLastDate"]
      """  Flag for Last Year Date validation  """  
      self.CloseFiscalPeriodList:str = obj["CloseFiscalPeriodList"]
      """  Available for selection closing periods  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Source GL Transaction currency code. GLJrnDtl.CurrencyCode  """  
      self.StatAmt:int = obj["StatAmt"]
      self.TotStatAmt:int = obj["TotStatAmt"]
      self.CurrencyCodeDesc:str = obj["CurrencyCodeDesc"]
      self.OrigFiscalPeriod:int = obj["OrigFiscalPeriod"]
      self.OrigFiscalYear:int = obj["OrigFiscalYear"]
      self.OrigFiscalYearSuffix:str = obj["OrigFiscalYearSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetGLTranList_input:
   """ Required : 
   abtUID
   """  
   def __init__(self, obj):
      self.abtUID:str = obj["abtUID"]
      """  ABTUID for the search.  """  
      pass

class GetGLTranList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AutoTranReversalTableset] = obj["returnObj"]
      pass

class GetListCurrentCompany_input:
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

class GetListCurrentCompany_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AutoTranReversalListTableset] = obj["returnObj"]
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
   NO_COMPANY
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      self.NO_COMPANY:str = obj["NO_COMPANY"]
      """  Is company in the where clause.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AutoTranReversalListTableset] = obj["returnObj"]
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

class OnChangeAmtStatToReverseRowMod_input:
   """ Required : 
   ipAmtStatToReverse
   ds
   """  
   def __init__(self, obj):
      self.ipAmtStatToReverse:int = obj["ipAmtStatToReverse"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeAmtStatToReverseRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAmtStatToReverse_input:
   """ Required : 
   ipAmtStatToReverse
   ds
   """  
   def __init__(self, obj):
      self.ipAmtStatToReverse:int = obj["ipAmtStatToReverse"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeAmtStatToReverse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAmtToReverseRowMod_input:
   """ Required : 
   ipAmtToReverse
   ds
   """  
   def __init__(self, obj):
      self.ipAmtToReverse:int = obj["ipAmtToReverse"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeAmtToReverseRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAmtToReverse_input:
   """ Required : 
   ipAmtToReverse
   ds
   """  
   def __init__(self, obj):
      self.ipAmtToReverse:int = obj["ipAmtToReverse"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeAmtToReverse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSelectedRowMod_input:
   """ Required : 
   ipSelected
   ds
   """  
   def __init__(self, obj):
      self.ipSelected:bool = obj["ipSelected"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeSelectedRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSelected_input:
   """ Required : 
   ipSelected
   ds
   """  
   def __init__(self, obj):
      self.ipSelected:bool = obj["ipSelected"]
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class OnChangeSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Post_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AutoTranReversalTableset] = obj["ds"]
      pass

class Post_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outErrorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

