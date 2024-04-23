import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMSerialNoSvc
# Description: Outbound integration point for SerialNo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckSerialNo
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountSerialNo
   Description: Returns the count of existing IntQueOut records along with the count of updated employees in the database that IntQueOut records have not yet been created for
   OperationID: CountSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllSerialNo
   Description: Generates IntQueOut and IMSerialNo rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNo
   Description: Generates IntQueOut and IMSerialNo rows since the last time this was called and then returns these along with any existing
   OperationID: GetSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSerialNoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckSerialNo_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMSerialNoTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckSerialNo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountSerialNo_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountSerialNo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMSerialNoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MscPackNum:int = obj["MscPackNum"]
      """  Misc Shipment Pack Num if related to a misc shipment  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.MscPackLine:int = obj["MscPackLine"]
      """  Misc Shipment Pack Line if related to a Misc Shipment  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the calculated value of CustID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ShipToName:str = obj["ShipToName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMSerialNoTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMSerialNo:list[Erp_Tablesets_IMSerialNoRow] = obj["IMSerialNo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class GetAllSerialNo_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllSerialNo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMSerialNoTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSerialNo_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetSerialNo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMSerialNoTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

