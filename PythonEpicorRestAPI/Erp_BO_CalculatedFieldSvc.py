import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CalculatedFieldSvc
# Description: CalculateField service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetByRelatedTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByRelatedTo
   Description: Generic get method for any related to entity
   OperationID: GetByRelatedTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByRelatedTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByRelatedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCalculatedField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCalculatedField
   Description: Generic GetNew for a CalculatedField row.
   OperationID: GetNewCalculatedField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCalculatedField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCalculatedField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCalculatedField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCalculatedField
   Description: Updates CalculatedField based on user input and sets the full expressions.
   OperationID: UpdateCalculatedField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCalculatedField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCalculatedField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFormulaSyntax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFormulaSyntax
   Description: Checks the SQL expression syntax
   OperationID: CheckFormulaSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFormulaSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFormulaSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckFormulaSyntax_input:
   """ Required : 
   fieldName
   ds
   """  
   def __init__(self, obj):
      self.fieldName:str = obj["fieldName"]
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

class CheckFormulaSyntax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CalculatedFieldListValuesRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  ID of related Attribute.  """  
      self.Code:str = obj["Code"]
      """  Code of the list value.  """  
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  Databse Schema Name  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.Description:str = obj["Description"]
      """  Description of the list values.  """  
      self.FieldName:str = obj["FieldName"]
      """  Field name.  """  
      self.TableID:str = obj["TableID"]
      """  Table ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CalculatedFieldRow:
   def __init__(self, obj):
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DataType:str = obj["DataType"]
      """  Data Type.  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  Database Schema Name.  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label.  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name.  """  
      self.FinalExpressionUOM:str = obj["FinalExpressionUOM"]
      """  Final Expression UOM  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.FullExpression:str = obj["FullExpression"]
      """  Full Expression.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Is Calculated.  """  
      self.IsFinalExpression:bool = obj["IsFinalExpression"]
      """  Is Final Expression.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Is Viewable.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence.  """  
      self.TableID:str = obj["TableID"]
      """  Table ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CalculatedFieldTableset:
   def __init__(self, obj):
      self.CalculatedField:list[Erp_Tablesets_CalculatedFieldRow] = obj["CalculatedField"]
      self.CalculatedFieldListValues:list[Erp_Tablesets_CalculatedFieldListValuesRow] = obj["CalculatedFieldListValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByRelatedTo_input:
   """ Required : 
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   ds
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

class GetByRelatedTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCalculatedField_input:
   """ Required : 
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   ds
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

class GetNewCalculatedField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
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

class UpdateCalculatedField_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

class UpdateCalculatedField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CalculatedFieldTableset] = obj["ds"]
      pass

      """  output parameters  """  

