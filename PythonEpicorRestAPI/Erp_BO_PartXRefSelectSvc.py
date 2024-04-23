import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartXRefSelectSvc
# Description: PartXRefSelect Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartXRefSelectSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartXRefSelectSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetXRefParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetXRefParts
   OperationID: GetXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartXRefSelectSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PartXRefSelectResultsRow:
   def __init__(self, obj):
      self.XRefPartNum:str = obj["XRefPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.Type:str = obj["Type"]
      self.UOM:str = obj["UOM"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendorID:str = obj["VendorID"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.VendorName:str = obj["VendorName"]
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name  """  
      self.RowGUID:str = obj["RowGUID"]
      self.DispID:str = obj["DispID"]
      self.DispName:str = obj["DispName"]
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartXRefSelectTableset:
   def __init__(self, obj):
      self.PartXRefSelectResults:list[Erp_Tablesets_PartXRefSelectResultsRow] = obj["PartXRefSelectResults"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetXRefParts_input:
   """ Required : 
   ipPartNum
   ipCustNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ipCustNum:int = obj["ipCustNum"]
      """  Customer Number  """  
      pass

class GetXRefParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartXRefSelectTableset] = obj["returnObj"]
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

