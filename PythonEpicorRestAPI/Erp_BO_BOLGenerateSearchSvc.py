import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BOLGenerateSearchSvc
# Description: BOLGenerateSearch BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLGenerateSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLGenerateSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, ipType, ipShipDate, ipShipViaCode, ipCustNum, ipVendorNum, ipPackNum, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method will try to mirror the functionality of the base GetRows method but since we are populating
a temp table (BOLSlip) we need our own public method.
Code is based on GetSlips from bo/BOL/BOL.p
   OperationID: Get_GetRows
      :param whereClause: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param ipType: Desc: The type of shipment   Required: True   Allow empty value : True
      :param ipShipDate: Desc: The ship date   Required: True   Allow empty value : True
      :param ipShipViaCode: Desc: The ship via code   Required: True   Allow empty value : True
      :param ipCustNum: Desc: The customer when type is Custopmer (ShipHead)   Required: True
      :param ipVendorNum: Desc: The supplier when type is Subcontract (SubShipH)   Required: True
      :param ipPackNum: Desc: Pack Num   Required: True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipType=" + ipType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipShipDate=" + ipShipDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipShipViaCode=" + ipShipViaCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipCustNum=" + ipCustNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipVendorNum=" + ipVendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipPackNum=" + ipPackNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLGenerateSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_BOLGenerateSearchTableset:
   def __init__(self, obj):
      self.BOLSlip:list[Erp_Tablesets_BOLSlipRow] = obj["BOLSlip"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BOLSlipRow:
   def __init__(self, obj):
      self.BOLType:str = obj["BOLType"]
      self.ShipLog:str = obj["ShipLog"]
      """  BOLNum field for linked slips  """  
      self.PackNum:int = obj["PackNum"]
      self.OrderNum:str = obj["OrderNum"]
      self.ShipDate:str = obj["ShipDate"]
      self.Name:str = obj["Name"]
      """  Name from Packing Slip  """  
      self.ShipTo:str = obj["ShipTo"]
      """  ShipTo ID for SubContract  """  
      self.EntryName:str = obj["EntryName"]
      """  Name of User who entered the packing slip  """  
      self.LineNum:int = obj["LineNum"]
      self.Class:str = obj["Class"]
      self.PkgType:str = obj["PkgType"]
      self.Direct:bool = obj["Direct"]
      """  Indicates if this is a direct transfer  """  
      self.ActionFlag:str = obj["ActionFlag"]
      """  L - Linking slip, U - Unlinking slip  """  
      self.Weight:int = obj["Weight"]
      self.Packages:int = obj["Packages"]
      self.BillNum:str = obj["BillNum"]
      """  Billing ID, used in creating the linked BOL record  """  
      self.Carrier:str = obj["Carrier"]
      """  ShipVia Carrier description  """  
      self.BOLLine:int = obj["BOLLine"]
      """  BOL Line linked to  """  
      self.BOLNum:int = obj["BOLNum"]
      self.MasterPackFlag:bool = obj["MasterPackFlag"]
      """  Flag to indicate whether or not this is generated from a Masterpack to be used when updating the source tables.  """  
      self.TempCustNum:int = obj["TempCustNum"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetRows_input:
   """ Required : 
   whereClause
   ipType
   ipShipDate
   ipShipViaCode
   ipCustNum
   ipVendorNum
   ipPackNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause to restrict data for  """  
      self.ipType:str = obj["ipType"]
      """  The type of shipment  """  
      self.ipShipDate:str = obj["ipShipDate"]
      """  The ship date  """  
      self.ipShipViaCode:str = obj["ipShipViaCode"]
      """  The ship via code  """  
      self.ipCustNum:int = obj["ipCustNum"]
      """  The customer when type is Custopmer (ShipHead)  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The supplier when type is Subcontract (SubShipH)  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Num  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BOLGenerateSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

