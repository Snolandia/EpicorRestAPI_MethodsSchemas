import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MetaUIHarnessSvc
# Description: Meta UI Harness related functionality
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetListSpecial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListSpecial
   Description: GetListSpecial - returns random list data w/scalars - whereClause has no effect
   OperationID: GetListSpecial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListSpecial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListSpecial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSampleRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSampleRows
   Description: GetSampleRows - returns random row data
   OperationID: GetSampleRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSampleRowsAdded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSampleRowsAdded
   Description: GetSampleRowsAdded - returns random row data
   OperationID: GetSampleRowsAdded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRowsAdded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRowsAdded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSampleRowsAddedNoSysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSampleRowsAddedNoSysRowID
   Description: GetSampleRowsAdded - returns random row data with blank SysRowID
   OperationID: GetSampleRowsAddedNoSysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRowsAddedNoSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRowsAddedNoSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDynamicData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDynamicData
   Description: GetDynamicData - returns an untyped dynamic dataset
   OperationID: GetDynamicData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynamicData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynamicData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSpecial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSpecial
   Description: Updates all the modified rows
   OperationID: UpdateSpecial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSpecial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSpecial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Updates all the modified / Added rows
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifyRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifyRows
   Description: Set Approved to true for all modified rows
   OperationID: ModifyRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuantity1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuantity1
   Description: Invoked on change of Quantity1.  Approve set true if quantity is greater than 50, false if less than.
   OperationID: OnChangeQuantity1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifyRowsReturnUnChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifyRowsReturnUnChanged
   Description: Set Approved to true for all modified rows and return them as unchanged
   OperationID: ModifyRowsReturnUnChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyRowsReturnUnChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyRowsReturnUnChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRows
   Description: Delete all modified rows
   OperationID: DeleteRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifyAddDeleteRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifyAddDeleteRows
   Description: This will expect three rows and then delete the first row / leave 2nd row unchanged / Modify the third row
