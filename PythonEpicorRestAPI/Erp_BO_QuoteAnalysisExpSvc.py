import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuoteAnalysisExpSvc
# Description: Quote Analysis Export Business Object
           This is not a typical business object and will not use the standard
           core/BOBase.i methods.  The only dataset used in this object is the
           browser of available QuoteDtl records.  Methods are available to do
           the Build/Delete of Quote Analysis data.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildAnalysis(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAnalysis
   Description: Call this method when the user already selected quote lines to process.
This method expects a LIST-DELIM delimited string of RowIds of all selected
QuoteDtl records.
   OperationID: BuildAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAllAnalysis(epicorHeaders = None):
   """  
   Summary: Invoke method ClearAllAnalysis
   Description: Call this method to delete or clear all QuoteAnalysis records.
This method expects that the user already confirmed that records will be deleted.
   OperationID: ClearAllAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAllAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetByQuoteLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByQuoteLine
   Description: This method finds the QuoteDtl record by QuoteNum/QuoteLine.
   OperationID: GetByQuoteLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByQuoteLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByQuoteLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteDtlBrw(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteDtlBrw
   Description: This method assembles the QuoteDtl browse for the main data set.
   OperationID: GetQuoteDtlBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAnalysisExpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildAnalysis_input:
   """ Required : 
   vRowList
   """  
   def __init__(self, obj):
      self.vRowList:str = obj["vRowList"]
      """  A RowId list of selected QuoteDtl records.  """  
      pass

class BuildAnalysis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearAllAnalysis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_QuoteAnalysisExpTableset:
   def __init__(self, obj):
      self.QuoteDtlBrw:list[Erp_Tablesets_QuoteDtlBrwRow] = obj["QuoteDtlBrw"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteDtlBrwRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Selected:bool = obj["Selected"]
      """  Row has been selected for processing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetByQuoteLine_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number  """  
      pass

class GetByQuoteLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAnalysisExpTableset] = obj["returnObj"]
      pass

class GetQuoteDtlBrw_input:
   """ Required : 
   whereClauseQuoteDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      """  Where clause to specify set of QuoteDtlBrw records to return  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetQuoteDtlBrw_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAnalysisExpTableset] = obj["returnObj"]
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

