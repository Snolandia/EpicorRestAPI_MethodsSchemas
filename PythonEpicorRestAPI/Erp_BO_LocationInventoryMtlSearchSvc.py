import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LocationInventoryMtlSearchSvc
# Description: Location Inventory Mtl Search service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventoryMtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventoryMtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLocInvMtlSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all the LocationWarrantyTran records
This method will try to mirror the functionality of the base GetRows method, but since we are
populating a temp table (LocationInventoryMtlSearch) we need our own public method.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "whereClauseLocInvMtlSearch=" + whereClauseLocInvMtlSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventoryMtlSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_LocationInventoryMtlSearchRow:
   def __init__(self, obj):
      self.DealerWarranty:str = obj["DealerWarranty"]
      self.DealerWarrantyDesc:str = obj["DealerWarrantyDesc"]
      self.DealerWarrantyExpiration:str = obj["DealerWarrantyExpiration"]
      self.DealerWarrantyStart:str = obj["DealerWarrantyStart"]
      self.LineDesc:str = obj["LineDesc"]
      self.LotNum:str = obj["LotNum"]
      self.PartNum:str = obj["PartNum"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      self.WarrantyComment:str = obj["WarrantyComment"]
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      self.WarrDescription:str = obj["WarrDescription"]
      self.JobNum:str = obj["JobNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryMtlSearchTableset:
   def __init__(self, obj):
      self.LocationInventoryMtlSearch:list[Erp_Tablesets_LocationInventoryMtlSearchRow] = obj["LocationInventoryMtlSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseLocInvMtlSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLocInvMtlSearch:str = obj["whereClauseLocInvMtlSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationInventoryMtlSearchTableset] = obj["returnObj"]
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

