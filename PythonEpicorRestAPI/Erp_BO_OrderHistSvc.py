import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OrderHistSvc
# Description: Handles the Order History
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderHistSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderHistSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetListOrderHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListOrderHistory
   Description: This method returns latest Parts sold by a given Customer.
   OperationID: GetListOrderHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOrderHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOrderHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderHistSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_OrderHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part Description  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Order Quantity  """  
      self.UOM:str = obj["UOM"]
      """  Selling Unit of Measure  """  
      self.OriginalPrice:int = obj["OriginalPrice"]
      """  Original Price  """  
      self.NewPrice:int = obj["NewPrice"]
      """  New Price  """  
      self.NewQty:int = obj["NewQty"]
      """  New Quantity  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderHistTableset:
   def __init__(self, obj):
      self.OrderHist:list[Erp_Tablesets_OrderHistRow] = obj["OrderHist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetListOrderHistory_input:
   """ Required : 
   custNum
   orderNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  CustNum  """  
      self.orderNum:int = obj["orderNum"]
      """  OrderNum  """  
      pass

class GetListOrderHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderHistTableset] = obj["returnObj"]
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

