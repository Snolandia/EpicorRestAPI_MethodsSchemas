import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SplitMergeUOMSvc
# Description: SplitMergeUOM Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CalculateRemainQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateRemainQty
   Description: Calculates The Remaining Qty
   OperationID: CalculateRemainQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateRemainQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateRemainQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSplitMergeHeadData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSplitMergeHeadData
   Description: Gets the default values for the ttSMHdr data table based on the part
number entered.
   OperationID: GetSplitMergeHeadData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSplitMergeHeadData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSplitMergeHeadData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNum
   Description: Used to verify if the selected Bin is valid for the selected warehouse
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNum
   Description: Used to default the Lot Number when the BinNum has been changed
   OperationID: OnChangeLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProcType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProcType
   Description: Used to create the Split or Merge Records
   OperationID: OnChangeProcType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProcType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuantity
   Description: Used to verify that quantity to split or merge
   OperationID: OnChangeQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUOM
   Description: Used to return a list of valid UOM to process the split or merge
   OperationID: OnChangeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWarehouse
   Description: Used to verify that selected warehouse is valid for the
part and current plant and to default the Bin and Lot Number when the Warehouse has been changed
   OperationID: OnChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessType
   Description: Runs the Split or Merge Process
   OperationID: ProcessType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: Negative inventory test
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshOnHandQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshOnHandQty
   Description: Update OnHandQty after splitting/merging the Quantity
   OperationID: RefreshOnHandQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshOnHandQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOnHandQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CalculateRemainQty_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class CalculateRemainQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_SMDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.Quantity:int = obj["Quantity"]
      self.UOM:str = obj["UOM"]
      self.UOMDescription:str = obj["UOMDescription"]
      self.ConvFactor:int = obj["ConvFactor"]
      self.ConvFactorUOM:str = obj["ConvFactorUOM"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity already allocated  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SMHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.ProcessType:str = obj["ProcessType"]
      """  S=Split; M=Merge  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.Quantity:int = obj["Quantity"]
      self.UOM:str = obj["UOM"]
      self.TransDate:str = obj["TransDate"]
      self.BinDescription:str = obj["BinDescription"]
      self.LotDescription:str = obj["LotDescription"]
      self.PartDescription:str = obj["PartDescription"]
      self.UOMDescription:str = obj["UOMDescription"]
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      self.EnableLot:bool = obj["EnableLot"]
      self.OnHandUOM:str = obj["OnHandUOM"]
      self.OnHandUOMDesc:str = obj["OnHandUOMDesc"]
      self.RemainQty:int = obj["RemainQty"]
      self.RemainUOM:str = obj["RemainUOM"]
      self.TransQty:int = obj["TransQty"]
      self.TransUOM:str = obj["TransUOM"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  Quantity already allocated for the Part to be split/merged  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SplitMergeUOMTableset:
   def __init__(self, obj):
      self.SMHdr:list[Erp_Tablesets_SMHdrRow] = obj["SMHdr"]
      self.SMDtl:list[Erp_Tablesets_SMDtlRow] = obj["SMDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetSplitMergeHeadData_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class GetSplitMergeHeadData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
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

class NegativeInventoryTest_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.negQtyAction:str = obj["parameters"]
      self.negInvMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBinNum_input:
   """ Required : 
   partNum
   binNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.binNum:str = obj["binNum"]
      """  Bin Number.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLotNum_input:
   """ Required : 
   partNum
   lotNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.lotNum:str = obj["lotNum"]
      """  Lot Number.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeProcType_input:
   """ Required : 
   partNum
   processType
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.processType:str = obj["processType"]
      """  Process Type.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeProcType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuantity_input:
   """ Required : 
   partNum
   dQuantity
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.dQuantity:int = obj["dQuantity"]
      """  Quantity.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUOM_input:
   """ Required : 
   partNum
   uOMCode
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.uOMCode:str = obj["uOMCode"]
      """  Unit of Messure.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWarehouse_input:
   """ Required : 
   partNum
   whseCode
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.whseCode:str = obj["whseCode"]
      """  Warehouse Code.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class OnChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessType_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to split or merge.  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class ProcessType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshOnHandQty_input:
   """ Required : 
   type
   ds
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  The process type. S = splitting, M = merging  """  
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

class RefreshOnHandQty_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SplitMergeUOMTableset] = obj["ds"]
      pass

      """  output parameters  """  

