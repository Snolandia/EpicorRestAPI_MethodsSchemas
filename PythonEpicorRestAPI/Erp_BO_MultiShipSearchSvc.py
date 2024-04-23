import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MultiShipSearchSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MultiShipSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MultiShipSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Purpose: Returns valid PayMethods.
Parameters:
<param name="whereClause">Data Table Where Clause </param><param name="type">type</param><param name="shipDate">shipDate</param><param name="sortBy">sortBy</param><param name="startAt">startAt</param><param name="dtStartAt">dtStartAt</param><param name="status">status</param><param name="vendorNum">vendorNum</param><param name="custNum">custNum</param><param name="shipToNum">shipToNum</param><param name="pageSize">Page Size</param><param name="absolutePage">Absolute Page</param><param name="morePages">More Pages flag</param><returns>Erp.BO.MultiShipSearchTableset</returns>
Notes:
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MultiShipSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_MultiShipSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustomerID:str = obj["CustomerID"]
      self.EntryPerson:str = obj["EntryPerson"]
      self.FromSite:str = obj["FromSite"]
      self.Log:str = obj["Log"]
      self.Name:str = obj["Name"]
      self.OrderNum:int = obj["OrderNum"]
      self.PackNum:int = obj["PackNum"]
      self.PONum:int = obj["PONum"]
      self.PurPoint:str = obj["PurPoint"]
      self.ShipDate:str = obj["ShipDate"]
      self.ShipmentType:str = obj["ShipmentType"]
      self.Shipped:bool = obj["Shipped"]
      self.ToSite:str = obj["ToSite"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MultiShipSearchTableset:
   def __init__(self, obj):
      self.MultiShipSearch:list[Erp_Tablesets_MultiShipSearchRow] = obj["MultiShipSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClause
   shipDate
   type
   sortBy
   startAt
   dtStartAt
   status
   vendorNum
   custNum
   shipToNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.shipDate:str = obj["shipDate"]
      self.type:str = obj["type"]
      self.sortBy:str = obj["sortBy"]
      self.startAt:int = obj["startAt"]
      self.dtStartAt:str = obj["dtStartAt"]
      self.status:str = obj["status"]
      self.vendorNum:int = obj["vendorNum"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MultiShipSearchTableset] = obj["returnObj"]
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

