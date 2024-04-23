import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialNumberSearchSvc
# Description: This process uses 3 tokens to generate a whereclause which is
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetNewSerialNumberSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialNumberSearch
   OperationID: GetNewSerialNumberSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialNumberSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNumberSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SerialNumberSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method _SerialNumberSearch
   Description: To be whenever a search on the serial table is required. Depending on the
contents of the tokens, a specific where clause is determined and returned.
            
ProcessToken contains the Sonoma process name.
GenericToken1 List of field names and corresponding values ~ delimited.
The format of each value pair is (field name)=(value).
GenericToken2 not used.
            
The following is a list of processes supported by this object.
xae65-jb            SerialNoAssign
ProcessToken    = SerialNoAssign
GenericToken1   = SortBy
xae65-ct            Customer transfer                       lib/brwsn
ProcessToken    = SerialNoAssign
GenericToken1   = SortBy
ime20-dg            Issues and returns                      xae65-mi
ProcessToken    = IssuesandReturns
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime10-dg            Receipts from manufacturing             xae65-mi
ProcessToken    = ReceiptsfromManufacturing
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime30-dg            Inventory transfers                     xae65-mi
ProcessToken    = InventoryTransfer
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime30-dg-vs         Inventory transfers                     xae65-mi
ProcessToken    = InventoryTransfer
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime40-qa            Inventory quantity adjust               xae65-mi
ProcessToken    = InventoryQtyAdj
GenericToken1   = TranType ~ TranQty ~ WareHseCode
jce10-gj            Processing of jobs                      xae65-mi
ProcessToken    = JobProcessing
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
jce10-js            Job split                               xae65-mi
ProcessToken    = JobSplit
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
mse30-dg            Receive from plant                      xae65-mi
ProcessToken    = PlantReceipt
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae10-in            NonConformance Entry from Inventory     xae65-qr
ProcessToken    = NonConf
GenericToken1   = TranType ~ TranQty ~ WareHseCode
qae10-ma            NonConformance Entry from Job Material  xae65-qr
ProcessToken    = NonConf
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae10-op            NonConformance Entry from Operation     xae65-qr
ProcessToken    = NonConf
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-iv            DMR to stock/inventory                  xae65-mi
ProcessToken    = DMRtoInventory
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-jm            DMR to job material                     xae65-mi
ProcessToken    = DMRtoJobMtl
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-op            DMR to job operation                    xae65-mi
ProcessToken    = DMRtoJobOper
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-rm            Rejecte material from DMR               xae65-mi
ProcessToken    = RejectfromDMR
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
xa/snleavetrig.i    SN select from receipts                 xae65-pm
ProcessToken    = Receipts
GenericToken1   = null
xa/snleavetrig.i    SN select from shipments                xae65-sh
ProcessToken    = Shipment
GenericToken1   = ShipFrom
xa/snleavetrig.i    SN select from transfer orders          xae65-to
ProcessToken    = TransferOrder
GenericToken1   = ShipFrom
xa/xam65-dg         Serial Number Maintenance
Process Token   = SNMaint
GenericToken1   = SortBy
om/ome80-dt         RMA detail maintentance                 xae65-rm
ProcessToken    = RMADTL
GenericToken1   = RMANum ~ RMALine
om/ome80-re         RMA Receipt maintenance                 xae65-rm
ProcessToken    = RMARCPT
GenericToken1   = RMANum ~ RMALine ~ RMAReceipt
om/ome81-rd         RMA Disposition                         xae65-rm
ProcessToken    = RMADISP
GenericToken1   = RMANum ~ RMALine ~ RMAReceipt ~ RMADisp
xa/xae65-sc         Service Contract Maintenance
Process Token   = ServiceContract
GenericToken1   = Null
SubConShipEntry     Subcontract Shipment Entry (NEW for 8.0)
Process Token = SubConShipment
GenericToken1 = null
Receipt Entry       Receipt Entry - (for Job Subcontract) (NEW for 8.0)
Process Token = SubConReceipts
GenericToken1 = null
   OperationID: _SerialNumberSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/_SerialNumberSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_SerialNumberSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_SerialNumberSearchRow:
   def __init__(self, obj):
      self.ProcessToken:str = obj["ProcessToken"]
      """  Token reserved for the process ID  """  
      self.GenericToken1:str = obj["GenericToken1"]
      """  1st generic token.  """  
      self.GenericToken2:str = obj["GenericToken2"]
      """  2nd generic token  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Returns where clause based on input tokens.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNumberSearchTableset:
   def __init__(self, obj):
      self.SerialNumberSearch:list[Erp_Tablesets_SerialNumberSearchRow] = obj["SerialNumberSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetNewSerialNumberSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSearchTableset] = obj["ds"]
      pass

class GetNewSerialNumberSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSearchTableset] = obj["ds"]
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

class _SerialNumberSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSearchTableset] = obj["ds"]
      pass

class _SerialNumberSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

