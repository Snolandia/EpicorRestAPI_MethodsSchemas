import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LotTraceSvc
# Description: Service to perform traces on part/lots
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_PerformTrace(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformTrace
   Description: Performs a trace on the specified part/lot
   OperationID: PerformTrace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformTrace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformTrace_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_LotTraceDtlRow:
   def __init__(self, obj):
      self.TraceMode:str = obj["TraceMode"]
      """   Code that indicates if data was generated for Forward or Reverse mode:

F = Forward / R = Reverse  """  
      self.Type:str = obj["Type"]
      """   Code that indicates what type of demand/supply record involves:

O = Sales Order               
T = Transfer Order
M = Job Mtl
P = Purchase Order  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum from related PartTran  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Qty from related PartTran  """  
      self.TranUOM:str = obj["TranUOM"]
      """  Transaction Qty Unit of Measure from related PartTran  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date from related PartTran  """  
      self.TranPartNum:str = obj["TranPartNum"]
      """  PartNum from related PartTran  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number when type is Sales Order  """  
      self.CustID:str = obj["CustID"]
      """  ID of related customer when type is Sales Order  """  
      self.CustName:str = obj["CustName"]
      """  Name of related customer when type is Sales Order  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of related material when type is JobMtl  """  
      self.AsmSeq:int = obj["AsmSeq"]
      """  Assembly Seq of related material when type is JobMtl  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Seq of related material when type is JobMtl  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the produced part from related job when type is JobMtl  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum of the produced part from related job when type is JobMtl  """  
      self.LotDesc:str = obj["LotDesc"]
      """  PartLotDescription of the produced part from related job when type is JobMtl  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Num when type is Transfer Order  """  
      self.TFSite:str = obj["TFSite"]
      """   To Site when type is Transfer Order and mode is Forward
From Site when type is Transfer Order and mode is Reverse  """  
      self.ShipDate:str = obj["ShipDate"]
      """   Ship Date from Customer Shipment when type is Sales Order
Ship Date from Transfer Order when type is Transfer Order  """  
      self.IssueDate:str = obj["IssueDate"]
      """   Date parent material was issued when mode is Forward
Date material was issued to the parent when mode is Reverse  """  
      self.OrderDate:str = obj["OrderDate"]
      """   Order Date from Sales Order when type is Sales Order
Order Date from Transfer Order when type is Transfer Order
Order Date from Purchase Order when type is Purchase Order  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order Number when type is Purchase Order  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Packing Slip Number from Receipt when type is Purchase Order  """  
      self.SupplierID:str = obj["SupplierID"]
      """  Supplier ID from Supplier when type is Purchase Order  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name from Supplier when type is Purchase Order  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID from PartTran  """  
      self.TypeDesc:str = obj["TypeDesc"]
      self.TraceModeDesc:str = obj["TraceModeDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The parent PartNum of this row in the hierarchy of manufactured part/lots  """  
      self.ParentLotNum:str = obj["ParentLotNum"]
      """  The parent LogNum of this row in the hierarchy of manufactured part/lots  """  
      self.HideOnNode:str = obj["HideOnNode"]
      """  Default is blank / "R" for hide on root node  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LotTraceTableset:
   def __init__(self, obj):
      self.LotTraceDtl:list[Erp_Tablesets_LotTraceDtlRow] = obj["LotTraceDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class PerformTrace_input:
   """ Required : 
   traceDirection
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.traceDirection:str = obj["traceDirection"]
      """  Direction to trace. F = Forward / R = Reverse (required)  """  
      self.partNum:str = obj["partNum"]
      """  Part to trace (required)  """  
      self.lotNum:str = obj["lotNum"]
      """  Lot to trace (required)  """  
      pass

class PerformTrace_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LotTraceTableset] = obj["returnObj"]
      pass

