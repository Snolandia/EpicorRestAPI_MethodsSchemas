import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.UOMSearchSvc
# Description: This BO is non-standard. It's provides a custom GetList method.
In this case the program parses the GetList input parameter whereClause.
            
It is looking for the following in the WhereClause:
1. UOMClassID ="
2. "ClassType ="
3. "PartNum = "
4  "TargetUOMCode ="
5. "StockOnly = true"
6. "RetrieveAll = true"
These are all EpiFilters of the UOMCombo object.
These all except for "StockOnly = " and "RetrieveAll = " are used to establish a UOMClassID to be used
in the query of UOMConv table.
It attempts to establish the UOMClassID in the order shown above.
As soon as one of these provides a UOMClassID then that it the UOMClass that will be used.
            
If it find "ClassType =" the program attempts to find the first UOMClass with the given type
and if found will use it's UOMClassID otherwise no UOM will be returned.
            
If it finds "PartNum = " it then extracts the partnum value from the phrase.
Finds the Part to get the Part.UOMClass. If it's a valid part it replaces the
PartNum = .... with UOMCLassID = 'value of part.uomclassid'.
If DualUOMClassID is specified on the part record, or if a specific combo sends
the EpiFilterAppend "DualUOMClass" parameter, then any active unit of measures
found on the Dual UOM Class will be added to the list of uoms retrieved.
            
If it finds TargetUOMCode = 'UOMCode value' it then extracts the UOMCode value and
finds the UOMConv to get the UOMConv.UOMClassID.
The phrase is replaced .... with UOMCLassID = 'value of UOMConv.UOMClassID'.
            
if it finds StockOnly = true then it means that if the Part is valid and it is set
for MultiUom Tracking then only UOMs that are tracked should be returned. That is
only where PartUOM.TrackOnHand = True.  This is used in Transactional programs that
involve updating inventory. The rule is that for multi uom tracked parts you
can only transact in a tracking uom.
            
if it finds RetrieveAll = true then it means that it will return ALL active UOMs including
standard and non standard UOMs.  This is used in the price list programs for product groups
to retrieve ALL valid UOMs that have been defined (standard and non-standard).
            
The original phrase is  alway removed from the query since it is an invalid expression.
            
If none of the Above it means you are searching for standard UOMs only.
It will add   UOMConv.StdUOM = True to the query and all standard UOMs will be returned.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMConvListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UOMConvListRow] = obj["value"]
      pass

class Erp_Tablesets_UOMConvListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  The UOM Class ID that this unit of measure belongs to.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.UOMSymbol:str = obj["UOMSymbol"]
      """  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_UOMConvListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  The UOM Class ID that this unit of measure belongs to.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.UOMSymbol:str = obj["UOMSymbol"]
      """  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UOMSearchTableset:
   def __init__(self, obj):
      self.UOMConvList:list[Erp_Tablesets_UOMConvListRow] = obj["UOMConvList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UOMSearchTableset] = obj["returnObj"]
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

