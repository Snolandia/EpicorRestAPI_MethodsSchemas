import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TransSugSearchSvc
# Description: Garher suggestions from TFOrdDtl and TFOrdSug
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransSugSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransSugSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSugList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSugList
   Description: Get a list of all (changed and new) transfer order suggestions.
   OperationID: GetSugList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSugList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransSugSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_TransSugSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.PartDesc:str = obj["PartDesc"]
      """  Part Description  """  
      self.NewSug:bool = obj["NewSug"]
      """  New Suggestion  """  
      self.RequireDate:str = obj["RequireDate"]
      """  Require Date  """  
      self.RequireQty:int = obj["RequireQty"]
      """  Require Quantity  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  TFLineNum  """  
      self.AttrSetDesc:str = obj["AttrSetDesc"]
      """  Description of values in set  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TransSugSearchTableset:
   def __init__(self, obj):
      self.TransSugSearch:list[Erp_Tablesets_TransSugSearchRow] = obj["TransSugSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetSugList_input:
   """ Required : 
   includeNew
   includeOld
   plant
   horizonDate
   columnName
   columnValue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.includeNew:bool = obj["includeNew"]
      """  Include suggestions from TFOrdDtl.  """  
      self.includeOld:bool = obj["includeOld"]
      """  Include suggestions from TFOrdSug.  """  
      self.plant:str = obj["plant"]
      """  Plant for the search filter.  """  
      self.horizonDate:str = obj["horizonDate"]
      """  Horizon date for the search filter.  """  
      self.columnName:str = obj["columnName"]
      """  Column name (Part or Part Descriotion) for the search filter.  """  
      self.columnValue:str = obj["columnValue"]
      """  Column value for the search filter.  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetSugList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransSugSearchTableset] = obj["returnObj"]
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

