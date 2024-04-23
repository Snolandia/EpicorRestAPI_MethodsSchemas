import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SupplierXRefSvc
# Description: Supplier Cross Reference
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierXRefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SupplierXRefSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSupplierXRefParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSupplierXRefParts
   Description: This method gets the XRef information for a given supplier part
   OperationID: GetSupplierXRefParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupplierXRefParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplierXRefParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SupplierXRefSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_SupplierXRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MfgID:str = obj["MfgID"]
      self.MfgName:str = obj["MfgName"]
      self.MfgNum:int = obj["MfgNum"]
      self.MfgPartNum:str = obj["MfgPartNum"]
      self.PartNum:str = obj["PartNum"]
      self.POReference:bool = obj["POReference"]
      self.Receipt:bool = obj["Receipt"]
      self.VendNum:int = obj["VendNum"]
      self.VendPartNum:str = obj["VendPartNum"]
      self.Invoice:bool = obj["Invoice"]
      self.RcvXRefNum:int = obj["RcvXRefNum"]
      """  RcvXRefNum  """  
      self.Inspected:bool = obj["Inspected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SupplierXRefTableset:
   def __init__(self, obj):
      self.SupplierXRef:list[Erp_Tablesets_SupplierXRefRow] = obj["SupplierXRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetSupplierXRefParts_input:
   """ Required : 
   partNum
   vendorNum
   poNum
   poLine
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Receipt Part Number  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Receipt Supplier Number  """  
      self.poNum:int = obj["poNum"]
      """  PO Number  """  
      self.poLine:int = obj["poLine"]
      """  PO Line  """  
      self.purPoint:str = obj["purPoint"]
      """  Purchase Point  """  
      self.packSlip:str = obj["packSlip"]
      """  packing Slip  """  
      self.packLine:int = obj["packLine"]
      """  packing Line  """  
      pass

class GetSupplierXRefParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SupplierXRefTableset] = obj["returnObj"]
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

