import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AdjustReturnContainerSvc
# Description: Allows user to adjust in or out returnable containers
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBinNum
   Description: Called when bin num is changed
   OperationID: ChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuantity
   Description: Called when quantity is changed - retrieves, validates and sets reason codes based on negative or positive qty
   OperationID: ChangeQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouse
   Description: Called when quantity is changed - retrieves, validates and sets reason codes based on negative or positive qty
   OperationID: ChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackageControlEnabled(epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackageControlEnabled
   Description: Checks whether Package Control is enabled.
   OperationID: CheckPackageControlEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageControlEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetAdjustReturnContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAdjustReturnContainer
   Description: Gets the default values for the AdjustReturnContainer data table based on the part
number entered.
   OperationID: GetAdjustReturnContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAdjustReturnContainerBrw(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAdjustReturnContainerBrw
   Description: Populates adjust return container inventory on-hand qty dataset when warehouse is selected
   OperationID: GetAdjustReturnContainerBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAdjustReturnContainerBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdjustReturnContainerBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMatchingCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatchingCount
   Description: Gets the number of matches for the given criteria and populates buffer if only one match found.
Can pass one of either PartNum, ShipToPartNum, PkgCode, or both PartNum and PkgCode
   OperationID: GetMatchingCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchingCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchingCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryAllocationsTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryAllocationsTest
   OperationID: NegativeInventoryAllocationsTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryAllocationsTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryAllocationsTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSetAdjustReturnContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSetAdjustReturnContainer
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreSetAdjustReturnContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAdjustReturnContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAdjustReturnContainer
   OperationID: SetAdjustReturnContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBinNum_input:
   """ Required : 
   binNum
   ds
   """  
   def __init__(self, obj):
      self.binNum:str = obj["binNum"]
      """  Proposed value  """  
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

class ChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuantity_input:
   """ Required : 
   qty
   ds
   """  
   def __init__(self, obj):
      self.qty:int = obj["qty"]
      """  Proposed qty  """  
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

class ChangeQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarehouse_input:
   """ Required : 
   warehouseCode
   ds
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      """  Proposed value  """  
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

class ChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackageControlEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if enabled/false if not  """  
      pass

class Erp_Tablesets_AdjustReturnContainerBrwRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On hand quantity  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Non nettable flag  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number  """  
      self.WhseBinDesc:str = obj["WhseBinDesc"]
      """  WareHouse Bin description.  """  
      self.StkUOMCode:str = obj["StkUOMCode"]
      self.StkUOMDesc:str = obj["StkUOMDesc"]
      self.BaseOnHandQty:int = obj["BaseOnHandQty"]
      """  The PartBin.OnHandQty expressed in Part Base UOM  """  
      self.BaseOnHandUOM:str = obj["BaseOnHandUOM"]
      """  Unit of Measure to qualifiy BaseOnHandQty. This is the Part Base UOM.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AdjustReturnContainerBrwTableset:
   def __init__(self, obj):
      self.AdjustReturnContainerBrw:list[Erp_Tablesets_AdjustReturnContainerBrwRow] = obj["AdjustReturnContainerBrw"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AdjustReturnContainerConflictRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.ShipToPartNum:str = obj["ShipToPartNum"]
      self.ShipToPartNumDesc:str = obj["ShipToPartNumDesc"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToSeq:int = obj["ShipToSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AdjustReturnContainerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.BinNum:str = obj["BinNum"]
      self.AdjustQuantity:int = obj["AdjustQuantity"]
      self.ReasonCode:str = obj["ReasonCode"]
      self.Reference:str = obj["Reference"]
      self.UnitOfMeasure:str = obj["UnitOfMeasure"]
      self.TransDate:str = obj["TransDate"]
      self.ReasonType:str = obj["ReasonType"]
      self.AllowNegQty:bool = obj["AllowNegQty"]
      self.StkUOMCode:str = obj["StkUOMCode"]
      self.OnHandUOM:str = obj["OnHandUOM"]
      self.PartDescription:str = obj["PartDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.Plant:str = obj["Plant"]
      self.PartNum:str = obj["PartNum"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ShipToPartNum:str = obj["ShipToPartNum"]
      self.ShipToPartNumDesc:str = obj["ShipToPartNumDesc"]
      self.ShipToSeq:int = obj["ShipToSeq"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AdjustReturnContainerTableset:
   def __init__(self, obj):
      self.AdjustReturnContainer:list[Erp_Tablesets_AdjustReturnContainerRow] = obj["AdjustReturnContainer"]
      self.AdjustReturnContainerConflict:list[Erp_Tablesets_AdjustReturnContainerConflictRow] = obj["AdjustReturnContainerConflict"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAdjustReturnContainerBrw_input:
   """ Required : 
   partNum
   warehouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the adjustment.  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetAdjustReturnContainerBrw_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AdjustReturnContainerBrwTableset] = obj["returnObj"]
      pass

class GetAdjustReturnContainer_input:
   """ Required : 
   partNum
   pkgCode
   shipToSeq
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.pkgCode:str = obj["pkgCode"]
      """  Pkg Code  """  
      self.shipToSeq:int = obj["shipToSeq"]
      """  ShipToSeq from PackingShipTo (optional)  """  
      pass

class GetAdjustReturnContainer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["returnObj"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMatchingCount_input:
   """ Required : 
   partNum
   shipToPartNum
   pkgCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to search against Part  """  
      self.shipToPartNum:str = obj["shipToPartNum"]
      """  Part number to search against ShipToPacking  """  
      self.pkgCode:str = obj["pkgCode"]
      """  PkgCode search against Packing and PackingPlant  """  
      pass

class GetMatchingCount_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.matches:int = obj["parameters"]
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

class NegativeInventoryAllocationsTest_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcPCID
   pcDimCode
   pdDimConvFactor
   ipSellingQuantity
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      pass

class NegativeInventoryAllocationsTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      self.opAllocAction:str = obj["parameters"]
      self.opAllocWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreSetAdjustReturnContainer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

class PreSetAdjustReturnContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class SetAdjustReturnContainer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

class SetAdjustReturnContainer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AdjustReturnContainerTableset] = obj["ds"]
      pass

      """  output parameters  """  

