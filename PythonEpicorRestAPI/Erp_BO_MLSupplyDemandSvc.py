import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MLSupplyDemandSvc
# Description: Material Supply Demand file.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_UpdateAttributeSetIDFromRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSupplyDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSupplyDemand
   Description: This method returns the pegging information for the selected supply/demand/part.
No maintenance is allowed in this object so there is only this one method.
   OperationID: GetSupplyDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplyDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplyDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MLSupplyDemandSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_MLSupplyDemandTableset:
   def __init__(self, obj):
      self.PegRequest:list[Erp_Tablesets_PegRequestRow] = obj["PegRequest"]
      self.PegDemand:list[Erp_Tablesets_PegDemandRow] = obj["PegDemand"]
      self.PegDmdPart:list[Erp_Tablesets_PegDmdPartRow] = obj["PegDmdPart"]
      self.PegMtl:list[Erp_Tablesets_PegMtlRow] = obj["PegMtl"]
      self.PegSupply:list[Erp_Tablesets_PegSupplyRow] = obj["PegSupply"]
      self.PegDmdIndented:list[Erp_Tablesets_PegDmdIndentedRow] = obj["PegDmdIndented"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PegDemandRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Type:str = obj["Type"]
      self.Quantity:int = obj["Quantity"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.DueDate:str = obj["DueDate"]
      self.SupplyDate:str = obj["SupplyDate"]
      self.Warehouse:str = obj["Warehouse"]
      self.Plant:str = obj["Plant"]
      self.DmdSeq:int = obj["DmdSeq"]
      """  The demand sequence number.  """  
      self.ParentDmd:int = obj["ParentDmd"]
      """  Sequence number of the Parent Demand  """  
      self.SupplyType:str = obj["SupplyType"]
      self.SupKey1:str = obj["SupKey1"]
      self.SupKey2:str = obj["SupKey2"]
      self.SupKey3:str = obj["SupKey3"]
      self.DemandQty:int = obj["DemandQty"]
      self.AsmSeq:int = obj["AsmSeq"]
      self.ParentAsm:int = obj["ParentAsm"]
      self.JobReference:str = obj["JobReference"]
      self.TOReference:str = obj["TOReference"]
      self.SOReference:int = obj["SOReference"]
      self.WhseReference:str = obj["WhseReference"]
      self.POReference:int = obj["POReference"]
      self.TypeCode:str = obj["TypeCode"]
      """  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  """  
      self.Reference:str = obj["Reference"]
      """  Contains the reference regardless of what type.  """  
      self.Level:int = obj["Level"]
      """  Current Level  """  
      self.ParentKey1:str = obj["ParentKey1"]
      self.ParentKey2:str = obj["ParentKey2"]
      self.ParentKey3:str = obj["ParentKey3"]
      self.POSugReference:int = obj["POSugReference"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity UOM  """  
      self.ConsumedQtyUOM:str = obj["ConsumedQtyUOM"]
      """  ConsumedQty UOM  """  
      self.DemandQtyUOM:str = obj["DemandQtyUOM"]
      """  DemandQty UOM  """  
      self.LinkPart:str = obj["LinkPart"]
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.RowIdent:str = obj["RowIdent"]
      """  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of values in set  """  
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PegDmdIndentedRow:
   def __init__(self, obj):
      self.Level:int = obj["Level"]
      """  Current level  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.PartDesc:str = obj["PartDesc"]
      """  Part Description  """  
      self.QtyRequired:int = obj["QtyRequired"]
      """  Quantity Required  """  
      self.MtlType:str = obj["MtlType"]
      """  Manufactured, Purchased, or Transferred  """  
      self.PartNumIndented:str = obj["PartNumIndented"]
      """  Part Number prefixed by dots  """  
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.ParentKey1:str = obj["ParentKey1"]
      self.ParentKey2:str = obj["ParentKey2"]
      self.ParentKey3:str = obj["ParentKey3"]
      self.PeggedQty:int = obj["PeggedQty"]
      self.SubAssy:bool = obj["SubAssy"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.ConsumedQtyUOM:str = obj["ConsumedQtyUOM"]
      """  ConsumedQty UOM  """  
      self.PeggedQtyUOM:str = obj["PeggedQtyUOM"]
      """  PeggedQty UOM  """  
      self.QtyRequiredUOM:str = obj["QtyRequiredUOM"]
      """  QtyRequired UOM  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of values in set  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PegDmdPartRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.Key1:str = obj["Key1"]
      """  Linked to the PegDemand.Key1  """  
      self.Key2:str = obj["Key2"]
      """  Linked to the PegDemand.Key2  """  
      self.Key3:str = obj["Key3"]
      """  Linked to the PegDemand.Key3  """  
      self.Type:str = obj["Type"]
      self.Quantity:int = obj["Quantity"]
      self.PartDesc:str = obj["PartDesc"]
      self.DueDate:str = obj["DueDate"]
      self.SupplyDate:str = obj["SupplyDate"]
      self.Warehouse:str = obj["Warehouse"]
      self.Plant:str = obj["Plant"]
      self.SeqNum:int = obj["SeqNum"]
      self.PartNum:str = obj["PartNum"]
      self.DmdSeq:int = obj["DmdSeq"]
      """  Sequence number of the associated Demand  """  
      self.SupKey1:str = obj["SupKey1"]
      """  Key field 1 of the Supply record.  """  
      self.SupKey2:str = obj["SupKey2"]
      """  Key field 2 of the Supply record.  """  
      self.SupKey3:str = obj["SupKey3"]
      """  Key field 3 of the Supply record.  """  
      self.DemandQty:int = obj["DemandQty"]
      self.JobReference:str = obj["JobReference"]
      self.TOReference:str = obj["TOReference"]
      self.SOReference:int = obj["SOReference"]
      self.WhseReference:str = obj["WhseReference"]
      self.POReference:int = obj["POReference"]
      self.TypeCode:str = obj["TypeCode"]
      """  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  """  
      self.Reference:str = obj["Reference"]
      """  Contains the reference regardless of what type.  """  
      self.Level:int = obj["Level"]
      """  Current Level  """  
      self.POSugReference:int = obj["POSugReference"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.ConsumedQtyUOM:str = obj["ConsumedQtyUOM"]
      """  ConsumedQty UOM  """  
      self.DemandQtyUOM:str = obj["DemandQtyUOM"]
      """  DemandQty UOM  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity UOM  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.RowIdent:str = obj["RowIdent"]
      """  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of values in set  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PegMtlRow:
   def __init__(self, obj):
      self.LineNum:int = obj["LineNum"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.Type:str = obj["Type"]
      self.Quantity:int = obj["Quantity"]
      self.DueDate:str = obj["DueDate"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Name:str = obj["Name"]
      self.LinkID:int = obj["LinkID"]
      self.SupKey1:str = obj["SupKey1"]
      self.SupKey2:str = obj["SupKey2"]
      self.SupKey3:str = obj["SupKey3"]
      self.DemandQty:int = obj["DemandQty"]
      self.JobReference:str = obj["JobReference"]
      self.TOReference:str = obj["TOReference"]
      self.SOReference:int = obj["SOReference"]
      self.WhseReference:str = obj["WhseReference"]
      self.POReference:int = obj["POReference"]
      self.TypeCode:str = obj["TypeCode"]
      """  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  """  
      self.Reference:str = obj["Reference"]
      """  Contains the reference regardless of what type.  """  
      self.Warehouse:str = obj["Warehouse"]
      self.WhseRefDesc:str = obj["WhseRefDesc"]
      self.POSugReference:int = obj["POSugReference"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.PeggedQty:int = obj["PeggedQty"]
      self.ConsumedQtyUOM:str = obj["ConsumedQtyUOM"]
      """  ConsumedQty UOM  """  
      self.DemandQtyUOM:str = obj["DemandQtyUOM"]
      """  DemandQty UOM  """  
      self.PeggedQtyUOM:str = obj["PeggedQtyUOM"]
      """  PeggedQty UOM  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity UOM  """  
      self.RowIdent:str = obj["RowIdent"]
      """  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of values in set  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PegRequestRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Type:str = obj["Type"]
      self.PartDesc:str = obj["PartDesc"]
      self.Quantity:int = obj["Quantity"]
      self.PartNum:str = obj["PartNum"]
      self.Reference:str = obj["Reference"]
      self.TypeCode:str = obj["TypeCode"]
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity UOM  """  
      self.RowIdent:str = obj["RowIdent"]
      """  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of values in set  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PegSupplyRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Type:str = obj["Type"]
      self.Quantity:int = obj["Quantity"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.DueDate:str = obj["DueDate"]
      self.DemandDate:str = obj["DemandDate"]
      self.Warehouse:str = obj["Warehouse"]
      self.Plant:str = obj["Plant"]
      self.JobReference:str = obj["JobReference"]
      self.TOReference:str = obj["TOReference"]
      self.SOReference:int = obj["SOReference"]
      self.WhseReference:str = obj["WhseReference"]
      self.POReference:int = obj["POReference"]
      self.TypeCode:str = obj["TypeCode"]
      """  "J" = Job   "S" = Sale Order  "W" = Warehouse "F" = Forecast "P" = PO  """  
      self.Reference:str = obj["Reference"]
      """  Contains the reference regardless of what type.  """  
      self.ParentKey1:str = obj["ParentKey1"]
      self.ParentKey2:str = obj["ParentKey2"]
      self.ParentKey3:str = obj["ParentKey3"]
      self.POSugReference:int = obj["POSugReference"]
      self.TreeSort:int = obj["TreeSort"]
      """  external field to the table that just indicates the sort order  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity UOM  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.RowIdent:str = obj["RowIdent"]
      """  Column RowIdent of type string required to emulate the behavior in E9. Not related to SysRowID.  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  The unique identifier of the Dynamic Attribute Set  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetSupplyDemand_input:
   """ Required : 
   key1
   key2
   key3
   key4
   mlType
   attributeSetID
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      """  First unique key  """  
      self.key2:str = obj["key2"]
      """  Second optional key  """  
      self.key3:str = obj["key3"]
      """  Third optional key  """  
      self.key4:str = obj["key4"]
      """  Third optional key  """  
      self.mlType:str = obj["mlType"]
      """  S = Sales Order, P = PO, J = Job, T = Transfer Order, R = Part  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class GetSupplyDemand_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MLSupplyDemandTableset] = obj["returnObj"]
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

class PartsAttributeClassHasRevisionAndIsMRPTracked_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  current Attribute Class ID  """  
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateAttributeSetIDFromRevisionNum_input:
   """ Required : 
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  new revision selected  """  
      pass

class UpdateAttributeSetIDFromRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      self.planningAttributeSetSeq:int = obj["parameters"]
      pass

      """  output parameters  """  

