import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POWorkbenchSvc
# Description: Purchase Part Multi UOM Planning Workbench Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CustomGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomGetByID
   Description: Validates Part and returns a dataset including POWPart, UOMTotals, POWorkbenchMatrix and associated metadata
   OperationID: CustomGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOnHandQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOnHandQty
   Description: Get the total quantity we have in stock of this part converted
to the parts primary inventory UOM.
   OperationID: GetOnHandQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOnHandQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOnHandQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOWorkbench(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOWorkbench
   Description: Retrieves data for UOM codes per part that are defined to be tracked for
it (PartUOM.TrackOnHand = true).
Part:         Only Parts where Part.TrackDimension is true should be used.
Horizon Date: Default to today.
If the date entered is before the current date an error message should appear.
This date will be used to limit the supply/demand displayed in the workbench.
Anything after the horizon date will be ignored.
   OperationID: GetPOWorkbench
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOWorkbench_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOWorkbench_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CustomGetByID_input:
   """ Required : 
   partNum
   horizonDate
   metadata
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.horizonDate:str = obj["horizonDate"]
      self.metadata:list[Erp_Tablesets_DynamicMetadataTableset] = obj["metadata"]
      pass

class CustomGetByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.metadata:list[Erp_Tablesets_DynamicMetadataTableset] = obj["metadata"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POWPartRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  Only parts tracked in multiple UOM’s should be allowed.  If a part is entered that is not tracked in multiple’s, an error will be displayed.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  This is the total quantity we have in stock of this part converted to the parts primary inventory UOM.  """  
      self.IUM:str = obj["IUM"]
      """  The parts primary inventory UOM  """  
      self.HorizonDate:str = obj["HorizonDate"]
      """  Default to today’s date.  Date entered must be greater than or equal to today’s date.  We should not allow past dates.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POWorkbenchRow:
   def __init__(self, obj):
      self.SortNum:int = obj["SortNum"]
      """  Internal identifier for table that will tie multiple UOM for the same Date/Source together.  """  
      self.SourceDate:str = obj["SourceDate"]
      """  Date of the supply or demand  """  
      self.Source:str = obj["Source"]
      """  Description of the supply or demand.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  Base Unit of Measure for the Part.  Will be used to create the titles of UOM columns.  """  
      self.Inv_Demand:int = obj["Inv_Demand"]
      """  The amount of the demand in base UOM  """  
      self.Inv_Supply:int = obj["Inv_Supply"]
      """  The amount of the supply in base UOM  """  
      self.Inv_Balance:int = obj["Inv_Balance"]
      """  The current inventory balance in base UOM  """  
      self.UOM_Available:int = obj["UOM_Available"]
      """  The inventory amount in the specified UOM  """  
      self.UOM_Demand:int = obj["UOM_Demand"]
      """  The amount of the demand in the specified UOM if this is the UOM of the demand.  Otherwise will be 0.  """  
      self.UOM_Supply:int = obj["UOM_Supply"]
      """  The amount of the supply in the specified UOM if this is the UOM of the supply.  Otherwise will be 0.  """  
      self.UOM_Balance:int = obj["UOM_Balance"]
      """  The inventory amount in the specified UOM  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POWorkbenchTableset:
   def __init__(self, obj):
      self.POWorkbench:list[Erp_Tablesets_POWorkbenchRow] = obj["POWorkbench"]
      self.POWPart:list[Erp_Tablesets_POWPartRow] = obj["POWPart"]
      self.UOMTotals:list[Erp_Tablesets_UOMTotalsRow] = obj["UOMTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UOMTotalsRow:
   def __init__(self, obj):
      self.UOMCode:str = obj["UOMCode"]
      """  Base Unit of Measure for the Part.  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """  Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions. For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Amount in this UOM that is on hand  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Amount in this UOM that is needed  """  
      self.UOMOnHandQty:int = obj["UOMOnHandQty"]
      """  Balance calculated by taking the Primary IUM Onhand qty and subtracting the demand qty and adding the demand qty (only if stock transaction, it will not be changed by non-stock transactions).  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetOnHandQty_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      pass

class GetOnHandQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opOnHandQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetPOWorkbench_input:
   """ Required : 
   ipPartNum
   ipHorizonDate
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ipHorizonDate:str = obj["ipHorizonDate"]
      """  Horizon Date  """  
      pass

class GetPOWorkbench_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POWorkbenchTableset] = obj["returnObj"]
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

