import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARAgingTrackerSvc
# Description: ARAgingTracker.
           AR Aging for Trackers.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GenerateTrackerForECC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTrackerForECC
   Description: This method should be called to populate the dataset for the AR Aging Tracker for ECC.
   OperationID: GenerateTrackerForECC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTrackerForECC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTrackerForECC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateReport
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GenerateReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTracker
   Description: This method should be called to populate the dataset for the AR Aging Tracker.
   OperationID: GenerateTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAgeBy(epicorHeaders = None):
   """  
   Summary: Invoke method GetAgeBy
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GetAgeBy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgeBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetAgingFormatCode(epicorHeaders = None):
   """  
   Summary: Invoke method GetAgingFormatCode
   Description: This method returns a list of valid 'AgingFormatCode' codes
UI note - user should  select only ONE of the valid codes.
   OperationID: GetAgingFormatCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgingFormatCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetARAccounts(epicorHeaders = None):
   """  
   Summary: Invoke method GetARAccounts
   Description: This method returns a list of ARAccounts and descriptions
   OperationID: GetARAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetNewParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewParams
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GetNewParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectBy(epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectBy
   Description: This method returns a select by list.
   OperationID: GetSelectBy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSortByList
   Description: This method returns a sort by list.
   OperationID: GetSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Killtask(epicorHeaders = None):
   """  
   Summary: Invoke method Killtask
   OperationID: Killtask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Killtask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DumpARDtls(epicorHeaders = None):
   """  
   Summary: Invoke method DumpARDtls
   OperationID: DumpARDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DumpARDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DumpARPrnt(epicorHeaders = None):
   """  
   Summary: Invoke method DumpARPrnt
   OperationID: DumpARPrnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DumpARPrnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DumpARDtls_output:
   def __init__(self, obj):
      pass

