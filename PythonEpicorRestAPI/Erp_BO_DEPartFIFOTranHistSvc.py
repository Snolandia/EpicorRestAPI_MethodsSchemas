import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DEPartFIFOTranHistSvc
# Description: Germany Part FIFO Transaction History BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetPartFIFOTranHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFIFOTranHistory
   Description: Retrieve Part FIFO Transaction History for specific Part and Date interval.
The Running Balance is calculated.
   OperationID: GetPartFIFOTranHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFIFOTranHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFIFOTranHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_DEPartFIFOTranHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part Description  """  
      self.PartIUM:str = obj["PartIUM"]
      """  PartIUM  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.FIFODate:str = obj["FIFODate"]
      """  FIFO Date  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  FIFO Seq  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  FIFO Sub Seq  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """  FIFO Action  """  
      self.TranQty:int = obj["TranQty"]
      """  Tran Qty  """  
      self.UnitCost:int = obj["UnitCost"]
      """  Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Ext Cost  """  
      self.OpenQty:int = obj["OpenQty"]
      """  Total Part Quantity before transaction.  """  
      self.OpenExtCost:int = obj["OpenExtCost"]
      """  Total Part Ext Cost before transaction.  """  
      self.CloseQty:int = obj["CloseQty"]
      """  Total Part Quantity after transaction.  """  
      self.CloseExtCost:int = obj["CloseExtCost"]
      """  Total Part Ext Cost after transaction.  """  
      self.PONum:int = obj["PONum"]
      """  PO Number  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Packing Slip  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number  """  
      self.PackType:str = obj["PackType"]
      """  Pack Type  """  
      self.TranReference:str = obj["TranReference"]
      """  Trans Reference  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse Code  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin Num  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.SysEntryDT:str = obj["SysEntryDT"]
      """  System Entry Date and Time  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DEPartFIFOTranHistTableset:
   def __init__(self, obj):
      self.DEPartFIFOTranHist:list[Erp_Tablesets_DEPartFIFOTranHistRow] = obj["DEPartFIFOTranHist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetPartFIFOTranHistory_input:
   """ Required : 
   partNum
   startDate
   endDate
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part  """  
      self.startDate:str = obj["startDate"]
      """  Start Date of the interval  """  
      self.endDate:str = obj["endDate"]
      """  End Date of the interval  """  
      pass

class GetPartFIFOTranHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DEPartFIFOTranHistTableset] = obj["returnObj"]
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

