import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartLotIncludeAttributesSvc
# Description: PartLotDynAttrValueSetView Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRowsLotTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsLotTracker
   OperationID: GetRowsLotTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartLotIncludeAttributesSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PartLotDynAttrValueSetViewRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PartLotDescription:str = obj["PartLotDescription"]
      """  Optional lot number description.  """  
      self.OnHand:bool = obj["OnHand"]
      """  Indicates that there is still some of the lot on hand.  """  
      self.FirstRefDate:str = obj["FirstRefDate"]
      """  Earliest date that the lot was referenced.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the lot was referenced.  """  
      self.LotLaborCost:int = obj["LotLaborCost"]
      """   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.LotBurdenCost:int = obj["LotBurdenCost"]
      """  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  """  
      self.LotMaterialCost:int = obj["LotMaterialCost"]
      """  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotSubContCost:int = obj["LotSubContCost"]
      """  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotMtlBurCost:int = obj["LotMtlBurCost"]
      """  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Determined by setting on Part.AttExpDt if required or tracked.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  """  
      self.Batch:str = obj["Batch"]
      """  Determined by setting on Part.AttBatch if required or tracked.  """  
      self.MfgBatch:str = obj["MfgBatch"]
      """  Determined by setting on Part.AttMfgBatch if required or tracked.  """  
      self.MfgLot:str = obj["MfgLot"]
      """  Determined by setting on Part.AttMfgLot if required or tracked.  """  
      self.HeatNum:str = obj["HeatNum"]
      """  Determined by setting on Part.AttHeat if required or tracked.  """  
      self.FirmWare:str = obj["FirmWare"]
      """  Determined by setting on Part.AttFirmware if required or tracked.  """  
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      """  Determined by setting on Part.AttBeforeDt if required or tracked.  """  
      self.MfgDt:str = obj["MfgDt"]
      """  Determined by setting on Part.AttMfgDt if required or tracked.  """  
      self.CureDt:str = obj["CureDt"]
      """  Determined by setting on Part.AttCureDt if required or tracked.  """  
      self.ExpireDt:str = obj["ExpireDt"]
      """  Expire Date  """  
      self.FIFOLotLaborCost:int = obj["FIFOLotLaborCost"]
      """   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOLotBurdenCost:int = obj["FIFOLotBurdenCost"]
      """  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  """  
      self.FIFOLotMaterialCost:int = obj["FIFOLotMaterialCost"]
      """  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotSubContCost:int = obj["FIFOLotSubContCost"]
      """  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotMtlBurCost:int = obj["FIFOLotMtlBurCost"]
      """  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.CSFLMWComOath:str = obj["CSFLMWComOath"]
      """   Malaysia Localization
LMW Commissioner of Oath's Number  """  
      self.CSFCJ5FormNbr:str = obj["CSFCJ5FormNbr"]
      """   Malaysia Localization
CJ5 Form Number  """  
      self.CSFCJ5Vessel:str = obj["CSFCJ5Vessel"]
      """   Malaysia Localization
CJ5 Vessel Number  """  
      self.CSFCJ5ApvlStart:str = obj["CSFCJ5ApvlStart"]
      """   Malaysia Localization
The start date of CJ5 approved period  """  
      self.CSFCJ5ApvlEnd:str = obj["CSFCJ5ApvlEnd"]
      """   Malaysia Localization
The end date of CJ5 approved period  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXImportLocation:str = obj["MXImportLocation"]
      """  MXImportLocation  """  
      self.MXImportDate:str = obj["MXImportDate"]
      """  MXImportDate  """  
      self.TotalQtyAvg:int = obj["TotalQtyAvg"]
      """  Total OnHand Quantity used specific for Average Costing calculations  """  
      self.ISOrigCountryNum:int = obj["ISOrigCountryNum"]
      """  Country number of the Origin Country (defaults from Part Country of Origin).  """  
      self.DynAttrValueSetAttributeSetID:int = obj["DynAttrValueSetAttributeSetID"]
      """  AttributeSetID associated with the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Description of Attribute Set  """  
      self.DynAttrValueSetRevisionNum:str = obj["DynAttrValueSetRevisionNum"]
      """  Revision Num associated with this Part  """  
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  Attribute Set's short description  """  
      self.PartBinOnhandQty:int = obj["PartBinOnhandQty"]
      """  Total OnhandQty from all bins  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      """  Attribute Class ID associated with the Part  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  IUM associated with Part number  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  SalesUM associated with Part number  """  
      self.ScrLotBurdenCost:int = obj["ScrLotBurdenCost"]
      self.ScrLotLaborCost:int = obj["ScrLotLaborCost"]
      self.ScrLotMaterialCost:int = obj["ScrLotMaterialCost"]
      self.ScrLotMtlBurCost:int = obj["ScrLotMtlBurCost"]
      self.ScrLotSubContCost:int = obj["ScrLotSubContCost"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartLotDynAttrValueSetViewTableset:
   def __init__(self, obj):
      self.PartLotDynAttrValueSetView:list[Erp_Tablesets_PartLotDynAttrValueSetViewRow] = obj["PartLotDynAttrValueSetView"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRowsLotTracker_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsLotTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartLotDynAttrValueSetViewTableset] = obj["returnObj"]
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

