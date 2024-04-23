import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AutoPrintSearchSvc
# Description: This service is used by the BAM on BPM Data Directives to search for reports for Autoprint.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRowsAutoPrint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsAutoPrint
   Description: This method searches for reports that can be set up for AutoPrinting on BAM.
   OperationID: GetRowsAutoPrint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsAutoPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsAutoPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListAutoPrint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAutoPrint
   Description: This method searches for reports that can be set up for AutoPrinting on BAM.
   OperationID: GetListAutoPrint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAutoPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAutoPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAutoReportSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAutoReportSettings
   Description: Adds a new row in the AutoReport table and returns the parameters for the service.
Invokes GetNewParameters on the service and returns list of parameters that the report expects.
Used by AutoPrint Action setup on BPM Data Directives
   OperationID: GetNewAutoReportSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAutoReportSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAutoReportSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupForRptCriteriaFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupForRptCriteriaFilter
   Description: Gets the adapter name and lookup field for the Report criteria filter.
   OperationID: GetLookupForRptCriteriaFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupForRptCriteriaFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupForRptCriteriaFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupForBAQReportFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupForBAQReportFilter
   Description: Gets the adapter name and lookup field for the BAQ Report filter.
   OperationID: GetLookupForBAQReportFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupForBAQReportFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupForBAQReportFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetListAutoPrint_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where Clause for the search  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListAutoPrint_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AutoPrintSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLookupForBAQReportFilter_input:
   """ Required : 
   reportId
   filterName
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.filterName:str = obj["filterName"]
      """  Name of the filter.  """  
      pass

class GetLookupForBAQReportFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.adapterName:str = obj["parameters"]
      self.lookupField:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLookupForRptCriteriaFilter_input:
   """ Required : 
   reportId
   reportStyleNum
   filterName
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.reportStyleNum:int = obj["reportStyleNum"]
      """  The report style number.  """  
      self.filterName:str = obj["filterName"]
      """  Name of the filter.  """  
      pass

class GetLookupForRptCriteriaFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.adapterName:str = obj["parameters"]
      self.lookupField:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewAutoReportSettings_input:
   """ Required : 
   reportID
   styleNum
   isBAQReport
   reportSettingsDS
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  Style number for the report.  """  
      self.isBAQReport:bool = obj["isBAQReport"]
      """  if set to `true` indicates the style points to a BAQ report.  """  
      self.reportSettingsDS:list[Ice_Tablesets_AutoRptSettingsTableset] = obj["reportSettingsDS"]
      pass

class GetNewAutoReportSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.reportSettingsDS:list[Ice_Tablesets_AutoRptSettingsTableset] = obj["reportSettingsDS"]
      pass

      """  output parameters  """  

