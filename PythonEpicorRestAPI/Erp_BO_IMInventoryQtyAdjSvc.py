import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMInventoryQtyAdjSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMInventoryQtyAdjSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMInventoryQtyAdjSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_SetInventoryQtyAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetInventoryQtyAdj
   Description: Performs an inventory adjustment
   OperationID: SetInventoryQtyAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMInventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_IMInventoryQtyAdjRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the inventory to adjust is located  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the inventory to adjust is located  """  
      self.AdjustQuantity:int = obj["AdjustQuantity"]
      """  The quantity in part base UOM to adjust. Negative amounts allowed.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode for Qty Adjustment - must be ReasonType = "M"  """  
      self.LotNum:str = obj["LotNum"]
      """  The lot number to adjust. Can only be specified for lot tracked parts.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum of the part to adjust.  """  
      self.Plant:str = obj["Plant"]
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to an Epicor FSA transaction  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Used by Epicor FSA  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Used by Epicor FSA  """  
      self.CallCode:str = obj["CallCode"]
      """  Used by Epicor FSA  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  FSA ContractNum  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PCID:str = obj["PCID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMInventoryQtyAdjTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMInventoryQtyAdj:list[Erp_Tablesets_IMInventoryQtyAdjRow] = obj["IMInventoryQtyAdj"]
      self.IMSelectedSerialNumbers:list[Erp_Tablesets_IMSelectedSerialNumbersRow] = obj["IMSelectedSerialNumbers"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMSelectedSerialNumbersRow:
   def __init__(self, obj):
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber to select  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of IntQueInOut record  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
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

class SetInventoryQtyAdj_input:
   """ Required : 
   ds
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IMInventoryQtyAdjTableset] = obj["ds"]
      self.company:str = obj["company"]
      """  Company ID  """  
      self.extSystemID:str = obj["extSystemID"]
      """  External System ID  """  
      self.transferMethod:str = obj["transferMethod"]
      """  Transfer Method  """  
      self.extCompanyID:str = obj["extCompanyID"]
      """  External Company ID  """  
      pass

class SetInventoryQtyAdj_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

