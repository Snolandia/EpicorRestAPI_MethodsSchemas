import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.SsrsReportAnalyzerSvc
# Description: Analyzes SSRS reports for a specific report style.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_SummarizeReportAnalysis(epicorHeaders = None):
   """  
   Summary: Invoke method SummarizeReportAnalysis
   Description: Analyzes all reports and summarizes the results.
   OperationID: SummarizeReportAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SummarizeReportAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_AnalyzeReportDataDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AnalyzeReportDataDefinition
   Description: Analyzes the report data definition analyzing all report styles that use the definition.
   OperationID: AnalyzeReportDataDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeReportDataDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportDataDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AnalyzeReportStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AnalyzeReportStyle
   Description: Analyzes the report style.
   OperationID: AnalyzeReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AnalyzeReportDataDefinition_input:
   """ Required : 
   reportDefinitionId
   """  
   def __init__(self, obj):
      self.reportDefinitionId:str = obj["reportDefinitionId"]
      """  The report definition identifier.  """  
      pass

class AnalyzeReportDataDefinition_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SsrsReportAnalyzerTableset] = obj["returnObj"]
      pass

class AnalyzeReportStyle_input:
   """ Required : 
   reportId
   styleNum
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  The style number.  """  
      pass

class AnalyzeReportStyle_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SsrsReportAnalyzerTableset] = obj["returnObj"]
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

class Ice_Tablesets_AnalyzerResultsRow:
   def __init__(self, obj):
      self.IssueText:str = obj["IssueText"]
      self.IssueType:int = obj["IssueType"]
      self.ReportDataDefinition:str = obj["ReportDataDefinition"]
      self.ReportPath:str = obj["ReportPath"]
      self.Sequence:int = obj["Sequence"]
      self.TableName:str = obj["TableName"]
      self.ColumnName:str = obj["ColumnName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SsrsReportAnalyzerTableset:
   def __init__(self, obj):
      self.AnalyzerResults:list[Ice_Tablesets_AnalyzerResultsRow] = obj["AnalyzerResults"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class SummarizeReportAnalysis_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SsrsReportAnalyzerTableset] = obj["returnObj"]
      pass

