import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CreateIDNumbersSvc
# Description: Service for generating ID Numbers
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCreateIDNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCreateIDNumbersParams
   OperationID: GetCreateIDNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCreateIDNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreateIDNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingFormatID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingFormatID
   Description: Call this method when the value of Epicor.Mfg.BO.CreateIDNumbersParams.FormatID is changing.
   OperationID: OnChangingFormatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingFormatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFormatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialNumber
   Description: Validates the entered Serial
   OperationID: ValidateSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetIDNumberShipmentStatusNoClear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetIDNumberShipmentStatusNoClear
   Description: Public method to set ID Numbers as shipped or not and do not clear ds at the end.
   OperationID: SetIDNumberShipmentStatusNoClear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetIDNumberShipmentStatusNoClear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIDNumberShipmentStatusNoClear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetIDNumberShipmentStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetIDNumberShipmentStatus
   Description: Public method to set ID Numbers as shipped or not.
   OperationID: SetIDNumberShipmentStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetIDNumberShipmentStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIDNumberShipmentStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignSerialsToIDNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignSerialsToIDNumbers
   Description: Public method to assign serials to ID Numbers.
   OperationID: AssignSerialsToIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignSerialsToIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignSerialsToIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignSerialandSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignSerialandSetID
   Description: Method covering existing functionality in to a single method - AssignSerialsToIDNumbers, and SetIDNumberShipmentStatusNoClear
   OperationID: AssignSerialandSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignSerialandSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignSerialandSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateIDNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateIDNumbers
   Description: Public method to create ID Numbers.
   OperationID: CreateIDNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistIDFormat(epicorHeaders = None):
   """  
   Summary: Invoke method ExistIDFormat
   Description: Public method to check id ID Format Exists.
   OperationID: ExistIDFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistIDFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AssignSerialandSetID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

class AssignSerialandSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignSerialsToIDNumbers_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

class AssignSerialsToIDNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateIDNumbers_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersParamsTableset] = obj["ds"]
      pass

class CreateIDNumbers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CreateIDNumbersParamsRow:
   def __init__(self, obj):
      self.FormatID:str = obj["FormatID"]
      self.PartNum:str = obj["PartNum"]
      self.Quantity:int = obj["Quantity"]
      self.SourceRowID:str = obj["SourceRowID"]
      self.AssignedQty:int = obj["AssignedQty"]
      self.BinNum:str = obj["BinNum"]
      self.Company:str = obj["Company"]
      self.EnableIDAddButton:bool = obj["EnableIDAddButton"]
      self.IDNumberSample:str = obj["IDNumberSample"]
      self.IDStatus:str = obj["IDStatus"]
      self.IsSystemGenerated:bool = obj["IsSystemGenerated"]
      self.JobNum:str = obj["JobNum"]
      self.LotNum:str = obj["LotNum"]
      self.NumberSeq:int = obj["NumberSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.QtyToAdd:int = obj["QtyToAdd"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.IsFullNum:bool = obj["IsFullNum"]
      """  Bool indicating if this manailly entered full ID number  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreateIDNumbersParamsTableset:
   def __init__(self, obj):
      self.CreateIDNumbersParams:list[Erp_Tablesets_CreateIDNumbersParamsRow] = obj["CreateIDNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CreateIDNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.IDNumber:str = obj["IDNumber"]
      self.JobNum:str = obj["JobNum"]
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.PartNum:str = obj["PartNum"]
      self.SeqNum:int = obj["SeqNum"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.SourceRowID:str = obj["SourceRowID"]
      self.TranType:str = obj["TranType"]
      self.BinNum:str = obj["BinNum"]
      self.LotNum:str = obj["LotNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.Selected:bool = obj["Selected"]
      self.Status:str = obj["Status"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreateIDNumbersTableset:
   def __init__(self, obj):
      self.CreateIDNumbers:list[Erp_Tablesets_CreateIDNumbersRow] = obj["CreateIDNumbers"]
      self.CreateIDNumbersParams:list[Erp_Tablesets_CreateIDNumbersParamsRow] = obj["CreateIDNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistIDFormat_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetCreateIDNumbersParams_input:
   """ Required : 
   ipPartNum
   ipQuantity
   ipJobNum
   ipFormatID
   ipIDStatus
   ipPackNum
   ipPackLine
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  ipPartNum  """  
      self.ipQuantity:int = obj["ipQuantity"]
      """  ipQuantity  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  ipJobNum  """  
      self.ipFormatID:str = obj["ipFormatID"]
      """  ipJobNum  """  
      self.ipIDStatus:str = obj["ipIDStatus"]
      """  ipIDStatus - either WIP or SHIPPED  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  ipPackLine  """  
      pass

class GetCreateIDNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["returnObj"]
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

class OnChangingFormatID_input:
   """ Required : 
   formatID
   """  
   def __init__(self, obj):
      self.formatID:str = obj["formatID"]
      """  Propose FormatID value.  """  
      pass

class OnChangingFormatID_output:
   def __init__(self, obj):
      pass

class SetIDNumberShipmentStatusNoClear_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

class SetIDNumberShipmentStatusNoClear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetIDNumberShipmentStatus_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

class SetIDNumberShipmentStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSerialNumber_input:
   """ Required : 
   ds
   SerialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreateIDNumbersTableset] = obj["ds"]
      self.SerialNumber:str = obj["SerialNumber"]
      """  Proposed Serial number to validate  """  
      pass

class ValidateSerialNumber_output:
   def __init__(self, obj):
      pass