class GetRowsAutoPrint_input:
   """ Required : 
   tableName
   systemCode
   reportID
   reportDesc
   reportDataDefID
   reportType
   reportTableCondition
   baqReportID
   baqReportDesc
   onlyBAQReports
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Name of table that the BPM Data Directive is for  """  
      self.systemCode:str = obj["systemCode"]
      """  SystemCode of the BAM/BPM table  """  
      self.reportID:str = obj["reportID"]
      """  ReportID search criteria (used as StartsWith)  """  
      self.reportDesc:str = obj["reportDesc"]
      """  Report Description search criteria (used as StartsWith)  """  
      self.reportDataDefID:str = obj["reportDataDefID"]
      """  Report Data Definition ID search criteria (used as StartsWith)  """  
      self.reportType:str = obj["reportType"]
      """  Report Type search criteria, selected from a dropdown (Base Definition, Crystal,Outbound EDI, Epicor Financial Report, Bartender Labels, SQL Server Reporting)  """  
      self.reportTableCondition:int = obj["reportTableCondition"]
      """  Report table search criteria, selected from a dropdown (IsPrimaryOnReport/1[tableName] is Primary on Report, IsSecondaryOnReport/2=[tableName] is not Primary on Report, IsUsedOnReport/3=[tableName] is used on Report at any level, None/0=(Search for all reports, irrespective of table used)  """  
      self.baqReportID:str = obj["baqReportID"]
      """  BAQ Report ID (used as StartsWith)  """  
      self.baqReportDesc:str = obj["baqReportDesc"]
      """  BAQ Report Description (used as StartsWith)  """  
      self.onlyBAQReports:bool = obj["onlyBAQReports"]
      """  Only search for BAQ reports  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsAutoPrint_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AutoPrintSearchTableset] = obj["returnObj"]
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

class Ice_Tablesets_AutoPrintSearchRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID from Ice.Report  """  
      self.ReportDescription:str = obj["ReportDescription"]
      """  Report Data Definition's Description  """  
      self.ReportTypeID:str = obj["ReportTypeID"]
      """  Report Type from ReportStyle.RptTypeID  """  
      self.ReportDataDefinitionID:str = obj["ReportDataDefinitionID"]
      """  Report Data Definition ID  """  
      self.BAQReportID:str = obj["BAQReportID"]
      """  BAQReport ID from BAQReport.BAQRptID  """  
      self.BAQReportDescription:str = obj["BAQReportDescription"]
      """  BAQ Report's Description from BAQReport.Description  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Style Description from ReportStyle.RptDescription  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Style Num from ReportStyle.StyleNum  """  
      self.IsBAQReport:bool = obj["IsBAQReport"]
      """  Indicates if search result row represents a BAQ Report  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """  Is SystemRpt from ReportStyle.SystemRpt  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  BO that handles the report  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AutoPrintSearchTableset:
   def __init__(self, obj):
      self.AutoPrintSearch:list[Ice_Tablesets_AutoPrintSearchRow] = obj["AutoPrintSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AutoReportRow:
   def __init__(self, obj):
      self.AutoProgram:str = obj["AutoProgram"]
      """  BO that handles the report  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID from Ice.Report  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Report style description  """  
      self.ReportDataDefinitionID:str = obj["ReportDataDefinitionID"]
      """  Data Definition ID  """  
      self.ReportTypeID:str = obj["ReportTypeID"]
      """  Report Type  """  
      self.IsBAQReport:bool = obj["IsBAQReport"]
      """  Indicates if this represents a BAQ Report  """  
      self.TaskNote:str = obj["TaskNote"]
      """  Task Note  """  
      self.RunSchedule:str = obj["RunSchedule"]
      """  When to run report - Immediate, Queued  """  
      self.PrinterSettings:str = obj["PrinterSettings"]
      """  Printer settings merged into one string  """  
      self.PageSettings:str = obj["PageSettings"]
      """  Report Page Settings as a string  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Printer Name  """  
      self.ReportDescription:str = obj["ReportDescription"]
      """  Report.RptDescription  """  
      self.PrintSel:str = obj["PrintSel"]
      """   Printer Selection: 'SEL' or 'NEW'
Indicates if user selected a predefined printer from AutoPrinter combo or they set up a new one on the form.  """  
      self.NewPrinterName:str = obj["NewPrinterName"]
      """  Printer selected by the user via the Print dialog instead of the combo  """  
      self.PrintQtySel:str = obj["PrintQtySel"]
      """   Printer quantity radio button selection. If Quantity comes from a constant or from a table.field
Values: "CONS", "DYN"  """  
      self.PrintQtyConstant:int = obj["PrintQtyConstant"]
      """  Constant value selected for Print Quantity  """  
      self.PrintQtyTableName:str = obj["PrintQtyTableName"]
      """  Table name if Print Quantity is dynamic  """  
      self.PrintQtyColumnName:str = obj["PrintQtyColumnName"]
      """  Column from which dynamic Print Qty is taken  """  
      self.PrintAction:str = obj["PrintAction"]
      """  Printer action: Print, Preview  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.DefaultSysAgentID:str = obj["DefaultSysAgentID"]
      """  Default SysAgent ID  """  
      self.ParametersTablesetType:str = obj["ParametersTablesetType"]
      """  This field stores the type name of the Tableset that GetNewParameters returns. It will be used in BPM later to instantiate the report parameters tableset.  """  
      self.SysAgentPwd:str = obj["SysAgentPwd"]
      """  SysAgent.SysPassword  """  
      self.SysAgentUserID:str = obj["SysAgentUserID"]
      """  SysAgent.SysUserID  """  
      self.OutputFormat:str = obj["OutputFormat"]
      """  Output format selected by user for SSRS reports  """  
      self.NewPrinterSettings:str = obj["NewPrinterSettings"]
      """  Printer Settings for the client side printer  """  
      self.NewPageSettings:str = obj["NewPageSettings"]
      """  Page Settings for the client side printer  """  
      self.SSRSEnableRouting:bool = obj["SSRSEnableRouting"]
      """  Maps to the SSRSEnableRouting report parameter. If enabled, sets the report parameter value.  """  
      self.IsDynamicCriteriaReport:bool = obj["IsDynamicCriteriaReport"]
      """  Indicates if this represents a Dynamic Criteria Report  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AutoRptParametersRow:
   def __init__(self, obj):
      self.ParameterName:str = obj["ParameterName"]
      """  Name of the Parameter  """  
      self.ParameterType:str = obj["ParameterType"]
      """  Data type of parameter  """  
      self.ParameterAction:str = obj["ParameterAction"]
      """  User selected prompt  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.ActionType:int = obj["ActionType"]
      """  Type of action selected by user:
        TableField=0, Constant=1, BAQConstant=2, Expression=3,BPMCallContext=4,None=5  """  
      self.ParameterLabel:str = obj["ParameterLabel"]
      """  Label for the parameter to display on the AutoPrint settings dialog,  """  
      self.IsCriteria:bool = obj["IsCriteria"]
      """  Indicates if this represents a Report Criteria Set's Prompt or Filter (for dynamic criteria reports). These are not submitted directly, they are built into a XML document.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AutoRptSettingsTableset:
   def __init__(self, obj):
      self.AutoReport:list[Ice_Tablesets_AutoReportRow] = obj["AutoReport"]
      self.AutoRptParameters:list[Ice_Tablesets_AutoRptParametersRow] = obj["AutoRptParameters"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

