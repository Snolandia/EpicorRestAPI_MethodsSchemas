import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CashFlowSvc
# Description: bo/CashFlow
           Report on weekly cash flow numbers
           Jennifer Johnson
           07/27/04
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(bookID, budgetCodeID, startingCash, displayType, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method replaces the standard GetRows method
   OperationID: Get_GetRows
      :param bookID: Desc: Book ID   Required: True   Allow empty value : True
      :param budgetCodeID: Desc: Book ID   Required: True   Allow empty value : True
      :param startingCash: Desc: Starting Cash   Required: True
      :param displayType: Desc: T = Terms, D = Terms w/Discount, A = Avg Pay Days   Required: True   Allow empty value : True
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
   params += "bookID=" + bookID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "budgetCodeID=" + budgetCodeID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "startingCash=" + startingCash
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "displayType=" + displayType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_SetCashFlowDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method SetCashFlowDefaults
   Description: Set default values for CashFlow Entry.
   OperationID: SetCashFlowDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCashFlowDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_CashFlowParametersRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      self.Calculation:str = obj["Calculation"]
      self.StartingCash:int = obj["StartingCash"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashFlowRow:
   def __init__(self, obj):
      self.EndDate:str = obj["EndDate"]
      self.OpenAR:int = obj["OpenAR"]
      self.OpenAP:int = obj["OpenAP"]
      self.Net:int = obj["Net"]
      self.AvailCash:int = obj["AvailCash"]
      self.OpenOrders:int = obj["OpenOrders"]
      self.OpenPOs:int = obj["OpenPOs"]
      self.BudExp:int = obj["BudExp"]
      self.ProjNet:int = obj["ProjNet"]
      self.ProjCash:int = obj["ProjCash"]
      self.ShipNotInv:int = obj["ShipNotInv"]
      self.RecNotInv:int = obj["RecNotInv"]
      self.OpenARPI:int = obj["OpenARPI"]
      self.OpenAPPI:int = obj["OpenAPPI"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashFlowTableset:
   def __init__(self, obj):
      self.CashFlow:list[Erp_Tablesets_CashFlowRow] = obj["CashFlow"]
      self.CashFlowParameters:list[Erp_Tablesets_CashFlowParametersRow] = obj["CashFlowParameters"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   bookID
   budgetCodeID
   startingCash
   displayType
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  Book ID  """  
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Book ID  """  
      self.startingCash:int = obj["startingCash"]
      """  Starting Cash  """  
      self.displayType:str = obj["displayType"]
      """  T = Terms, D = Terms w/Discount, A = Avg Pay Days  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashFlowTableset] = obj["returnObj"]
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

class SetCashFlowDefaults_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashFlowTableset] = obj["returnObj"]
      pass