It will then add one 'unchanged' row and one with rowMod = 'A'
   OperationID: ModifyAddDeleteRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyAddDeleteRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyAddDeleteRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReturnMultipleUnModifiedRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReturnMultipleUnModifiedRows
   Description: This will expect a row and change it but return two unmodified rows which are different and we need to ensure that the 'last' row is the one that is shown in the Harness
   OperationID: ReturnMultipleUnModifiedRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReturnMultipleUnModifiedRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnMultipleUnModifiedRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultEvents(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultEvents
   Description: Returns sample rows for epScheduler control in Misc harness
   OperationID: GetDefaultEvents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEvents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetNewEvent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEvent
   Description: Get a new event for the ep-scheduler control
   OperationID: GetNewEvent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEvent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEvent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSampleDataTreeStructure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSampleDataTreeStructure
   Description: GetSampleDataTreeStructure
   OperationID: GetSampleDataTreeStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleDataTreeStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleDataTreeStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSomeDatasetsOneType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSomeDatasetsOneType
   Description: Returns two datasets with the same type.
   OperationID: GetSomeDatasetsOneType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSomeDatasetsOneType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSomeDatasetsOneType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NullStringTestNonEmptyResult(epicorHeaders = None):
   """  
   Summary: Invoke method NullStringTestNonEmptyResult
   Description: Returns non-empty string
   OperationID: NullStringTestNonEmptyResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NullStringTestNonEmptyResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_NullStringTestNullResult(epicorHeaders = None):
   """  
   Summary: Invoke method NullStringTestNullResult
   Description: Returns null result
   OperationID: NullStringTestNullResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NullStringTestNullResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class DeleteRows_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
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

class Erp_Tablesets_MetaUIHarnessListTableset:
   def __init__(self, obj):
      self.ParentList:list[Erp_Tablesets_ParentListRow] = obj["ParentList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MetaUIHarnessTableset:
   def __init__(self, obj):
      self.Parent:list[Erp_Tablesets_ParentRow] = obj["Parent"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ParentListRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ParentRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      self.FirstName:str = obj["FirstName"]
      self.LastName:str = obj["LastName"]
      self.Approved:bool = obj["Approved"]
      self.Photo:str = obj["Photo"]
      self.DOB:str = obj["DOB"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.Amount:int = obj["Amount"]
      self.IntNum:int = obj["IntNum"]
      self.GenAmount:int = obj["GenAmount"]
      self.DocGenAmount:int = obj["DocGenAmount"]
      self.Rpt1GenAmount:int = obj["Rpt1GenAmount"]
      self.Rpt2GenAmount:int = obj["Rpt2GenAmount"]
      self.Rtp3GenAmount:int = obj["Rtp3GenAmount"]
      self.CostAmount:int = obj["CostAmount"]
      self.DocCostAmount:int = obj["DocCostAmount"]
      self.Rpt1CostAmount:int = obj["Rpt1CostAmount"]
      self.Rpt2CostAmount:int = obj["Rpt2CostAmount"]
      self.Rpt3CostAmount:int = obj["Rpt3CostAmount"]
      self.PriceAmount:int = obj["PriceAmount"]
      self.DocPriceAmount:int = obj["DocPriceAmount"]
      self.CurrentyCode:str = obj["CurrentyCode"]
      self.UOM1:str = obj["UOM1"]
      self.UOM2:str = obj["UOM2"]
      self.Quantity1:int = obj["Quantity1"]
      self.Quantity2:int = obj["Quantity2"]
      self.EmailAddress:str = obj["EmailAddress"]
      self.EventStart:str = obj["EventStart"]
      self.EventEnd:str = obj["EventEnd"]
      self.EventTitle:str = obj["EventTitle"]
      self.EventDescription:str = obj["EventDescription"]
      self.EventIsAllDay:bool = obj["EventIsAllDay"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetDefaultEvents_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["returnObj"]
      pass

class GetDynamicData_input:
   """ Required : 
   formatNum
   """  
   def __init__(self, obj):
      self.formatNum:int = obj["formatNum"]
      pass

class GetDynamicData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynamicMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListSpecial_input:
   """ Required : 
   whereClause
   firstName
   onlyLastNamesThatStartWith
   seed
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.firstName:str = obj["firstName"]
      self.onlyLastNamesThatStartWith:str = obj["onlyLastNamesThatStartWith"]
      self.seed:int = obj["seed"]
      pass

class GetListSpecial_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MetaUIHarnessListTableset] = obj["returnObj"]
      pass

class GetNewEvent_input:
   """ Required : 
   startDateTime
   endDateTime
   ds
   """  
   def __init__(self, obj):
      self.startDateTime:str = obj["startDateTime"]
      """  Event start time  """  
      self.endDateTime:str = obj["endDateTime"]
      """  Event end time  """  
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class GetNewEvent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSampleDataTreeStructure_input:
   """ Required : 
   treeSelection
   """  
   def __init__(self, obj):
      self.treeSelection:str = obj["treeSelection"]
      """  The string identifier that corresponds to the tree you want  """  
      pass

class GetSampleDataTreeStructure_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The requested JSON as a string  """  
      pass

class GetSampleRowsAddedNoSysRowID_input:
   """ Required : 
   rowCount
   seed
   rowMod
   ds
   """  
   def __init__(self, obj):
      self.rowCount:int = obj["rowCount"]
      self.seed:int = obj["seed"]
      self.rowMod:str = obj["rowMod"]
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class GetSampleRowsAddedNoSysRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSampleRowsAdded_input:
   """ Required : 
   rowCount
   seed
   rowMod
   ds
   """  
   def __init__(self, obj):
      self.rowCount:int = obj["rowCount"]
      self.seed:int = obj["seed"]
      self.rowMod:str = obj["rowMod"]
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class GetSampleRowsAdded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSampleRows_input:
   """ Required : 
   rowCount
   seed
   rowMod
   """  
   def __init__(self, obj):
      self.rowCount:int = obj["rowCount"]
      self.seed:int = obj["seed"]
      self.rowMod:str = obj["rowMod"]
      pass

class GetSampleRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["returnObj"]
      pass

class GetSomeDatasetsOneType_input:
   """ Required : 
   firstDSParam
   ds
   """  
   def __init__(self, obj):
      self.firstDSParam:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["firstDSParam"]
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class GetSomeDatasetsOneType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.firstDSParam:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["firstDSParam"]
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
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

class ModifyAddDeleteRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class ModifyAddDeleteRows_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ModifyRowsReturnUnChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class ModifyRowsReturnUnChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ModifyRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class ModifyRows_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class NullStringTestNonEmptyResult_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class NullStringTestNullResult_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class OnChangeQuantity1_input:
   """ Required : 
   id
   proposedQuantity1
   ds
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.proposedQuantity1:int = obj["proposedQuantity1"]
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class OnChangeQuantity1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReturnMultipleUnModifiedRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class ReturnMultipleUnModifiedRows_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateSpecial_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class UpdateSpecial_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MetaUIHarnessTableset] = obj["ds"]
      pass

      """  output parameters  """  