class DumpARPrnt_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARAgedRecReportParamRow:
   def __init__(self, obj):
      self.SelectBy:str = obj["SelectBy"]
      self.AgeBy:str = obj["AgeBy"]
      self.AgingDate:str = obj["AgingDate"]
      self.AgingDateToken:str = obj["AgingDateToken"]
      self.ARAccounts:str = obj["ARAccounts"]
      self.CustList:str = obj["CustList"]
      self.SummaryOnly:bool = obj["SummaryOnly"]
      self.AgingFormatCode:str = obj["AgingFormatCode"]
      self.SortBy:str = obj["SortBy"]
      self.CustType:str = obj["CustType"]
      """  B) for sorting detail by bill to customer and S) for sort by sold to.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.GLControlCodeList:str = obj["GLControlCodeList"]
      self.GLControlType:str = obj["GLControlType"]
      self.GLControlTypeDesc:str = obj["GLControlTypeDesc"]
      self.SortGLControlType:str = obj["SortGLControlType"]
      """  Sort by GL Control Type  """  
      self.SortGLControlTypeDesc:str = obj["SortGLControlTypeDesc"]
      """  SortGLControlTypeDesc  """  
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.PrintSelCriteria:bool = obj["PrintSelCriteria"]
      self.PrintLegNum:bool = obj["PrintLegNum"]
      """  Allow printing of legal numbers  """  
      self.SortByDesc:str = obj["SortByDesc"]
      self.PrintPromissoryNote:bool = obj["PrintPromissoryNote"]
      """  Allow printing of payment instruments  """  
      self.CustListID:str = obj["CustListID"]
      self.SysRowID:str = obj["SysRowID"]
      self.AutoAction:str = obj["AutoAction"]
      self.PrinterName:str = obj["PrinterName"]
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      self.AgentID:str = obj["AgentID"]
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      self.RecurringTask:bool = obj["RecurringTask"]
      self.RptPageSettings:str = obj["RptPageSettings"]
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      self.RptVersion:str = obj["RptVersion"]
      self.ReportStyleNum:int = obj["ReportStyleNum"]
      self.WorkstationID:str = obj["WorkstationID"]
      self.TaskNote:str = obj["TaskNote"]
      self.ArchiveCode:int = obj["ArchiveCode"]
      self.DateFormat:str = obj["DateFormat"]
      self.NumericFormat:str = obj["NumericFormat"]
      self.AgentCompareString:str = obj["AgentCompareString"]
      self.ProcessID:str = obj["ProcessID"]
      self.ProcessCompany:str = obj["ProcessCompany"]
      self.ProcessSystemCode:str = obj["ProcessSystemCode"]
      self.ProcessTaskNum:int = obj["ProcessTaskNum"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.GlbDecimalsGeneral:int = obj["GlbDecimalsGeneral"]
      self.GlbDecimalsCost:int = obj["GlbDecimalsCost"]
      self.GlbDecimalsPrice:int = obj["GlbDecimalsPrice"]
      self.FaxSubject:str = obj["FaxSubject"]
      self.FaxTo:str = obj["FaxTo"]
      self.FaxNumber:str = obj["FaxNumber"]
      self.EMailTo:str = obj["EMailTo"]
      self.EMailCC:str = obj["EMailCC"]
      self.EMailBCC:str = obj["EMailBCC"]
      self.EMailBody:str = obj["EMailBody"]
      self.AttachmentType:str = obj["AttachmentType"]
      self.ReportCurrencyCode:str = obj["ReportCurrencyCode"]
      self.ReportCultureCode:str = obj["ReportCultureCode"]
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      self.UIXml:str = obj["UIXml"]
      self.PrintReportParameters:bool = obj["PrintReportParameters"]
      self.SSRSEnableRouting:bool = obj["SSRSEnableRouting"]
      self.DesignMode:bool = obj["DesignMode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARDtlsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AgeBaseAll:int = obj["AgeBaseAll"]
      """  AgeBaseAll  """  
      self.AgeCurAll:int = obj["AgeCurAll"]
      """  AgeCurAll  """  
      self.AgeCurTotal1:int = obj["AgeCurTotal1"]
      """  AgeCurTotal1  """  
      self.AgeCurTotal2:int = obj["AgeCurTotal2"]
      """  AgeCurTotal2  """  
      self.AgeCurTotal3:int = obj["AgeCurTotal3"]
      """  AgeCurTotal3  """  
      self.AgeCurTotal4:int = obj["AgeCurTotal4"]
      """  AgeCurTotal4  """  
      self.AgeCurTotal5:int = obj["AgeCurTotal5"]
      """  AgeCurTotal5  """  
      self.AgeCurTotal6:int = obj["AgeCurTotal6"]
      """  AgeCurTotal6  """  
      self.AgeInvAmt1:int = obj["AgeInvAmt1"]
      """  AgeInvAmt1  """  
      self.AgeInvAmt2:int = obj["AgeInvAmt2"]
      """  AgeInvAmt2  """  
      self.AgeInvAmt3:int = obj["AgeInvAmt3"]
      """  AgeInvAmt3  """  
      self.AgeInvAmt4:int = obj["AgeInvAmt4"]
      """  AgeInvAmt4  """  
      self.AgeInvAmt5:int = obj["AgeInvAmt5"]
      """  AgeInvAmt5  """  
      self.AgeInvAmt6:int = obj["AgeInvAmt6"]
      """  AgeInvAmt6  """  
      self.AgeLbl1:str = obj["AgeLbl1"]
      """  AgeLbl1  """  
      self.AgeLbl2:str = obj["AgeLbl2"]
      """  AgeLbl2  """  
      self.AgeLbl3:str = obj["AgeLbl3"]
      """  AgeLbl3  """  
      self.AgeLbl4:str = obj["AgeLbl4"]
      """  AgeLbl4  """  
      self.AgeLbl5:str = obj["AgeLbl5"]
      """  AgeLbl5  """  
      self.AgeLbl6:str = obj["AgeLbl6"]
      """  AgeLbl6  """  
      self.AgeParentAll:int = obj["AgeParentAll"]
      """  AgeParentAll  """  
      self.AgeParentTotal1:int = obj["AgeParentTotal1"]
      """  AgeParentTotal1  """  
      self.AgeParentTotal2:int = obj["AgeParentTotal2"]
      """  AgeParentTotal2  """  
      self.AgeParentTotal3:int = obj["AgeParentTotal3"]
      """  AgeParentTotal3  """  
      self.AgeParentTotal4:int = obj["AgeParentTotal4"]
      """  AgeParentTotal4  """  
      self.AgeParentTotal5:int = obj["AgeParentTotal5"]
      """  AgeParentTotal5  """  
      self.AgeParentTotal6:int = obj["AgeParentTotal6"]
      """  AgeParentTotal6  """  
      self.ContPer:str = obj["ContPer"]
      """  Contact Person  """  
      self.ContPh:str = obj["ContPh"]
      """  Phone  """  
      self.crMemo:str = obj["crMemo"]
      """  crMemo  """  
      self.curDesc:str = obj["curDesc"]
      """  Currency  """  
      self.CurDueDate:str = obj["CurDueDate"]
      """  CurDueDate  """  
      self.CurrCode:str = obj["CurrCode"]
      """  CurrCode  """  
      self.CustID:str = obj["CustID"]
      """  Customer  """  
      self.CustName:str = obj["CustName"]
      """  CustName Parent:  """  
      self.DispCurTot:bool = obj["DispCurTot"]
      """  DispCurTot  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  ParentCustID  """  
      self.RptARAcctID:str = obj["RptARAcctID"]
      """  A/R Account  """  
      self.RptUserID:str = obj["RptUserID"]
      """  RptUserID  """  
      self.SInvcNum:str = obj["SInvcNum"]
      """  SInvcNum  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.PONum:str = obj["PONum"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.CreditMemo:bool = obj["CreditMemo"]
      self.PoDnNbr:str = obj["PoDnNbr"]
      """  For Debit Note type invoices this is Debit Note number assigned by the customer, for regular invoice this field is PO number  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARDtlsTableset:
   def __init__(self, obj):
      self.ARDtls:list[Erp_Tablesets_ARDtlsRow] = obj["ARDtls"]
      self.ARAgedRecReportParam:list[Erp_Tablesets_ARAgedRecReportParamRow] = obj["ARAgedRecReportParam"]
      self.ARPrnt:list[Erp_Tablesets_ARPrntRow] = obj["ARPrnt"]
      self.Company:list[Erp_Tablesets_CompanyRow] = obj["Company"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPrntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptUserID:str = obj["RptUserID"]
      """  RptUserID  """  
      self.RptARAcctID:str = obj["RptARAcctID"]
      """   The ARAcct.ARAcctID value of the specific set of AR accounts that will be used by the invoice and payment transactions related to the customer. If left blank then the default AR accounts are used.
(see ARSyst.ArAcctID).  """  
      self.CurrCode:str = obj["CurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CustName:str = obj["CustName"]
      """  The full name of the customer.  """  
      self.Summary:bool = obj["Summary"]
      """  Summary  """  
      self.ARTot1:int = obj["ARTot1"]
      """  Ar total1  """  
      self.ARTot2:int = obj["ARTot2"]
      """  Ar total 2  """  
      self.ARTot3:int = obj["ARTot3"]
      """  AR total3  """  
      self.ARTot4:int = obj["ARTot4"]
      """  AR total4  """  
      self.ARTot5:int = obj["ARTot5"]
      """  AR total 5  """  
      self.ARTot6:int = obj["ARTot6"]
      """  AR total 6  """  
      self.MulChildren:bool = obj["MulChildren"]
      """  MulChildren  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  ParentCustID  """  
      self.RptTitle1:str = obj["RptTitle1"]
      """  RptTitle1  """  
      self.RptTitle2:str = obj["RptTitle2"]
      """  RptTitle2  """  
      self.RptTitle3:str = obj["RptTitle3"]
      """  RptTitle3  """  
      self.SubTitle1:str = obj["SubTitle1"]
      """  SubTitle1  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARTrackerTotRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CurNumInv:int = obj["CurNumInv"]
      """  Curent number of invoices  """  
      self.InvTotal:int = obj["InvTotal"]
      """  Total by Invoice Date  """  
      self.PaidYtd:int = obj["PaidYtd"]
      """  Paid YTD  """  
      self.LastPymt:int = obj["LastPymt"]
      """  Last Payment  """  
      self.LastPymtDate:str = obj["LastPymtDate"]
      """  Last Pymt Date  """  
      self.YTDNumInv:int = obj["YTDNumInv"]
      """  Number of Invoices  """  
      self.YTDRevenue:int = obj["YTDRevenue"]
      """  Revenue  """  
      self.YTDProfit:int = obj["YTDProfit"]
      """  Profit  """  
      self.YTDMargin:int = obj["YTDMargin"]
      """  Gross Margin  """  
      self.YTDAvgInvAmt:int = obj["YTDAvgInvAmt"]
      """  Avg Invoice Amount  """  
      self.YTDAvgDaysToPay:int = obj["YTDAvgDaysToPay"]
      """  Avg Days to Pay  """  
      self.PYTDNumInv:int = obj["PYTDNumInv"]
      """  Last year number of invoices  """  
      self.PYTDRevenue:int = obj["PYTDRevenue"]
      """  Last year revenue  """  
      self.PYTDProfit:int = obj["PYTDProfit"]
      """  Last year profit  """  
      self.PYTDMargin:int = obj["PYTDMargin"]
      """  Last year margain  """  
      self.PYTDAvgInvAmt:int = obj["PYTDAvgInvAmt"]
      """  Last year average invoice amount  """  
      self.PYTDAvgDaysToPay:int = obj["PYTDAvgDaysToPay"]
      """  Last year average days to pay  """  
      self.CurrDueAmt:int = obj["CurrDueAmt"]
      """  Current due amount  """  
      self.CurrDuePct:int = obj["CurrDuePct"]
      """  Current due percent  """  
      self.CurrInvAmt:int = obj["CurrInvAmt"]
      """  Current invoice amount  """  
      self.CurrInvPct:int = obj["CurrInvPct"]
      """  Current invoice percent  """  
      self.FutureDueAmt:int = obj["FutureDueAmt"]
      """  Future days due amount  """  
      self.FutureDuePct:int = obj["FutureDuePct"]
      """  Future due percent  """  
      self.FutureInvAmt:int = obj["FutureInvAmt"]
      """  Future invoice amount  """  
      self.FutureInvPct:int = obj["FutureInvPct"]
      """  Future invoice percent  """  
      self.Due30Amt:int = obj["Due30Amt"]
      """  Over 30 days due amount  """  
      self.Due30Pct:int = obj["Due30Pct"]
      """  Over 30 days due percent  """  
      self.Inv30Amt:int = obj["Inv30Amt"]
      """  Over 30 days invoice amount  """  
      self.Inv30Pct:int = obj["Inv30Pct"]
      """  Over 30 days invoice percent  """  
      self.Due60Amt:int = obj["Due60Amt"]
      """  Over 60 days due amount  """  
      self.Due60Pct:int = obj["Due60Pct"]
      """  Over 60 days due percent  """  
      self.Inv60Amt:int = obj["Inv60Amt"]
      """  Over 60 days invoice percent  """  
      self.Inv60Pct:int = obj["Inv60Pct"]
      """  Over 60 days invoice percent  """  
      self.Due90Amt:int = obj["Due90Amt"]
      """  90 days due amount  """  
      self.Due90Pct:int = obj["Due90Pct"]
      """  90 days due percent  """  
      self.Inv90Amt:int = obj["Inv90Amt"]
      """  90 days invoice amount  """  
      self.Inv90Pct:int = obj["Inv90Pct"]
      """  90 days invoice percent  """  
      self.Due120Amt:int = obj["Due120Amt"]
      """  120 days due amount  """  
      self.Inv120Amt:int = obj["Inv120Amt"]
      """  120 days invoice amount  """  
      self.Due120Pct:int = obj["Due120Pct"]
      """  120 days due percent  """  
      self.Inv120Pct:int = obj["Inv120Pct"]
      """  120 days invoice percent  """  
      self.ColHead1:str = obj["ColHead1"]
      """  Column one heading (Current)  """  
      self.ColHead2:str = obj["ColHead2"]
      """  Column 2 heading (Over 30)  """  
      self.ColHead3:str = obj["ColHead3"]
      """  Coumn heading 3 (Over 60)  """  
      self.ColHead4:str = obj["ColHead4"]
      """  Coumn heading 4 (Over 90)  """  
      self.ColHead5:str = obj["ColHead5"]
      """  Column heading 5 (Over 120)  """  
      self.ColHead6:str = obj["ColHead6"]
      """  Coumn heading 6 (Future)  """  
      self.CustName:str = obj["CustName"]
      """  Customer name  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.YTDNetInvoiceTotal:int = obj["YTDNetInvoiceTotal"]
      """  Year to Date Net Invoice Total. This is the sum of all invoice type total amount including Credit Memos with exception of Unapplied Cash Receipt Invoices and Debit Notes.  """  
      self.PYTDNetInvoiceTotal:int = obj["PYTDNetInvoiceTotal"]
      """  Last Year Net Invoice Total. This is the sum of all invoice type total amount including Credit Memos with exception of Unapplied Cash Receipt Invoices and Debit Notes.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARTrackerTotTableset:
   def __init__(self, obj):
      self.ARTrackerTot:list[Erp_Tablesets_ARTrackerTotRow] = obj["ARTrackerTot"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  First company address line.  """  
      self.Address2:str = obj["Address2"]
      """  Second company address line.  """  
      self.Address3:str = obj["Address3"]
      """  Third company address line.  """  
      self.City:str = obj["City"]
      """  City portion of company address.  """  
      self.State:str = obj["State"]
      """  State portion of company address.  """  
      self.Zip:str = obj["Zip"]
      """  Postal code or zip code portion of company address.  """  
      self.Country:str = obj["Country"]
      """  Country portion of company address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Company phone number  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Company fax number  """  
      self.FEIN:str = obj["FEIN"]
      """  Federal Income Tax Number  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  Current fiscal year  """  
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.Number:int = obj["Number"]
      """  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  """  
      self.FRxDSN:str = obj["FRxDSN"]
      """  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  """  
      self.EschedFileSet:str = obj["EschedFileSet"]
      """  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier from and external G/L interface  """  
      self.LogoFile:str = obj["LogoFile"]
      """  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  """  
      self.EmpPhotoPath:str = obj["EmpPhotoPath"]
      """  Path the Employee Photos are stored in.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.FrxUserid:str = obj["FrxUserid"]
      """  The User ID for FRx.  """  
      self.FRxPassWord:str = obj["FRxPassWord"]
      """  FRxUserID password  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar id for the company.  """  
      self.LegalName:str = obj["LegalName"]
      """  Company legal name  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.ActTypeCode:str = obj["ActTypeCode"]
      """  Economic Activity Type  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Chief Executive Officerr name  """  
      self.ChiefAcctName:str = obj["ChiefAcctName"]
      """  Chief Financial Officer Name  """  
      self.ReportTypePref:str = obj["ReportTypePref"]
      """  Type of report  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WIAutoCreateJob:bool = obj["WIAutoCreateJob"]
      """  WIAutoCreateJob  """  
      self.WIGetDetails:bool = obj["WIGetDetails"]
      """  WIGetDetails  """  
      self.WISchedule:bool = obj["WISchedule"]
      """  WISchedule  """  
      self.WIRelease:bool = obj["WIRelease"]
      """  WIRelease  """  
      self.WIShippingCosts:bool = obj["WIShippingCosts"]
      """  WIShippingCosts  """  
      self.DeepCopy:bool = obj["DeepCopy"]
      """  DeepCopy  """  
      self.DeepCopyDupOrRevEst:bool = obj["DeepCopyDupOrRevEst"]
      """  DeepCopyDupOrRevEst  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MapURL:str = obj["MapURL"]
      """  MapURL  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.APBOECheck:int = obj["APBOECheck"]
      """  APBOE Check  """  
      self.COSequenceCert:int = obj["COSequenceCert"]
      """  COSequenceCert  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Company has to be synchronized with Epicor FSA application.  """  
      self.EpicorAccountNum:int = obj["EpicorAccountNum"]
      """  Epicor client number for CRE  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.KindOfEmp:str = obj["KindOfEmp"]
      """  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  """  
      self.EmploymentCode:str = obj["EmploymentCode"]
      """  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      """  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  """  
      self.BaseCurrCode:str = obj["BaseCurrCode"]
      """  Currency.BaseCurrCode field  """  
      self.ExtPRConfig:bool = obj["ExtPRConfig"]
      self.HasCurrTrans:bool = obj["HasCurrTrans"]
      """  Has Currency Transactions  """  
      self.Intrastat:bool = obj["Intrastat"]
      self.ProductName:str = obj["ProductName"]
      """  Name of product (MFGSYS Name)  """  
      self.AllowSchedulingBeforeToday:bool = obj["AllowSchedulingBeforeToday"]
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GenerateReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARDtlsTableset] = obj["ds"]
      pass

class GenerateReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARDtlsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateTrackerForECC_input:
   """ Required : 
   CustID
   """  
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      """  Customer ID.  """  
      pass

class GenerateTrackerForECC_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARTrackerTotTableset] = obj["returnObj"]
      pass

class GenerateTracker_input:
   """ Required : 
   CustID
   """  
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      """  Customer ID.  """  
      pass

class GenerateTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARTrackerTotTableset] = obj["returnObj"]
      pass

class GetARAccounts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.arActsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAgeBy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AgeBylist:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAgingFormatCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AgingFormatCodelist:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARDtlsTableset] = obj["ds"]
      pass

class GetNewParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARDtlsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectBy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.selectbylist:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sortbylist:str = obj["parameters"]
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

class Killtask_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

