import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APAgingTrackerSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GenerateTrackerAgingSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTrackerAgingSite
   Description: This method should be called to populate the dataset for the AP Aging Tracker.
   OperationID: GenerateTrackerAgingSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTrackerAgingSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTrackerAgingSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateTracker
   Description: This method should be called to populate the dataset for the AP Aging Tracker.
   OperationID: GenerateTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_APAgingTotalsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CurNumInv:int = obj["CurNumInv"]
      self.InvTotal:int = obj["InvTotal"]
      self.PaidYtd:int = obj["PaidYtd"]
      self.YTDNumInv:int = obj["YTDNumInv"]
      self.PYTDNumInv:int = obj["PYTDNumInv"]
      self.PYTDPurchased:int = obj["PYTDPurchased"]
      self.PYTDAvgInvAmt:int = obj["PYTDAvgInvAmt"]
      self.YTDPurchased:int = obj["YTDPurchased"]
      self.YTDAvgInvAmt:int = obj["YTDAvgInvAmt"]
      self.LastPayment:int = obj["LastPayment"]
      self.LastPaymentDate:str = obj["LastPaymentDate"]
      self.CurDueAmt:int = obj["CurDueAmt"]
      self.CurDuePct:int = obj["CurDuePct"]
      self.Due30Amt:int = obj["Due30Amt"]
      self.Due30Pct:int = obj["Due30Pct"]
      self.Due60Amt:int = obj["Due60Amt"]
      self.Due60Pct:int = obj["Due60Pct"]
      self.Due90Amt:int = obj["Due90Amt"]
      self.Due90Pct:int = obj["Due90Pct"]
      self.Due120Amt:int = obj["Due120Amt"]
      self.Due120Pct:int = obj["Due120Pct"]
      self.FutureDueAmt:int = obj["FutureDueAmt"]
      self.FutureDuePct:int = obj["FutureDuePct"]
      self.CurInvAmt:int = obj["CurInvAmt"]
      self.CurInvPct:int = obj["CurInvPct"]
      self.Inv30Amt:int = obj["Inv30Amt"]
      self.Inv30Pct:int = obj["Inv30Pct"]
      self.Inv60Amt:int = obj["Inv60Amt"]
      self.Inv60Pct:int = obj["Inv60Pct"]
      self.Inv90Amt:int = obj["Inv90Amt"]
      self.Inv90Pct:int = obj["Inv90Pct"]
      self.Inv120Amt:int = obj["Inv120Amt"]
      self.FutureInvAmt:int = obj["FutureInvAmt"]
      self.FutureInvPct:int = obj["FutureInvPct"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendorName:str = obj["VendorName"]
      self.Inv120Pct:int = obj["Inv120Pct"]
      self.ColHead1:str = obj["ColHead1"]
      """  Column 1 heading (Current)  """  
      self.ColHead2:str = obj["ColHead2"]
      """  Column 2 heading (Over 30)  """  
      self.ColHead3:str = obj["ColHead3"]
      """  Column 3 heading (Over 60)  """  
      self.ColHead4:str = obj["ColHead4"]
      """  Column 4 heading (Over 90)  """  
      self.ColHead5:str = obj["ColHead5"]
      """  Column 5 heading (Over 120)  """  
      self.ColHead6:str = obj["ColHead6"]
      """  Column 6 heading (Future)  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APAgingTrackerTableset:
   def __init__(self, obj):
      self.APAgingTotals:list[Erp_Tablesets_APAgingTotalsRow] = obj["APAgingTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateTrackerAgingSite_input:
   """ Required : 
   supplierID
   plant
   """  
   def __init__(self, obj):
      self.supplierID:str = obj["supplierID"]
      """  Supplier ID.  """  
      self.plant:str = obj["plant"]
      """  Supplier ID.  """  
      pass

class GenerateTrackerAgingSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APAgingTrackerTableset] = obj["returnObj"]
      pass

class GenerateTracker_input:
   """ Required : 
   supplierID
   """  
   def __init__(self, obj):
      self.supplierID:str = obj["supplierID"]
      """  Supplier ID.  """  
      pass

class GenerateTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APAgingTrackerTableset] = obj["returnObj"]
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

