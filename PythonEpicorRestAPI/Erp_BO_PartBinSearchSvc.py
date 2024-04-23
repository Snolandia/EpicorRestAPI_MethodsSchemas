import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartBinSearchSvc
# Description: Searches plants, warehouses, and part bins based on input parameters.
PartOnHandWhse was used as a template.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBin
   Description: Validate the bin and warehouse for the current plant..
   OperationID: CheckBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBinContents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBinContents
   Description: Gets a listing of parts in a particular whse/bin.
   OperationID: GetBinContents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBinContents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBinContents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFullBinSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullBinSearch
   Description: Gets the dataset of bins, in difference with GetPartBinSearch, this one includes All bins whether they have
a dimension or lot number or neither of both.
   OperationID: GetFullBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryAttributeValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryAttributeValues
   Description: Create InventoryDynAttrValues table and populate it with inventory attribute values
   OperationID: GetInventoryAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryAttributeValuesOutDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryAttributeValuesOutDS
   OperationID: GetInventoryAttributeValuesOutDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryAttributeValuesOutDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryAttributeValuesOutDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartBinByLotAndPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartBinByLotAndPlant
   Description: Gets the warehouse/bin information for a specific lot, filtered by plant
   OperationID: GetPartBinByLotAndPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinByLotAndPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinByLotAndPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartBinByLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartBinByLot
   Description: Gets the warehouse/bin information for a specific lot.
   OperationID: GetPartBinByLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinByLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinByLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartBinSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartBinSearch
   Description: Gets the dataset of warehouses and bins for a Part.
If a change is made to this method the same change should be applied to
the GetSpecificBinSearch method.
   OperationID: GetPartBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSpecificBinSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSpecificBinSearch
   Description: Gets the dataset of warehouses and bins for a Part.
If a change is made to this method the same change should be applied to
the GetPartBinSearch method.
   OperationID: GetSpecificBinSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecificBinSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecificBinSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Invokes Internal.Lib.FindPart which checks for the existence of a part.
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartBinSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckBin_input:
   """ Required : 
   whseCode
   binNum
   """  
   def __init__(self, obj):
      self.whseCode:str = obj["whseCode"]
      """  The Warehouse.  """  
      self.binNum:str = obj["binNum"]
      """  The Bin.  """  
      pass

class CheckBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errMsg:str = obj["parameters"]
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
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.UniqueTableID:str = obj["UniqueTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartBinSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.WhseCode:str = obj["WhseCode"]
      """  Warehouse code.  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number.  """  
      self.LotNumber:str = obj["LotNumber"]
      """  Lot number.  """  
      self.DimCode:str = obj["DimCode"]
      """  Dimension code.  """  
      self.QtyOnHand:int = obj["QtyOnHand"]
      """  Quantity on hand for the bin.  """  
      self.PartDesc:str = obj["PartDesc"]
      """  Part description  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant name.  """  
      self.WhseCodeDesc:str = obj["WhseCodeDesc"]
      """  Warehouse code description.  """  
      self.BinDesc:str = obj["BinDesc"]
      """  Bin description.  """  
      self.LotNumberDesc:str = obj["LotNumberDesc"]
      """  Lot number description.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Part dimension description.  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Non nettable flag from WhseBin  """  
      self.IUM:str = obj["IUM"]
      self.BinType:str = obj["BinType"]
      """  Bin Type  """  
      self.ContractID:str = obj["ContractID"]
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Part Bin has to be synchronized with Epicor FSA application.  """  
      self.QtyAllocated:int = obj["QtyAllocated"]
      """  Allocated quantity for the bin  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartBinSearchTableset:
   def __init__(self, obj):
      self.PartBinSearch:list[Erp_Tablesets_PartBinSearchRow] = obj["PartBinSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Entered Part Number  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBinContents_input:
   """ Required : 
   whseCode
   binNum
   """  
   def __init__(self, obj):
      self.whseCode:str = obj["whseCode"]
      """  The Warehouse is required.  """  
      self.binNum:str = obj["binNum"]
      """  A specific Bin.  Required.  """  
      pass

class GetBinContents_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
      pass

class GetFullBinSearch_input:
   """ Required : 
   partNum
   whseCode
   consolidateInvAttributes
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number.  """  
      self.whseCode:str = obj["whseCode"]
      """  The Warehouse can be for a specific warehouse
            or null for all warehouses.  """  
      self.consolidateInvAttributes:bool = obj["consolidateInvAttributes"]
      """  Controls if search results are consolidated into a single row when the only difference is Attribute Set ID.  """  
      pass

class GetFullBinSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
      pass

class GetInventoryAttributeValuesOutDS_input:
   """ Required : 
   partNum
   consolidateInvAttributes
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.consolidateInvAttributes:bool = obj["consolidateInvAttributes"]
      self.ds      #schema had no properties on an object.
      pass

class GetInventoryAttributeValuesOutDS_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataTableset:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataTableset"]
      pass

      """  output parameters  """  

class GetInventoryAttributeValues_input:
   """ Required : 
   partNum
   consolidateInvAttributes
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.consolidateInvAttributes:bool = obj["consolidateInvAttributes"]
      self.ds      #schema had no properties on an object.
      pass

class GetInventoryAttributeValues_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetPartBinByLotAndPlant_input:
   """ Required : 
   partNum
   lotNum
   plant
   attributeSetID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.lotNum:str = obj["lotNum"]
      """  Lot number - Optional  """  
      self.plant:str = obj["plant"]
      """  Plant - Optional  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class GetPartBinByLotAndPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
      pass

class GetPartBinByLot_input:
   """ Required : 
   partNum
   lotNum
   attributeSetID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.lotNum:str = obj["lotNum"]
      """  Lot number - Optional  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class GetPartBinByLot_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
      pass

class GetPartBinSearch_input:
   """ Required : 
   pageSize
   absolutePage
   whereClause
   """  
   def __init__(self, obj):
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      self.whereClause:str = obj["whereClause"]
      """  Where Clause.  """  
      pass

class GetPartBinSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetSpecificBinSearch_input:
   """ Required : 
   partNum
   whseCode
   lotNum
   uomCode
   displayAllBins
   binNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number. Required  """  
      self.whseCode:str = obj["whseCode"]
      """  The Warehouse can be for a specific warehouse or null for all.  """  
      self.lotNum:str = obj["lotNum"]
      """  The Lot number can be for a specific lot if null is passed,
            only bins with no lot number will be returned.  """  
      self.uomCode:str = obj["uomCode"]
      """  The UOM Code can be for a specific Unit of Measure code if null is passed,
            only bins with no UOM codes will be returned.  """  
      self.displayAllBins:bool = obj["displayAllBins"]
      """  True or False. False will search for bins with a qty ne 0.
            True will return all bins for a warehouse.  """  
      self.binNum:str = obj["binNum"]
      """  A specific Bin. Required.  """  
      pass

class GetSpecificBinSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartBinSearchTableset] = obj["returnObj"]
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

