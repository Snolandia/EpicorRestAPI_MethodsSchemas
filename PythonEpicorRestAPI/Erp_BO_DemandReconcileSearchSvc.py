import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandReconcileSearchSvc
# Description: List of Demand Reconciliation records by Demand Contract Name.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: List of Demand Reconciliation records by Demand Contract Name.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_DemandReconcileSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this reconcilliation is for.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The demand contract this reconcilliation is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the reconcilliation is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PONum:str = obj["PONum"]
      """  The customers Purchase Order Number the reconcilliation is for.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Contains the Ship To Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.ShipToCustomerName:str = obj["ShipToCustomerName"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo the reconcilliation is for.  """  
      self.ShipToName:str = obj["ShipToName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileSearchTableset:
   def __init__(self, obj):
      self.DemandReconcileSearch:list[Erp_Tablesets_DemandReconcileSearchRow] = obj["DemandReconcileSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseDemandReconcileSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandReconcileSearch:str = obj["whereClauseDemandReconcileSearch"]
      """  Where condition  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned. 0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandReconcileSearchTableset] = obj["returnObj"]
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

