import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuoteAsmSearchSvc
# Description: The QuoteAsm Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuoteAsmSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all of the QuoteAsmSearch records which will be a subset
of the QuoteAsm records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (QuoteAsmSearch) we need our own public method.
   OperationID: Get_GetRows
      :param whereClauseQuoteAsmSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "whereClauseQuoteAsmSearch=" + whereClauseQuoteAsmSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_QuoteAsmSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The assembly sequence number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.IndentedPartNum:str = obj["IndentedPartNum"]
      """  The indented part number (with leading dots).  """  
      self.Description:str = obj["Description"]
      """  The part description.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  The BOM Level.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  The BOM Sequence.  """  
      self.Template:bool = obj["Template"]
      """  Is this a template?  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmSearchTableset:
   def __init__(self, obj):
      self.QuoteAsmSearch:list[Erp_Tablesets_QuoteAsmSearchRow] = obj["QuoteAsmSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseQuoteAsmSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteAsmSearch:str = obj["whereClauseQuoteAsmSearch"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmSearchTableset] = obj["returnObj"]
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

