import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartOnHandWhseSvc
# Description: Methods for retrieving on hand quanities
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetPartOnHandWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartOnHandWhse
   Description: Get the Part quantity on hand records from the parameters.
   OperationID: GetPartOnHandWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartOnHandWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartOnHandWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PartBinInfoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part Number. It must be valid in the Part table.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """  Safety quantity is a "purchasing cushion" limit.  """  
      self.KBCode:str = obj["KBCode"]
      """  Uniquely indentifies the record.  """  
      self.KBPONUM:int = obj["KBPONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.KBPOLine:int = obj["KBPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.KBWarehouseCode:str = obj["KBWarehouseCode"]
      """  Kanban Warehouse  """  
      self.KBBinNum:str = obj["KBBinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.KBPlant:str = obj["KBPlant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  """  
      self.KBQty:int = obj["KBQty"]
      """  Indicates the desired minimum on-hand Kanban quantity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.KBActionCode:str = obj["KBActionCode"]
      self.KBActionDesc:str = obj["KBActionDesc"]
      self.MaxQtyUOM:str = obj["MaxQtyUOM"]
      """  Maximum Quantity UOM  """  
      self.MinQtyUOM:str = obj["MinQtyUOM"]
      """  Minimum Quantity UOM  """  
      self.Plant:str = obj["Plant"]
      """  Filled in by BO, not phiscally in database.  """  
      self.PlantOwner:str = obj["PlantOwner"]
      self.SafetyQtyUOM:str = obj["SafetyQtyUOM"]
      """  Safety Quantity UOM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.BinNumNonNettable:bool = obj["BinNumNonNettable"]
      self.KBBinNumDescription:str = obj["KBBinNumDescription"]
      self.KBCodeKBDescription:str = obj["KBCodeKBDescription"]
      self.KBCodeKBActionCode:str = obj["KBCodeKBActionCode"]
      self.KBPlantName:str = obj["KBPlantName"]
      self.KBWarehouseCodeDescription:str = obj["KBWarehouseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOnHandBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.QuantityOnHand:int = obj["QuantityOnHand"]
      self.NonNettable:bool = obj["NonNettable"]
      self.BinDescription:str = obj["BinDescription"]
      self.UnitOfMeasure:str = obj["UnitOfMeasure"]
      self.IsPrimaryBin:str = obj["IsPrimaryBin"]
      self.SeqNum:int = obj["SeqNum"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOnHandWhseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.PrimaryBinNum:str = obj["PrimaryBinNum"]
      self.AllocQty:int = obj["AllocQty"]
      self.IUM:str = obj["IUM"]
      self.QuantityOnHand:int = obj["QuantityOnHand"]
      self.CountedDate:str = obj["CountedDate"]
      self.IsPrimaryWarehouse:str = obj["IsPrimaryWarehouse"]
      self.MultipleUOMs:bool = obj["MultipleUOMs"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOnHandWhseTableset:
   def __init__(self, obj):
      self.PartOnHandWhse:list[Erp_Tablesets_PartOnHandWhseRow] = obj["PartOnHandWhse"]
      self.PartOnHandBin:list[Erp_Tablesets_PartOnHandBinRow] = obj["PartOnHandBin"]
      self.PartBinInfo:list[Erp_Tablesets_PartBinInfoRow] = obj["PartBinInfo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetPartOnHandWhse_input:
   """ Required : 
   cPartNum
   cPlant
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      """  The Part Number  """  
      self.cPlant:str = obj["cPlant"]
      """  The plant  """  
      pass

class GetPartOnHandWhse_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartOnHandWhseTableset] = obj["returnObj"]
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

