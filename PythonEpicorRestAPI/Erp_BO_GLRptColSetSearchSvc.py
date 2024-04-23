import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLRptColSetSearchSvc
# Description: Search for column sets for a given financial report.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLRptColSetSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLRptColSetSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLRptColSetSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method returns the Data Schema records
   OperationID: Get_GetRows
      :param whereClause: Desc: Where clause   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLRptColSetSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns the Data Schema records
   OperationID: Get_GetList
      :param whereClause: Desc: Where clause   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLRptColSetSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRptColSetListRow] = obj["value"]
      pass

class Erp_Tablesets_GLRptColSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnTitle01:str = obj["ColumnTitle01"]
      self.ColumnTitle02:str = obj["ColumnTitle02"]
      self.ColumnTitle03:str = obj["ColumnTitle03"]
      self.ColumnTitle04:str = obj["ColumnTitle04"]
      self.ColumnTitle05:str = obj["ColumnTitle05"]
      self.ColumnTitle06:str = obj["ColumnTitle06"]
      self.ColumnTitle07:str = obj["ColumnTitle07"]
      self.ColumnTitle08:str = obj["ColumnTitle08"]
      self.ColumnTitle09:str = obj["ColumnTitle09"]
      self.ColumnTitle10:str = obj["ColumnTitle10"]
      self.ColumnTitle11:str = obj["ColumnTitle11"]
      self.ColumnTitle12:str = obj["ColumnTitle12"]
      self.ColumnTitle13:str = obj["ColumnTitle13"]
      self.ColumnTitle14:str = obj["ColumnTitle14"]
      self.ColumnTitle15:str = obj["ColumnTitle15"]
      self.ColumnTitle16:str = obj["ColumnTitle16"]
      self.ColumnTitle17:str = obj["ColumnTitle17"]
      self.ColumnTitle18:str = obj["ColumnTitle18"]
      self.ColumnTitle19:str = obj["ColumnTitle19"]
      self.ColumnTitle20:str = obj["ColumnTitle20"]
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_GLRptColSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnTitle01:str = obj["ColumnTitle01"]
      self.ColumnTitle02:str = obj["ColumnTitle02"]
      self.ColumnTitle03:str = obj["ColumnTitle03"]
      self.ColumnTitle04:str = obj["ColumnTitle04"]
      self.ColumnTitle05:str = obj["ColumnTitle05"]
      self.ColumnTitle06:str = obj["ColumnTitle06"]
      self.ColumnTitle07:str = obj["ColumnTitle07"]
      self.ColumnTitle08:str = obj["ColumnTitle08"]
      self.ColumnTitle09:str = obj["ColumnTitle09"]
      self.ColumnTitle10:str = obj["ColumnTitle10"]
      self.ColumnTitle11:str = obj["ColumnTitle11"]
      self.ColumnTitle12:str = obj["ColumnTitle12"]
      self.ColumnTitle13:str = obj["ColumnTitle13"]
      self.ColumnTitle14:str = obj["ColumnTitle14"]
      self.ColumnTitle15:str = obj["ColumnTitle15"]
      self.ColumnTitle16:str = obj["ColumnTitle16"]
      self.ColumnTitle17:str = obj["ColumnTitle17"]
      self.ColumnTitle18:str = obj["ColumnTitle18"]
      self.ColumnTitle19:str = obj["ColumnTitle19"]
      self.ColumnTitle20:str = obj["ColumnTitle20"]
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptColSetListTableset:
   def __init__(self, obj):
      self.GLRptColSetList:list[Erp_Tablesets_GLRptColSetListRow] = obj["GLRptColSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLRptColSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnTitle01:str = obj["ColumnTitle01"]
      self.ColumnTitle02:str = obj["ColumnTitle02"]
      self.ColumnTitle03:str = obj["ColumnTitle03"]
      self.ColumnTitle04:str = obj["ColumnTitle04"]
      self.ColumnTitle05:str = obj["ColumnTitle05"]
      self.ColumnTitle06:str = obj["ColumnTitle06"]
      self.ColumnTitle07:str = obj["ColumnTitle07"]
      self.ColumnTitle08:str = obj["ColumnTitle08"]
      self.ColumnTitle09:str = obj["ColumnTitle09"]
      self.ColumnTitle10:str = obj["ColumnTitle10"]
      self.ColumnTitle11:str = obj["ColumnTitle11"]
      self.ColumnTitle12:str = obj["ColumnTitle12"]
      self.ColumnTitle13:str = obj["ColumnTitle13"]
      self.ColumnTitle14:str = obj["ColumnTitle14"]
      self.ColumnTitle15:str = obj["ColumnTitle15"]
      self.ColumnTitle16:str = obj["ColumnTitle16"]
      self.ColumnTitle17:str = obj["ColumnTitle17"]
      self.ColumnTitle18:str = obj["ColumnTitle18"]
      self.ColumnTitle19:str = obj["ColumnTitle19"]
      self.ColumnTitle20:str = obj["ColumnTitle20"]
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptColSetSearchTableset:
   def __init__(self, obj):
      self.GLRptColSet:list[Erp_Tablesets_GLRptColSetRow] = obj["GLRptColSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLRptColSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLRptColSetSearchTableset] = obj["returnObj"]
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

